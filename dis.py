import tkinter as tk

def button_click():
    if my_button["text"] == "Click Me":
        my_button["text"] = "Clicked!"
    else:
        my_button["text"] = "Click Me"

root = tk.Tk()
root.title("Button Example")

my_button = tk.Button(root, text="Click Me", command=button_click)
my_button.pack()

root.mainloop()

