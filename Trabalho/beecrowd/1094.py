n = int(input())

total_coelho = 0
total_rato = 0
total_sapo = 0
total_cobaia = 0

for i in range(n):
    entrada = input().split()
    quantidade = int(entrada[0])
    tipo = str(entrada[1])
    
    total_cobaia += quantidade
    if tipo == "C":
        total_coelho += quantidade
    if tipo == "R":
        total_rato += quantidade
    if tipo == "S":
        total_sapo += quantidade
        
        
pcent_coelho = (total_coelho / total_cobaia) * 100        
pcent_rato = (total_rato / total_cobaia) * 100
pcent_sapo = (total_sapo / total_cobaia) * 100


print(f"Total: {total_cobaia:.0f} cobaias")
print(f"Total de coelhos: {total_coelho:.0f}")
print(f"Total de ratos: {total_rato:.0f}")
print(f"Total de sapos: {total_sapo:.0f}")
print(f"Percentual de coelhos: {pcent_coelho:.2f} %")
print(f"Percentual de ratos: {pcent_rato:.2f} %")
print(f"Percentual de sapos: {pcent_sapo:.2f} %")