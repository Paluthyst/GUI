# when you want to run it take it over to replit bc the code wont run here >:C
import tkinter as tk


def doorbell(event):
    print("You range the bell!")


window = tk.Tk()
window.title("Doorbell App")
window.geometry("500x400")
mybutton = tk.Button(window, text = "doorbell")
mybutton.grid(column=1, row=0)
mybutton.bind("<Button - 1>", doorbell)
window.mainloop
