num_tournaments = int(input())
starting_point = int(input())
tournaments_points = 0
num_won_tournaments = 0

for tournaments in range(num_tournaments):
    stage = input()
    if stage == "W":
        num_won_tournaments += 1
        tournaments_points += 2000
    elif stage == "F":
        tournaments_points += 1200
    elif stage == "SF":
        tournaments_points += 720

all_points = tournaments_points + starting_point

print(f"Final points: {all_points}")
average_points = tournaments_points // num_tournaments
print(f"Average points: {average_points}")
won_tournaments_percent = num_won_tournaments / num_tournaments * 100
print(f"{won_tournaments_percent:.2f}%")