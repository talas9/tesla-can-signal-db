#!/usr/bin/env python3
"""
Generate the searchable documentation site under docs/ from the DBC JSON twins.

    python3 tools/gen_docs.py            # regenerate docs/
    python3 tools/gen_docs.py --check    # regenerate to a temp dir, diff against docs/,
                                         # run the PII + source-disclosure gates on it

Inputs: dbc/<model>/<firmware>/<BUS>.json (the machine-readable twins that
tools/export_dbc.py writes next to every .dbc; they carry the same messages,
signals, value tables, confidence and comments as the DBC files, so the docs
cannot disagree with them). Model names, ECU labels and the bus labels come
from export_dbc. Only Model3, ModelY and AllModels are documented: the
product-codename folders have no confirmed model.

Output (all paths lowercase, URL-safe, deterministic, no timestamps):
    docs/<model>/<fw>/<bus>/<ecu>/<message>.md   one page per message
    docs/<model>/<fw>/<ecu>.md                   ECU index (all buses)
    docs/index.md                                models -> firmware -> buses -> ECUs
    docs/messages.md                             message name -> pages
    docs/signals/index.md, docs/signals/<a-z>.md signal name -> pages
    docs/sitemap.xml, docs/robots.txt, docs/_config.yml   GitHub Pages wiring
(<bus> is veh, ch, party or eth; eth pages use Ethernet-side ids, not CAN ids.
Two messages of one ECU that differ only in letter case get the id appended.)

Library API: build_site(repo) -> dict[relpath, text]; write(repo, out_dir);
check(repo) -> list[str] (errors, empty = pass).
"""

import argparse
import json
import re
import shutil
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402
from export_dbc import BUS_LABELS, fmt_num, model_label, node_label, node_of  # noqa: E402

MODELS = ['Model3', 'ModelY', 'AllModels']
BUS_ORDER = ['VEH', 'CH', 'PARTY', 'ETH']
SITE_TITLE = 'Tesla Model 3 and Model Y CAN Signal Database'
SITE_DESC = ('Searchable reference of Tesla Model 3 and Model Y CAN bus messages and signals: '
             'bit layout, scaling, units and value tables, with DBC files.')
CHUNK_BYTES = 600000


def tesla(model):
    return 'Tesla ' + model_label(model)


def ecu_code(node):
    """ECU code as shown in docs; a node name that fails the source-disclosure gate is shown as 'tester'."""
    if node == 'Vector__XXX':
        return 'other'
    return 'tester' if build.scan_source_disclosure(node) else node


def ecu_of(msg_name):
    return ecu_code(node_of(msg_name))


def ecu_label(ecu):
    if ecu == 'other':
        return 'Messages without an ECU prefix'
    if ecu == 'tester':
        return 'External diagnostic tester'
    return node_label(ecu)


def esc(text):
    """Escape a table cell."""
    return (str(text).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            .replace('|', '\\|').replace('\n', ' '))


def yq(text):
    return json.dumps(text, ensure_ascii=False)


def rel(from_path, to_path):
    """Relative link between two docs/-relative paths."""
    a = from_path.split('/')[:-1]
    b = to_path.split('/')
    i = 0
    while i < len(a) and i < len(b) - 1 and a[i] == b[i]:
        i += 1
    return '../' * (len(a) - i) + '/'.join(b[i:])


def front(title, description):
    return '---\nlayout: default\ntitle: %s\ndescription: %s\n---\n' % (yq(title), yq(description))


def bus_bits(sig):
    return '%d\\|%d' % (sig['start'], sig['length'])


def enum_text(values):
    if not values:
        return ''
    items = sorted(values.items(), key=lambda kv: int(kv[0]))
    return '<br>'.join('%s = `%s`' % (esc(k), esc(v)) for k, v in items)


def rng(sig):
    if sig['min'] is None or sig['max'] is None:
        return ''
    return '%s to %s' % (fmt_num(sig['min']), fmt_num(sig['max']))


# ----------------------------------------------------------------- loading

def load(repo):
    """-> list of dict(model, fw, bus, path, data) for every documented twin."""
    out = []
    for model in MODELS:
        mdir = repo / 'dbc' / model
        if not mdir.exists():
            continue
        for fwdir in sorted(p for p in mdir.iterdir() if p.is_dir()):
            for bus in BUS_ORDER:
                jp = fwdir / ('%s.json' % bus)
                if jp.exists():
                    out.append({'model': model, 'fw': fwdir.name, 'bus': bus,
                                'data': json.loads(jp.read_text(encoding='utf-8'))})
    return out


