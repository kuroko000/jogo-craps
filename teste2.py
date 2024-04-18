import random #importação para podermos simular um dado

def roll_dice(): #def que vai atribuir o valor as jogadas do game
    return random.randint(1, 6) + random.randint(1, 6)

def craps_game(): #
    point = 0
    while True: #loop do gamep, pra fazer os teste do valor recebido na def roll_dice
        input("Pressione Enter para lançar os dados...")
        dice_sum = roll_dice()
        print("Você lançou um total de", dice_sum)
        
        if point == 0: #primeira rodada
            if dice_sum in [7, 11]:
                print("Você tirou um natural! Você ganhou!")
                break
            elif dice_sum in [2, 3, 12]:
                print("Você tirou um craps! Você perdeu!")
                break
            else:
                print("Seu ponto é", dice_sum)
                point = dice_sum
        else:
            if dice_sum == point: #segunda rodada em diante
                print("Você tirou seu ponto novamente! Você ganhou!")
                break
            elif dice_sum == 7:
                print("Você tirou um 7! Você perdeu!")
                break

print("Bem-vindo ao jogo de Craps!")
craps_game()
