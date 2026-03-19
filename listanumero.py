print("Me cite uma lista de 5 numeros: ")

numero1 = int(input())
numero2 = int(input())
numero3 = int(input())
numero4 = int(input())
numero5 = int(input())

numeros = [numero1, numero2, numero3, numero4, numero5]
print("O maior numero da lista é, " + str(max(numeros)) + " o menor numero da lista é, " + str(min(numeros)) + " e a soma de todos é, " + str(sum(numeros)))
