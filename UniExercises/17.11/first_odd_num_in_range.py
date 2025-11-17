start = int(input("Въведете първото число: "))
end = int(input("Въведете последното число: "))

for num in range(start, end+1):
    if num % 2 != 0:
        print(f"Първото нечетно число в интервала {start}, {end} е: {num}")
        break