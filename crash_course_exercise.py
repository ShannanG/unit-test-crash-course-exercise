'''def divide():
    numerator = int(input("Please enter your numerator: "))
    denominator = int(input("Please enter your denominator: "))
    print(numerator/denominator)'''

##### REFACTORED CODE TO TEST #####
class IncorrectInputError(Exception):
    pass
def divide(num1, num2):
    try:
        is_int = num1 / num2
        total = num1/num2
        print(total)
        return total
    except TypeError:
        raise IncorrectInputError("Enter numbers, not words")



# numerator = int(input("Please enter your numerator: "))
# denominator = int(input("Please enter your denominator: "))
# divide(numerator, denominator)

# identify two possible error states - 1 custom
# Value Error and custom: IncorrectInput
# Write test file - keep to conventions, one valid, one boundary, one invalid

