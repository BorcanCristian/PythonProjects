#Convert Weight

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")


if unit.upper() == "K":
    unit = "Kgs."
    weight = weight * 2.205
    unit = "Lbs."


elif unit.upper() == "L":
    weight = weight / 2.205
    unit = "Kgs."


else:
    print(f"{unit} was not valid")

print(f"Your weight is: {round(weight, 1)} {unit}")

