deposit_sum = float(input())
deposit_term = int(input())
interest_rate_percentage = float(input())
annual_interest = deposit_sum * (interest_rate_percentage/100)
annual_interest_per_month = annual_interest /12
fullSum = deposit_sum + annual_interest_per_month * deposit_term



print(fullSum)