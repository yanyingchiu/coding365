#001
import sys
a1=input()#課程編號
if len(a1)<4 :
    print("-1")
    sys.exit()
a2=input()#時數
a3=list(input())
if int(a3[0])<1 or int(a3[0])>5 or int(a3[1])>8 or int(a3[1])<1 :
        print("-1")
        sys.exit()
elif int(a2)>1:
    a4=list(input())
    if int(a4[0])<1 or int(a4[0])>5 or int(a4[1])>8 or int(a4[1])<1 :
        print("-1")
        sys.exit()
       

#002
b1=input()#課程編號
if len(b1)<4 :
    print("-1")
    sys.exit() 
b2=input()#時數
b3=list(input())
if int(b3[0])<1 or int(b3[0])>5 or int(b3[1])>8 or int(b3[1])<1 :
        print("-1")
        sys.exit()
elif int(b2)>1:
    b4=list(input())
elif int(b4[0])<1 or int(b4[0])>5 or int(b4[1])>8 or int(b4[1])<1 :
        print("-1")
        sys.exit()
#003
c1=input()#課程編號
if len(c1)<4 :
    print("-1")
    sys.exit(1) 
c2=input()#時數
c3=list(input())
if int(c3[0])<1 or int(c3[0])>5 or int(c3[1])>8 or int(c3[1])<1 :
        print("-1")
        sys.exit()
elif int(c2)>1:
    c4=list(input())
    if int(c4[0])<1 or int(c4[0])>5 or int(c4[1])>8 or int(c4[1])<1 :
        print("-1")
        sys.exit()
s = 0
#ab衝突
if a3==b3:
    print(a1,b1,a3[0]+a3[1],sep=",")
    s=1
if int(b2)>1 and a3==b4:
    s=1
    print(a1,b1,a3[0]+a3[1],sep=",")
if int(a2)>1 and a4==b3:
    s=1
    print(a1,b1,a4[0]+a4[1],sep=",")
if int(a2)>1 and int(b2)>1 and a4==b4:
    print(a1,b1,a4[0]+a4[1],sep=",")
    s=1

#ac衝突   
if a3==c3:
    s=1
    print(a1,c1,a3[0]+a3[1],sep=",")
if int(c2)>1 and a3==c4:
    s=1
    print(a1,c1,a3[0]+a3[1],sep=",")
if int(a2)>1 and a4==c3:
    s=1
    print(a1,c1,a4[0]+a4[1],sep=",")
if int(a2)>1 and int(c2)>1 and a4==c4:
    s=1
    print(a1,c1,a4[0]+a4[1],sep=",")

#bc衝突
if b3==c3:
    s=1
    print(b1,c1,b3[0]+b3[1],sep=",")
if int(c2)>1 and b3==c4:
    s=1
    print(b1,c1,b3[0]+b3[1],sep=",")
if int(b2)>1 and b4==c3:
    s=1
    print(b1,c1,b4[0]+b4[1],sep=",")
if int(b2)>1 and int(c2)>1 and b4==c4:
    s=1
    print(b1,c1,b4[0]+b4[1],sep=",")
if s==0:
    print("correct")