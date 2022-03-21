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

# Main routine goes here

# set up dict later

item_list = []
quantity_list = []
price_list = []

variable_dict = {
    "Item": item_list,
    "Quantity": quantity_list,
    "Price": price_list
}

# Get user data
product_name = not_blank("Company name: ", "The company name can't be blank")

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

    quantity = num_check("Quantity: ", int, "Please enter a whole number more than 0", 1)
    price = num_check("How much for a single item? $", float, "The price must be a number <more than 0>", 0.01)

    # add item quantity and price to lists
    item_list.append(item_name)
    quantity_list.append(quantity)
    price_list.append(price)

variable_frame = pandas.DataFrame(variable_dict)
variable = variable_frame.set_index("Item")

# Calculate cost of each component
variable_frame["Cost"] = variable_frame["Quantity"]\
                         * variable_frame["Price"]

# Find sub total
variable_sub = variable_frame["Cost"].sum()

# Currency Formatting (uses currency function)
add_dollars = ["Price", "Cost"]
for item in add_dollars :
    variable_frame[item] = variable_frame[item].apply(currency)

# *** Printing Area *** #

print(variable_frame)

print()

print("variable costs: ${:.2f}".format(variable_sub))