"""
Um sorteio de bombom para alunos,
esses bombos serão sorteados randômicamenteO número deve corresponder ao número do diário"""


import random

#looping - iteração - repetição - laço
while True:
    num_aleatorio = random.randint(1,25)
    resposta = input("Deseja sortear outro número? (s/n)" ).strip().lower()
    if resposta != "s":
        print("encerrando o sorteio")
        break
    else:
        continue