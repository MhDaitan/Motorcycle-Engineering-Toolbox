import pytest
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

def test_kilometer_per_hour_to_meter_per_second():
    assert conversions.kilometer_per_hour_to_meter_per_second(36) == 10


def test_meter_per_second_to_kilometer_per_hour():
    assert conversions.meter_per_second_to_kilometer_per_hour(10) == 36

def test_kilopascal_to_pascal():
    assert conversions.kilopascal_to_pascal(2) == 2000


def test_pascal_to_kilopascal():
    assert conversions.pascal_to_kilopascal(2000) == 2


def test_megapascal_to_pascal():
    assert conversions.megapascal_to_pascal(2) == 2000000


def test_pascal_to_megapascal():
    assert conversions.pascal_to_megapascal(2000000) == 2


def test_psi_to_pascal():
    assert conversions.psi_to_pascal(1) == 6894.757293168


def test_pascal_to_psi():
    assert conversions.pascal_to_psi(6894.757293168) == 1

def test_newton_meter_to_foot_pound():
    assert conversions.newton_meter_to_foot_pound(1) == 0.7375621493


def test_foot_pound_to_newton_meter():
    assert conversions.foot_pound_to_newton_meter(0.7375621493) == 1

def test_watt_to_kilowatt():
    assert conversions.watt_to_kilowatt(2000) == 2


def test_kilowatt_to_watt():
    assert conversions.kilowatt_to_watt(2) == 2000


def test_horsepower_to_kilowatt():
    assert conversions.horsepower_to_kilowatt(1) == 0.745699872


def test_kilowatt_to_horsepower():
    assert conversions.kilowatt_to_horsepower(0.745699872) == 1

def test_degree_to_radian():
    assert conversions.degree_to_radian(180) == pytest.approx(3.141592653589793)


def test_radian_to_degree():
    assert conversions.radian_to_degree(3.141592653589793) == pytest.approx(180)

def test_rpm_to_radian_per_second():
    assert conversions.rpm_to_radian_per_second(60) == pytest.approx(2 * 3.141592653589793)


def test_radian_per_second_to_rpm():
    assert conversions.radian_per_second_to_rpm(2 * 3.141592653589793) == pytest.approx(60)