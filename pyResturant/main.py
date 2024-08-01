import tkinter as tk
import tkinter.messagebox as messagebox

def say_hello():
    messagebox.showinfo("Hello", "Hello, world!")

def print_something(text):
    print(text)

# สร้างหน้าต่างหลัก
window = tk.Tk()
window.title("Hello World")

# สร้างปุ่ม "Say Hello"
button = tk.Button(window, text="Say Hello", command=say_hello)
button.pack(pady=20)

tk.Button(window, text="Try This!!!", bg="red", command=print_something("TEST")).pack()

tk.Button(window,text='A', bg = "yellow").pack()
tk.Button(window,text='B', bg = "yellow").pack()
tk.Button(window,text='C', bg = "yellow").pack()
tk.Button(window,text='D', bg = "yellow").pack()

# รัน GUI
window.mainloop()