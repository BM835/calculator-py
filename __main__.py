import tkinter.ttk as tk
import tkinter
import calc

w = tkinter.Tk()
w.title("Calculator")
w.geometry('110x115')


def plus (e):
    calc.setMathSign(0)


def minus (e):
    calc.setMathSign(1)


def multiply (e):
    calc.setMathSign(2)


def divide (e):
    calc.setMathSign(3)


def show_result(e):
    result.config(text=calc.calculate(numinput.get(), numinput1.get()))
    

numinput = tk.Entry(w)
numinput.pack()

go_res = tk.Button(w, text="=", width=20)
go_res.place(y=70, x=0)
go_res.bind("<Button-1>", show_result)

numinput1 = tk.Entry(w, width=20)
numinput1.place(y=50, x=0)

go_button = tk.Button(w, text="+", width=2)
go_button.place(y=25, x=5)
go_button.bind("<Button-1>", plus)

go_min = tk.Button(w, text="-", width=2)
go_min.place(y=25, x=35)
go_min.bind("<Button-1>", minus)

go_mul = tk.Button(w, text="*", width=2)
go_mul.place(y=25, x=65)
go_mul.bind("<Button-1>", multiply)

go_div = tk.Button(w, text="/", width=2)
go_div.place(y=25, x=95)
go_div.bind("<Button-1>", divide)

result = tkinter.Label(w)
result.place(y=95, x=0, width=110)

w.mainloop()