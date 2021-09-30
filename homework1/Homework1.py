import mysql.connector
from mysql.connector import Error

#Importing functions from SQL python file followed from class.
from SQL import execute_query 
from SQL import create_connection 
from SQL import execute_read_query
import datetime
from datetime import date


#Initialize Cart as empty List


#Prints the menu options using \n to indicate a new line after every option.


class cart:
    items = []
    total = 0

    def __init__(self):
        self.item = ""
        self.total = 0
        self.description = ""
        

    

    def add_item(item_name):
        cart.items.append(item_name)
        cart.total += 1

        
        print("cart.items")
        print(cart.items)






value = ""
while (value != "q"):

    print("MENU\n a - Add item\n d - Remove item\n u - Update item details\n r1 - Output all items in alphabetical order\n r2- Output all items by sorted by quantity (ascending)\n q - Quit")

    value = input("Please Select an option: ")


    if (value == "a"):

        item_name = (input("Please enter item name: "))
        
        cart.add_item(item_name)





    if(value == "d"):
        item_name = input("Please enter the item you want to delete: ")


    else:
        print("not coded yet")
        


print("See YA!")