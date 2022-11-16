

class No:
    def __init__(self, data, direita=None, esquerda=None):
        self.data = data
        self.direita = direita
        self.esquerda = esquerda


class ArvoreAkinator:

    def __init__(self):
        self.raiz = No("macaco")

    def inserir_direita(self, no, data):
        no.direita = data


    def inserir_esquerda(self, no, data):
        no.esquerda = No(data)


class Akinator:
    def __init__(self):
        self.arvore = ArvoreAkinator()

    # push test

    def jogar(self):
        rodando = True
        contador = 0
        print("Pense em um animal")
        no_atual = self.arvore.raiz
        no_anterior = self.arvore.raiz
        is_animal = True
        recomecar = True
        msg = no_atual.data

        while rodando:
            if(recomecar == True):
                no_atual = self.arvore.raiz
                no_anterior = self.arvore.raiz
                print("--------------------------------")
                recomecar = False


            if(contador > 0):
                if(type(no_atual) == str):
                    msg = no_atual
                    is_animal = True
                else:
                    msg = no_atual.data
                    is_animal = False


            contador += 1
            usr_resposta = input(f'Seu animal é {msg}? [s/n]: ')

            #se nó for animal, verifica se acertou e prossegue de acordo
            if(is_animal == True):
                if usr_resposta.lower() == 's':
                    print('Eu sabia!')
                    rodando = False

                else:
                    animal_usuario = input("Que animal você pensou? ")
                    nova_caracteristica = input(f'Como o {animal_usuario} é diferente de {msg}? Diga uma caracteristica: ')

                    #direita é sim, esquerda não(animal antigo vai pra esquerda)
                    novoNo = No(data = nova_caracteristica, direita = animal_usuario, esquerda = msg)

                    if(contador == 1):
                        self.arvore.raiz.data = nova_caracteristica
                        self.arvore.raiz.direita = animal_usuario
                        self.arvore.raiz.esquerda = msg

                    else:
                        self.arvore.inserir_direita(no_anterior, novoNo)

                    recomecar = True

            #se nó for pergunta, avança para esquerda/direita
            else:
                #sim indica que deve ir para direita
                if (usr_resposta.lower() == "s"):
                    no_anterior = no_atual
                    no_atual = no_atual.direita

                else:
                    no_anterior = no_atual
                    no_atual = no_atual.esquerda



jogo = Akinator()
jogo.jogar()
