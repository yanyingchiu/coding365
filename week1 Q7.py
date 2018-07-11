x=input()
y=input()
z=input()

x=int(x)
y=int(y)
z=int(z)

if x<=10:
    g=x*380
elif x<=20:
    g=x*380*0.9
elif x<=30:
    g=x*380*0.85
else :
    g=x*380*0.8

if y<=10:
    h=y*1200
elif y<=20:
    h=y*1200*0.95
elif y<=30:
    h=y*1200*0.85
else :
    h=y*1200*0.8

if z<=10:
    i=z*180
elif z<=20:
    i=z*180*0.85
elif z<=30:
    i=z*180*0.8
else :
    i=z*180*0.7

print("%d"%(g+h+i))

