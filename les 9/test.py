#from math import division_by_2
#for x in range(10):
#    print (x)
#x = 0
#print(5/x)
leeftijd = 10

#def over_2_jaar():
#    global leeftijd
#    leeftijd = leeftijd + 2
#    return leeftijd
#print(over_2_jaar())
'''
getal1 = input("Wat is getal1?")
getal2 = input("Wat is getal2?")
uitkomst = int(getal1) + int(getal2)
print(f"{getal1} + {getal2} = {uitkomst}")
#print("Hello World")
def pi():
    return 3.1415
    
radius = 2
oppervlakte = pi() * (radius ** 2)
print (oppervlakte)
'''
print("hello")
import math

def discriminant(a, b, c):
    # Voor de formule ax^2 + bx + c
    D1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
    D2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2 * a)
    uitvoer = [D1, D2]
    return uitvoer

print("Voor de formule ax^2 + bx + c, geef a, b en c:")
a = -3 #int(input("Wat is a? "))
b = 2 #int(input("Wat is b? "))
c = 5 #int(input("Wat is c? "))

uitkomst = discriminant(a, b, c)

D1 = uitkomst[0]
D2 = uitkomst[1]

print(f"De discriminant(en) voor {a}x^2 + {b}x + {c} zijn:")
print(f"{D1} en {D2}")