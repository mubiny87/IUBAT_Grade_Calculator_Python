print("GPA CALCULATOR FOR IUBAT")
mid=float(input())
ct=float(input())
attendance=float(input())
presentation=float(input())
assignment=float(input())
final=float(input())

total=(mid*0.25+ct*0.10+attendance+presentation+assignment+final*0.5)

total=round(total,2)

if total>=80:
  grade = "A+"
  gpa = 4.00
elif total>=75:
  grade = "A"
  gpa = 3.75
elif total>=70:
  grade = "A-"
  gpa = 3.50
elif total>=65:
  grade = "B+"
  gpa = 3.25
elif total>=60:
  grade = "B"
  gpa = 3.00
elif total>=55:
  grade = "B-"
  gpa = 2.75
elif total>=50:
  grade = "C+"
  gpa = 2.50
elif total>=45:
  grade = "C"
  gpa = 2.25
elif total>=40:
  grade = "D"
  gpa = 2.00
else:
  grade = "F"
  gpa = 0.00

print(total)
print(grade)
print(gpa)
