from nodo import Nodo
class Lista_doble:
    primero = None
    ultimo = None
    def __init__(self, x) -> None:
        self.raiz = Nodo(x)

    def agregar_in_orden(self, nodo, x):
        if x < nodo.dato:
            if nodo.izquierda == None:
                nodo.izquierda = Nodo(x)
            else:
                self.agregar_in_orden(nodo.izquierda, x) 
        else:
            if nodo.derecha == None:
                nodo.derecha = Nodo(x)
            else:
                self.agregar_in_orden(nodo.derecha, x)

    def buscar(self, nodo, x):
        if nodo == None:
            return None
        elif nodo.x == x:
            return nodo
        elif x < nodo.x:
            return self.buscar(nodo.izquierda, x)
        else:
            return self.buscar(nodo.derecha, x)
    
    def agregar(self, x):
        self.agregar_in_orden(self.raiz, x)
    
    def inOrden(self, nodo):
        if nodo != None:
            self.inOrden(nodo.izquierda)
            print(nodo.dato, end = ", ")
            self.inOrden(nodo.derecha)
            
    def mostrar_inOrden(self):
        print("Arbol In orden:")
        self.inOrden(self.raiz)
        print(" ")

    def preOrden(self, nodo):
        if nodo != None:
            print(nodo.dato, end = ", ")
            self.preOrden(nodo.izquierda)
            self.preOrden(nodo.derecha)
    
    def mostrar_preOrden(self):
        print("Arbol en pre orden:")
        self.preOrden(self.raiz)
        print(" ")
    
    def posOrden(self, nodo):
        if nodo != None:
            self.posOrden(nodo.izquierda)
            self.posOrden(nodo.derecha)
            print(nodo.dato, end = ", ")
    
    def mostrar_posOrden(self):
        print("Arbol pos orden:")
        self.posOrden(self.raiz)
        print(" ")
        
        
