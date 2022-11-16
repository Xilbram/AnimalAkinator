
class No:
    def __init__(self, data, direita =  None, esquerda = None, ehAnimal = True):
        self.data = data
        self.direita = direita
        self.esquerda  = esquerda
        self.ehAnimal = ehAnimal


class ArvoreAkinator:
    def __init__(self):
        self.raiz = No("macaco")

    def inserirDireita(self, no, data):
        no.direita = No(data)

    def inserirEsquerda(self, no, data):
        no.esquerda = No(data)

class Akinator:
    def __init__(self):
        self.arvore = ArvoreAkinator()


    def jogar(self):
        rodando = True
        contador = 0
        print("Pense em um animal")
        no_atual = self.arvore.raiz
        while rodando:
            if(contador > 0):
                print("Deixe-me pensar, vamos novamente")

            usr_resposta = input("Seu animal é %s? [s/n]" %no_atual.data)

            #se nó for animal, verifica se acertou e prossegue de acordo
            if(no_atual.ehAnimal == True):
                if (usr_resposta.lower() == "s"):
                    print("Eu sabia!")
                    rodando = False

                else:
                    animal_usuario = input("Que animal você pensou?")

                    #A caracteristica fornecida pelo usuario vira a cabeça, o animal base vai para a esquerda(não)
                    #e o novo animal para a direita(sim)

                    nova_pergunta = input("Como o %s é diferente de %s? Diga uma caracteristica" %(animal_usuario, no_atual.data))

                    #direita é sim, esquerda não(animal antigo vai pra esquerda)
                    aux = No(nova_pergunta, animal_usuario, no_atual.data, False)
                    no_atual = aux

            #se nó for pergunta, avança para esquerda/direita
            else:
                #sim indica que deve ir para direita
                if (usr_resposta.lower() == "s"):
                    no_atual = no_atual.direita

                else:
                    no_atual = no_atual.esquerda

            contador += 1


jogo = Akinator()
jogo.jogar()







