x=input()
x= x.split(" ")
a=(x[0])
b=(x[1])
c=(x[2])
a=int(a)
b=int(b)
c=int(c)

#0:Not Triangle
if a+b<=c or a+c<=b or b+c<=a or a<=0 or b<=0 or c<=0:
    print("Not Triangle")
#1:Right Triangle 其中有兩個邊的平方和等於第三邊的平方
elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
    print("Right Triangle")
#2:Obtuse Triangle 其中有兩個邊的平方和小於第三邊的平方
elif a**2+b**2<c**2 or a**2+c**2<b**2 or b**2+c**2<a**2:
    print("Obtuse Triangle")
#3:Acute Triangle 任兩邊的平方和大於第三邊的平方
elif a**2+b**2>c**2 or a**2+c**2>b**2 or b**2+c**2>a**2:
    print("Acute Triangle")
