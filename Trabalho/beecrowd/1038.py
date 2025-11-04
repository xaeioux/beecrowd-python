[pedido, quantia] = map(int, input().split())

if pedido == 1:
    print(f"Total: R$ {quantia * 4:.2f}")
elif pedido == 2:
    print(f"Total: R$ {quantia * 4.5:.2f}")
elif pedido == 3:
    print(f"Total: R$ {quantia * 5:.2f}")
elif pedido == 4:
    print(f"Total: R$ {quantia * 2:.2f}")
else:
    print(f"Total: R$ {quantia * 1.5:.2f}")