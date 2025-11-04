[id1, qt1, val1] = map(float, input().split())
[id2, qt2, val2] = map(float, input().split())

tot1 = (qt1 * val1)
tot2 = (qt2 * val2)

total = tot1 + tot2

print(f"VALOR A PAGAR: R$ {total:.2f}")