#Esse código tem objetivo de trazer o preço total de um produto 

#Variáveis com detalhes do produto
nome_produto = "Cadeira Infantil"
preco_unitario = 12.40
quantidade = 3

#Variáveis com o cálculo do valor total
preco_total = quantidade * preco_unitario

#Exibição das informações do produto e do valor total
print(f"Produto: {nome_produto}")
print(f"Preço unitário: R$ {preco_unitario:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Preço total: R$ {preco_total:.2f}")