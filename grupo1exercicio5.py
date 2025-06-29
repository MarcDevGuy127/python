#5. Crie uma calculadora básica (+, -, *, /) usando `if`, `elif`, `else`.

print("Calculadora")
operador = input("Selecione um operador(+ - * /) --> ")

print("Digite os valores:\n")
x = float(input("x:"))
y = float(input("y:"))

if operador == "+":
    calculo = x + y
    print(f"{x} + {y} = {calculo}")

elif operador == "-":
    calculo = x - y
    print(f"{x} - {y} = {calculo}")

elif operador == "*":
    calculo = x * y
    print(f"{x} * {y} = {calculo}")

elif operador == "/":
    calculo = x / y
    print(f"{x} / {y} = {calculo}")
else:
    print("Operador invalido")