def plan(files):
    """Assign every message its page path. -> list of page dicts."""
    pages = []
    for f in files:
        used = {}
        for m in sorted(f['data']['messages'], key=lambda m: (ecu_of(m['name']), m['name'].lower(), m['frame_id'])):
            ecu = ecu_of(m['name'])
            base = m['name'].lower()
            key = (ecu, base)
            fname = base if key not in used else '%s-0x%x' % (base, m['frame_id'])
            used[key] = True
            path = '%s/%s/%s/%s/%s.md' % (f['model'].lower(), f['fw'], f['bus'].lower(), ecu.lower(), fname)
            pages.append({'model': f['model'], 'fw': f['fw'], 'bus': f['bus'], 'ecu': ecu,
                          'msg': m, 'path': path, 'dbc_model': f['model']})
    return pages


# ------------------------------------------------------------- page bodies

def message_page(p):
    m, model, fw, bus, ecu = p['msg'], p['model'], p['fw'], p['bus'], p['ecu']
    sigs = m['signals']
    label = ecu_label(ecu)
    idtxt = '0x%X' % m['frame_id']
    bus_txt = 'ETH' if bus == 'ETH' else '%s CAN' % bus
    title = '%s (%s) \u2014 %s, %s %s %s' % (m['name'], idtxt, label, tesla(model), fw, bus_txt)
    names = [s['name'] for s in sigs]
    shown = ', '.join(names[:4]) + (' and %d more' % (len(names) - 4) if len(names) > 4 else '')
    if bus == 'ETH':
        desc = ('%s. Ethernet-side message %s of %s for %s firmware %s, %d signals (%s). '
                'Bit layout, scaling, units and value tables.' % (
                    m['comment'].split(';')[0], m['name'], label, tesla(model), fw, len(sigs), shown))
    else:
        desc = ('%s. %s CAN bus message %s (%s) of %s, firmware %s, %d signals (%s). '
                'Bit layout, scaling, units and value tables.' % (
                    m['comment'].split(';')[0], tesla(model), m['name'], idtxt, label, fw, len(sigs), shown))
    path = p['path']
    dbc_rel = '../../../../../dbc/%s/%s/%s' % (model, fw, bus)
    ecu_page = rel(path, '%s/%s/%s.md' % (model.lower(), fw, ecu.lower()))
    L = [front(title, desc), '# %s\n' % title]
    L.append('%s. This page documents the %s signals of %s as defined for %s firmware %s%s.\n' % (
        m['comment'].rstrip('.'), len(sigs), m['name'], tesla(model), fw,
        ' (Ethernet-side id, not a CAN id)' if bus == 'ETH' else ' on the %s bus' % BUS_LABELS[bus].split(' (')[0]))
    L.append('## Message details\n')
    L.append('| Property | Value |\n|---|---|')
    L.append('| Message name | `%s` |' % m['name'])
    L.append('| %s | %s (%d) |' % ('Ethernet-side id' if bus == 'ETH' else 'CAN id', idtxt, m['frame_id']))
    L.append('| ECU | [%s](%s) |' % (esc(label), ecu_page))
    L.append('| Vehicle | %s |' % tesla(model))
    L.append('| Firmware | %s |' % fw)
    L.append('| Bus | %s |' % esc(BUS_LABELS[bus]))
    L.append('| Transmitter | %s |' % esc(ecu_code(m['transmitter'])))
    L.append('| Frame length | %d bytes%s |' % (m['length'], ' (CAN FD)' if m['fd'] else ''))
    L.append('| Cycle time | %s |' % ('%d ms' % m['cycle_ms'] if m['cycle_ms'] else 'not cyclic or not known'))
    L.append('| Signals | %d |' % len(sigs))
    L.append('')
    sel = [s for s in sigs if s['multiplexer']]
    paged = [s for s in sigs if s['mux_value'] is not None]
    L.append('## Signals of %s\n' % m['name'])
    L.append('Tesla %s CAN bus signals in `%s`: start bit and length, byte order, scaling, unit, '
             'range, value table and confidence.\n' % (model_label(model), m['name']))
    hdr = '| Signal | Meaning | Start\\|length | Byte order | Signed | Scale | Offset | Unit | Min to max | Values | Confidence |'
    if sel:
        hdr = hdr.replace('| Meaning', '| Mux | Meaning')
    L.append(hdr)
    L.append('|' + '---|' * (hdr.replace('\\|', '').count('|') - 1))
    for s in sigs:
        mux = ''
        if s['multiplexer']:
            mux = 'selector'
        elif s['mux_value'] is not None:
            mux = 'page %s' % s['mux_value']
        cells = ['`%s`' % s['name']]
        if sel:
            cells.append(mux)
        cells += [esc(s['comment']), bus_bits(s), s['byte_order'].replace('_', '-'),
                  'signed' if s['signed'] else 'unsigned', fmt_num(s['scale']), fmt_num(s['offset']),
                  esc(s['unit']), rng(s), enum_text(s['values']), s['confidence']]
        L.append('| ' + ' | '.join(cells) + ' |')
    L.append('')
    if sel:
        L.append('## Multiplexing\n')
        pages = sorted({s['mux_value'] for s in paged})
        L.append('`%s` is the multiplexer selector of this message. Its value picks which group of signals '
                 'is valid in a frame: %s. Signals without a page are present in every frame.\n' % (
                     ', '.join(s['name'] for s in sel),
                     ', '.join('page %s (%d signals)' % (v, sum(1 for s in paged if s['mux_value'] == v)) for v in pages)
                     if pages else 'no paged signals'))
    L.append('## Download the DBC file\n')
    L.append('- [%s %s %s DBC file](%s.dbc) (Vector DBC)' % (tesla(model), fw, bus, dbc_rel))
    L.append('- [Same data as JSON](%s.json)' % dbc_rel)
    if bus == 'ETH':
        L.append('\nEthernet-side ids differ from CAN ids; do not load this file on a CAN bus.')
    L.append('')
    L.append('## See also\n')
    L.append('- [All %s messages (%s)](%s)' % (esc(label), ecu, ecu_page))
    L.append('- [Signal index A-Z](%s)' % rel(path, 'signals/index.md'))
    L.append('- [All messages](%s)' % rel(path, 'messages.md'))
    L.append('- [Documentation home](%s)' % rel(path, 'index.md'))
    return '\n'.join(L) + '\n'


