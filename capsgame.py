import random

#dado entre 2 a 12

numero_aleatorio = random.randint (2,12)
numero_aleatorio2 = 0

#verificar o primeiro dado

def primeirodado ():
    print(numero_aleatorio)
    if numero_aleatorio == 11:
        print("Você ganhou")
    elif numero_aleatorio == 7:
        print("Você ganhou")
    elif numero_aleatorio == 2:
        print("Você perdeu")
    elif numero_aleatorio == 3:
        print("Você perdeu")
    elif numero_aleatorio == 12:
        print("Você perdeu")
    elif numero_aleatorio == 4:
        print("você vai precisar rodar outro dado !")
    elif numero_aleatorio == 5:
        print("você vai precisar rodar outro dado !")
    elif numero_aleatorio == 6:
        print("você vai precisar rodar outro dado !")
    elif numero_aleatorio == 8:
        print("você vai precisar rodar outro dado !")
    elif numero_aleatorio == 9:
        print("você vai precisar rodar outro dado !")
    elif numero_aleatorio == 10:
        print("você vai precisar rodar outro dado !")
    

#segunda parte do jogo

def final ():
    numero_aleatorio == numero_aleatorio2
    numero_aleatorio = random.randint (2,12)


############################################
#implementação

primeiraJogada = primeirodado()