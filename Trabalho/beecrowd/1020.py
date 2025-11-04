n = int(input())

ano = n // 365
n = n % 365
print(f"{ano:.0f} ano(s)")
mes = n // 30
n = n % 30
print(f"{mes:.0f} mes(es)")
print(f"{n:.0f} dia(s)")