def ecu_page(model, fw, ecu, plist):
    label = ecu_label(ecu)
    path = '%s/%s/%s.md' % (model.lower(), fw, ecu.lower())
    title = '%s (%s) CAN messages and signals \u2014 %s %s' % (label, ecu, tesla(model), fw)
    nsig = sum(len(p['msg']['signals']) for p in plist)
    desc = ('%s %s CAN bus messages and signals of the %s (%s) for firmware %s: %d messages, %d signals '
            'with bit layout, scaling and value tables.' % (tesla(model), ecu, label, ecu, fw, len(plist), nsig))
    L = [front(title, desc), '# %s\n' % title]
    L.append('All %d messages of the %s (%s) documented for %s firmware %s, across the buses that carry them.\n' % (
        len(plist), label, ecu, tesla(model), fw))
    L.append('| Message | Bus | Id | Length | Cycle | Signals |\n|---|---|---|---:|---:|---:|')
    for p in sorted(plist, key=lambda p: (BUS_ORDER.index(p['bus']), p['msg']['name'].lower(), p['msg']['frame_id'])):
        m = p['msg']
        L.append('| [`%s`](%s) | %s | 0x%X | %d | %s | %d |' % (
            m['name'], rel(path, p['path']), p['bus'], m['frame_id'], m['length'],
            '%d ms' % m['cycle_ms'] if m['cycle_ms'] else '', len(m['signals'])))
    L.append('\n[Documentation home](%s) | [Signal index A-Z](%s)\n' % (rel(path, 'index.md'), rel(path, 'signals/index.md')))
    return path, '\n'.join(L)


def link_label(p):
    return '%s %s %s' % (model_label(p['model']), p['fw'], p['bus'])


def signals_index(pages):
    """name -> {'comment', 'targets': [(page, ...)]}; deterministic."""
    idx = defaultdict(list)
    for p in pages:
        for s in p['msg']['signals']:
            idx[s['name']].append((p, s))
    return idx


def letter_of(name):
    c = name[:1].lower()
    return c if 'a' <= c <= 'z' else 'other'


