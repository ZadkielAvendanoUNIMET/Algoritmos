import requests

def obtener_info_pokemon(nombre_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
    especie_url = f"https://pokeapi.co/api/v2/pokemon-species/{nombre_pokemon.lower()}"

    tipo_traducciones = {
        "normal": "normal", "fighting": "lucha", "flying": "volador", 
        "poison": "veneno", "ground": "tierra", "rock": "roca", 
        "bug": "bicho", "ghost": "fantasma", "steel": "acero", 
        "fire": "fuego", "water": "agua", "grass": "planta", 
        "electric": "eléctrico", "psychic": "psíquico", "ice": "hielo", 
        "dragon": "dragón", "dark": "siniestro", "fairy": "hada"
    }
    
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos = respuesta.json()
        
        respuesta_especie = requests.get(especie_url)
        respuesta_especie.raise_for_status()
        datos_especie = respuesta_especie.json()
        
        nombre = datos['name'].capitalize()
        genero = 'desconocido'
        for texto in datos_especie['flavor_text_entries']:
            if texto['language']['name'] == 'es':
                flavor_text = texto['flavor_text']
                break
        
        tipos = [tipo['type']['name'] for tipo in datos['types']]
        
        double_damage_to = set()
        double_damage_from = set()
        
        for tipo in tipos:
            url_tipo = f"https://pokeapi.co/api/v2/type/{tipo}"
            respuesta_tipo = requests.get(url_tipo)
            respuesta_tipo.raise_for_status()
            datos_tipo = respuesta_tipo.json()
            
            for doble_dano in datos_tipo['damage_relations']['double_damage_to']:
                double_damage_to.add(tipo_traducciones[doble_dano['name']])
            for doble_dano in datos_tipo['damage_relations']['double_damage_from']:
                double_damage_from.add(tipo_traducciones[doble_dano['name']])
        
        for i in range(0, len(tipos)):
            tipos[i] = tipo_traducciones[tipos[i]]

        print(f"\n{nombre} el pokémon {genero}.")
        print(flavor_text)
        print(f"\n{nombre} es de tipo {', '.join(tipos)} por lo que es fuerte contra {', '.join(double_damage_to)} y débil contra {', '.join(double_damage_from)}.")
        
    except requests.exceptions.HTTPError as err:
        print(f"Error al obtener la información del Pokémon: {err}")
        print("Inténtalo de nuevo.")
        return False
    
    return True

def llamar_pokedex():
    while True:
        nombre_pokemon = input("Introduce el nombre del Pokémon: ")
        if obtener_info_pokemon(nombre_pokemon):
            break

if __name__ == "__main__":
    llamar_pokedex()
