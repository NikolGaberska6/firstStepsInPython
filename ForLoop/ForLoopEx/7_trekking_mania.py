num_groups = int(input())
all_people = 0
people_for_musala = 0
people_for_monblan = 0
people_for_kilimandjaro = 0
people_for_K2 = 0
people_for_everest = 0

for group in range(num_groups):
    num_people_in_group = int(input())
    all_people += num_people_in_group
    if num_people_in_group <= 5:
        people_for_musala += num_people_in_group
    elif 6 <= num_people_in_group <= 12:
        people_for_monblan += num_people_in_group
    elif 13 <= num_people_in_group <= 25:
        people_for_kilimandjaro += num_people_in_group
    elif 26 <= num_people_in_group <= 40:
        people_for_K2 += num_people_in_group
    elif 41 <= num_people_in_group:
        people_for_everest += num_people_in_group

percent_musala = people_for_musala / all_people * 100
percent_monblan = people_for_monblan / all_people * 100
percent_kilimandjaro = people_for_kilimandjaro / all_people * 100
percent_K2 = people_for_K2 / all_people * 100
percent_everest = people_for_everest / all_people * 100

print(f"{percent_musala:.2f}%")
print(f"{percent_monblan:.2f}%")
print(f"{percent_kilimandjaro:.2f}%")
print(f"{percent_K2:.2f}%")
print(f"{percent_everest:.2f}%")
