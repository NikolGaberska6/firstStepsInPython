# Match case statement (switch): An alternative to use many 'elif' statements
#                                Execute some code if a value matches a 'case'
#                                Benefits: clear and syntax is more readable

from unittest import case

def day_of_the_week(day):
    if day == 1:
        return "Monday"
    elif day == 2:
        return "Tuesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    elif day == 6:
        return "Saturday"
    elif day == 7:
        return "Sunday"
    else:
        return "Error"
print(day_of_the_week(1))

#Match-case statement:
def day_of_the_week(day):
    match day:
     case 1:
        return "Monday"
     case 2:
        return "Tuesday"
     case 3:
        return "Wednesday"
     case 4:
         return "Thursday"
     case 5:
         return "Friday"
     case 6:
         return "Saturday"
     case 7:
         return "Sunday"
     case _:                  # 'case _' is the empty else
         return "Error"
print(day_of_the_week(2))

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return "Error"
print(is_weekend("Monday"))