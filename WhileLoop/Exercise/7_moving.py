width = int(input())
length = int(input())
height = int(input())
took_space = 0
left_space = 0

free_space = width * length * height

while free_space > left_space:
    num_bagage = input()
    if num_bagage == "Done":
        print(f"{abs(took_space)} Cubic meters left.")
        break
    else:
        num_bagage = int(num_bagage)
        took_space += num_bagage
        free_space -= num_bagage

if num_bagage != "Done":
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
