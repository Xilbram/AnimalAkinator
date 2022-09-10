



class SAI:
    def __init__(self, li: int, ls: int):
        self.__dataArray = []
        self.__first_index = li
        self.__last_index = ls
        self.__indexArray = []
        self.__arrSize = int((((self.__first_index - self.__last_index)**2)**(1/2)) + 1)


        for i in range(self.__arrSize):
            self.__dataArray.append(None)
            if self.__first_index > self.__last_index:
                self.__indexArray.append(self.__first_index - i)
            else:
                self.__indexArray.append(self.__first_index + i)

    def exibir_listas(self):
        return self.__dataArray, self.__indexArray

    def inserir(self, pIndex, pData):
        for i in range(self.__arrSize):
            if self.__indexArray[i] == pIndex:
              indexTrue = i
              self.__dataArray[indexTrue] = pData


    def acessar(self, pIndex):
        for i in range(self.__arrSize):
            if self.__indexArray[i] == pIndex:
                return self.__dataArray[i]



teste = SAI(7,3)
teste2 = SAI(-4,-2)
teste3 = SAI(5,10)


teste.inserir(6, 10)
print("Inserindo 10 na segunda posição")
print("Teste 1: %s" %teste.acessar(6))

teste2.inserir(-3, "a")
print("Inserindo a na segunda posição")
print("Teste 2: %s" %teste2.acessar(-1))

teste3.inserir(8,"funcionou")
print("Inserindo funcionou na quarta posição")
print("Teste 3: %s " %teste3.acessar(8))


print('''Teste 1: %s
Teste 2: %s
Teste 3 %s''' %(teste.exibir_listas(), teste2.exibir_listas(), teste3.exibir_listas()))




class SAI():
    def __init__(self, inf, sup):
        self.__sup = sup
        self.__inf = inf
        if inf>sup:
            self.__sup = inf
            self.__inf = sup

        self.__range = self.__sup - self.__inf + 1
        self.__arr = [None] * self.__range

    def atribuir(self, pIndex, pData):
        self.__arr[pIndex - self.__inf] = pData
    def acessar(self, pIndex):
        return self.__arr[pIndex - self.__inf]


