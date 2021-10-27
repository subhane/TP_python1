import math

def division() :
    valeur1 = input("Saisir valeur 1 : ")
    valeur2 = input("Saisir valeur 2 : ")

    print(valeur1/valeur2)

def modulo():
    valeur1 = input("Saisir valeur 1 : ")
    valeur2 = input("Saisir valeur 2 : ")
    print(valeur1 % valeur2)

def calculAir(r):
    return 2*math.pi*r**2

def compte_triangle(n):
    s = 0
    for i in range(1, n+1):
        s = s+i
    return s

def nb_differences(s1,s2):
    s = 0
    if len(s1) < len(s2):
        n = len(s1)
    else:
        n = len(s2)
    for i in range(n):
        if s1[i] != s2[i]:
           s = s+1
    return s

print(nb_differences("oiseau","bateau"))

def triangle_motif(n):
    a = 2*n-1
    b = int((a-1)/2)
    for i in range(n):
        c = a-2*(b-i)
        print((b-i)*" "+c*"*"+(b-i)*" ")
triangle_motif(13)





