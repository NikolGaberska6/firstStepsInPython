points = int(input())
bonus_points = 0

if 0 <= points <= 100:
    bonus_points = 5
elif 100 < points <= 1000:
    bonus_points = 20/100 * points
elif points > 1000:
    bonus_points = 10/100 * points

if points % 2 == 0:
    bonus_points = bonus_points + 1
elif points % 10 == 5:
    bonus_points = bonus_points + 2

sum = points + bonus_points
print(bonus_points)
print(sum)