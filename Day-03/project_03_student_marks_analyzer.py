students_marks = [30,23,45,90,85]
total_marks = 0


for marks in students_marks:
    total_marks += marks

average_marks = total_marks / len(students_marks)
highest_marks = max(students_marks)
lowest_marks = min(students_marks)

print(f"""
      total_marks: {total_marks}
      average_marks: {average_marks} 
      highest_marks: {highest_marks} 
      lowest_marks: {lowest_marks}
""")
