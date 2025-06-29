#4. Determine se um número é par ou ímpar.

num = float(input("Insira um numero:"))

if num % 2 == 0:
    print(f"{num} e par!")
else:
    print(f"{num} e impar!")