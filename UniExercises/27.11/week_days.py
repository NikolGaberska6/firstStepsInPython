days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

try:
  number = int(input("Въведете цяло чило: "))
  if 1 <= number <= 7:
    day_based_on_number = days[number - 1]
    print(day_based_on_number)
except:
    print("Invalid number")