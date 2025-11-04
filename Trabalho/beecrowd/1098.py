I = float(0)
J = float(1)


while I <= 2:
    cont = 0
    while cont != 3:
        if I == 0 or I == 1 or I == 2:
            print(f"I={I:.0f} J={J:.0f}")
        else:
            print(f"I={I} J={J}")
        J += 1
        cont += 1
        
        
    J = round(J - 2.8, 1)
    I = round(I + 0.2, 1)