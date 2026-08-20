year = int(input("Enter Year: "))

if year % 400 == 0:
    print("leap year")
else:
    if year % 4 == 0 and year % 100 != 0:
        print("leap year")
    else:
        print("not a leap year")

# logic
# A year is a leap year if:

# It is divisible by 400, OR
# It is divisible by 4 and not divisible by 100.