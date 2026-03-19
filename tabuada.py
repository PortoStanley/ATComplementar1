print("Me diga um numero: ")

numero = int(input())
print("A tabuada do numero " + str(numero) + "é: ")
for i in range(1, 11):
    print(str(numero) + " x " + str(i) + " = " + str(numero * i))
