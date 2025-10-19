type_projection = input()
num_rows = int(input())
num_columns = int(input())
ticket_price = 0

if type_projection == "Normal":
    ticket_price = 7.50
elif type_projection == "Premiere":
    ticket_price = 12.00
elif type_projection == "Discount":
    ticket_price = 5.00

full_price = num_columns * num_rows * ticket_price
print(f"{full_price:.2f} leva")
