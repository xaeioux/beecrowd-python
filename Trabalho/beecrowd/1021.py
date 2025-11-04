n = float(input())

cedulas = [100, 50, 20, 10, 5, 2]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for cedula in cedulas:
    quantia = n // cedula
    print(f"{quantia:.0f} nota(s) de R$ {cedula:.2f}")
    n = n % cedula
    
print("MOEDAS:")
for moeda in moedas:
    quantia = n // moeda
    print(f"{quantia:.0f} moeda(s) de R$ {moeda:.2f}")
    n = n % moeda + 0.001
