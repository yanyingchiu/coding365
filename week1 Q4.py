x=input()
x= x.split(" ")
a=(x[0])
b=(x[1])
c=(x[2])
a=int(a)
b=int(b)
c=int(c)
#不能成為三角形：輸出 1
if a+b<=c or a+c<=b or b+c<=a or a<=0 or b<=0 or c<=0:
    print(1)
#正三角形：輸出 2
elif a==b==c:
    print(2)
#等腰三角形：輸出 
elif a==b!=c or a==c!=b or b==c!=a:
    print(3)
#一般三角形：輸出 4
else:
    print(4)