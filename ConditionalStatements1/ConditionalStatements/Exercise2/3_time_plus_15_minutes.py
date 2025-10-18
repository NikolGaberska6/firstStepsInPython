hour = int(input())
minutes = int(input())

final_minutes = minutes + 15 #50 + 15 = 65

if final_minutes >= 60:
    hour = hour + 1
    minutes = final_minutes - 60
    if hour > 23:
        hour = 0
else:
    hour = hour
    minutes = minutes + 15

print(f"{hour}:{minutes:02d}")