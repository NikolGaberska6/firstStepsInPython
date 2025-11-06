width = int(input())
height = int(input())
all_pieces = width * height

while all_pieces > 0:
    took_pieces = input()
    if took_pieces == "STOP":
        print(f"{all_pieces} pieces are left.")
        break
    else:
        took_pieces = int(took_pieces)
        all_pieces -= took_pieces

if all_pieces <= 0:
    print(f"No more cake left! You need {abs(all_pieces)} pieces more.")