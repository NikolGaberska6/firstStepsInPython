petur_budget = float(input())
num_video_cards = int(input())
num_procesors = int(input())
num_ram_memory = int(input())

price_for_video_cards = num_video_cards * 250
processor_price = 35/100 * price_for_video_cards
price_for_processors = processor_price * num_procesors
ram_memory_price = 10/100 * price_for_video_cards
price_for_ram_memory = ram_memory_price * num_ram_memory
final_sum = price_for_video_cards + price_for_processors + price_for_ram_memory
discount = 0

if num_video_cards > num_procesors:
    discount =  15/100 * final_sum
    final_sum = final_sum - discount
else:
    final_sum = final_sum
    discount = 0

if petur_budget >= final_sum:
    left_sum = petur_budget - final_sum
    print(f"You have {left_sum:.2f} leva left!")
else:
    left_sum = final_sum - petur_budget
    print (f"Not enough money! You need {left_sum:.2f} leva more!")