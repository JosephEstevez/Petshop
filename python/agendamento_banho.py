from dataclasses import dataclass
from pet import Pet
from pet import pet1, pet2, pet3, pet4, pet5, pet6, pet7, pet8, pet9, pet10
from servico_adicional import Servico_Adicional
from servico_adicional import servico1, servico8


@dataclass
class Agendamento_Banho:
    id_agendamento: int
    pet: Pet
    data_do_agendamento: str
    tipo_do_banho: Servico_Adicional


agendamento_banho1 = Agendamento_Banho(
    id_agendamento=1,
    pet=pet1,
    data_do_agendamento="2024-03-01",
    tipo_do_banho=servico1
)

agendamento_banho2 = Agendamento_Banho(
    id_agendamento=2,
    pet=pet2,
    data_do_agendamento="2024-03-02",
    tipo_do_banho=servico8
)

agendamento_banho3 = Agendamento_Banho(
    id_agendamento=3,
    pet=pet3,
    data_do_agendamento="2024-03-03",
    tipo_do_banho=servico1
)

agendamento_banho4 = Agendamento_Banho(
    id_agendamento=4,
    pet=pet4,
    data_do_agendamento="2024-03-04",
    tipo_do_banho=servico8
)

agendamento_banho5 = Agendamento_Banho(
    id_agendamento=5,
    pet=pet5,
    data_do_agendamento="2024-03-05",
    tipo_do_banho=servico1
)

agendamento_banho6 = Agendamento_Banho(
    id_agendamento=6,
    pet=pet6,
    data_do_agendamento="2024-03-06",
    tipo_do_banho=servico8
)

agendamento_banho7 = Agendamento_Banho(
    id_agendamento=7,
    pet=pet7,
    data_do_agendamento="2024-03-07",
    tipo_do_banho=servico1
)

agendamento_banho8 = Agendamento_Banho(
    id_agendamento=8,
    pet=pet8,
    data_do_agendamento="2024-03-08",
    tipo_do_banho=servico8
)

agendamento_banho9 = Agendamento_Banho(
    id_agendamento=9,
    pet=pet9,
    data_do_agendamento="2024-03-09",
    tipo_do_banho=servico1
)

agendamento_banho10 = Agendamento_Banho(
    id_agendamento=10,
    pet=pet10,
    data_do_agendamento="2024-03-10",
    tipo_do_banho=servico8
)
