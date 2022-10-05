from typing import Optional


class Node:
    def __init__(self, val, next):
        self.__val = val
        self.__next = next

    def getNext(self):
        return self.__next
    def getVal(self):
        return self.__val
    def setNext(self, pNext):
        self.__next = pNext
    def setVal(self, pVal):
        self.__val = pVal



class Lista:
    def __init__(self):
        self.__first: Optional[Node] = None


    def show(self):
        contador = 0
        nodeExibir = self.__first
        if (self.__first == None):
            return "Não há elementos"
        else:
            while True:
                print("Posição nó: %s -> valor: %s" %(contador, nodeExibir.getVal()))

                contador += 1
                aux = nodeExibir.getNext()
                nodeExibir = aux
                if (nodeExibir == None):
                    break

    def removeFirst(self):
        auxNext = self.__first.getNext()
        self.__first = auxNext

    def removeLast(self):
        if(self.__first == None):
            return "Não há elementos"

        aux = self.__first
        auxNext = self.__first.getNext()

        if(aux.getNext() == None):
            self.__first = None
            return

        while True:
            if (auxNext.getNext() == None):
                aux.setNext(None)
                return
            aux = aux.getNext()
            auxNext = auxNext.getNext()



    def insertFirst(self, pValue):
        newNode = Node(pValue, None)

        if(self.__first == None):
            self.__first = newNode

        else:
            newNode.setNext(self.__first)
            self.__first = newNode



    def insertLast(self, pValue):
        newNode = Node(pValue, None)

        if(self.__first == None):
            self.__first = newNode
            return

        else:
            aux = self.__first
            while True:
                if(aux.getNext() == None):
                    aux.setNext(newNode)
                    return
                aux = aux.getNext()



    def insertAfter(self, pNodeValue, pValue):
        newNode = Node(pValue, None)

        #Insert the desired node on the last position. If the getNext on your node is equal to None, and your last node is the node you are searching, it means
        #he didn't exist on the list before

        #after 40 insert X
        #10 -> 20 -> 30 -> 40 ->50
        #goto 10 -> goto 20 -> goto 30 -> goto 40 -> found him
        #swap 40 for X, create new node, put 40 on new node, make 40 point to old 40 nextVal, make X point to 40 (30 will point to X)

        if(self.__first == None):
            return "Não há valores"

        else:
            aux = self.__first
            self.insertLast(pNodeValue)
            while True:
                if(aux.getVal() == pNodeValue):
                    nextAux = aux.getNext()
                    newNode.setNext(nextAux)
                    aux.setNext(newNode)
                    self.removeLast()
                    return
                aux = aux.getNext()
                if(aux.getNext() == None):
                    self.removeLast()
                    return "O elemento de indexação não está presente."


    def insertBefore(self, pNodeValue, pValue):
        newNode = Node(pValue, None)

        if(self.__first == None):
            return "Não há elementos"

        aux = self.__first


lista = Lista()
print("Sem elementos")
lista.show()
lista.insertFirst(10)
lista.insertFirst(5)
lista.insertFirst(3)
lista.insertFirst(900)


lista.insertLast(313)
lista.insertLast(314)
lista.show()

lista.insertAfter(10,50)
lista.show()