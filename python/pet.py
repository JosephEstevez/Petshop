from dataclasses import dataclass, field
from cliente import Cliente
from cliente import cliente1, cliente2, cliente3, cliente4, cliente5, cliente6, cliente7, cliente8, cliente9, cliente10


@dataclass
class Pet:
    id_pet: int
    nome_do_pet: str
    especie: str
    raca: str
    idade: int
    cliente: tuple


pet1 = Pet(
    id_pet=1,
    nome_do_pet="Max",
    especie="Cachorro",
    raca="Labrador",
    idade=2,
    cliente=(cliente1, cliente2),
)

pet2 = Pet(
    id_pet=2,
    nome_do_pet="Mia",
    especie="Gato",
    raca="Siamês",
    idade=3,
    cliente=cliente2
)

pet3 = Pet(
    id_pet=3,
    nome_do_pet="Rocky",
    especie="Cachorro",
    raca="Bulldog",
    idade=4,
    cliente=cliente3
)

pet4 = Pet(
    id_pet=4,
    nome_do_pet="Luna",
    especie="Gato",
    raca="Persa",
    idade=1,
    cliente=cliente4
)

pet5 = Pet(
    id_pet=5,
    nome_do_pet="Bella",
    especie="Cachorro",
    raca="Golden Retriever",
    idade=5,
    cliente=cliente5
)

pet6 = Pet(
    id_pet=6,
    nome_do_pet="Coco",
    especie="Gato",
    raca="Maine Coon",
    idade=2,
    cliente=cliente6
)

pet7 = Pet(
    id_pet=7,
    nome_do_pet="Charlie",
    especie="Cachorro",
    raca="Poodle",
    idade=3,
    cliente=cliente7
)

pet8 = Pet(
    id_pet=8,
    nome_do_pet="Duke",
    especie="Gato",
    raca="Ragdoll",
    idade=4,
    cliente=cliente8
)

pet9 = Pet(
    id_pet=9,
    nome_do_pet="Buddy",
    especie="Cachorro",
    raca="Dachshund",
    idade=1,
    cliente=cliente9
)

pet10 = Pet(
    id_pet=10,
    nome_do_pet="Lily",
    especie="Gato",
    raca="Bengal",
    idade=2,
    cliente=cliente10
)
