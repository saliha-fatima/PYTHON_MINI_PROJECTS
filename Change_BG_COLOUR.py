import tkinter as tk
import random

def change_color():
    """Change the background color to a random color"""
    color = '#{:06x}'.format(random.randint(0, 0xFFFFFF))
    root.config(background=color)

root = tk.Tk()
root.title("Change Background Color")

button = tk.Button(root, text="Change Color", command=change_color)
button.pack()

root.mainloop()