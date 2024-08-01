class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Menu:
    def __init__(self):
        self.menu_items = {}

    def add_item(self):
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        self.menu_items[name] = MenuItem(name, price)
        print("Item added successfully!")

    def edit_item(self):
        name = input("Enter item name to edit: ")
        if name in self.menu_items:
            new_price = float(input("Enter new price: "))
            self.menu_items[name].price = new_price
            print("Item updated successfully!")
        else:
            print("Item not found.")

    def delete_item(self):
        name = input("Enter item name to delete: ")
        if name in self.menu_items:
            del self.menu_items[name]
            print("Item deleted successfully!")
        else:
            print("Item not found.")

    def display_menu(self):
        print("\nMenu:")
        for name, item in self.menu_items.items():
            print(f"{name} - ${item.price:.2f}")

    def find_item(self, name):
        if name in self.menu_items:
            return self.menu_items[name]
        return None

    def manage_menu(self):
        while True:
            print("\nMenu Management")
            print("1. Add Item")
            print("2. Edit Item")
            print("3. Delete Item")
            print("4. Display Menu")
            print("5. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_item()
            elif choice == "2":
                self.edit_item()
            elif choice == "3":
                self.delete_item()
            elif choice == "4":
                self.display_menu()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")