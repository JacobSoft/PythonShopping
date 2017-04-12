# Python:   2.7.13
#
# Author:   Jake Clark
#
# Purpose:  Create a shopping system. It allows customers to pick one of several items
#           and checkout.
#
#
#

##Let's Pop Some Tags:

def start(items="",total=0,name="",choice=0,counter=0): #set each variable to blank or zero
    #get their name
    name = describe_shop(name)
    items,total,name,choice = items_total(items,total,name,choice,counter)

def describe_shop(name):
    stop = True
    while stop:
        if name == "":
            name = raw_input("\nWhat is your full name? ").title()
            if name !="": #if we have been given a name, greet the guest below:
                print("\nWelcome to our shop, {}!".format(name))
                print("\nWe have a few rare items you may want to purchase. \n\nLet's go over our entire selection together: ")
                for items in rare_items: #prints each item in the rare_items dictionary to a new line so customer may see options
                    print items
                print("\nJust answer 'y' for 'yes' or 'n' for 'no' for each item, depending on if you'd like to purchase it.")    
                stop = False
            else:
                print ("\nI'm sorry, that's not recognized. GIVE US YOUR NAME NOW.")
                describe_shop(name)
    return name

#create dictionary of items in the shop and their price value
rare_items={'Fossilized Golden Mole: $200.50':200.50,
            'Crunchy Dead-ish Moth: $100.00':100.00,
            'Irradiated Platypus Tooth: $705.25':705.25,
            'Bottled Echidna Fetus: $6.00':6.00,
            'Bacon-Wrapped Gnats: $2008.40':2008.40
            }
#create a variable for each item so it can be used in the following functions
item0 = rare_items['Fossilized Golden Mole: $200.50']
item1 = rare_items['Crunchy Dead-ish Moth: $100.00']
item2 = rare_items['Irradiated Platypus Tooth: $705.25']
item3 = rare_items['Bottled Echidna Fetus: $6.00']
item4 = rare_items['Bacon-Wrapped Gnats: $2008.40']

rare_cart = [] #creates empty list for customer's purchase items to go into

def items_total(items,total,name,choice,counter):
    stop = True
    while stop:
        pick = raw_input ("\nOur first item on the shelf! \n\nFossilized Golden Mole: $200.50. \n\nWould you like to purchase this? y/n ")
        if pick == "y":
            choice = item0
            pick2 = raw_input ("\nHow many would you like? We'd prefer not to split items in half, but you may request it if you must. Enter a number: ").format(total)
            total = float(choice)*float(pick2)
            counter += 1 #count how many times they opt to purchase something
            items = ("Fossilized Golden Mole")
            rare_cart.append("Fossilized Golden Mole") #appends empty list to add this item if chosen by customer.
            next_item(items,total,name,choice,counter)
            stop = False
        elif pick == "n":
            total = 0
            next_item(items,total,name,choice,counter)
        else: #catch when user inputs something other than a 'y' or 'n'
            print ("\nI'm sorry, that's not recognized. Maybe try following the instructions and type either 'Y' or 'N' and press enter.") #scold user for wrong input
            items_total(items,total,name,choice,counter) #loop back to beginning of function

def next_item(items,total,name,choice,counter):
    stop = True
    while stop:
        if total !=0:
            show_total(items,total,name,choice,counter)
        pick = raw_input ("\nOur second item! \n\nCrunchy Dead-ish Moth: $100. \n\nWould you like to purchase this? y/n ")
        if pick == "y":
            pick2 = raw_input ("\nHow many would you like? We'd prefer not to split items in half, but you may request it if you must. Enter a number: ").format(total)
            choice1 = float(item1)*float(pick2)
            total = total + choice1
            counter += 1
            items = items + (", ") + ("Crunchy Dead-ish Moth")
            rare_cart.append("Crunchy Dead-ish Moth")
            next_item2(items,total,name,choice,counter)
            stop = False
        elif pick == "n":
            next_item2(items,total,name,choice,counter)
        else:    
            print ("\nIT'S SIMPLE, PUNK. YOU EITHER TYPE A 'Y' OR AN 'N' AND PRESS ENTER.")
            next_item(items,total,name,choice,counter)

def next_item2(items,total,name,choice,counter):
    stop = True
    while stop:
        if total !=0:
            show_total(items,total,name,choice,counter)
        pick = raw_input ("\nOur third item! \n\nIrradiated Platypus Tooth: $705.25. \n\nWould you like to purchase this? y/n ")
        if pick == "y":
            pick2 = raw_input ("\nHow many would you like? We'd prefer not to split items in half, but you may request it if you must. Enter a number: ").format(total)
            choice2 = float(item2)*float(pick2)
            total = total + choice2
            counter += 1
            items = items + (", ") + ("Irradiated Platypus Tooth")
            rare_cart.append("Irradiated Platypus Tooth")
            next_item3(items,total,name,choice,counter)
            stop = False
        elif pick == "n":
            next_item3(items,total,name,choice,counter)
        else:    
            print ("\nIT'S SIMPLE, PUNK. YOU EITHER TYPE A 'Y' OR AN 'N' AND PRESS ENTER.")
            next_item2(items,total,name,choice,counter)    

