import tkinter.ttk as tk
import tkinter
import calc

w = tkinter.Tk()
w.title("Calculator")
w.geometry('110x90')


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

go_button = tk.Button(w, text="+", width=2)
go_button.place(y=40, x=5)
go_button.bind("<Button-1>", plus)

go_min = tk.Button(w, text="-", width=2)
go_min.place(y=40, x=35)
go_min.bind("<Button-1>", minus)

go_mul = tk.Button(w, text="*", width=2)
go_mul.place(y=40, x=65)
go_mul.bind("<Button-1>", multiply)

go_div = tk.Button(w, text="/", width=2)
go_div.place(y=40, x=95)
go_div.bind("<Button-1>", divide)

result = tk.Label(w)
result.place(y=70, x=0, width=110)

w.mainloop()