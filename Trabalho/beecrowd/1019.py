n = int(input())

horas = n // 3600
n = n % 3600
minutos = n // 60
n = n % 60

print(f"{horas:.0f}:{minutos:.0f}:{n:.0f}")