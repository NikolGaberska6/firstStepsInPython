start = int(input("Въведете първото число: "))
end = int(input("Въведете последното число: "))

for num in range(start, end+1):
    if num % 7 == 0:
        print(f"Първото число, кратно на 7, в интервала е: {num} ")
        break