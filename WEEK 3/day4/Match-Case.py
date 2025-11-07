# Match-case statement (swtich) : An alternative to using many 'elif' statements
# Execute some code if a value matches a 'case'
# Benefits: cleaner and sysntax is more readable

# def day_of_week(day):
#     match int(day):
#         case 1:
#             return "It is Sunday"
#         case 2:
#             return "It is Monday"
#         case 3:
#             return "It is Tuesday"
#         case 4:
#             return "It is Wednesday"
#         case 5:
#             return "It is Thursday"
#         case 6:
#             return "It is Friday"
#         case 7:
#             return "It is Saturday"
#         case _:
#             return "Invalid day"
#
# print(day_of_week("4"))

def is_weekend(day):
    match day:
        case "Monday":
            return False
        case "Tuesday":
            return False
        case "Wednesday":
            return False
        case "Thursday":
            return False
        case "Friday":
            return False
        case "Saturday":
            return True
        case "Sunday":
            return True
        case _:
            return False

print(is_weekend("Saturday"))