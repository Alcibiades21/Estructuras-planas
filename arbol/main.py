from random import randint
from arbol import abb
arb = abb()
# n = int(input("Cantidad de numeros: "))
n = 12
for i in range(n):
    x = randint(10, 99)
    print(x, end=" ")
    #x = int(input("Valor: "))
    arb.agregar(x, arb.raiz)
print("")
print(arb.preorden(arb.raiz))
print("N:", arb.len(arb.raiz))
print("H:", arb.altura(arb.raiz))
print("Hojas:", arb.hojas(arb.raiz))