import pandas

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

def not_blank(question, error_msg):
    valid = False

    while not valid:
        response = input(question)

        if response == "":
            print(error_msg)
        
        # credit: Ryan Ogilvy; for the whitespace checker
        elif str.isspace(response):
            print(error_msg)
        else:
            return response

# currency formatting function
def currency(x):
    return "${:.2f}".format(x)

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

# gets expenses and returns list with
# the data frame and subtotal
def get_expenses(var_fixed):
    # get dictionaries and lists

    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }
    # loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":

        print()
        # get name quantity and item
        item_name = not_blank("Item name: ",
                            " The component name can't be "
                            "blank")
        if item_name.lower() == "xxx":
            break
        
        if var_fixed == "variable":
            quantity = num_check("Quantity: ", int, "Please enter a whole number more than 0", 1)
        else:
            quantity = 1
        price = num_check("How much for a single item? $", float, "The price must be a number <more than 0>", 0.01)

        # add item quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index("Item")

    # Calculate cost of each component
    expense_frame["Cost"] = expense_frame["Quantity"]\
                            * expense_frame["Price"]

    # Find sub total
    sub_total = expense_frame["Cost"].sum()

    # Currency Formatting (uses currency function)
    add_dollars = ["Price", "Cost"]
    for item in add_dollars :
        expense_frame[item] = expense_frame[item].apply(currency)
    
    return [expense_frame, sub_total]

## prints expense frames
def expense_print(heading, frame, subtotal):
    print()
    print("*** {} Costs ***".format(heading))
    print(frame)
    print()
    print("{} Costs: ${:.2f}".format(heading, subtotal))
    return ""

def konami():
    print("looks like we got a gamer in the chat")
# Main routine goes here



# get product name
product_name = not_blank("Company name: ", "The company name can't be blank")

if product_name == "upupdowndownleftrightleftrightbastart":
    easter_egg = konami()
    
else:
    # get variable costs
    print()
    print("Please enter your variable costs below...")
    variable_expenses = get_expenses("variable")
    variable_frame = variable_expenses[0]
    variable_sub = variable_expenses[1]

    print()
    have_fixed = yes_no("Do you have fixed costs (y / n)? ")
    if have_fixed == "yes":

        #Get fixed costs
        fixed_expenses = get_expenses("fixed")
        # fixed_expenses = get_expenses("variable")
        fixed_frame = fixed_expenses[0]
        fixed_sub = fixed_expenses[1]
    else:
        fixed_sub = 0

    # ask user for profit goal

    # calculate recommended price

    # write data to file

    # *** Printing Area *** #

    print()
    print("*** Fund Raising - {} ***".format(product_name))
    print()
    expense_print("Variable", variable_frame, variable_sub)

    if have_fixed == "yes":
        expense_print("Fixed", fixed_frame[["Cost"]], fixed_sub)
