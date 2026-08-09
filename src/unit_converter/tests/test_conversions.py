from src.unit_converter import conversions


def test_meter_to_millimeter():
    assert conversions.meter_to_millimeter(2) == 2000


def test_millimeter_to_meter():
    assert conversions.millimeter_to_meter(2000) == 2


def test_newton_to_kilonewton():
    assert conversions.newton_to_kilonewton(2500) == 2.5


def test_kilonewton_to_newton():
    assert conversions.kilonewton_to_newton(2.5) == 2500


def test_bar_to_pascal():
    assert conversions.bar_to_pascal(2) == 200000


def test_pascal_to_bar():
    assert conversions.pascal_to_bar(200000) == 2


def test_kilogram_to_gram():
    assert conversions.kilogram_to_gram(2.5) == 2500


def test_gram_to_kilogram():
    assert conversions.gram_to_kilogram(2500) == 2.5