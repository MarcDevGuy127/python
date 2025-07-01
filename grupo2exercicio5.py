#10. Some os números pares entre 1 e 100.

soma = 0
for i in range(1,101):
    if  i % 2 == 0:
        soma = soma + i
        print(soma)