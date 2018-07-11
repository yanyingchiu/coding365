x1=int(input())
x2=int(input())
a=[x1,x2]
a.sort()

y1=int(input())
y2=int(input())
b=[y1,y2]
b.sort()

z1=int(input())
z2=int(input())
c=[z1,z2]
c.sort()

d=[a,b,c]
d.sort()

lon=d[0][1]-d[0][0]
if d[1][0]>d[0][1] :
    lon=lon+(d[1][1]-d[1][0])
elif d[1][1]>d[0][1] :
    lon=lon+(d[1][1]-d[0][1])
    
if d[2][0]>d[1][1] and d[0][1]<d[2][0] :
    lon=lon+(d[2][1]-d[2][0])
elif d[1][1]<d[2][1] and d[0][1]<d[2][1] :
    if d[0][1]>d[1][1] :
        lon=lon+(d[2][1]-d[0][1])
    else :lon=lon+(d[2][1]-d[1][1])
print(lon)

