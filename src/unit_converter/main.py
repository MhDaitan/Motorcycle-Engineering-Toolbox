import conversions


conversions_menu = {
    "1": ("Metre → Milimetre", conversions.meter_to_millimeter, "m", "mm"),
    "2": ("Milimetre → Metre", conversions.millimeter_to_meter, "mm", "m"),
    "3": ("Metre → Santimetre", conversions.meter_to_centimeter, "m", "cm"),
    "4": ("Santimetre → Metre", conversions.centimeter_to_meter, "cm", "m"),
    "5": ("Metre → Kilometre", conversions.meter_to_kilometer, "m", "km"),
    "6": ("Kilometre → Metre", conversions.kilometer_to_meter, "km", "m"),
    "7": ("Newton → Kilonewton", conversions.newton_to_kilonewton, "N", "kN"),
    "8": ("Kilonewton → Newton", conversions.kilonewton_to_newton, "kN", "N"),
    "9": ("Bar → Pascal", conversions.bar_to_pascal, "bar", "Pa"),
    "10": ("Pascal → Bar", conversions.pascal_to_bar, "Pa", "bar"),
    "11": ("Newton metre → Kilonewton metre",
           conversions.newton_meter_to_kilonewton_meter, "N·m", "kN·m"),
    "12": ("Kilonewton metre → Newton metre",
           conversions.kilonewton_meter_to_newton_meter, "kN·m", "N·m"),
}


while True:
    print("\n=== UNIT CONVERTER ===")

    for number, conversion in conversions_menu.items():
        print(f"{number}. {conversion[0]}")

    print("0. Çıkış")

    choice = input("Seçimin: ")

    if choice == "0":
        print("Unit Converter kapatılıyor.")
        break

    if choice not in conversions_menu:
        print("Hata: Geçersiz seçim.")
        continue

    try:
        value = float(input("Değer: "))
    except ValueError:
        print("Hata: Lütfen sayısal bir değer girin.")
        continue

    name, conversion_function, from_unit, to_unit = conversions_menu[choice]

    result = conversion_function(value)

    print(f"{value} {from_unit} = {result} {to_unit}")