inventory = {"a":3 , "b":3}

def add_item(item, quantity):
    if item in inventory:
        inventory[item]=inventory[item]+quantity
    else:
        inventory[item]=quantity
    print(f"Added {item} {quantity}.")

def view_inventory():
    print("\nitem name: quantity")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def update_item(item, quantity):
    if item in inventory:
        inventory[item]=quantity
    else:
        print("\nIt's not found.")

def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        if choice=='1':
            item=input("Enter item name: ")
            x=input("Enter quantity: ")
            if x.isdigit():
              quantity=int(x)
              add_item(item, quantity)
            else:
              print("\nError! Please try again")
            print(item)
        elif choice=='2':
            view_inventory()
        elif choice=='3':
            item=input("Enter item name: ")
            x=input("Enter new quantity: ")
            if x.isdigit():
              quantity=int(x)
              update_item(item, quantity)
            else:
              print("\nError! Please try again")
            print(inventory)
        elif choice=='4':
            break
        else:
            print("\nError! Please try again")

if __name__ == "__main__":
    manage_inventory()