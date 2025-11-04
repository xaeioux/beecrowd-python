[x, y] = map(int, input().split())

while x != y:
    if x > y:
        print("Decrescente")
        [x, y] = map(int, input().split())

    else:
        print("Crescente")
        [x, y] = map(int, input().split())
