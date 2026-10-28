students = []

for i in range(5):
    print("Student", i + 1)

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    hours = float(input("Enter study hours: "))
    score = float(input("Enter Python score: "))

    student = {
        "name": name,
        "age": age,
        "hours": hours,
        "score": score
    }

    students.append(student)

def average_score():
    total = 0

    for student in students:
        total = total + student["score"]

    return total / len(students)

grades = ("A", "B", "C", "D", "F")

passing = 0
failing = 0

print("Student report")

grades={
    "A": "Excellent",
    "B": "Good",
    "C": "Pass",
    "D": "Fail"
}

for student in students:
    score = student["score"]

    if score >= 80:
        grade = grades["A"]
    elif score >= 60:
        grade = grades["B"]
    elif score >= 40:
        grade = grades["C"]
    else:
        grade = grades["D"]

    if score >= 40:
        result = "Pass"
        passing = passing + 1
    else:
        result = "Fail"
        failing = failing + 1

    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Study Hours:", student["hours"])
    print("Score:", score)
    print("Grade:", grade)
    print("Result:", result)

print("Total students:", len(students))
print("Average score:", round(average_score(), 2))
print("Passing students:", passing)
print("Failing students:", failing)
print("Grade categories:", grades)






