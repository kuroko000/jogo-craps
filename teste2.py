import random #importação para podermos simular um dado

def rolaguem_de_dados(): #def que vai atribuir o valor as jogadas do game
    return random.randint(1, 6) + random.randint(1, 6)

def game(): 
    ponto = 0
    while True: #loop do game, pra fazer os teste do valor recebido na def rolaguem_de_dados
        input("Pressione Enter para lançar os dados...")
        resultado = rolaguem_de_dados()
        print("Você lançou um total de", resultado)
        
        if ponto == 0: #primeira rodada
            if resultado in [7, 11]:
                print("Você tirou um natural! Você ganhou!")
                break
            elif resultado in [2, 3, 12]:
                print("Você tirou um craps! Você perdeu!")
                break
            else:
                print("Seu ponto é", resultado)
                ponto = resultado
        else:
            if resultado == ponto: #segunda rodada em diante
                print("Você tirou seu ponto novamente! Você ganhou!")
                break
            elif resultado == 7:
                print("Você tirou um 7! Você perdeu!")
                break

print("Bem-vindo ao jogo de Craps!")
game()
