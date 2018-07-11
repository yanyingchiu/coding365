import math
a=input()
b=input()
c=input()
a=int(a)
b=int(b)
c=int(c)
x1 = ((-b)+math.sqrt(b*b-4*a*c))/(2*a)
x2 = ((-b)-math.sqrt(b*b-4*a*c))/(2*a)
print("%.1f"%x1)
print("%.1f"%x2)

