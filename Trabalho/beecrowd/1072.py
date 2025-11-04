n = int(input())

in_cont = 0
out_cont = 0

for i in range(n):
    num = int(input())
    if num < 10 or num > 20:
        out_cont = out_cont + 1
    else:
        in_cont = in_cont + 1
        
print(f"{in_cont:.0f} in")
print(f"{out_cont:.0f} out")