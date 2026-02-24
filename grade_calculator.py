#taking input marks for 5 subjects
marks = []

for i in range(1, 6):
    subject_marks = float(input(f"Enter marks for Subject {i}: "))
    marks.append(subject_marks)

#displaying marks of each subject
print("\nMarks in each subject:")
for i in range(5):
    print(f"Subject {i+1}: {marks[i]}")

#calculating total marks
total=0
for i in marks:
    total+=i
print("\nTotal Marks:", total)

#calculating percentage
percentage = (total / 500) * 100
print("Percentage: ", percentage ,"%")

#Grade calculation
if 90 <= percentage <= 100:
    grade = "A+ (Outstanding)"
elif 80 <= percentage < 90:
    grade = "A (Excellent)"
elif 70 <= percentage < 80:
    grade = "B (Good)"
elif 60 <= percentage < 70:
    grade = "C (Average)"
elif 50 <= percentage < 60:
    grade = "D (Pass)"
else:
    grade = "F (Fail)"

print("Grade:", grade)

#Pass status
i = 0
pass_status = True

while i < len(marks):
    if marks[i] < 40:
        pass_status = False
        break
    i += 1

if pass_status:
    print("Result: Pass")
else:
    print("Result: Fail")