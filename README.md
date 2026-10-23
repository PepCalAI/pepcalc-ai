# pepcalc-ai — free peptide reconstitution & syringe-unit calculator ([pepcalc.ai](https://pepcalc.ai))

> **Educational information only. Not medical advice.**

A tiny, dependency-free Python library and CLI for the general arithmetic behind reconstitution calculators: concentration in mg/mL, the volume containing a target amount, and U-100 syringe units. It contains no recommendations about amounts to use for any person or purpose.

## Install

```bash
pip install pepcalc-ai
```

## Usage

```python
from pepcalc_ai import concentration_mg_per_ml, volume_for_amount_ml, syringe_units

conc = concentration_mg_per_ml(vial_mg=10, diluent_ml=2)   # 5.0 mg/mL
vol = volume_for_amount_ml(amount_mg=1, concentration_mg_per_ml=conc)  # 0.2 mL
units = syringe_units(vol)                                  # 20.0 units on a U-100 syringe
```

CLI:

```bash
pepcalc-ai --vial-mg 10 --diluent-ml 2 --amount-mg 1
```

## Formulas

- concentration (mg/mL) = vial mg ÷ diluent mL
- volume (mL) = target mg ÷ concentration (mg/mL)
- U-100 syringe units = volume (mL) × 100

## Development

```bash
pip install -e . pytest
pytest
```

## Disclaimer

Educational information only. Not medical advice. This software is provided as-is under the MIT license.

## License

MIT
