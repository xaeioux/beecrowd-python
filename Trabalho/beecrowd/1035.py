[a, b, c, d] = map(int, input().split())

somacd = c + d
somaab = a + b
if b > c and d > a and somacd > somaab and c > 0 and d > 0 and a % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
    