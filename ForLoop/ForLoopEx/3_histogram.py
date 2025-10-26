n = int(input())
p1_nums = 0
p2_nums = 0
p3_nums = 0
p4_nums = 0
p5_nums = 0

for idx in range(n):
    new_number = int(input())
    if 0 <= new_number < 200:
        p1_nums += 1
    elif 200 <= new_number <= 399:
        p2_nums += 1
    elif 400 <= new_number <= 599:
        p3_nums += 1
    elif 600 <= new_number <= 799:
        p4_nums += 1
    elif new_number >= 800:
        p5_nums += 1

p1_percentage = p1_nums/n * 100
p2_percentage = p2_nums/n * 100
p3_percentage = p3_nums/n * 100
p4_percentage = p4_nums/n * 100
p5_percentage = p5_nums/n * 100

print(f"{p1_percentage:.2f}%")
print(f"{p2_percentage:.2f}%")
print(f"{p3_percentage:.2f}%")
print(f"{p4_percentage:.2f}%")
print(f"{p5_percentage:.2f}%")

