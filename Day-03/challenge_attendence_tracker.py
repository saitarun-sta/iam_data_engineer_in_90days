total_students = int(input("How many students are there in the class: "))

eligible = 0
not_eligible = 0


for student in range(total_students):
    student_name = input("Enter Name: ")
    attendence_percentage = int(input("attendence_percentage: "))

    if attendence_percentage >= 75:
        eligible += 1
    else:
        not_eligible -= 1

template = f"""
{" Attendance Report ":=^30}

Total Students : {total_students}

Eligible (≥75%) : {eligible}

Not Eligible    : {not_eligible}

{"=":=^30}
"""

print(template)
