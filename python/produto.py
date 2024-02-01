from dataclasses import dataclass


@dataclass
class Produto:
    id_produto: int
    nome_do_produto: str
    preco: float


produto1 = Produto(
    id_produto=1,
    nome_do_produto="Ração Premium para Cães",
    preco=50.99
)

produto2 = Produto(
    id_produto=2,
    nome_do_produto="Areia para Gatos",
    preco=12.99
)

produto3 = Produto(
    id_produto=3,
    nome_do_produto="Brinquedo de Pelúcia para Cães",
    preco=15.50
)

produto4 = Produto(
    id_produto=4,
    nome_do_produto="Coleira Antipulgas",
    preco=22.99
)

produto5 = Produto(
    id_produto=5,
    nome_do_produto="Petisco para Gatos (Sabor Salmão)",
    preco=8.99
)

produto6 = Produto(
    id_produto=6,
    nome_do_produto="Shampoo Hipoalergênico para Cães",
    preco=18.75
)

produto7 = Produto(
    id_produto=7,
    nome_do_produto="Caixa de Transporte para Gatos",
    preco=35.99
)

produto8 = Produto(
    id_produto=8,
    nome_do_produto="Escova para Pelos de Gatos",
    preco=10.49
)

produto9 = Produto(
    id_produto=9,
    nome_do_produto="Tapete Higiênico para Cães",
    preco=28.99
)

produto10 = Produto(
    id_produto=10,
    nome_do_produto="Comedouro Automático para Cães",
    preco=40.50
)
