from dataclasses import dataclass


@dataclass
class Funcionario:
    id_funcionario: int
    nome_do_funcionario: str
    cargo: str
    salario: float


funcionario1 = Funcionario(
    id_funcionario=1,
    nome_do_funcionario="João Silva",
    cargo="Atendente de Vendas",
    salario=4000.00
)

funcionario2 = Funcionario(
    id_funcionario=2,
    nome_do_funcionario="Maria Oliveira",
    cargo="Tosador",
    salario=4500.00
)

funcionario3 = Funcionario(
    id_funcionario=3,
    nome_do_funcionario="Carlos Santos",
    cargo="Veterinário",
    salario=6000.00
)

funcionario4 = Funcionario(
    id_funcionario=4,
    nome_do_funcionario="Ana Souza",
    cargo="Auxiliar de Limpeza",
    salario=3500.00
)

funcionario5 = Funcionario(
    id_funcionario=5,
    nome_do_funcionario="Pedro Rocha",
    cargo="Recepcionista",
    salario=4200.00
)

funcionario6 = Funcionario(
    id_funcionario=6,
    nome_do_funcionario="Luiza Lima",
    cargo="Atendente de Banho e Tosa",
    salario=3800.00
)

funcionario7 = Funcionario(
    id_funcionario=7,
    nome_do_funcionario="Giovanna Almeida",
    cargo="Farmacêutica",
    salario=5500.00
)

funcionario8 = Funcionario(
    id_funcionario=8,
    nome_do_funcionario="Rafael Oliveira",
    cargo="Gerente de Loja",
    salario=7000.00
)

funcionario9 = Funcionario(
    id_funcionario=9,
    nome_do_funcionario="Amanda Costa",
    cargo="Auxiliar Veterinário",
    salario=4800.00
)

funcionario10 = Funcionario(
    id_funcionario=10,
    nome_do_funcionario="Lucas Pereira",
    cargo="Estoquista",
    salario=4000.00
)
