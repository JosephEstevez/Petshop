from dataclasses import dataclass
from servico_adicional import Servico_Adicional
from servico_adicional import servico1, servico2, servico3, servico4, servico5, servico6, servico7, servico8, servico9, servico10
from pet import Pet
from pet import pet1, pet2, pet3, pet4, pet5, pet6, pet7, pet8, pet9, pet10


@dataclass
class Servico_Pet:
    servico: Servico_Adicional
    pet: Pet
    data_do_servico: int
    preco: int


servico_pet1 = Servico_Pet(
    servico=servico1,
    pet=pet1,
    data_do_servico="01-02-2024",
    preco=80
)

servico_pet2 = Servico_Pet(
    servico=servico2,
    pet=pet2,
    data_do_servico="02-02-2024",
    preco=55
)

servico_pet3 = Servico_Pet(
    servico=servico3,
    pet=pet3,
    data_do_servico="03-02-2024",
    preco=40
)

servico_pet4 = Servico_Pet(
    servico=servico4,
    pet=pet4,
    data_do_servico="04-02-2024",
    preco=95
)

servico_pet5 = Servico_Pet(
    servico=servico5,
    pet=pet5,
    data_do_servico="05-02-2024",
    preco=75
)

servico_pet6 = Servico_Pet(
    servico=servico6,
    pet=pet6,
    data_do_servico="06-02-2024",
    preco=60
)

servico_pet7 = Servico_Pet(
    servico=servico7,
    pet=pet7,
    data_do_servico="07-02-2024",
    preco=110
)

servico_pet8 = Servico_Pet(
    servico=servico8,
    pet=pet8,
    data_do_servico="08-02-2024",
    preco=65
)

servico_pet9 = Servico_Pet(
    servico=servico9,
    pet=pet9,
    data_do_servico="09-02-2024",
    preco=85
)

servico_pet10 = Servico_Pet(
    servico=servico10,
    pet=pet10,
    data_do_servico="10-02-2024",
    preco=100
)
