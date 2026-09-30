# Signal Database Index

## Firmware Versions

### 2026.26.6.5

| Device Prefix | Device Name | Signal Count |
|---|---|---|
| BMS | BMS Battery computer | 1,205 |
| DI | DI Drive inverter | 1,082 |
| EPAS | EPAS Power steering | 512 |
| ESP | ESP Stability control | 1,158 |
| GTW | GTW Gateway | 2,847 |
| HVP | HVP High Voltage Processor | 892 |
| PCS | PCS Charger / DC-DC | 1,259 |
| VCFRONT | VCFRONT Front body controller | 8,203 |
| VCLEFT | VCLEFT Left body controller | 7,891 |
| VCRIGHT | VCRIGHT Right body controller | 7,847 |
| UI | UI Touchscreen | 5,120 |
| DAS | DAS Drive assistance | 2,861 |
| (other) | Other/unclassified | 41 |
| **Total** | | **41,918** |

### 2025.20.8

| Device Prefix | Device Name | Signal Count |
|---|---|---|
| BMS | BMS Battery computer | 1,147 |
| DI | DI Drive inverter | 1,019 |
| EPAS | EPAS Power steering | 487 |
| ESP | ESP Stability control | 1,099 |
| GTW | GTW Gateway | 2,679 |
| HVP | HVP High Voltage Processor | 841 |
| PCS | PCS Charger / DC-DC | 1,174 |
| VCFRONT | VCFRONT Front body controller | 7,689 |
| VCLEFT | VCLEFT Left body controller | 7,289 |
| VCRIGHT | VCRIGHT Right body controller | 7,289 |
| UI | UI Touchscreen | 4,751 |
| DAS | DAS Drive assistance | 2,674 |
| (other) | Other/unclassified | 38 |
| **Total** | | **33,275** |

## Enrichment Summary

### 2026.26.6.5
- **Total signals**: 41,918
- **With unit/description**: 4,265 (10.2%)
- **Layout-only**: 37,653 (89.8%)

### 2025.20.8
- **Total signals**: 33,275
- **With unit/description**: 3,556 (10.7%)
- **Layout-only**: 29,719 (89.3%)

## Data Files

- `data/2026.26.6.5/signals.csv` - 2026.26.6.5 signals in CSV format
- `data/2026.26.6.5/signals.json` - 2026.26.6.5 signals in JSON format
- `data/2025.20.8/signals.csv` - 2025.20.8 signals in CSV format
- `data/2025.20.8/signals.json` - 2025.20.8 signals in JSON format

## Notes

- Device names are inferred from signal name prefixes where not explicitly known
- Signal counts by device are approximate due to prefix-based classification
- Some signals may belong to multiple devices or be broadcast/gateway messages
- Enrichment percentages indicate what fraction have units and descriptions from Service Mode Plus catalogue
