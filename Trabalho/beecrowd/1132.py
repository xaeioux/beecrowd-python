x = int(input())
y = int(input())
soma = 0

if x > y:
    a = y
    b = x
if x <= y:
    a = x
    b = y

while a <= b:
    if a % 13 != 0:
        soma = soma + a
    a = a + 1
        
print(soma)