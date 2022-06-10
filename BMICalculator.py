m = 0.0
kg = 0.0
bmi = 0.0

print("BMI Calculator:")

feet = float(input("\nYour height in feet only: "))
lbs = float(input("Your weight in lbs only: "))

kg = lbs / 2.205
m = feet / 3.281
bmi = kg / (m*m)

print(f"\nYour BMI is {bmi}")