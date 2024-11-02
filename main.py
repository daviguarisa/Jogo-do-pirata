# matriz (localização)
class ponto: 
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self): 
        return (f'{self.x}, {self.y}')

# personagem
class personagem(ponto):

    def move_up(self):
        if self.y < 10:
            self.y += 1
        else:
            print('movimento proibido')
    def move_down(self):
        if self.y > 0:
            self.y -= 1
        else:
            print('movimento proibido')
    def move_right(self):
        if self.x < 10:
            self.x += 1
        else:
            print('movimento proibido')
    def move_left(self):
        if self.x > 0:
            self.x -= 1
        else:
            print('movimento proibido')

#tesouro
class recompensa(ponto):
    def __init__(self, x, y, nome):
        super(recompensa, self).__init__(x, y)
        self.nome = nome
    
    def __str__(self):
        return (f'{self.x}, {self.y}, {self.nome}')

    def __repr__(self):
        return (f'Tesouro: {str(self)}')

#gerar posiçoes aleatorias para os tesouros e para o personagem principal
import random

t1 = recompensa(random.randint(0, 10), random.randint(0, 10), 'Moeda')
t2 = recompensa(random.randint(0, 10), random.randint(0, 10), 'Moeda')
t3 = recompensa(random.randint(0, 10), random.randint(0, 10), 'Fruta')
t4 = recompensa(random.randint(0, 10), random.randint(0, 10), 'Fruta')
t5 = recompensa(random.randint(0, 10), random.randint(0, 10), 'Fruta')
t6 = recompensa(random.randint(0, 10), random.randint(0, 10), 'Baú do tesouro')

tesouros = [t1, t2, t3, t4, t5, t6]

pirata = personagem(random.randint(0, 10), random.randint(0, 10))

#checar tesouro
verificador = 0
def checar_recompensa(personagem, tesouros):
    global verificador
    verificador = 0
    for tesouro in tesouros:
        if tesouro.x == personagem.x and tesouro.y == personagem.y:
            print(f'Você encontrou um tesouro: {tesouro.nome}')
            if tesouro.nome == 'Fruta':
                verificador = 1
            elif tesouro.nome == 'Moeda':
                verificador = 2
            elif tesouro.nome == 'Baú do tesouro':
                verificador = 3
    return verificador

#dinamica com usuario
# print(tesouros) # -> Cheat
print("\nFinalmente chegamos em terra firme marujo! Agora explore essa ilha e me encontre um tesouro!")
print(f"Você está na posição {pirata.x}, {pirata.y}\n")
cont = 10
while True:
    movimento = input("Pra qual lado deseja ir? [cima, baixo, esquerda, direita]: ")
    if movimento == 'cima':
        pirata.move_up()
        cont -= 1
    elif movimento == 'baixo':
        pirata.move_down()
        cont -= 1
    elif movimento == 'esquerda':
        pirata.move_left()
        cont -= 1
    elif movimento == 'direita':
        pirata.move_right()
        cont -= 1
    else:
        print('Movimento Inválido')
        continue
    print(f"Você está na posição {pirata.x}, {pirata.y}, restam {cont} jogadas\n")

    checar_recompensa(pirata, tesouros)
    if verificador == 1:
        cont += 3
        print('Você achou uma fruta e ganhou mais 3 jogadas!')
        print(f"Agora você tem {cont} jogadas\n")
    elif verificador == 2:
        print("O tesouro deve estar próximo!\n")
    elif verificador == 3:
        print("AARRGH MARUJO!! Você encontrou o tesouro!! ESTAMOS RICOS!")
        break
    elif cont == 0:
        print("Você não encontrou o tesouro marujo? ARRGH AGORA VAI ANDAR NA PRANCHA!!")
        break
