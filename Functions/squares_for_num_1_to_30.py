def squares(start_num, end_num):
    for num in range(start_num, end_num + 1):

       square = num ** 2

      # print(square, end=" ") #if we don't want to use lists
       list_of_squares.append(square)

    for idx in list_of_squares:
       print(idx, end=" ")


start_num = int(input())
end_num = int(input())
list_of_squares = []
squares(start_num, end_num)