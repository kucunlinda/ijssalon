def print_10():
    for i in range(10):
        print(i+1)
print_10()
def devider():
    print()
    print("-----------------")
    print()
print("Dit is mijn eerste code")
devider()
print("Dit is mijn tweede code")
devider()
print("Dit is mijn derde code")
devider()
def pi():
    return 3.1415
print(pi())
def tel_op(a,b):
    return a+b
totaal = tel_op(5,10)
print(totaal)
def info(naam, leeftijd, in_dienst):
    if in_dienst == True:
        tekst_1 = "en nog altijd in dienst van onze firma"
    else:
        tekst_1 = "en iet meer bij ons in dienst."
    uitvoer = f"Beste {naam}, u bent {leeftijd} jaar" + tekst_1
    return uitvoer
print(info("Harry", 54, True))
print(info("Magda", 54, False))
def tel_op(a=1,b=2):
    return a + b
totaal = tel_op(2)
print(totaal)
b= 2
def mijn_functie():
    global b
    b = b + 10
    print("binnen: ", b)
print("buiten: ", b)
mijn_functie()
print("buiten: ", b)
c = 5
def mijn_functie2():
    a = c + 10
    print("binnen: ", a)
print("buiten: ", c)
mijn_functie2()
print("buiten: ", c)