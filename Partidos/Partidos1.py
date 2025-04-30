import json
from collections import defaultdict

Json = "Cuartos de final1.json"

with open(Json, 'r', encoding='utf-8') as file:
    datos = json.load(file)

equipos_goles = defaultdict(int)  # {equipo: goles_totales}
equipos_pasan = []

for fase in datos:
    if fase["Fase"] == "Cuartos de final":
        partidos = fase["Partidos"]
        eliminatorias = [
            [partidos[0], partidos[1]], 
            [partidos[2], partidos[3]],  
            [partidos[4], partidos[5]],  
            [partidos[6], partidos[7]]   
        ]
        for eliminatoria in eliminatorias:
            equipo1 = eliminatoria[0]["Local"]
            equipo2 = eliminatoria[0]["Visitante"]
            goles_equipo1 = 0
            goles_equipo2 = 0

            for partido in eliminatoria:
                if partido["Local"] == equipo1:
                    goles_local, goles_visitante = map(int, partido["Resultado"].split("-"))
                    goles_equipo1 += goles_local
                    goles_equipo2 += goles_visitante
                else:
                    goles_local, goles_visitante = map(int, partido["Resultado"].split("-"))
                    goles_equipo2 += goles_local
                    goles_equipo1 += goles_visitante
            if goles_equipo1 > goles_equipo2:
                equipos_pasan.append(equipo1)
            else:
                equipos_pasan.append(equipo2)

print("Semifinalistas de la Champions League 2022:")
for i, equipo in enumerate(equipos_pasan, 1):
    print(f"{i}. {equipo}")