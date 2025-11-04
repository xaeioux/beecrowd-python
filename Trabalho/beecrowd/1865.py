x = int(input())

for i in range(x):
    [a, b] = map(str, input().split())
    if a != "Thor":
        print("N")
    else:
        print("Y")