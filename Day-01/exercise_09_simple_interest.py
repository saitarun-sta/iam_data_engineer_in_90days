print("Simple Interest Calculator")

principal = int(input("Enter the principal amount: "))
rate = float(input("Enter the rate (%): "))
months = int(input("Enter the time period in months: "))

time_in_years = months / 12

interest = (principal * rate * time_in_years) / 100

print(f"Interest: {interest:.2f}")