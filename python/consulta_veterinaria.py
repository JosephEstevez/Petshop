from dataclasses import dataclass
from pet import Pet
from pet import pet1, pet2, pet3, pet4, pet5, pet6, pet7, pet8, pet9, pet10


@dataclass
class Consulta_Veterinaria:
    id_consulta: int
    pet: Pet
    data_da_consulta: str
    diagnostico: str


consulta1 = Consulta_Veterinaria(
    id_consulta=1,
    pet=pet1,
    data_da_consulta="2024-02-01",
    diagnostico="Exame de rotina e cuidados dentários"
)

consulta2 = Consulta_Veterinaria(
    id_consulta=2,
    pet=pet2,
    data_da_consulta="2024-02-02",
    diagnostico="Avaliação de saúde e orientação nutricional"
)

consulta3 = Consulta_Veterinaria(
    id_consulta=3,
    pet=pet3,
    data_da_consulta="2024-02-03",
    diagnostico="Tratamento de infecção de ouvido"
)

consulta4 = Consulta_Veterinaria(
    id_consulta=4,
    pet=pet4,
    data_da_consulta="2024-02-04",
    diagnostico="Exame de sangue e avaliação geral"
)

consulta5 = Consulta_Veterinaria(
    id_consulta=5,
    pet=pet5,
    data_da_consulta="2024-02-05",
    diagnostico="Avaliação dental e orientação de cuidados"
)

consulta6 = Consulta_Veterinaria(
    id_consulta=6,
    pet=pet6,
    data_da_consulta="2024-02-06",
    diagnostico="Exame de rotina e análise de comportamento"
)

consulta7 = Consulta_Veterinaria(
    id_consulta=7,
    pet=pet7,
    data_da_consulta="2024-02-07",
    diagnostico="Tratamento de alergia e orientação nutricional"
)

consulta8 = Consulta_Veterinaria(
    id_consulta=8,
    pet=pet8,
    data_da_consulta="2024-02-08",
    diagnostico="Acompanhamento pós-cirúrgico"
)

consulta9 = Consulta_Veterinaria(
    id_consulta=9,
    pet=pet9,
    data_da_consulta="2024-02-09",
    diagnostico="Avaliação de comportamento e orientação de treinamento"
)

consulta10 = Consulta_Veterinaria(
    id_consulta=10,
    pet=pet10,
    data_da_consulta="2024-02-10",
    diagnostico="Tratamento de ferida e análise de saúde geral"
)
