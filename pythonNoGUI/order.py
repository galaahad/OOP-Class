class OrderItem:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

class Order:
    def __init__(self):
        self.order_items = []
        self.table_number = 0

    def add_item(self, menu):
        item_name = input("Enter item name: ")
        item = menu.find_item(item_name)
        if item:
            quantity = int(input("Enter quantity: "))
            self.order_items.append(OrderItem(item, quantity))
            print("Item added to order.")
        else:
            print("Item not found in menu.")

    def remove_item(self):
        if not self.order_items:
            print("Order is empty.")
            return

        self.display_order()
        item_number = int(input("Enter item number to remove: ")) - 1
        if 0 <= item_number < len(self.order_items):
            del self.order_items[item_number]
            print("Item removed from order.")
        else:
            print("Invalid item number.")

    def display_order(self):
        if not self.order_items:
            print("Order is empty.")
            return

        print("\nOrder:")
        for i, item in enumerate(self.order_items):
            print(f"{i+1}. {item.item.name} x{item.quantity} - ${item.item.price * item.quantity:.2f}")

    def calculate_total(self):
        total = 0
        for item in self.order_items:
            total += item.item.price * item.quantity
        return total

    def place_order(self, table_manager):
        if not self.order_items:
            print("Order is empty. Cannot place order.")
            return

        print(f"Total: ${self.calculate_total():.2f}")

        if self.table_number == 0:
            print("Please select a table first.")
            return

        table_manager.mark_table_occupied(self.table_number)
        print("Order placed successfully!")
        self.order_items.clear()
        self.table_number = 0

    def create_order(self, menu, table_manager):
        while True:
            print("\nCreate Order")
            print("1. Add Item")
            print("2. Remove Item")
            print("3. Display Order")
            print("4. Select Table")
            print("5. Place Order")
            print("6. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_item(menu)
            elif choice == "2":
                self.remove_item()
            elif choice == "3":
                self.display_order()
            elif choice == "4":
                table_manager.display_available_tables()
                table_num = int(input("Enter table number: "))
                if table_manager.is_valid_table(table_num):
                    self.table_number = table_num
                    print("Table selected.")
                else:
                    print("Invalid table number.")
            elif choice == "5":
                self.place_order(table_manager)
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")