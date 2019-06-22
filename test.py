import calc as c
from sys import exit
import random

def generate():
	global a, b
	a = random.randint(0, 1000)
	b = random.randint(0, 1000)

generate()
c.setMathSign(0)
print('\n\n'+str(a) +'+'+ str(b) + '='+ str(c.calculate(a, b)))
if str(float(a+b)) == str(c.calculate(a, b)):
	print('Add successful\n')
else:
	print('\n\nBuild unsuccessful\n'+str(float(a+b)))
	exit(1)

generate()
c.setMathSign(1)
print(str(a) +'-'+ str(b) + '='+ c.calculate(a, b))
if str(float(a-b)) == str(c.calculate(a, b)):
	print('Remove successful\n')
else:
	print('\n\nBuild unsuccessful')
	exit(1)

generate()
c.setMathSign(2)
print(str(a) +'*'+ str(b) + '='+ c.calculate(a, b))
if str(float(a*b)) == str(c.calculate(a, b)):
	print('Myltiply successful\n')
else:
	print('\n\nBuild unsuccessful')
	exit(1)

generate()
c.setMathSign(0)
print(str(a) +'/'+ str(b) + '='+ c.calculate(a, b))
if str(float(a+b)) == str(c.calculate(a, b)):
	print('Division successful\n')
else:
	print('\n\nBuild unsuccessful')
	exit(1)

print('\n\nBuild successful')
exit(0)
