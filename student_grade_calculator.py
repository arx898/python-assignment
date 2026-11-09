# Problem 1: Student Grade Calculator

name = input("Enter student name: ")

marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))

total = marks1 + marks2 + marks3
average = total / 3

if average >= 80:
    grade = "A+"
elif average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"

total_display = int(total) if total == int(total) else total

print()
print(f"Student Name: {name}")
print(f"Total Marks: {total_display}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
