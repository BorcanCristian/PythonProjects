#Convert Weight

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")


if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    # print("Your weight in pounds is", weight)
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    # print("Your weight in kilograms is", weight)
else:
    print(f"{unit} was not valid")

print(f"Your weight is: {round(weight, 1)} {unit}")

