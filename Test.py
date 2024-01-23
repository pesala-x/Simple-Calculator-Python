import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("500x500")
root.title("My First GUI")

label = tk.Label(root, text="Hello World", font=("Arial", 10))
label.pack(padx=10, pady=10)

textbox = tk.Text(root,height=3,font=("Arial", 16))
textbox.pack(padx=10, pady=10)

button = tk.Button(root, text="Click Me", font=("Arial", 18))
button.pack(padx=10, pady=10)
root.mainloop()
