#6. Verifique se um número é positivo, negativo ou zero.

x = float(input("Digite um numero:"))

if x > 0:
    print(f"{x} e positivo.")
elif x < 0:
    print(f"{x} e negativo.")
elif x == 0:
    print(f"{x} e zero.")