class Nodo:
    
    def __init__(self,arbol,valor):
        self.izquierda = None
        self.derecha = None
        self.dato = valor

    def insertar(self,arbol,valor):
        if arbol.dato > valor:
            self.insertarizquierda(arbol,valor)
        elif arbol.dato < valor:
            self.insertarderecha(arbol,valor)

    def insertarizquierda(self,arbol,valor):
        if arbol.izquierda == None:
            arbol.izquierda = Nodo(arbol,valor)
        else:
            self.insertar(arbol.izquierda,valor)
            
    def insertarderecha(self,arbol,valor):
        if arbol.derecha == None:
            arbol.derecha= Nodo(arbol,valor)
        else:
            self.insertar(arbol.derecha,valor)

    def inorden(self,arbol):
        if arbol.izquierda != None:
            self.inorden(arbol.izquierda)
        print (arbol.dato,end=' ')
        
        if arbol.derecha != None:
            self.inorden(arbol.derecha)
            
    def preorden(self,arbol):
        print (arbol.dato,end=' ')
        if arbol.izquierda != None:
            self.preorden(arbol.izquierda)       
        
        if arbol.derecha != None:
            self.preorden(arbol.derecha)
    
    def posorden(self,arbol):
        if arbol.izquierda != None:
            self.preorden(arbol.izquierda)       
        
        if arbol.derecha != None:
            self.preorden(arbol.derecha)        
        print (arbol.dato,end=' ')
    
    def buscar(arbol,valor):
        if arbol == None:
            return false
        elif arbol.valor == valor:
            return true
        else:
            return buscar(arbol.izquierda) or buscar (arbol.derecha)

    def evaluar(arbol):
        if arbol.valor == '+':
            return evaluar(arbol.izquierda) + evaluar(arbol.derecha)
        elif arbol.valor == '-':
            return evaluar(arbol.izquierda) + evaluar(arbol.derecha)
        else:
            return int(arbol.valor)

arbol=Nodo(None,0)
arbol.insertar(arbol,100)
arbol.insertar(arbol,50)
arbol.insertar(arbol,200)
arbol.inorden(arbol)
arbol.preorden(arbol)
arbol.posorden(arbol)
