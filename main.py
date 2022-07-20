from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Calculadora")
window.geometry("300x500")

window_frame = Frame(window, width=300, height=80,bg="#db1212")
window_frame.grid(row=0, column=0)

window.mainloop()
