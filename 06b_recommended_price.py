import math


def num_check(question, num_type, error, low=None, high=None, exit_code=None):

    valid = False
    while not valid:
        try:
            response = input(question).lower()


            if response == exit_code:
                return response

            else:
                response = num_type(response)
 
            if low is not None and high is not None:
                if low <= response <= high:
                    return response
                else:
                    print(error)
                    print()
                    continue

            elif low is not None:
                if response >= low:
                    return response
                else:
                    print(error)
                    print()
                    continue

            elif high is not None:
                if response <= high:
                    return response
                else:
                    print(error)
                    print()
                    continue

            else:
                return response

        except ValueError:
            print(error)
            print()

def round_up(amount, round_to):
    return int(math.ceil(amount / round_to) * round_to)



# Main routine starts here
how_many = num_check("How many items? ", int, "Can't be zero or decimal" , 1)
total = num_check("Total costs? ", float, "More than 0", 0.01)
profit_goal = num_check("Profit Goal? ", float, "More than 0", 0.01)
round_to = num_check("Round to nearest...?", int, "Can't be 0 or decimal")

sales_needed = total + profit_goal

print("Total: ${:.2f}".format(total))
print("Profit Goal: ${:.2f}".format(profit_goal))

selling_price = sales_needed / how_many
print("Selling Price (Unrounded): ${:.2f}".format(selling_price))

recommended_price = round_up(selling_price, round_to)
print("Recommended Price: ${:.2f}".format(recommended_price))