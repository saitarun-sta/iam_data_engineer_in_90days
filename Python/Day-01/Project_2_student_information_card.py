print("Student Information Card")

name = input("Enter your name: ")
age = input("Enter your age: ")
student_class = input("Enter your class: ")
school = input("Enter your school: ")

template = f"""
======== Student Card ========

Name   : {name}
Age    : {age}
Class  : {student_class}
School : {school}

==============================
"""

print(template)


# Bonus by ChatGPT

# template = f"""
# ======== Student Card ========

# Name   : {name:<20}
# Age    : {age:<20}
# Class  : {student_class:<20}
# School : {school:<20}

# ==============================
# """

# The <20 means "left-align the text in a field 20 characters wide," which keeps the card neatly aligned even when names have different lengths.