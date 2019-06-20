import tkinter as tk
import calc

w = tk.Tk()
w.title("Calculator")


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
go_button.pack()
go_button.bind("<Button-1>", plus)

go_min = tk.Button(w, text="-")
go_min.pack()
go_min.bind("<Button-1>", minus)

go_mul = tk.Button(w, text="*")
go_mul.pack()
go_mul.bind("<Button-1>", multiply)

go_div = tk.Button(w, text="/")
go_div.pack()
go_div.bind("<Button-1>", divide)

result = tk.Label(w)
result.pack()

w.mainloop()