print("Calcule seu desconto aqui!")

preco_produto = float(input("Preço do produto: "))
desconto = float(input("% do desconto: "))

valor_desconto = preco_produto * (desconto / 100)

preco_final = preco_produto - valor_desconto
print(f"Preço final do produto com desconto é: {preco_final:.2f}")
