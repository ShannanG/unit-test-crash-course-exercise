'''def divide():
    numerator = int(input("Please enter your numerator: "))
    denominator = int(input("Please enter your denominator: "))
    print(numerator/denominator)'''

##### REFACTORED CODE TO TEST #####
class IncorrectInputError(Exception):
    pass
def divide(num1, num2):
    try:
        total = num1/num2
        print(total)
        return total
    except TypeError:
        raise IncorrectInputError("Please enter a numeric value")
    except ZeroDivisionError:
        raise ValueError("You cannot divide by zero. Please enter a number above 0.")


# numerator = int(input("Please enter your numerator: "))
# denominator = int(input("Please enter your denominator: "))
# divide(numerator, denominator)

# identify two possible error states - 1 custom
# Value Error and custom: IncorrectInput
# Write test file - keep to conventions, one valid, one boundary, one invalid

