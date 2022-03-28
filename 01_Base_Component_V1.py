import pandas
import time
from turtle import Turtle

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

# kirbo
def kirbo():
    count = 0
  
    while count != 10000:
        count += 8
        print("kirbo #{}".format(count))
    myTurtle = Turtle()
    myTurtle.hideturtle()
    myTurtle.setpos(-200,200)
    myTurtle.pos()
    side = 20
    #color pixel method
    def square(color):
        myTurtle.speed(5000)
        myTurtle.color(color)
        myTurtle.begin_fill()
        for i in range(4):
            myTurtle.forward(side)
            myTurtle.right(90)
        myTurtle.end_fill()
        myTurtle.forward(side)
        
    #next row method, doing rows from top to bottom
    def nextRow(numSquares):
        myTurtle.speed(5000)
        myTurtle.penup()
        myTurtle.back(numSquares * side)
        myTurtle.right(90)
        myTurtle.forward(side)
        myTurtle.left(90)
        myTurtle.pendown()
        
    # prints the row of pixels that color
    def row(colors,numbers):
        myTurtle.speed(5000)
        numsquares = 0;
        for i in range(len(colors)):
            for i2 in range(numbers[i]):
                square(colors[i])
            numsquares += numbers[i]
        nextRow(numsquares) # reset the cursor


    myTurtle.speed(5000)   
    # colors we have
    # colors = ["white" ,"black", "pink", "deeppink"]
    pink = "#FF99CF"
    darkpink = "#B54365"
    # row 1
    colors = ["white", "black", "white", "black", "white"]
    numbers = [ 2, 2, 1, 5, 6]
    row(colors,numbers)
    # row 2
    colors = ["white", "black", pink, "black", pink, "black", "white"]
    numbers = [ 1, 1, 2, 1, 5, 2, 4]
    row(colors,numbers)
    # row 3 bppbppppppppbwww
    colors = ["black", pink, "black", pink, "black", "white"]
    numbers = [ 1, 2, 1, 8, 1, 3]
    row(colors,numbers)
    # row 4 bpppppbpbppppbww
    for r in range(2): # row 4 and 5 are the same
        colors = ["black", pink, "black", pink, "black", pink, "black", "white"]
        numbers = [ 1, 5, 1, 1, 1, 4, 1, 2]
        row(colors,numbers)
    # row 6 bpppppbpbpppppbw
    colors = ["black", pink, "black", pink, "black", pink, "black", "white"]
    numbers = [ 1, 5, 1, 1, 1, 5, 1, 1]
    row(colors,numbers)
    # row 7 bpppddpppddppppb
    colors = ["black", pink, darkpink, pink, darkpink, pink, "black"]
    numbers = [ 1, 3, 2, 3, 2, 4, 1]
    row(colors,numbers)
    # row 8 bppppppbpppppppb
    colors = ["black", pink, "black", pink, "black"]
    numbers = [ 1, 6, 1, 7, 1]
    row(colors,numbers)
    # row 9 wbpppppbpppppppb
    colors = ["white", "black", pink, "black", pink, "black"]
    numbers = [ 1, 1, 5, 1, 7, 1]
    row(colors,numbers)
    # row 10 wbppppppppppbbbw
    colors = ["white", "black", pink, "black", "white"]
    numbers = [ 1, 1, 10, 3, 1]
    row(colors,numbers)
    # row 11 wbpppppppppbdddb
    colors = ["white", "black", pink, "black", darkpink, "black"]
    numbers = [ 1, 1,9, 1, 3, 1]
    row(colors,numbers)
    # row 12 wwbpppppppbddddb
    colors = ["white", "black", pink, "black", darkpink, "black"]
    numbers = [ 2, 1, 7, 1, 4, 1]
    row(colors,numbers)
    # row 13  wwbbppppppbddddb
    colors = ["white", "black", pink, "black", darkpink, "black"]
    numbers = [ 2, 2, 6, 1, 4, 1]
    row(colors,numbers)
    # row 14 wbddbbpppbddddbw
    colors = ["white", "black", darkpink, "black", pink, "black", darkpink, "black", "white"]
    numbers = [ 1, 1, 2, 2, 3, 1, 4, 1, 1]
    row(colors,numbers)
    # row 15 bdddddbbbbbddbww
    colors = ["black", darkpink, "black", darkpink, "black", "white"]
    numbers = [ 1, 5, 5, 2, 1, 2]
    row(colors,numbers)
    # row 16 wbbbbbbwwwbbbwww
    colors = ["white", "black", "white", "black", "white"]
    numbers = [ 1, 6, 3, 3, 3]
    row(colors,numbers)
    time.sleep(10)

# upupdowndownleftrightleftrightbastart
def konami():

    print()
    time.sleep(1.5)
    print("***** In honor of the late T.V. *****")
    print()
    time.sleep(1.5)
    print("1. The Godfather")
    print()
    time.sleep(1.5)
    print("2. Goodfellas")
    print()
    time.sleep(1.5)
    print("3. The Wolf Of Wall Street")
    print()
    time.sleep(1.5)
    print("4. The Irishman")
    print()
    time.sleep(1.5)
    print("5. The Social Network")
    time.sleep(1.5)
    print("(tHE bIG zUCC)")
    time.sleep(1.5)
    print("Like did you even see that picture of him with the sunscreen?")
    time.sleep(1.5)
    print("Bro isn't even human at this point")
    time.sleep(1.5)
    print("*cough cough*")
    time.sleep(1.5)
    print("anyway, back to the list")
    print()
    time.sleep(1.5)
    print("6. Scarface")
    print()
    time.sleep(1.5)
    print("7. Catch me if you Can")
    print()
    time.sleep(1.5)
    print("8. The Dark Knight")
    print()
    time.sleep(1.5)
    print("9. Into the Spider Verse")
    print()
    time.sleep(1.5)
    print("10. Baby Driver")
    print()
    time.sleep(10)
    print("(gamer)")
    print()
# Main routine goes here



# get product name
product_name = not_blank("Company name: ", "The company name can't be blank")

if product_name == "upupdowndownleftrightleftrightbastart":
    easter_egg = konami()

elif product_name == "kirbo":
    kirbo()
    
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
