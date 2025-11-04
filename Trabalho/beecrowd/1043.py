[a, b, c] = map(float, input().split())

if a + b > c and c + b > a and c + a > b:
    perimetro = a + b + c
    print(f"Perimetro = {perimetro:.1f}")
else:
    area = (( a + b ) * c) / 2
    print(f"Area = {area:.1f}")
