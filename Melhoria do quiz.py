print("Seja bem-vindo ao Quiz do Jean!")

answer_user = input("Quer começar? (S/N) ").upper()

if answer_user != "S":
    print("Quiz encerrado.")
    quit()

print("Começando...\n")

score = 0

# Pergunta 1
print("Quem é o melhor jogador de futebol do mundo?")
print("A) Neymar")
print("B) Messi")
print("C) Cristiano Ronaldo")

answer_1 = input("Resposta: ").upper()

if answer_1 == "B":
    print("Resposta correta!\n")
    score += 1
else:
    print("Resposta incorreta.\n")

# Pergunta 2
print("Quem foi o maior artilheiro da Seleção Brasileira?")
print("A) Neymar")
print("B) Pelé")
print("C) Ronaldo")

answer_2 = input("Resposta: ").upper()

if answer_2 == "A":
    print("Resposta correta!\n")
    score += 1
else:
    print("Resposta incorreta.\n")

# Resultado final
print(f"Você acertou {score} de 2 perguntas.")

if score == 2:
    print("Mandou muito bem! 🔥")
elif score == 1:
    print("Foi bem! 👏")
else:
    print("Precisa melhorar 😅")