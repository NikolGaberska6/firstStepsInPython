all_steps = 0
steps_over = 0
is_true = True

while is_true:
    num_steps = input()
    if num_steps == "Going home":
        num_steps = float(input())
        all_steps += num_steps
    else:
     num_steps = float(num_steps)
     all_steps += num_steps
    if all_steps >= 10000:
        steps_over = all_steps - 10000
        print("Goal reached! Good job!")
        print(f"{steps_over:.0f} steps over the goal!")
        is_true = False

