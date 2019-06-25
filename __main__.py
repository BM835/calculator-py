import tkinter.ttk as tk
import tkinter
import calc

w = tkinter.Tk()
w.title("Calculator")
w.geometry('132x160')


def plus (e):
    calc.setMathSign(0)


def minus (e):
    calc.setMathSign(1)


def multiply (e):
    calc.setMathSign(2)


def divide (e):
    calc.setMathSign(3)


def show_result(e):
    result.config(text=calc.calculate())


go_res = tk.Button(w, text="=", width=2)
go_res.place(y=133, x=70)
go_res.bind("<Button-1>", show_result)

go_button = tk.Button(w, text="+", width=2)
go_button.place(y=43, x=100)
go_button.bind("<Button-1>", plus)

go_min = tk.Button(w, text="-", width=2)
go_min.place(y=73, x=100)
go_min.bind("<Button-1>", minus)

go_mul = tk.Button(w, text="*", width=2)
go_mul.place(y=103, x=100)
go_mul.bind("<Button-1>", multiply)

go_div = tk.Button(w, text="/", width=2)
go_div.place(y=133, x=100)
go_div.bind("<Button-1>", divide)

b1 = tk.Button(w, text='1', width=2)
b1.place(y=43, x=10)

b1 = tk.Button(w, text='2', width=2)
b1.place(y=43, x=40)

b1 = tk.Button(w, text='3', width=2)
b1.place(y=43, x=70)

b1 = tk.Button(w, text='4', width=2)
b1.place(y=73, x=10)

b1 = tk.Button(w, text='5', width=2)
b1.place(y=73, x=40)

b1 = tk.Button(w, text='6', width=2)
b1.place(y=73, x=70)

b1 = tk.Button(w, text='7', width=2)
b1.place(y=103, x=10)

b1 = tk.Button(w, text='8', width=2)
b1.place(y=103, x=40)

b1 = tk.Button(w, text='9', width=2)
b1.place(y=103, x=70)

b1 = tk.Button(w, text='0', width=2)
b1.place(y=133, x=40)

answer_style = tk.Style()
answer_style.configure("BW.TLabel", font=('Comic Sans', 12))

example = tk.Label(w, text="5+5")
example.place(y=0, x=0, width=110)

result = tk.Label(w, text="10", style='BW.TLabel')
result.place(y=20, x=0, width=110)

w.mainloop()