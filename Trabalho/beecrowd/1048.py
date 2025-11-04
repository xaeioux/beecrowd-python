salario = float(input())

if salario <= 400:
    percentual = 0.15
    ajuste = salario * percentual
elif salario <= 800:
    percentual = 0.12
    ajuste = salario * percentual
elif salario <= 1200:
    percentual = 0.10
    ajuste = salario * percentual
elif salario <= 2000:
    percentual = 0.07
    ajuste = salario * percentual
else:
    percentual = 0.04
    ajuste = salario * percentual

percentual = percentual * 100    
total = salario + ajuste

print (f"Novo salario: {total:.2f}")
print (f"Reajuste ganho: {ajuste:.2f}")
print (f"Em percentual: {percentual:.0f} %")