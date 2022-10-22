# Use Python 3.x or higher interpreter for output per terminal. Otherwise rare characters may appear or throw errors of type charset = "UTF-8"


def setRemainder():
    remainder = 0
    return 

# The previous remainder is moved 17 places to the left and added in original number
def addDividendToRest (p_remainder, p_digit_multiplier, p_original_number):
    return (p_remainder * p_digit_multiplier) + p_original_number

def newRemainder(p_remainder_plus_original_number, p_divder):
    return p_remainder_plus_original_number % p_divder

def addRemainderToList(remainders_list_str, remainder_as_list_item):
    return remainders_list_str + str(remainder_as_list_item)

def main():

    original_number = 58184241583791680
    digit_multiplier = 100000000000000000
    divder = 2017
    remainder_not_repeated = True
    iteration_counter = 0
    max_iter_check = 10000
    remainder = 0
    remainder_as_list_item = [remainder]
    remainders_list_str = str(remainder_as_list_item)


    print("This program solves the challenge of finding the remainder (modulus) \nof the division by the number 58184241583791680 concatenated 58184241583791680 times \n (almost 3,390,000,000,000,000,000,000,000,000,000,000 digits) \n and the number 2017")


    while remainder_not_repeated:
        iteration_counter+=1
        remainder_plus_original_number = addDividendToRest(remainder, digit_multiplier, original_number)
        remainder = newRemainder(remainder_plus_original_number, divder)
        remainder_as_list_item = [remainder]
        if str(remainder_as_list_item) in remainders_list_str or iteration_counter > max_iter_check: # The counter is evaluated to avoid a possible infinite cycle
            remainder_not_repeated = False
        else:
            remainders_list_str = addRemainderToList(remainders_list_str, remainder_as_list_item)

    remaining_iterations = original_number % iteration_counter
    setRemainder()


    for i in range(0,remaining_iterations):
        remainder_plus_original_number = addDividendToRest(remainder, digit_multiplier, original_number)
        remainder = newRemainder(remainder_plus_original_number, divder)

    print("\nThe final Remainder or Module of the division is: ", remainder)

    print("\n End of Program")

if __name__ == "__main__":
    main()