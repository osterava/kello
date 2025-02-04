import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digitaalinen Kello")

label = tk.Label(root, font=("calibri", 60, "bold"), background="black", foreground="yellow")
label.pack(anchor="center")

def time():
    string = strftime('%H:%M:%S %p') 
    label.config(text=string)
    label.after(1000, time) 

time()

root.mainloop()
