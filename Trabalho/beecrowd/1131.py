resposta = 1
vit_inter = 0
vit_gremio = 0
empates = 0
loop = 0

while resposta == 1:
    [inter, gremio] = map(int, input().split())
    loop += 1
    if inter > gremio:
        vit_inter += 1
    elif gremio > inter:
        vit_gremio += 1
    else:
        empates += 1
        
    print("Novo grenal (1-sim 2-nao)")
    resposta = int(input())
    
    
print(f"{loop:.0f} grenais")
print(f"Inter:{vit_inter:.0f}")
print(f"Gremio:{vit_gremio:.0f}")
print(f"Empates:{empates:.0f}")

if vit_inter > vit_gremio:
    print("Inter venceu mais")
elif vit_gremio > vit_inter:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")