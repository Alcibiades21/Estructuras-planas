from nodo import Nodo
class abb:
    raiz = None
    def __init__(self) -> None:
        pass
    def agregar(self, x, ptr):
        if self.raiz == None:
            self.raiz = Nodo(x)
        else:
            if x < ptr.dato:
                if ptr.izq == None:
                    nuevo = Nodo(x)
                    ptr.izq = nuevo
                else:
                    self.agregar(x, ptr.izq)
            elif x > ptr.dato:
                if ptr.der == None:
                    nuevo = Nodo(x)
                    ptr.der = nuevo
                else:
                    self.agregar(x, ptr.der)
            else:
                return False
        return True
    def preorden(self, ptr):
        if ptr == None:
            return ""
        else:
            return str(ptr.dato) + " " + self.preorden(ptr.izq) + self.preorden(ptr.der)
    def len(self, ptr): # cuantos nodos hay en el arbol
        if ptr == None:
            return 0
        else:
            return 1 + self.len(ptr.izq) + self.len(ptr.der)
    def hojas(self, ptr): # Devuelva las hojas del arbol
        if ptr == None:
            return ""
        else:
            d = ""
            if ptr.izq == None and ptr.der == None:
                d = str(ptr.dato) + " "
            return d + self.hojas(ptr.izq) + self.hojas(ptr.der)
    def altura(self, ptr):
        if ptr == None:
            return 0
        else:
            alti = self.altura(ptr.izq)
            altd = self.altura(ptr.der)
            if alti > altd:
                return alti + 1
            else:
                return altd + 1