book_pages = int(input())
pages_per_hour = int(input())
num_days = int(input())
full_time_for_reading = book_pages/pages_per_hour
full_num_days = full_time_for_reading/num_days
print(int(full_num_days))