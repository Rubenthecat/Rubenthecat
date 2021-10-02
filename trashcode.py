
        item_desc = (input("Describe this item: "))
        quantity = (input("How many do you want to add?: "))

class item:
    
        def __init__(self, item_name, quantity, item_desc):
            self.item = ""
            self.total = 0
            self.description = ""


        def item_desc(self, description):
            self.description = description

        def item_quantity(self, item_name):
            
            print(self.total(item_name))
            


        desc = input("Add a Description? Y/N: ")
        if (desc == "y" or desc == "Y"):
            D = input("Describe the item: ")
            
            item_name = cart.add_description(item_name, D)
            cart.items.append(item_name)
            continue

        if (desc != "y" or desc != "Y"):
            print("No Description Added")
            cart.items.append(item_name)
            continue   
