#8. Imprima a tabuada de um número fornecido pelo usuário.

num = int(input("Digite um numero:"))

for i in range(1, num+1):
    resultado = i * num 
    print(f"{i} * {num}: ",resultado)