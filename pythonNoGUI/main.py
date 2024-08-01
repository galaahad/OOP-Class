from menu import Menu
from order import Order
from table import Table

def main():
    menu = Menu()
    order = Order()
    table_manager = Table()

    while True:
        print("\nRestaurant Management System")
        print("1. Manage Menu")
        print("2. Create Order")
        print("3. Manage Tables")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            menu.manage_menu()
        elif choice == "2":
            order.create_order(menu, table_manager)
        elif choice == "3":
            table_manager.manage_tables()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()