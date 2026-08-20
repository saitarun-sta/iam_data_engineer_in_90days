age = int(input("Enter your age: "))
salary = int(input("Enter your salary: "))
credit_score = int(input("Enter you credit score: "))

if age >= 21 and salary >= 30000 and credit_score >= 700:
    print("you are eligible")
else:
    print("not eligible")