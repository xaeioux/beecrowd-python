[inicio, final] = map(int, input().split())

if final > inicio:
    duracao = final - inicio
elif final < inicio:
    duracao = (24 - inicio) + final
else:
    duracao = 24
    
print(f"O JOGO DUROU {duracao:.0f} HORA(S)")
