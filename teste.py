import random

def determinar_resultado(numero_aleatorio):
    resultados = {
        "ganhou": [11, 7],
        "perdeu": [2, 3, 12],
        "outra_vez": [4, 5, 6, 8, 9, 10]
    }
    for resultado, numeros in resultados.items():
        if numero_aleatorio in numeros:
            return resultado

def jogar():
    numero_aleatorio = random.randint(2, 12)
    print("Número aleatório:", numero_aleatorio)
    resultado = determinar_resultado(numero_aleatorio)
    if resultado == "ganhou":
        print("Você ganhou!")
    elif resultado == "perdeu":
        print("Você perdeu!")
    elif resultado == "outra_vez":
        print("Você vai precisar rodar outro dado!")

# Teste
jogar()
