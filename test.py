import calc as c
from sys import exit

if str(c.add("1", "1")) == "2.0" and str(c.remove("1", "1")) == "0.0" and str(c.multiplication("5", "5")) == "25.0" and str(c.division("20", "5")) == "4.0":
    exit(0)
else:
    exit(1)