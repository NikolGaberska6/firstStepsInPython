import math
record_in_seconds = float(input())
disatance_in_meters = float(input())
time_in_second_for_one_meter = float(input())

disatance = disatance_in_meters // 15
delay = disatance * 12.5

all_time = (disatance_in_meters * time_in_second_for_one_meter) + delay

if all_time < record_in_seconds:
    print (f"Yes, he succeeded! The new world record is {all_time:.2f} seconds.")
else:
    needed_seconds = math.fabs(record_in_seconds - all_time)
    print(f"No, he failed! He was {needed_seconds:.2f} seconds slower.")