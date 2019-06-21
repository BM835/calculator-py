import calc as c
from sys import exit

print("1 + 1 = " + str(c.add("1", "1")) +"\n1 - 1 = " + str(c.remove("1", "1")) + "\n5 * 5 = " + str(c.multiplication("5", "5")) + "\n20 / 5 = " + str(c.division("20", "5")))

if str(c.add("1", "1")) == "2.0" and str(c.remove("1", "1")) == "0.0" and str(c.multiplication("5", "5")) == "25.0" and str(c.division("20", "5")) == "4.0":
	print("\n\nBuild successful")
	exit(0)
else:
	print('\n\nBuild unsuccessful')
	exit(1)