a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

i = 0
lista = []


if a > 0:
    i = i + 1
    lista.append(a)
if b > 0:
    i = i + 1
    lista.append(b)
if c > 0:
    i = i + 1
    lista.append(c)
if d > 0:
    i = i + 1
    lista.append(d)
if e > 0:
    i = i + 1
    lista.append(e)
if f > 0:
    i = i + 1
    lista.append(f)

soma = sum(lista)
media = (soma / i)   
print(f"{i:.0f} valores positivos")
print(f"{media:.1f}")