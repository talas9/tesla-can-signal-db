"""Naming regressions: preserve API identity without claiming extra coverage."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import export_dbc
import gen_docs


class DocumentationNamesTest(unittest.TestCase):
    def test_coverage_separates_names_from_identifiers_and_preserves_counts(self):
        rows = []
        for model in ('AllModels', 'Model3', 'ModelY', 'Bayberry', 'GoldenSnitch'):
            rows.append(dict(model=model, firmware='2026.26.6.5', bus='VEH',
                             file=f'{model}/2026.26.6.5/VEH.dbc', messages=2,
                             signals=7, enums=3, validated=1, plausible=2,
                             layout_only=4, contradicted=0))
        table = export_dbc.coverage_markdown(rows)
        self.assertIn('| Model | API name / codename |', table)
        self.assertIn('| Model Y (2025+ / Juniper; community mapping) | `Bayberry` |', table)
        self.assertIn('| Unidentified vehicle | `GoldenSnitch` |', table)
        self.assertIn('| Model 3 / Model Y (union) | `AllModels` |', table)
        for row in table.splitlines()[2:]:
            self.assertEqual(row.split('|')[5:-1], [' 2 ', ' 7 ', ' 3 ', ' 1 ', ' 2 ', ' 4 ', ' 0 '])
        self.assertIn('dbc/Bayberry/2026.26.6.5/VEH.dbc', table)
        self.assertEqual(export_dbc.model_label('Bayberry'), 'Bayberry')

    def test_scope_distinguishes_subset_and_union_from_model_coverage(self):
        for product in ('Bayberry', 'GoldenSnitch'):
            scope = export_dbc.documentation_scope(product)
            self.assertIn('Product-metadata signal subset', scope)
            self.assertIn('no product-specific CAN routing map', scope)
        self.assertIn('not every Tesla model', export_dbc.documentation_scope('AllModels'))
        self.assertIn('enum names do not establish', export_dbc.documentation_scope('Model3'))

    def test_generated_product_page_preserves_identifier_and_explains_scope(self):
        msg = dict(name='GTW_status', frame_id=0x348, signals=[], comment='Gateway status',
                   transmitter='GTW', length=8, fd=False, cycle_ms=1000)
        for model in ('Bayberry', 'GoldenSnitch'):
            page = gen_docs.message_page(dict(msg=msg, model=model, fw='2026.26.6.5',
                    bus='VEH', ecu='GTW', path=f'{model.lower()}/2026.26.6.5/veh/gtw/gtw_status.md'))
            self.assertIn(f'| API name / codename | `{model}` |', page)
            self.assertIn('no product-specific CAN routing map', page)
            self.assertIn(f'dbc/{model}/2026.26.6.5/VEH.dbc', page)
        self.assertIn('Bayberry', gen_docs.MODELS)
        self.assertIn('GoldenSnitch', gen_docs.MODELS)


if __name__ == '__main__':
    unittest.main()
