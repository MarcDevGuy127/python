#9. Conte de 0 a 50 e pule os múltiplos de 4.

for i in range(0,51):
    if i % 4 == 0:
        i = i+1
    else:
        print(i)