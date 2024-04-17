import random

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def craps_game():
    point = 0
    while True:
        input("Pressione Enter para lançar os dados...")
        dice_sum = roll_dice()
        print("Você lançou um total de", dice_sum)
        
        if point == 0:
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
            if dice_sum == point:
                print("Você tirou seu ponto novamente! Você ganhou!")
                break
            elif dice_sum == 7:
                print("Você tirou um 7! Você perdeu!")
                break

print("Bem-vindo ao jogo de Craps!")
craps_game()
