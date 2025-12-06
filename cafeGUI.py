import tkinter as tk
from tkinter import messagebox

#Items & Prices
menu = {
    "Coffee": 30,
    "Tea": 20,
    "Cake": 50,
    "Sandwich": 40
}

#Main Window
root = tk.Tk()
root.title("Cafe Menu")
root.geometry("350x350")

title = tk.Label(root, text="☕ Simple Café System", font=("Arial", 16, "bold"))
title.pack(pady=10)

#Variables
vars_dict = {}

#Create Checkboxes
for item, price in menu.items():
    var = tk.IntVar()
    cb = tk.Checkbutton(root, text=f"{item} - {price} EGP", variable=var, font=("Arial", 12))
    cb.pack(anchor='w')
    vars_dict[item] = var

#Calculate Total
def calculate_total():
    total = 0
    items_chosen = []

    for item, var in vars_dict.items():
        if var.get() == 1:
            total += menu[item]
            items_chosen.append(item)

    if not items_chosen:
        messagebox.showinfo("Receipt", "No items selected!")
        return

    receipt = "Your Order:\n" + "\n".join(items_chosen) + f"\n\nTotal: {total} EGP"
    messagebox.showinfo("Receipt", receipt)

#Button
btn = tk.Button(root, text="Show Receipt", command=calculate_total, font=("Arial", 12), bg="brown", fg="white")
btn.pack(pady=20)

root.mainloop()
