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

get_int = num_check("How many dost thou needesteth? Pleaseth entyereth a numbereth moreth thaneth zeroeth.", int, "Please entereth aeth numbereth moreth thaneth zeroeth", 0)
get_cost = num_check("How much does it cost? $", float, "Please enter a number above 0", 0)
print("amount: ", get_int)
print("cost", get_cost)