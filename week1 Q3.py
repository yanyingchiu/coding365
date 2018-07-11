num1= input()
num2= input()
num1=int(num1)
num2=int(num2)

x1=num1+num2
x2=abs(num1-num2)
x3=num1*num2
x4=num1/num2
a=("%.2f"%x1)
b=("%.2f"%x2)
c=("%.2f"%x3)

#到小數點後第二位！＝四捨五入到小數點第二位
d=x4*100
d=int(d)
e=d/100
e=("%.2f"%e)


print("Sum:",a,sep='')
print("Difference:",b,sep='')
print("Product:",c,sep='')
print("Quotient:",e,sep='')

