students = {"Bob": 85, "Dimeji": 100, "David": 78, "Alfie": 54, "Michael": 100}
total = 0

for score in students.values():
    total+=score

average = total/len(students)
print("Class average is ", average)

top_student=max(students, key=students.get)
bottom_student=min(students, key=students.get)

print("The student with the highest score is ",top_student, students[top_student])
print("Bottom scorer is this guy : ", bottom_student, students[bottom_student])

search_name = input("Enter one of the student's name: ")
grade = students.get(search_name)

if grade is not None:
    print(search_name, "scored", grade)
else:
    print("student does not exist?")