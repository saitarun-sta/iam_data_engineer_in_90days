student_name = input("Enter you name: ")
marks = int(input("Enter marks: "))
attendance_percentage = int(input("Enter Percentage: "))
scholarship_status = ""


if marks >= 85 and attendance_percentage >= 90:
    scholarship_status = "Eligible" 
else:
    scholarship_status = "Not Eligible"

template = f"""
======== Student Card ========

Name                    : {student_name:<20}
marks                   : {marks:<20}
attendence_percentage   : {attendance_percentage:<20}
scholarship_status      : {scholarship_status:<20}

==============================
"""

print(template)