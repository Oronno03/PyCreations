def convert(temp, unit):
    if unit.upper() == "C":
        temp = round((temp * 9 / 5) + 32, 2)
        print(f"{temp} degrees F")
    elif unit.upper() == "F":
        temp = round((temp - 32) * 5 / 9, 2)
        print(f"{temp} degrees C")


while True:
    unit = input(
        "What is the unit of the temperature you want to convert? (C/F) > "
    ).upper()

    if not unit in ["C", "F"]:
        print("Please enter a valid unit")
        continue

    try:
        temp = float(input("What is the temperature? "))
    except ValueError:
        print("Please enter a valid temperature")
        continue

    convert(temp, unit)
    break
