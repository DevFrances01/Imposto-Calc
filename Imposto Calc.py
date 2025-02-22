# Solicitar ao usuário os nomes e as quantidades
print("Seja bem-vindo!")
estabelecimento = input("Digite o nome do seu estabelecimento: ")
funcionarios = int(input("Digite quantos funcionários o seu estabelecimento tem: "))

if funcionarios >= 4:
    print("Você precisa informar a quantidade de funcionários à prefeitura.")
else:
    print("Você não precisa informar à prefeitura a quantidade de funcionários.")

idade_estabelecimento = int(input("Digite a idade do seu estabelecimento (em anos): "))

if idade_estabelecimento >= 4:
    print("Você precisa informar a idade do estabelecimento à prefeitura.")
else:
    print("Você não precisa informar a idade à prefeitura.")

nomes = input("Digite os nomes dos produtos separados por vírgula: ")
quantidades = input("Digite as quantidades correspondentes a cada produto, separadas por vírgula: ")
preco = float(input("Digite o faturamento mensal do seu estabelecimento: "))



imposto_total = 2 * preco
#calc

print(f"o imposto total R$:",imposto_total)