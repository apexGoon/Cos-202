print("=== PERSONAL POCKET CGPA CALCULATOR ===")

courses = int(input("Enter number of courses: "))

total_points = 0
total_units = 0

for i in range(courses):
    print(f"\nCourse {i+1}")

    unit = int(input("Course Unit: "))
    score = int(input("Score: "))

    if score >= 70:
        gp = 5
    elif score >= 60:
        gp = 4
    elif score >= 50:
        gp = 3
    elif score >= 45:
        gp = 2
    elif score >= 40:
        gp = 1
    else:
        gp = 0

    total_points += gp * unit
    total_units += unit

cgpa = total_points / total_units

print("\nTotal Units:", total_units)
print("Total Grade Points:", total_points)
print("CGPA:", round(cgpa, 2))
