# Simple Python Weight Converter

weight = float(input("Please enter your weight: "))
unit = input("Kilograms or Pounds? (Kg or Lb): ")

if unit == "Kg":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your weight is {round(weight, 1)} {unit}")
elif unit == "Lb":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is {round(weight, 1)} {unit}")
else:
    print(f"{unit} is not a valid unit")



