#a=input().split(" ")
#切割跟輸入放一起 
#list內字串轉數字 就是a[i] = int(a[i]) 丟西 a[1]=int(a[1])
#a[:] = [int(x) for x in a]
#相加（困難版）可以直接叫出來加 丟西 a[0]+a[1]+a[2]+a[3]+a[4]
a=[0,0,0,0,0]
a[:] = [int(i) for i in (input().split(" "))]
from functools import reduce
b=reduce(lambda x,y:x+y, a)



#平均數d 可以這樣寫c=int(b/5*100)
c=b/5*100
c=int(c)
d=c/100
print("%.2f"%d)

#變異數g
e=((a[0]-d)**2+(a[1]-d)**2+(a[2]-d)**2+(a[3]-d)**2+(a[4]-d)**2)/5
f=e*100
f=int(f)
g=f/100
print("%.2f"%g)

#標準差
h=(g**0.5)*100
h=int(h)
i=h/100
print("%.2f"%i)