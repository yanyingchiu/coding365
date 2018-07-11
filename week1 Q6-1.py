import math
a=float(input())
b=float(input())
c=float(input())

if a==0 :
    x=-c/b
    print("%.1f"%x)
elif b**2-4*a*c<0 :
    T = math.sqrt(abs(b**2-4*a*c))
    #因為是虛根所以要分開算
    x1 = (-b)/(2*a)
    x2 = (T)/(2*a)
    x1 = int(x1*10)/10.0
    x2 = int(x2*10)/10.0
    if x1==-0.0 : 
        x1=0.0
    if x2==-0.0 : 
        x2=0.0
    
    if x2<0 :
        x2 = abs(x2)
        print("%.1f-%.1fi"%(x1,x2))
        print("%.1f+%.1fi"%(x1,x2))
    else :
        print("%.1f+%.1fi"%(x1,x2))
        print("%.1f-%.1fi"%(x1,x2))
else :
    T = math.sqrt(b**2-4*a*c)
    x1 = (-b+T)/(2*a)
    x2 = (-b-T)/(2*a)
    print("%.1f"%x1)
    print("%.1f"%x2)


