"""pepcalc-ai: small, dependency-free reconstitution math helpers.

Educational information only. Not medical advice.

These functions perform general unit arithmetic only:

* concentration (mg/mL) = vial contents (mg) / diluent volume (mL)
* volume (mL) = target amount (mg) / concentration (mg/mL)
* U-100 syringe units = volume (mL) * 100
"""

from __future__ import annotations

import argparse
from typing import List, Optional

__all__ = [
    "DISCLAIMER",
    "UNITS_PER_ML_U100",
    "concentration_mg_per_ml",
    "volume_for_amount_ml",
    "syringe_units",
    "main",
]

__version__ = "0.1.0"

DISCLAIMER = "Educational information only. Not medical advice."
UNITS_PER_ML_U100 = 100.0


def _positive(name: str, value: float) -> float:
    try:
        value = float(value)
    except (TypeError, ValueError):
        raise ValueError(f"{name} must be a number") from None
    if not value > 0 or value != value or value == float("inf"):
        raise ValueError(f"{name} must be a positive, finite number")
    return value


def concentration_mg_per_ml(vial_mg: float, diluent_ml: float) -> float:
    """Return concentration in mg/mL: ``vial_mg / diluent_ml``."""
    return _positive("vial_mg", vial_mg) / _positive("diluent_ml", diluent_ml)


def volume_for_amount_ml(amount_mg: float, concentration_mg_per_ml: float) -> float:
    """Return the volume in mL that contains ``amount_mg`` at the given mg/mL."""
    return _positive("amount_mg", amount_mg) / _positive(
        "concentration_mg_per_ml", concentration_mg_per_ml
    )


def syringe_units(volume_ml: float) -> float:
    """Convert a volume in mL to units on a U-100 syringe (100 units = 1 mL)."""
    return _positive("volume_ml", volume_ml) * UNITS_PER_ML_U100


def main(argv: Optional[List[str]] = None) -> int:
    """Command-line entry point."""
    p = argparse.ArgumentParser(
        prog="pepcalc-ai",
        description="Reconstitution unit math (mg/mL, mL, U-100 units). " + DISCLAIMER,
        epilog="More: https://pepcalc.ai",
    )
    p.add_argument("--vial-mg", type=float, required=True, help="total mg in the vial")
    p.add_argument("--diluent-ml", type=float, required=True, help="mL of diluent added")
    p.add_argument("--amount-mg", type=float, help="target amount in mg to convert to volume/units")
    args = p.parse_args(argv)

    try:
        conc = concentration_mg_per_ml(args.vial_mg, args.diluent_ml)
        print(f"Concentration: {conc:.4g} mg/mL")
        if args.amount_mg is not None:
            vol = volume_for_amount_ml(args.amount_mg, conc)
            print(f"Volume: {vol:.4g} mL")
            print(f"U-100 syringe: {syringe_units(vol):.4g} units")
    except ValueError as exc:
        p.error(str(exc))
    print(DISCLAIMER)
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
