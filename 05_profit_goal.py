# functions go here


# checks that user has entered yes / no to a question
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please input yes / no")


def profit_goal(total_costs, error):

    # initialise variables and error message
    error = "Please enter a valid profit goal\n"

    valid = False
    while not valid:

        # ask for profit goal...
        response = input("What is your profit goal (eg $500 or 50%")

        # if contains both % and $, error and loop
        if response[0] == "$" and response[-1] == "%":
            print(error)
            continue
        # check response if first character is $...
        elif response[0] == "$":
            profit_type = "$"
            # get amount (everything after $)
            amount = response [1:]

        #check if last character is %
        elif response[-1] == "%":
            profit_type = "%"
            # Get amount (everything before the %)
            amount = response[:-1]
        else:
            # set response to amount for now
            profit_type = "unknown"
            amount = response
        
        try:
            #check amount is a number more than zero
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue
        
        except ValueError:
            print(error)
            continue
            
        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no("Do you mean ${:.2f}. ie {:.2f} dollars?, y/n ".format(amount, amount))

            # set profit goal type based on user answer above
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"
        
        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no("Do you mean {}%?, y/n".format(amount))
            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"
        
        # return profit goal to main routine
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal
