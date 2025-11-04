a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

i = 0

if a % 2 == 0:
    i = i + 1
if b % 2 == 0:
    i = i + 1
if c % 2 == 0:
    i = i + 1
if d % 2 == 0:
    i = i + 1
if e % 2 == 0:
    i = i + 1
    
print(f"{i:.0f} valores pares")