numero = int(input("Digite um número: "))
# Verifica par ou ímpar
if numero % 2 == 0:
    tipo = "PAR"
else:  tipo = "IMPAR"

# Verifica positivo, negativo ou zero
if numero > 0: 
    sinal = "POSITIVO"
elif numero < 0:
        sinal = "NEGATIVO"
 else:
        sinal = "ZERO"
print(f"O número é {tipo} e {sinal}")
