import re,json
from collections import defaultdict


def procesar_log(archivo_log):
    navegadores_contador = defaultdict(int)
    
    with open(archivo_log, "r") as file:
        for linea in file:
            navegador = extraer_navegador(linea)
            navegadores_contador[navegador] += 1
    
    return dict(navegadores_contador)

def extraer_navegador(user_agent):
    patron = r"(Chrome|Firefox|Safari|Edg|Opera|OPR|MSIE|Trident|Edge|AppleWebKit)[\/\s](\d+\.\d+)?"
    match = re.search(patron, user_agent)
    if match:
        navegador = match.group(1)
        if navegador in ("Edg", "Edge"):
            return "Edge"
        elif navegador == "OPR":
            return "Opera"
        elif navegador in ("Trident", "MSIE"):
            return "Internet Explorer"
        elif navegador == "AppleWebKit":
            return "Safari" 
        else:
            return navegador
    return "Otro"

def guardar_json(datos, archivo_salida):
    with open(archivo_salida, "w") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

def main():
    archivo_log = "access.log"  
    archivo_json = "resultados_navegadores.json"  
    conteo_navegadores = procesar_log(archivo_log)
    guardar_json(conteo_navegadores, archivo_json)
    
    print("Estadísticas de Navegadores")
    for navegador, cantidad in sorted(conteo_navegadores.items(), key=lambda x: -x[1]):
        print(f"{navegador}: {cantidad}")
    
    print(f"\nResultados guardados en '{archivo_json}'.")

if __name__ == "__main__":
    main()