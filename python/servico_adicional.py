from dataclasses import dataclass


@dataclass
class Servico_Adicional:
    id_servico: int
    nome_do_servico: str
    preco: float


# Criando instâncias de Servico_Adicional
servico1 = Servico_Adicional(
    id_servico=1,
    nome_do_servico="Banho Especial",
    preco=25.99
)

servico2 = Servico_Adicional(
    id_servico=2,
    nome_do_servico="Tosa Diferenciada",
    preco=30.50
)

servico3 = Servico_Adicional(
    id_servico=3,
    nome_do_servico="Manicure para Gatos",
    preco=15.75
)

servico4 = Servico_Adicional(
    id_servico=4,
    nome_do_servico="Massagem Relaxante",
    preco=40.00
)

servico5 = Servico_Adicional(
    id_servico=5,
    nome_do_servico="Passeio Personalizado",
    preco=18.99
)

servico6 = Servico_Adicional(
    id_servico=6,
    nome_do_servico="Consulta de Comportamento",
    preco=35.00
)

servico7 = Servico_Adicional(
    id_servico=7,
    nome_do_servico="Acessórios de Luxo",
    preco=50.00
)

servico8 = Servico_Adicional(
    id_servico=8,
    nome_do_servico="Hidratação Capilar para Cães",
    preco=22.49
)

servico9 = Servico_Adicional(
    id_servico=9,
    nome_do_servico="Aula de Adestramento",
    preco=28.75
)

servico10 = Servico_Adicional(
    id_servico=10,
    nome_do_servico="Kit Spa para Gatos",
    preco=45.99
)
