import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from menu import Menu
from order import Order
from table import Table

class RestaurantGUI:
    def __init__(self, master):
        self.master = master
        master.title("Restaurant Management System")

        # สร้างเฟรมสำหรับเมนู
        self.menu_frame = tk.Frame(master)
        self.menu_frame.pack(pady=10)

        # ปุ่มจัดการเมนู
        self.manage_menu_button = tk.Button(self.menu_frame, text="จัดการเมนู", command=self.manage_menu)
        self.manage_menu_button.pack(side="left", padx=5)

        # ปุ่มสร้างคำสั่งซื้อ
        self.create_order_button = tk.Button(self.menu_frame, text="สร้างออเดอร์", command=self.create_order)
        self.create_order_button.pack(side="left", padx=5)

        # ปุ่มจัดการโต๊ะอาหาร
        self.manage_tables_button = tk.Button(self.menu_frame, text="จัดการโต๊ะ", command=self.manage_tables)
        self.manage_tables_button.pack(side="left", padx=5)

        # สร้างเฟรมสำหรับแสดงรายการเมนู
        self.menu_list_frame = tk.Frame(master)
        self.menu_list_frame.pack(pady=10)

        # สร้าง Treeview สำหรับแสดงรายการเมนู
        self.menu_tree = ttk.Treeview(self.menu_list_frame, columns=("name", "price", "test"), show="headings")
        self.menu_tree.heading("name", text="ชื่ออาหาร")
        self.menu_tree.heading("price", text="ราคา")
        self.menu_tree.heading("test", text="ทดสอบ")
        self.menu_tree.pack(side="left")

        # สร้าง Scrollbar สำหรับ Treeview
        self.menu_scrollbar = tk.Scrollbar(self.menu_list_frame, orient="vertical", command=self.menu_tree.yview)
        self.menu_scrollbar.pack(side="right", fill="y")
        self.menu_tree.configure(yscrollcommand=self.menu_scrollbar.set)

        # สร้างเฟรมสำหรับคำสั่งซื้อ
        self.order_frame = tk.Frame(master)
        self.order_frame.pack(pady=10)

        # สร้าง Treeview สำหรับแสดงคำสั่งซื้อ
        self.order_tree = ttk.Treeview(self.order_frame, columns=("name", "quantity", "total_price"), show="headings")
        self.order_tree.heading("name", text="ชื่ออาหาร")
        self.order_tree.heading("quantity", text="จำนวน")
        self.order_tree.heading("total_price", text="ราคารวม")
        self.order_tree.pack(side="left")

        # สร้าง Scrollbar สำหรับ Treeview
        self.order_scrollbar = tk.Scrollbar(self.order_frame, orient="vertical", command=self.order_tree.yview)
        self.order_scrollbar.pack(side="right", fill="y")
        self.order_tree.configure(yscrollcommand=self.order_scrollbar.set)

        # สร้างเฟรมสำหรับโต๊ะอาหาร
        self.table_frame = tk.Frame(master)
        self.table_frame.pack(pady=10)

        # สร้าง Treeview สำหรับแสดงโต๊ะอาหาร
        self.table_tree = ttk.Treeview(self.table_frame, columns=("table_number", "status"), show="headings")
        self.table_tree.heading("table_number", text="หมายเลขโต๊ะ")
        self.table_tree.heading("status", text="สถานะ")
        self.table_tree.pack(side="left")

        # สร้าง Scrollbar สำหรับ Treeview
        self.table_scrollbar = tk.Scrollbar(self.table_frame, orient="vertical", command=self.table_tree.yview)
        self.table_scrollbar.pack(side="right", fill="y")
        self.table_tree.configure(yscrollcommand=self.table_scrollbar.set)

        # สร้างเฟรมสำหรับปุ่มควบคุมคำสั่งซื้อ
        self.order_control_frame = tk.Frame(master)
        self.order_control_frame.pack(pady=10)

        # ปุ่มเพิ่มอาหาร
        self.add_item_button = tk.Button(self.order_control_frame, text="Add Item", command=self.add_item_to_order)
        self.add_item_button.pack(side="left", padx=5)

        # ปุ่มลบอาหาร
        self.remove_item_button = tk.Button(self.order_control_frame, text="Remove Item", command=self.remove_item_from_order)
        self.remove_item_button.pack(side="left", padx=5)

        # ปุ่มเลือกโต๊ะ
        self.select_table_button = tk.Button(self.order_control_frame, text="Select Table", command=self.select_table)
        self.select_table_button.pack(side="left", padx=5)

        # ปุ่มวางคำสั่งซื้อ
        self.place_order_button = tk.Button(self.order_control_frame, text="Place Order", command=self.place_order)
        self.place_order_button.pack(side="left", padx=5)

        # สร้างเฟรมสำหรับแสดงผลลัพธ์
        self.output_frame = tk.Frame(master)
        self.output_frame.pack(pady=10)

        # สร้างเลเบลสำหรับแสดงข้อความผลลัพธ์
        self.output_label = tk.Label(self.output_frame, text="")
        self.output_label.pack()

        # สร้างวัตถุสำหรับจัดการเมนู คำสั่งซื้อ และโต๊ะอาหาร
        self.menu = Menu()
        self.order = Order()
        self.table = Table()

        # แสดงรายการเมนูใน Treeview
        self.display_menu()
        # แสดงรายการคำสั่งซื้อใน Treeview
        self.display_order()
        # แสดงรายการโต๊ะอาหารใน Treeview
        self.display_tables()

    def manage_menu(self):
        self.menu.manage_menu()
        self.display_menu()

    def create_order(self):
        self.order.create_order(self.menu, self.table)
        self.display_order()

    def manage_tables(self):
        self.table.manage_tables()
        self.display_tables()

    def add_item_to_order(self):
        selected_item = self.menu_tree.selection()
        if selected_item:
            item_name = self.menu_tree.item(selected_item[0])["values"][0]
            item = self.menu.find_item(item_name)
            if item:
                try:
                    quantity = int(input("Enter quantity: "))
                    self.order.add_item(item, quantity)
                    self.display_order()
                    self.output_label.config(text="Item added to order")
                except ValueError:
                    messagebox.showerror("Error", "Please enter a valid quantity")
            else:
                messagebox.showerror("Error", "Item not found in menu")
        else:
            messagebox.showerror("Error", "Please select an item from the menu")

    def remove_item_from_order(self):
        selected_item = self.order_tree.selection()
        if selected_item:
            item_index = int(selected_item[0]) - 1
            if 0 <= item_index < len(self.order.order_items):
                self.order.remove_item(item_index)
                self.display_order()
                self.output_label.config(text="Item removed from order")
            else:
                messagebox.showerror("Error", "Invalid item number")
        else:
            messagebox.showerror("Error", "Please select an item from the order")

    def select_table(self):
        selected_table = self.table_tree.selection()
        if selected_table:
            table_number = int(self.table_tree.item(selected_table[0])["values"][0])
            self.order.table_number = table_number
            self.output_label.config(text=f"Table {table_number} selected")
        else:
            messagebox.showerror("Error", "Please select a table")

    def place_order(self):
        if self.order.table_number == 0:
            messagebox.showerror("Error", "Please select a table first")
        else:
            self.order.place_order(self.table)
            self.display_order()
            self.display_tables()
            self.output_label.config(text="Order placed successfully")

    def display_menu(self):
        # ล้างข้อมูลเก่าใน Treeview
        for i in self.menu_tree.get_children():
            self.menu_tree.delete(i)

        # เพิ่มเมนูใหม่ลงใน Treeview
        for name, item in self.menu.menu_items.items():
            self.menu_tree.insert("", tk.END, values=(name, item.price))

    def display_order(self):
        # ล้างข้อมูลเก่าใน Treeview
        for i in self.order_tree.get_children():
            self.order_tree.delete(i)

        # เพิ่มคำสั่งซื้อใหม่ลงใน Treeview
        for i, item in enumerate(self.order.order_items):
            self.order_tree.insert("", tk.END, values=(item.item.name, item.quantity, item.item.price * item.quantity))

    def display_tables(self):
        # ล้างข้อมูลเก่าใน Treeview
        for i in self.table_tree.get_children():
            self.table_tree.delete(i)

        # เพิ่มโต๊ะอาหารใหม่ลงใน Treeview
        for i, status in enumerate(self.table.tables):
            self.table_tree.insert("", tk.END, values=(i + 1, "Occupied" if status else "Available"))

# เรียกใช้ GUI
root = tk.Tk()
app = RestaurantGUI(root)
root.mainloop()