def next_item3(items,total,name,choice,counter):
    stop = True
    while stop:
        if total !=0:
            show_total(items,total,name,choice,counter)
        pick = raw_input ("\nOur fourth item! \n\nBottled Echidna Fetus: $6.00. \n\nWould you like to purchase this? y/n ")
        if pick == "y":
            pick2 = raw_input ("\nHow many would you like? We'd prefer not to split items in half, but you may request it if you must. Enter a number: ").format(total)
            choice3 = float(item3)*float(pick2)
            total = total + choice3
            counter += 1
            items = items + (", ") + ("Bottled Echidna Fetus")
            rare_cart.append("Bottled Echidna Fetus")
            next_item4(items,total,name,choice,counter)
            stop = False
        elif pick == "n":
            next_item4(items,total,name,choice,counter)
        else:    
            print ("\nIT'S SIMPLE, PUNK. YOU EITHER TYPE A 'Y' OR AN 'N' AND PRESS ENTER.")
            next_item3(items,total,name,choice,counter)

def next_item4(items,total,name,choice,counter):
    stop = True
    while stop:
        if total !=0:
            show_total(items,total,name,choice,counter)
        pick = raw_input ("\nOur fifth item! \n\nBacon-Wrapped Gnats: $2008.40. \n\nWould you like to purchase this? y/n ")
        if pick == "y":
            pick2 = raw_input ("\nHow many would you like? We'd prefer not to split items in half, but you may request it if you must. Enter a number: ").format(total)
            choice4 = float(item4)*float(pick2)
            total = total + choice4
            counter += 1
            items = items + (", ") + ("Bacon-Wrapped Gnats")
            rare_cart.append("Bacon-Wrapped Gnats")
            view_cart(items,total,name,choice,counter)
            stop = False
        elif pick == "n" and counter >= 1: #use of 'and' statement to combine these two conditions
            view_cart(items,total,name,choice,counter)
        elif pick == "n" and counter < 1: #if user has no items in cart, send to end_this function
            end_this(items,total,name,choice,counter)
        else:    
            print ("\nIT'S SIMPLE, PUNK. YOU EITHER TYPE A 'Y' OR AN 'N' AND PRESS ENTER.")
            next_item4(items,total,name,choice,counter)

def end_this(items,total,name,choice,counter): #if user has no items in cart, this function scolds them and closes the program.
    stop = True
    while stop:
        if counter < 1:
            print("You sure say 'NO!' a lot! Thanks for nothing.") #they're horrible customers
            exit()
        elif counter >=1:
            view_cart(items,total,name,choice,counter)
        

def view_cart(items,total,name,choice,counter): #checkout function
    print ("\n{}, your cart is stocked and ready! \nHere's what you chose:".format(name))
    for item in rare_cart: #print list of items in cart on separate lines
        print item
    print ("\nFor a grand total of {}".format(total)) #give total
    if counter >=2: #reward the customer for buying 2 or more items and being so frivolous
        print ("You sure say 'YES!' a lot. {} times to be exact. Thanks for shopping!".format(counter)) 
    else: #else statement to scold the customer for being frugal if they said yes less than two times.
        print ("You sure say 'NO!' a lot! Thanks for only buying ONE THING.")
    #offer opportunity to split payments between two cards (which will require division operation):    
    payment = raw_input("\n{}, we only accept credit cards for payment. Would you like to split your payment between more than one card? y/n ".format(name))
    if payment == "y":
        paymentcount = raw_input("\nHow many cards would you like to use? Enter a number: ") #input card quantity
        payments = float(total)/float(paymentcount)
        print ("Partial payment due: $" + str(payments) + "\nTotal payment due: $" + str(total)) #give partial payment and total amounts
        enter_payment_deets(items,total,name,choice,counter) #send to payment function
    if payment == "n":
        payments = float(total) #if they just want to use one card, show them the total:
        print ("Payment due: $" + str(payments))
        enter_payment_deets(items,total,name,choice,counter) #send to payment function
    else:    
        print ("\nYOU ARE TERRIBLE AT THIS. YOU EITHER TYPE A 'Y' OR AN 'N' AND PRESS ENTER.") #scold them for using the wrong input again.
        view_cart(items,total,name,choice,counter)

def enter_payment_deets(items,total,name,choice,counter): #function to collect payment info
    print ("\n{}, please enter your card info below:".format(name))
    card_number = raw_input("\nCard number: ")
    card_exp = raw_input("\nCard exp: ")
    card_cvv = raw_input("\nCVV: ")
    card_billing = raw_input("\nBilling zip: ")
    print ("\nThank you! Do you have another card to enter?") #ask if they have more cards to enter
    more_cards = raw_input("\ny/n")
    if more_cards == "y": #if yes, reloop this function
        enter_payment_deets(items,total,name,choice,counter)
    elif more_cards == "n": #if no, thank for payment and exit program.
        print ("\nThank you for finalizing payment, {}! We hope you enjoyed this tedious shopping experience. Until next time!".format(name))
        exit()
    else:    
        print ("\nIT'S SIMPLE, PUNK. YOU EITHER PUT A 'Y' OR AN 'N' IN.")
        enter_payment_deets(items,total,name,choice,counter)

def show_total(items,total,name,choice,counter): #prints running total and items in rare_cart after every selection.
    print ("\n{}, you currently have in your cart:".format(name))
    for item in rare_cart:
        print ("\n") + item +("\n-------------------------")
    print ("\nfor a total of ${}".format(total))


if __name__ == "__main__":
    start()
