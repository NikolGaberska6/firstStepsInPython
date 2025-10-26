name_of_actor = input()
point_from_academy = float(input())
num_raters = int(input())
name_lenght = 0
all_points = 0

for raters in range(num_raters):
    name_of_the_rater = input()
    points_from_rater = float(input())
    name_lenght = len(name_of_the_rater)
    all_points_from_rater = (name_lenght * points_from_rater)/2
    all_points = all_points_from_rater + point_from_academy
    point_from_academy = all_points

if all_points >= 1250.5:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {all_points:.1f}! ")
else:
    diff = 1250.5 - all_points
    print(f"Sorry, {name_of_actor} you need {diff:.1f} more! ")