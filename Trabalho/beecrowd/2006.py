t = int(input())
[a, b, c, d, e] = map(int, input().split())

lista = [a, b, c, d, e]
resposta = 0

for i in lista:
    if i == t:
        resposta = resposta + 1

print (resposta)