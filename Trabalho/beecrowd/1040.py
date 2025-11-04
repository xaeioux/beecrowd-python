[a, b, c, d] = map(float, input().split())

media = ((a * 2) + (b * 3) + (c * 4) + d ) / 10

print (f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    e = float(input())
    print(f"Nota do exame: {e:.1f}")
    if e < 4.9:
        print("Aluno reprovado.")
        
    else:
        mf = (media + e) / 2
        print("Aluno aprovado.")
        print("Media final:", mf)
    