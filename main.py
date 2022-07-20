from tkinter import *
from tkinter import ttk

#Janelas

window = Tk()
window.title("Calculadora")
window.geometry("330x500")

window_frame = Frame(window, width=330, height=70, bg="cyan")
window_frame.grid(row=0, column=0)

window_frame2 = Frame(window, width=330, height=430, bg="white")
window_frame2.grid(row=1, column=0)

#Botões

b1 = Button(window_frame2, text="%", width=10, height=4, bg="grey")
b1.place(x=0, y=0)

b2 = Button(window_frame2, text="CE", width=10, height=4, bg="grey")
b2.place(x=85, y=0)

b2 = Button(window_frame2, text="C", width=10, height=4, bg="grey")
b2.place(x=170, y=0)

b2 = Button(window_frame2, text="⌫", width=10, height=4, bg="grey")
b2.place(x=255, y=0)

window.mainloop()
