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
        "name": "Pressure",
        "conversions": {
            "1": ("Bar → Pascal", conversions.bar_to_pascal, "bar", "Pa"),
            "2": ("Pascal → Bar", conversions.pascal_to_bar, "Pa", "bar"),
        }
    },

    "4": {
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
        }
    }
}

while True:
    print("\n=== UNIT CONVERTER ===")

    for number, category in categories.items():
        print(f"{number}. {category['name']}")

    print("0. Çıkış")

    category_choice = input("Kategori seç: ")

    if category_choice == "0":
        print("Unit Converter kapatılıyor.")
        break

    if category_choice not in categories:
        print("Hata: Geçersiz kategori.")
        continue

    selected_category = categories[category_choice]

    while True:
        print(f"\n=== {selected_category['name'].upper()} ===")

        for number, conversion in selected_category["conversions"].items():
            print(f"{number}. {conversion[0]}")

        print("0. Geri")

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

        print(f"{value} {from_unit} = {result} {to_unit}")