print("Seja bem-vindo ao Quiz do Jean!")
answer_user = input("Quer começar? (S/N) ")

if answer_user != "S":
    quit()

score = 0

print("Começando...")

print("Quem é o melhor jogador de futebol do mundo? \n A) Neymar \n B) Messi \n C) Cristiano Ronaldo \n")
answer_1 = input("Resposta: ")

if answer_1 == "B":
    print("Resposta correta! ")
    score = score + 1
else:
    print("Resposta incorreta.")

print("Quem foi o maior artilheiro da Seleção Brasileira? \n A) Neymar \n B) Pelé \n C) Ronaldo \n")
answer_2 = input("Resposta: ")

if answer_2 == "A":
    print("Resposta correta! Uns dos melhores jogadores de todos os tempos.")
    score = score + 1
else:
    print("Resposta incorreta.")

print(f"Quiz acabou!... Sua pontuação foi: {score}/2")
