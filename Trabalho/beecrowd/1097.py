I = 1
J = 7

while I < 10:
    cont = 0
    J = J
    while cont != 3:
        print(f"I={I:.0f} J={J:.0f}")
        J -= 1
        cont += 1
    I += 2
    J += 5