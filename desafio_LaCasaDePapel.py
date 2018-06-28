#Autores: Gisela Miranda Difini e Tiago Costa

import random
    
def NUMBER_OF_TRIES():
    return 10

def MSG_INPUT_START():
  return "Tente adivinhar o segredo do cofre:"

def MSG_INPUT():
    return "Insira 3 números (de 1 a 9) para tentar abrir o cofre!"

def MSG_WIN():
    return "Parabéns! Você acertou o segredo!"

def MSG_GAME_OVER():
    return "O COFRE EXPLODIU!"

numbers = []
numbersGuest = []

def getNumbersGuest():
  print(MSG_INPUT_START())
  print(MSG_INPUT())
  #pedir para o usuário inserir 3 números
  for x in range (0, 3):
    input_number = input()
    numbersGuest.append(int(input_number))
  print(numbersGuest)

def getRandNumbers():
  #inserir 3 números aleatórios no array numbers
  for x in range (0, 3):
    numbers.append(random.randint(1, 9))
  

def start_game():
    global numbersGuest
    global numbers
    tries = 0

    while tries < NUMBER_OF_TRIES():
        #gerar o array com números aleatórias a cada tentaiva
        getRandNumbers()
        getNumbersGuest()
        
        if numbers==numbersGuest:
          print(MSG_WIN())
          return
        countCorreto = 0;
        countErrado = 0;
        
        for x in range (3):
          if numbersGuest[x] == numbers[x]:
            countCorreto += 1            
          else:
            countErrado +=1
        print("Número gerado: ", numbers)
        print("Número digitado: ", numbersGuest)
        print(countCorreto, "número correto no lugar correto")
        print(countErrado, "número errado no lugar errado", '\n')

        tries = tries + 1
        del numbersGuest[0:3]
        del numbers[0:3]

    print(MSG_GAME_OVER())

#---------
start_game()