num_unpleasured_grades = int(input())
exercise_name = input()
last_exercise = ""
bad_grades = 0
sum_of_grades = 0
num_of_grades = 0

while exercise_name != "Enough":
    grade = int(input())
    num_of_grades += 1
    sum_of_grades += grade
    if grade <= 4:
        bad_grades += 1
        if bad_grades == num_unpleasured_grades:
            print(f"You need a break, {bad_grades} poor grades.")
            break
    exercise_name = input()
    if exercise_name != "Enough":
        last_exercise = exercise_name

avarage = 0

if bad_grades < num_unpleasured_grades:
    avarage = sum_of_grades / num_of_grades
    print(f"Average score: {avarage:.2f}")
    print(f"Number of problems: {num_of_grades}")
    print(f"Last problem: {last_exercise}")
