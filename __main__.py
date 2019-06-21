import tkinter as tk
import calc

w = tk.Tk()
w.title("Calculator")
w.geometry('110x80')


def plus (e):
    result.config(text = calc.add(numinput.get(), numinput1.get()))


def minus (e):
    result.config(text = calc.remove(numinput.get(), numinput1.get()))


def multiply (e):
    result.config(text = calc.multiplication(numinput.get(), numinput1.get()))


def divide (e):
    result.config(text = calc.division(numinput.get(), numinput1.get()))
    

numinput = tk.Entry(w)
numinput.pack()
numinput1 = tk.Entry(w)
numinput1.pack()

go_button = tk.Button(w, text="+")
go_button.place(y=40, x=10)
go_button.bind("<Button-1>", plus)

go_min = tk.Button(w, text="-")
go_min.place(y=40, x=35)
go_min.bind("<Button-1>", minus)

go_mul = tk.Button(w, text="*")
go_mul.place(y=40, x=60)
go_mul.bind("<Button-1>", multiply)

go_div = tk.Button(w, text="/")
go_div.place(y=40, x=85)
go_div.bind("<Button-1>", divide)

result = tk.Label(w)
result.place(y=60, x=5, width=100)

w.mainloop()