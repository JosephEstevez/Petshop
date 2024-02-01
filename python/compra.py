from dataclasses import dataclass
from produto import Produto
from produto import produto1, produto2, produto3, produto4, produto5, produto6, produto7, produto8, produto9, produto10
from servico_adicional import Servico_Adicional
from servico_adicional import servico1, servico2, servico3, servico4, servico5, servico6, servico7, servico8, servico9, servico10
from cliente import Cliente
from cliente import cliente1, cliente2, cliente3, cliente4, cliente5, cliente6, cliente7, cliente8, cliente9, cliente10


@dataclass
class Compra:
    id_compra: int
    produto: tuple
    servico: tuple
    cliente: Cliente
    data_da_compra: str
    valor_total: float


compra1 = Compra(
    id_compra=1,
    produto=(produto1),
    servico=(servico1),
    cliente=cliente1,
    data_da_compra="01-02-2024",
    valor_total=76.98
)

compra2 = Compra(
    id_compra=2,
    produto=(produto2),
    servico=(servico2),
    cliente=cliente2,
    data_da_compra="02-02-2024",
    valor_total=45.99
)

compra3 = Compra(
    id_compra=3,
    produto=(produto3),
    servico=(servico3),
    cliente=cliente3,
    data_da_compra="03-02-2024",
    valor_total=28.50
)

compra4 = Compra(
    id_compra=4,
    produto=(produto4),
    servico=(servico4),
    cliente=cliente4,
    data_da_compra="04-02-2024",
    valor_total=117.99
)

compra5 = Compra(
    id_compra=5,
    produto=(produto5),
    servico=(servico5),
    cliente=cliente5,
    data_da_compra="05-02-2024",
    valor_total=58.48
)

compra6 = Compra(
    id_compra=6,
    produto=(produto6),
    servico=(servico6),
    cliente=cliente6,
    data_da_compra="06-02-2024",
    valor_total=53.50
)

compra7 = Compra(
    id_compra=7,
    produto=(produto7),
    servico=(servico7),
    cliente=cliente7,
    data_da_compra="07-02-2024",
    valor_total=79.49
)

compra8 = Compra(
    id_compra=8,
    produto=(produto8),
    servico=(servico8),
    cliente=cliente8,
    data_da_compra="08-02-2024",
    valor_total=51.47
)

compra9 = Compra(
    id_compra=9,
    produto=(produto9),
    servico=(servico9),
    cliente=cliente9,
    data_da_compra="09-02-2024",
    valor_total=41.49
)

compra10 = Compra(
    id_compra=10,
    produto=(produto10),
    servico=(servico10),
    cliente=cliente10,
    data_da_compra="10-02-2024",
    valor_total=91.48
)
