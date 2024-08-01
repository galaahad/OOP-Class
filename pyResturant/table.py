class Table:
    def __init__(self, num_tables=5):
        self.tables = [False] * num_tables  # 0: Available, 1: Occupied

    def manage_tables(self):
        while True:
            print("\nTable Management")
            print("1. Display Available Tables")
            print("2. Mark Table Occupied")
            print("3. Mark Table Available")
            print("4. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.display_available_tables()
            elif choice == "2":
                table_num = int(input("Enter table number: "))
                if self.is_valid_table(table_num):
                    self.mark_table_occupied(table_num)
                    print("Table marked as occupied.")
                else:
                    print("Invalid table number.")
            elif choice == "3":
                table_num = int(input("Enter table number: "))
                if self.is_valid_table(table_num):
                    self.mark_table_available(table_num)
                    print("Table marked as available.")
                else:
                    print("Invalid table number.")
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

    def display_available_tables(self):
        print("\nAvailable Tables:")
        for i, table in enumerate(self.tables):
            if not table:
                print(i + 1, end=" ")
        print()

    def is_valid_table(self, table_number):
        return 1 <= table_number <= len(self.tables)

    def mark_table_occupied(self, table_number):
        if self.is_valid_table(table_number):
            self.tables[table_number - 1] = True

    def mark_table_available(self, table_number):
        if self.is_valid_table(table_number):
            self.tables[table_number - 1] = False