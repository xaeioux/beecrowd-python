[a, b, c] = map(int, input().split())

maior1 = ( a + b + abs ( a - b )) / 2
maior2 = ( c + maior1 + abs ( maior1 - c )) / 2

print(f"{maior2:.0f} eh o maior")