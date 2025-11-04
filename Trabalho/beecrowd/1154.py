idade = 100
soma = 0
i = 0

while idade >= 0:
    idade = int(input())
    if idade >= 0:
        soma += idade
        i += 1

media = soma / i
print(f"{media:.2f}")
    