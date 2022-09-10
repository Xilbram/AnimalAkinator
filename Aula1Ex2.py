



class SM:
    def __init__(self, linhas: int, colunas: int):
        self.__arr = []
        self.__linhas = linhas
        self.__colunas = colunas
        self.__arrSize = self.__linhas * self.__colunas
        self.__arr = [None] * self.__arrSize

    def atribuir(self, pLinha, pCol, pData):
        self.__arr[((-1 + pLinha) * self.__colunas + pCol) - 1] = pData


    def acessar(self, pLinha, pCol):
        return self.__arr[((pLinha - 1) * self.__colunas + pCol) -1]


    def verMatriz(self):
        return self.__arr



teste = SM(4,4)
teste.atribuir(2,4, "olá")
print(teste.verMatriz())

teste2 = SM(10,2)
teste2.atribuir(8,2,"Linha 8 coluna 2")
print(teste2.verMatriz())

teste3 = SM(3,4)
teste3.atribuir(3,1,"oi")
print(teste3.verMatriz())