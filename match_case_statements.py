# match-case statement (switch) = an alternative to using many 'elif' statements
# execute some code if a value matches a 'case'
# benefits: cleaner and syntax is more readable

def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7: 
            return "It is Saturday"
        case _: # _ is our else statement
            return "Not a valid day"

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        # case "Sunday":
        #     return True
        # case "Monday":
        #     return False
        # case "Tuesday":
        #     return False
        # case "Wednesday":
        #     return False
        # case "Thursday":
        #     return False
        # case "Friday":
        #     return False
        # case "Saturday": 
        #     return True
        case _: # _ is our else statement
            return False

print (day_of_week(2))
print (is_weekend("Sunday"))