from dataclasses import dataclass
from pet import Pet
from pet import pet1, pet2, pet3, pet4, pet5, pet6, pet7, pet8, pet9, pet10

@dataclass
class Banho_Cortesia:
    id_banho_cortesia: int
    pet: Pet
    data_do-banho_cortesia: str

banho_cortesia1 = Banho_Cortesia(
    id_banho_cortesia=1,
    pet=pet1,
    data_do_banho_cortesia="2024-03-01"
)

banho_cortesia2 = Banho_Cortesia(
    id_banho_cortesia=2,
    pet=pet2,
    data_do_banho_cortesia="2024-03-02"
)

banho_cortesia3 = Banho_Cortesia(
    id_banho_cortesia=3,
    pet=pet3,
    data_do_banho_cortesia="2024-03-03"
)

banho_cortesia4 = Banho_Cortesia(
    id_banho_cortesia=4,
    pet=pet4,
    data_do_banho_cortesia="2024-03-04"
)

banho_cortesia5 = Banho_Cortesia(
    id_banho_cortesia=5,
    pet=pet5,
    data_do_banho_cortesia="2024-03-05"
)

banho_cortesia6 = Banho_Cortesia(
    id_banho_cortesia=6,
    pet=pet6,
    data_do_banho_cortesia="2024-03-06"
)

banho_cortesia7 = Banho_Cortesia(
    id_banho_cortesia=7,
    pet=pet7,
    data_do_banho_cortesia="2024-03-07"
)

banho_cortesia8 = Banho_Cortesia(
    id_banho_cortesia=8,
    pet=pet8,
    data_do_banho_cortesia="2024-03-08"
)

banho_cortesia9 = Banho_Cortesia(
    id_banho_cortesia=9,
    pet=pet9,
    data_do_banho_cortesia="2024-03-09"
)

banho_cortesia10 = Banho_Cortesia(
    id_banho_cortesia=10,
    pet=pet10,
    data_do_banho_cortesia="2024-03-10"
)
