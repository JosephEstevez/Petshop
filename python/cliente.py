from dataclasses import dataclass, field


@dataclass
class Cliente:
    id_cliente: int
    nome_do_cliente: str
    endereco: str
    telefone: int


cliente1 = Cliente(
    id_cliente=1,
    nome_do_cliente="Sofia Oliveira",
    endereco="Rua das Flores, 123",
    telefone=5511987654321
)

cliente2 = Cliente(
    id_cliente=2,
    nome_do_cliente="Lucas Pereira",
    endereco="Avenida dos Pássaros, 45",
    telefone=5521912345678
)

cliente3 = Cliente(
    id_cliente=3,
    nome_do_cliente="Isabela Santos",
    endereco="Travessa da Lua, 789",
    telefone=5531876543210
)

cliente4 = Cliente(
    id_cliente=4,
    nome_do_cliente="Gabriel Silva",
    endereco="Alameda das Estrelas, 56",
    telefone=5541890123456
)

cliente5 = Cliente(
    id_cliente=5,
    nome_do_cliente="Amanda Costa",
    endereco="Praça do Sol, 234",
    telefone=5551765432109
)

cliente6 = Cliente(
    id_cliente=6,
    nome_do_cliente="Pedro Rocha",
    endereco="Viela das Borboletas, 78",
    telefone=5561234567890
)

cliente7 = Cliente(
    id_cliente=7,
    nome_do_cliente="Julia Ferreira",
    endereco="Beco das Maravilhas, 12",
    telefone=5571543210987
)

cliente8 = Cliente(
    id_cliente=8,
    nome_do_cliente="Matheus Almeida",
    endereco="Estrada do Arco-Íris, 345",
    telefone=5581678901234
)

cliente9 = Cliente(
    id_cliente=9,
    nome_do_cliente="Giovanna Lima",
    endereco="Largo das Fadas, 67",
    telefone=5591210987654
)

cliente10 = Cliente(
    id_cliente=10,
    nome_do_cliente="Rafael Oliveira",
    endereco="Caminho das Nuvens, 890",
    telefone=551199876543210
)
