produtos = {
    "Suco": 4.00,
    "Refrigerante": 6.00,
    "Água": 2.00,
    "Cerveja": 5.00
}

print("Digite o produto: ")
produto = input()
if produto in produtos:
    print("O preço é: " + str(produtos[produto]))
else:
    print("Produto não encontrado")
