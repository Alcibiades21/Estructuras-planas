from lista_doble import Lista_doble

lista = [60, 99, 95, 93, 27, 74, 67, 14, 26, 31]
for dato in lista:
    if dato == lista[0]:
        arbol = Lista_doble(dato)
    else:
        arbol.agregar(dato)

arbol.mostrar_inOrden()
arbol.mostrar_preOrden()
arbol.mostrar_posOrden()