#!/usr/bin/python


#move the circles stuff over here

def sayHello(*args):
    for a in args:
        print("Hello, "+a)

def fibo(n):
    if (n <= 1):
        return n
    else:
        return fibo(n-1) + fibo(n-2)

def circles(r, x):
    pi = 3.14159
    area = pi*r**2

    #circumference of a circle
    circumference = 2*pi*r

    #arc length of a circle
    arc = x/360*2*pi*r

    #area of a sector
    sector = x/360*pi*r**2

    return area, circumference, arc, sector

sayHello("Alice", "Joe", "Bob")
say = sayHello("Jane")
print(say)

#area, circumference, arc, sector = circles(4, 30)
#print("The area is "+str(area))
#print("The circumference is "+str(circumference))
#print("The arc is "+str(arc))
#print("The sector is "+str(sector))

#myNumber = fibo(10)
#print(myNumber)
