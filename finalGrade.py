# def finalGrade(grade, completed_projects):
#     if grade > 90 or completed_projects > 10:
#         return 100
#     elif grade > 75 and completed_projects >= 5:
#         return 90
#     elif grade > 50 and completed_projects >= 2:
#         return 75
#     return 0


# print(finalGrade(100, 12))

# def same_case(a, b):
#     if (a.islower() and b.islower()) or (a.isupper() and b.isupper()):
#         return 1
#     elif not a.isalpha() or not b.isalpha():
#         return -1
#     return 0

# print(same_case('A', '>'))

def BMI(weight, height):
    bmi = weight/(height ** height)
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25:
        return "Normal"
    elif bmi <= 30:
        return "Overweight"
    elif bmi > 30:
        return "Obese"


print(BMI(25, 5))