def build_site(repo):
    files = load(repo)
    pages = plan(files)
    site = {}
    for p in pages:
        site[p['path']] = message_page(p)
    # ECU indexes
    by_ecu = defaultdict(list)
    for p in pages:
        by_ecu[(p['model'], p['fw'], p['ecu'])].append(p)
    for (model, fw, ecu), plist in sorted(by_ecu.items()):
        pth, text = ecu_page(model, fw, ecu, plist)
        assert pth not in site, pth
        site[pth] = text + '\n'
    # home
    L = [front(SITE_TITLE, SITE_DESC), '# %s\n' % SITE_TITLE]
    L.append('%s Pick a vehicle, firmware and bus, then an ECU, or search the '
             '[signal index A-Z](signals/index.md) or the [message list](messages.md).\n' % SITE_DESC)
    for model in MODELS:
        fws = sorted({f['fw'] for f in files if f['model'] == model}, reverse=True)
        if not fws:
            continue
        L.append('## %s CAN signals\n' % tesla(model))
        for fw in fws:
            L.append('### %s firmware %s\n' % (tesla(model), fw))
            for bus in BUS_ORDER:
                bp = [p for p in pages if (p['model'], p['fw'], p['bus']) == (model, fw, bus)]
                if not bp:
                    continue
                ecus = defaultdict(int)
                for p in bp:
                    ecus[p['ecu']] += 1
                L.append('- **%s**: %d messages, %d signals' % (
                    BUS_LABELS[bus], len(bp), sum(len(p['msg']['signals']) for p in bp)))
                L.append('  - ' + ', '.join('[%s](%s) (%d)' % (e, '%s/%s/%s.md' % (model.lower(), fw, e.lower()), n)
                                              for e, n in sorted(ecus.items())))
            L.append('')
    L.append('## Files\n')
    L.append('The DBC files themselves are in the repository `dbc/` folder, one per model, firmware and bus; '
             'see the [repository README](../README.md).\n')
    site['index.md'] = '\n'.join(L) + '\n'
    # messages
    msgs = defaultdict(list)
    for p in pages:
        msgs[p['msg']['name']].append(p)
    L = [front('Tesla CAN message list (A-Z)', 'Every Tesla Model 3 and Model Y CAN message name with links to its signal '
               'documentation per model, firmware and bus.'), '# Tesla Model 3 and Model Y CAN messages A-Z\n']
    L.append('%d message names. Each links to the page for every model, firmware and bus that carries it.\n' % len(msgs))
    for name in sorted(msgs, key=lambda n: (n.lower(), n)):
        ps = sorted(msgs[name], key=lambda p: p['path'])
        L.append('- `%s` (%s): %s' % (name, ecu_of(name), ' \u00b7 '.join(
            '[%s](%s)' % (link_label(p), p['path']) for p in ps)))
    site['messages.md'] = '\n'.join(L) + '\n'
    # signals
    idx = signals_index(pages)
    letters = defaultdict(list)
    for name in sorted(idx, key=lambda n: (n.lower(), n)):
        letters[letter_of(name)].append(name)
    chunk_of = {}
    for letter, names in sorted(letters.items()):
        # entries per name, then split into pages of at most CHUNK_BYTES
        entries = []
        for name in names:
            items = idx[name]
            ms = defaultdict(list)
            for p, s in items:
                ms[p['msg']['name']].append(p)
            entries.append((name, items[0][1]['comment'], [(mn, sorted(ms[mn], key=lambda p: p['path'])) for mn in sorted(ms)]))
        chunks, cur, size = [], [], 0
        for e in entries:
            sz = 200 + sum(120 + 160 * len(ps) for _, ps in e[2])
            if cur and size + sz > CHUNK_BYTES:
                chunks.append(cur)
                cur, size = [], 0
            cur.append(e)
            size += sz
        chunks.append(cur)
        lname = letter.upper() if letter != 'other' else 'other characters'
        paths = ['signals/%s.md' % letter] + ['signals/%s-%d.md' % (letter, i + 1) for i in range(1, len(chunks))]
        if len(chunks) > 1:
            paths = ['signals/%s-%d.md' % (letter, i + 1) for i in range(len(chunks))]
            T = 'Tesla CAN signals starting with %s' % lname
            L = [front(T, 'Tesla Model 3 and Model Y CAN bus signals beginning with %s: pages of signal names '
                       'with links to the messages that define them.' % lname), '# %s\n' % T,
                 '%d signals, split over %d pages.\n' % (len(names), len(chunks))]
            for pth, ch in zip(paths, chunks):
                L.append('- [%s to %s](%s) (%d signals)' % (ch[0][0], ch[-1][0], pth.split('/')[1], len(ch)))
            site['signals/%s.md' % letter] = '\n'.join(L) + '\n'
        for pth, ch in zip(paths, chunks):
            T = 'Tesla CAN signals %s to %s' % (ch[0][0], ch[-1][0])
            L = [front(T, 'Tesla Model 3 and Model Y CAN bus signals %s to %s: signal name, meaning and the message '
                       'pages that define its bit layout.' % (ch[0][0], ch[-1][0])), '# %s\n' % T]
            L.append('%d signals. [Back to the signal index](index.md).\n' % len(ch))
            for name, comment, msgs_ in ch:
                L.append('- <a id="%s"></a>**`%s`**: %s' % (name.lower(), name, esc(comment)))
                for mname, ps in msgs_:
                    L.append('  - in `%s` (%s): %s' % (mname, ecu_of(mname), ' \u00b7 '.join(
                        '[%s](%s)' % (link_label(p), rel(pth, p['path'])) for p in ps)))
            site[pth] = '\n'.join(L) + '\n'
    L = [front('Tesla CAN signal index A-Z', 'Alphabetical index of %d Tesla Model 3 and Model Y CAN bus signal names '
               'with links to message pages.' % len(idx)), '# Tesla Model 3 and Model Y CAN signal index A-Z\n']
    L.append('%d distinct signal names. Pick the first letter of the signal name you are looking for, or use '
             'your browser\'s find on a letter page.\n' % len(idx))
    for letter, names in sorted(letters.items()):
        L.append('- [%s](%s.md) (%d signals)' % (letter.upper() if letter != 'other' else 'Other', letter, len(names)))
    L.append('\n[Documentation home](../index.md) | [Message list](../messages.md)')
    site['signals/index.md'] = '\n'.join(L) + '\n'
    # pages wiring
    site['_config.yml'] = (
        'title: "%s"\n'
        'description: "%s"\n'
        '# Placeholder: set the real site address before publishing.\n'
        'url: "https://example.invalid"\n'
        'baseurl: "/tesla-can-signal-db"\n'
        'theme: jekyll-theme-minimal\n'
        'markdown: kramdown\n'
        'kramdown:\n  input: GFM\n'
        'plugins:\n  - jekyll-seo-tag\n  - jekyll-sitemap\n  - jekyll-relative-links\n'
        'relative_links:\n  enabled: true\n  collections: false\n'
        '' % (SITE_TITLE, SITE_DESC))
    site['robots.txt'] = ('User-agent: *\nAllow: /\n\n'
                          '# Replace the host with the published site address.\n'
                          'Sitemap: https://example.invalid/tesla-can-signal-db/sitemap.xml\n')
    urls = sorted(k[:-3] + '.html' for k in site if k.endswith('.md'))
    sm = ['---', '---', '<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append('<url><loc>{{ site.url }}{{ site.baseurl }}/%s</loc></url>' % u)
    sm.append('</urlset>')
    site['sitemap.xml'] = '\n'.join(sm) + '\n'
    for k, v in site.items():
        if k != 'sitemap.xml' and ('{{' in v or '{%' in v):
            raise SystemExit('template syntax in %s' % k)
    return site


def write(repo, out_dir):
    site = build_site(repo)
    if out_dir.exists():
        shutil.rmtree(out_dir)
    for k, v in site.items():
        pth = out_dir / k
        pth.parent.mkdir(parents=True, exist_ok=True)
        pth.write_text(v, encoding='utf-8', newline='\n')
    return site


def check(repo):
    """Regenerate to a temp dir and diff against docs/ (+ gates on the result)."""
    errors = []
    tmp = Path(tempfile.mkdtemp(prefix='docs_check_'))
    try:
        site = write(repo, tmp / 'docs')
        docs = repo / 'docs'
        have = {str(p.relative_to(docs)) for p in docs.rglob('*') if p.is_file()} if docs.exists() else set()
        for k in sorted(set(site) - have):
            errors.append('docs: missing %s (run tools/gen_docs.py)' % k)
        for k in sorted(have - set(site)):
            errors.append('docs: stale %s (run tools/gen_docs.py)' % k)
        for k in sorted(set(site) & have):
            if (docs / k).read_text(encoding='utf-8') != site[k]:
                errors.append('docs: differs %s (run tools/gen_docs.py)' % k)
        for k, v in site.items():
            errors += ['docs/%s: %s' % (k, f) for f in build.gate_docs_file(k, v.encode('utf-8'))]
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return errors[:200]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[1])
    ap.add_argument('--repo', default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args(argv)
    repo = Path(args.repo)
    if args.check:
        errs = check(repo)
        for e in errs:
            print('ERROR: ' + e)
        if errs:
            print('DOCS CHECK FAILED: %d errors' % len(errs))
            return 1
        print('DOCS CHECK OK: docs/ regenerated identically, PII + source-disclosure gates clean')
        return 0
    site = write(repo, repo / 'docs')
    print('wrote %d files under docs/' % len(site))
    return 0


if __name__ == '__main__':
    sys.exit(main())
