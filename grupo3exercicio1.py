#Crie uma lista com 10 números e imprima o maior e o menor valor.

i = 0
maior = 0
menor = 0

for i in range(1, 11):
    arr = int(input(f"Digite um valor para a posicao {i}:"))
    
    if i == 1:
        maior = arr
        menor = arr
    else:
        if arr > maior:
            maior = arr
        elif arr < menor:
            menor = arr

print(f"Maior: {maior} - Menor: {menor}")