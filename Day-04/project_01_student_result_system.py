def get_student_details():
    return {"name": "Sai Tarun", "Math": 85, "Science": 90, "English": 88}


def calculate_total(student_details):
    calculated_total = 0
    count = 0
    SUBJECTS = ["Math", "Science", "English"]
    for key, value in student_details.items():
        if key in SUBJECTS:
            calculated_total += value
            count += 1
    return calculated_total, count


def calculate_average(calculated_total, count):
    if count == 0:
        return 0

    return calculate_total / count


def calculate_grade(calculated_average):
    if calculated_average >= 80:
        return "A"
    elif calculated_average >= 60:
        return "B"
    elif calculated_average >= 40:
        return "C"
    else:
        return "F"


def display_report(
    student_details, calculated_total, calculated_average, calculated_grade
):
    return f"""
{" Report Card ":=^30}

Name    : {student_details["name"]:<20}
Math    : {student_details["math"]:<20}
Science : {student_details["science"]:<20}
English : {student_details["English"]:<20}
Total   : {calculated_total:<20}
Average : {calculated_average:<20.2f}
Grade   : {calculated_grade:<20}

{"=" * 30}
"""


def main():
    student = get_student_details()
    total, count = calculate_total(student)
    average = calculate_average(total, count)
    grade = calculate_grade(average)
    print(display_report(student, total, average, grade))


main()
