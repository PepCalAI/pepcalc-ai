import pytest

from pepcalc_ai import (
    DISCLAIMER,
    concentration_mg_per_ml,
    main,
    syringe_units,
    volume_for_amount_ml,
)


def test_concentration():
    assert concentration_mg_per_ml(10, 2) == 5


def test_volume():
    assert volume_for_amount_ml(1, 5) == pytest.approx(0.2)


def test_units_u100():
    assert syringe_units(0.2) == pytest.approx(20)
    assert syringe_units(1) == pytest.approx(100)


@pytest.mark.parametrize("bad", [0, -1, float("nan"), float("inf"), "x", None])
def test_invalid(bad):
    with pytest.raises(ValueError):
        concentration_mg_per_ml(bad, 1)
    with pytest.raises(ValueError):
        concentration_mg_per_ml(1, bad)


def test_cli(capsys):
    assert main(["--vial-mg", "10", "--diluent-ml", "2", "--amount-mg", "1"]) == 0
    out = capsys.readouterr().out
    assert "5 mg/mL" in out and "0.2 mL" in out and "20 units" in out
    assert DISCLAIMER in out


def test_cli_invalid():
    with pytest.raises(SystemExit):
        main(["--vial-mg", "0", "--diluent-ml", "2"])
