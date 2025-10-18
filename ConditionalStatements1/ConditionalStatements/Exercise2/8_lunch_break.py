import math
from math import ceil

serial_name = input()
episode_long = int(input())
break_long = int(input())

time_for_lunch = 1/8 * break_long
time_for_something = 1/4 * break_long

left_time = break_long - (time_for_something + time_for_lunch)

if left_time >= episode_long:
    time = left_time - episode_long
    print(f"You have enough time to watch {serial_name} and left with {math.ceil(time)} minutes free time.")
else:
    time = episode_long - left_time
    print(f"You don't have enough time to watch {serial_name}, you need {math.ceil(time)} more minutes.")