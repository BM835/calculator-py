math_sign = None

def add(a, b):
    return float(a)+float(b)


def remove(a, b):
    return float(a)-float(b)


def multiplication(a, b):
    return float(a)*float(b)


def division(a,b):
    return float(a)/float(b) 


def setMathSign(signNum): # 0 - `+`; 1 - `-`, 2 - `*`, 3 - `/`
    global math_sign
    math_sign = signNum

def calculate(a, b):
    global math_sign, result
    result = "Check inputs"
    if math_sign == 0:
        result = str(add(a, b))
    elif math_sign == 1:
        result = str(remove(a, b))
    elif math_sign == 2:
        result = str(multiplication(a, b))
    elif math_sign == 3:
        result = str(division(a, b))
    return result
