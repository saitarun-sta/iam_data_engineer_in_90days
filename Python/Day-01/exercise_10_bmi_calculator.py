print("BMI Calculator")

weight = int(input("Enter your weight (kg): "))
height_in_cm = int(input("Enter your height (cm): "))

height_in_m = height_in_cm / 100

body_mass_index = weight / (height_in_m ** 2)

print(f"BMI: {body_mass_index:.2f}")

# .2f is a format specifier used inside an f-string to display a floating-point number with 2 digits after the decimal point.