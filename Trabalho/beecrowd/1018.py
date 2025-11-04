n = int(input())

print(n)

cedulas = [100, 50, 20, 10, 5, 2, 1]

for cedula in cedulas:
    quantia = n // cedula
    print(f"{quantia:.0f} nota(s) de R$ {cedula:.0f},00")
    n = n % cedula