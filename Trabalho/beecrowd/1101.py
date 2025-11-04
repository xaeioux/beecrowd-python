[m, n] = map(int, input().split())
lista = []
soma = sum(lista)

while n > 0 and m > 0:
    if n > m:
        for i in range (m, n):
            lista.append(i)
            i += 1
            print(f"{lista} Sum={soma}")
            [n, m] = map(int, input().split())

    else:
        for i in range (n, m):
            lista.append(i)
            i += 1
            print(f"{lista} Sum={soma}")
            [n, m] = map(int, input().split())
