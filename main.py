import math

def division() :
    valeur1 = input("Saisir valeur 1 : ")
    valeur2 = input("Saisir valeur 2 : ")

    print(valeur1/valeur2)

def modulo():
    valeur1 = input("Saisir valeur 1 : ")
    valeur2 = input("Saisir valeur 2 : ")
    print(valeur1%valeur2)

def calculAir(r):
    return 2*math.pi*r**2

def compte_triangle(n):
    s = 0
    for i in range(1,n+1):
        s = s+i
    return s




