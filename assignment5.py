print("================================")
print("       STUDENT MARK ANALYZER")
print("================================")

student_name = input("Enter student name: ")

marks = []

subjects = int(input("How many subjects? "))

for i in range(subjects):

    mark = float(input("Enter marks for subject " + str(i + 1) + ": "))

    if mark < 0 or mark > 100:
        print("Invalid marks. Enter a value between 0 and 100.")
        continue

    marks.append(mark)

if len(marks) > 0:

    total = sum(marks)
    percentage = total / len(marks)

    highest = max(marks)
    lowest = min(marks)

    print("\n========== STUDENT RESULT ==========")

    print("Student name:", student_name)
    print("Number of subjects:", len(marks))
    print("Total marks:", total)
    print("Percentage:", round(percentage, 2), "%")
    print("Highest mark:", highest)
    print("Lowest mark:", lowest)

    if percentage >= 90:
        grade = "A+"

    elif percentage >= 80:
        grade = "A"

    elif percentage >= 70:
        grade = "B"

    elif percentage >= 60:
        grade = "C"

    elif percentage >= 50:
        grade = "D"

    else:
        grade = "F"

    print("Grade:", grade)

    failed = False

    for mark in marks:

        if mark < 35:
            failed = True

    if failed:
        print("Result: FAIL")

    else:
        print("Result: PASS")

else:
    print("\nNo valid marks were entered.")

print("\nAnalysis complete!")
