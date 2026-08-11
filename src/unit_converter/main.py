import conversions



categories = {

    "1": {
        "name": "Length",
        "conversions": {
            "1": ("Metre → Milimetre", conversions.meter_to_millimeter, "m", "mm"),
            "2": ("Milimetre → Metre", conversions.millimeter_to_meter, "mm", "m"),
            "3": ("Metre → Santimetre", conversions.meter_to_centimeter, "m", "cm"),
            "4": ("Santimetre → Metre", conversions.centimeter_to_meter, "cm", "m"),
            "5": ("Metre → Kilometre", conversions.meter_to_kilometer, "m", "km"),
            "6": ("Kilometre → Metre", conversions.kilometer_to_meter, "km", "m"),
        }
    },

    "2": {
        "name": "Force",
        "conversions": {
            "1": ("Newton → Kilonewton", conversions.newton_to_kilonewton, "N", "kN"),
            "2": ("Kilonewton → Newton", conversions.kilonewton_to_newton, "kN", "N"),
        }
    },

    "3": {
        "name": "Mass",
        "conversions": {
            "1": ("Kilogram → Gram", conversions.kilogram_to_gram, "kg", "g"),
            "2": ("Gram → Kilogram", conversions.gram_to_kilogram, "g", "kg"),
        }
    },
    "4": {
    "name": "Speed",
    "conversions": {
        "1": (
            "Kilometre/saat → Metre/saniye",
            conversions.kilometer_per_hour_to_meter_per_second,
            "km/h",
            "m/s"
        ),
        "2": (
            "Metre/saniye → Kilometre/saat",
            conversions.meter_per_second_to_kilometer_per_hour,
            "m/s",
            "km/h"
        ),
    }
    },

    "5": {
        "name": "Pressure",
        "conversions": {
        "1": ("Bar → Pascal", conversions.bar_to_pascal, "bar", "Pa"),
        "2": ("Pascal → Bar", conversions.pascal_to_bar, "Pa", "bar"),
        "3": ("Kilopascal → Pascal", conversions.kilopascal_to_pascal, "kPa", "Pa"),
        "4": ("Pascal → Kilopascal", conversions.pascal_to_kilopascal, "Pa", "kPa"),
        "5": ("Megapascal → Pascal", conversions.megapascal_to_pascal, "MPa", "Pa"),
        "6": ("Pascal → Megapascal", conversions.pascal_to_megapascal, "Pa", "MPa"),
        "7": ("PSI → Pascal", conversions.psi_to_pascal, "psi", "Pa"),
        "8": ("Pascal → PSI", conversions.pascal_to_psi, "Pa", "psi"),
        }
    },

    "6": {
        "name": "Torque",
        "conversions": {
            "1": (
            "Newton metre → Kilonewton metre",
            conversions.newton_meter_to_kilonewton_meter,
            "N·m",
            "kN·m"
        ),
        "2": (
            "Kilonewton metre → Newton metre",
            conversions.kilonewton_meter_to_newton_meter,
            "kN·m",
            "N·m"
        ),
        "3": (
            "Newton metre → Foot pound",
            conversions.newton_meter_to_foot_pound,
            "N·m",
            "ft·lbf"
        ),
        "4": (
            "Foot pound → Newton metre",
            conversions.foot_pound_to_newton_meter,
            "ft·lbf",
            "N·m"
            ),
        }
    },

    "7": {
    "name": "Power",
    "conversions": {
        "1": (
            "Watt → Kilowatt",
            conversions.watt_to_kilowatt,
            "W",
            "kW"
        ),
        "2": (
            "Kilowatt → Watt",
            conversions.kilowatt_to_watt,
            "kW",
            "W"
        ),
        "3": (
            "Horsepower → Kilowatt",
            conversions.horsepower_to_kilowatt,
            "hp",
            "kW"
        ),
        "4": (
            "Kilowatt → Horsepower",
            conversions.kilowatt_to_horsepower,
            "kW",
            "hp"
        ),
    },
    },

    "8": {
    "name": "Angle",
    "conversions": {
        "1": (
            "Degree → Radian",
            conversions.degree_to_radian,
            "°",
            "rad"
        ),
        "2": (
            "Radian → Degree",
            conversions.radian_to_degree,
            "rad",
            "°"
        ),
    },
    },

    "9": {
    "name": "Rotation",
    "conversions": {
        "1": (
            "RPM → Radyan/saniye",
            conversions.rpm_to_radian_per_second,
            "rpm",
            "rad/s"
        ),
        "2": (
            "Radyan/saniye → RPM",
            conversions.radian_per_second_to_rpm,
            "rad/s",
            "rpm"
        ),
    },
    },

}

def show_categories():
    print("\n=== UNIT CONVERTER ===")

    for number, category in categories.items():
        print(f"{number}. {category['name']}")

    print("0. Çıkış")


def show_conversions(category):
    print(f"\n=== {category['name'].upper()} ===")

    for number, conversion in category["conversions"].items():
        print(f"{number}. {conversion[0]}")

    print("0. Geri")

while True:
    show_categories()

    category_choice = input("Kategori seç: ")

    if category_choice == "0":
        print("Unit Converter kapatılıyor.")
        break

    if category_choice not in categories:
        print("Hata: Geçersiz kategori.")
        continue

    selected_category = categories[category_choice]

    while True:
        show_conversions(selected_category)


        conversion_choice = input("Dönüşüm seç: ")

        if conversion_choice == "0":
            break

        if conversion_choice not in selected_category["conversions"]:
            print("Hata: Geçersiz dönüşüm.")
            continue

        conversion = selected_category["conversions"][conversion_choice]

        try:
            value = float(input("Değer: "))
        except ValueError:
            print("Hata: Lütfen sayısal bir değer girin.")
            continue

        conversion_function = conversion[1]
        from_unit = conversion[2]
        to_unit = conversion[3]

        result = conversion_function(value)

        print(f"{value:g} {from_unit} = {result:.6g} {to_unit}")