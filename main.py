class No:
    def __init__(self, data, direita=None, esquerda=None):
        self.data = data
        self.direita = direita
        self.esquerda = esquerda
        
        
class ArvoreAkinator:

    def __init__(self):
        self.raiz = No("macaco")

    def inserir_direita(self, no, data):
        no.direita = No(data)

    def inserir_esquerda(self, no, data):
        no.esquerda = No(data)


class Akinator:
    def __init__(self):
        self.arvore = ArvoreAkinator()

    def jogar(self):

        rodando = True
        contador = 0

        print('Pense em um animal')
        # raiz = self.arvore.raiz  # não estava sendo usado. comentei para ver se há mudança no código
        no_atual = self.arvore.raiz
        is_animal = True
        msg = no_atual.data

        while rodando:

            if contador > 0:
                print('-'*35)

                if isinstance(no_atual, str):
                    msg = no_atual
                    is_animal = True

                else:
                    msg = no_atual.data
                    is_animal = False

            usr_resposta = input(f'Seu animal é {msg}? [s/n]: ')

            # se nó for animal, verifica se acertou e prossegue de acordo
            if is_animal:
                if usr_resposta.lower() == 's':
                    print('Eu sabia!')
                    rodando = False

                else:
                    animal_usuario = input('Que animal você pensou? ')

                    # a caracteristica fornecida pelo usuario vira a cabeça, o animal base vai para a esquerda(não)
                    # e o novo animal para a direita(sim)

                    nova_pergunta = input(f'Como o {animal_usuario} é diferente de {msg}? Diga uma caracteristica: ')

                    # direita é sim, esquerda não(animal antigo vai pra esquerda)
                    no_atual = No(data=nova_pergunta, direita=animal_usuario, esquerda=msg)

            # se nó for pergunta, avança para esquerda/direita
            else:
                # 'sim' indica que deve ir para direita
                no_atual = no_atual.direita if usr_resposta.lower() == 's' else no_atual.esquerda

            contador += 1


jogo = Akinator()
jogo.jogar()
