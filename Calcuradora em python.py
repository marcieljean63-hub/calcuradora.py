# Calculadora Simples 

print("===Calculadora===")

# Entrada de dados 
num1 = int(input("Digite o primeiro número: "))
operacao = input ("Digite a operação (+, -, *, /): ")
num2 = int(input("Digite o segundo número: "))

#Lógica 
if operacao == "+": 
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero"
else: 
    resultado = "Operação inválida"
print(f"Resultado: {resultado}")

