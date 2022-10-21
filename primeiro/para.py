x: int
soma: int

N = int(input("Quantos numeros serao digitados: "))

soma = 0

for i in range(0, N, 1):
    x = int(input("Digite um número: "))
    soma = soma + x

print("SOMA = ", soma)