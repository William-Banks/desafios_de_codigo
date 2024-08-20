# Declaração das variáveis de número a partir dos valores digitados pelo usuário
num1 = input("Digite o primeiro número para ser somado: ")
num2 = input("Digite o segundo número para ser somado: ")

# Conversão das variáveis para números inteiros
num1 = int(num1)
num2 = int(num2)

# Declaração da variável de soma
soma = num1 + num2

# Impressão da soma dos valores recebidos
print("====================")
print(f"A soma dos números é: {soma}")
print("====================")