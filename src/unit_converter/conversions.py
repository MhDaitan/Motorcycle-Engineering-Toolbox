import math

def meter_to_millimeter(value):
    return value * 1000


def millimeter_to_meter(value):
    return value / 1000


def meter_to_centimeter(value):
    return value * 100


def centimeter_to_meter(value):
    return value / 100


def meter_to_kilometer(value):
    return value / 1000


def kilometer_to_meter(value):
    return value * 1000

def newton_to_kilonewton(value):
    return value / 1000


def kilonewton_to_newton(value):
    return value * 1000


def bar_to_pascal(value):
    return value * 100000


def pascal_to_bar(value):
    return value / 100000

def kilopascal_to_pascal(value):
    return value * 1000


def pascal_to_kilopascal(value):
    return value / 1000


def megapascal_to_pascal(value):
    return value * 1000000


def pascal_to_megapascal(value):
    return value / 1000000


def psi_to_pascal(value):
    return value * 6894.757293168


def pascal_to_psi(value):
    return value / 6894.757293168


def newton_meter_to_kilonewton_meter(value):
    return value / 1000


def kilonewton_meter_to_newton_meter(value):
    return value * 1000


def kilogram_to_gram(value):
    return value * 1000


def gram_to_kilogram(value):
    return value / 1000


def kilogram_to_gram(value):
    return value * 1000


def gram_to_kilogram(value):
    return value / 1000

def kilometer_per_hour_to_meter_per_second(value):
    return value / 3.6


def meter_per_second_to_kilometer_per_hour(value):
    return value * 3.6

def newton_meter_to_foot_pound(value):
    return value * 0.7375621493


def foot_pound_to_newton_meter(value):
    return value / 0.7375621493

def watt_to_kilowatt(value):
    return value / 1000


def kilowatt_to_watt(value):
    return value * 1000


def horsepower_to_kilowatt(value):
    return value * 0.745699872


def kilowatt_to_horsepower(value):
    return value / 0.745699872

def degree_to_radian(value):
    return value * math.pi / 180


def radian_to_degree(value):
    return value * 180 / math.pi

def rpm_to_radian_per_second(value):
    return value * 2 * math.pi / 60


def radian_per_second_to_rpm(value):
    return value * 60 / (2 * math.pi)