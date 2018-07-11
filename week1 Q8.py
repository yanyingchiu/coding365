#網內語音(秒)，整數(?)
a=input()
a=int(a)
#網外語音(秒)，整數
b=input()
b=int(b)
#市話    (秒)，整數
c=input()
c=int(c)
#網內簡訊數，整數
d=input()
d=int(d)
#網外簡訊數，整數
e=input()
e=int(e)

#183x
o=a*0.08+b*0.139+c*0.135+d*1.128+e*1.483
if o<=183:
    x=183
else:x=o
#383y
p=a*0.07+b*0.13+c*0.121+d*1.128+e*1.483
if p<=383:
    y=383
else:y=p
#983z
q=a*0.06+b*0.108+c*0.101+d*1.128+e*1.483
if q<=983:
    z=983
else:z=q

if x<y<z or x<z<y:
    print("183")
    print("%.f"%x)
elif y<x<z or y<z<x:
    print("383")
    print("%.f"%y)
else :
    print("983")
    print("%.f"%z)
