import math

def secAngle(a):
    k = float(a)/100
    l = float(k*360)
    return l

def isinside(x,y):
    k = ((x-50)**2)+((y-50)**2)
    l =  math.sqrt(k)
    if(l<=50):
        return True

    else:
        return False

def pointangle(x,y):
    x_c = 50
    y_c = 50

    x1 = float(x-x_c)
    y1 = float(y-y_c)

    b_x = 50-x_c
    b_y = 100-y_c

    v = float(x1*b_x+y1*b_y)

    h = x1**2+y1**2
    j = math.sqrt(float(h))

    f = float(j)*float(50)

    d = float(v)/float(f)
    return math.degrees(math.acos(d))

def color(p,x,y):
    if(pointangle(x,y)<secAngle(p) and isinside(x,y)):
        return "black"
    else:
        return "white"

T = int(raw_input())

for i in range(0,T):
    a = map(int,raw_input().split(" "))
    print color(a[0],a[1],a[2])
