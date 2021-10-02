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

    def __init__(self, item_name, quantity, description):
        self.item = {"Item": item_name}
        self.total = {"Quantity": quantity}
        self.desc = {"Description": description}


       


    def pattributes(self):
        print(self.item, self.total, self.desc)
        

    


    def add_description(self, item_description):
        self.desc = {'Description': item_description}
        print(self.desc)

    def add_item(self):

        cart.items.append(self)
        cart.total += 1





value = ""
while (value != "q"):

    print("MENU\n a - Add item\n d - Remove item\n u - Update item details\n r1 - Output all items in alphabetical order\n r2- Output all items by sorted by quantity (ascending)\n q - Quit")

    value = input("Please Select an option: ")


    if (value == "a"):

        new_item = (input("Please enter item name: "))
        quantity = (input("How many do you want to add?: "))
        description = ""
        

        item_name = new_item
        item_name = cart(new_item, quantity, description)
        item_name.add_item()



        


    if (value == "u"):
        item_name = (input("What item do you want to describe?: "))

        describe = item_name
        describe = cart.add_description(describe)
        
    if (value == "p"):
        item_name = (input("which attributes?: "))

        cart.pattributes(item_name)

        


    if(value == "d"):
        item_name = input("Please enter the item you want to delete: ")


    else:
        continue
        



print("See YA!")