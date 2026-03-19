import requests

# # 1. Definimos la dirección (URL) de la API
# url = "https://dog.ceo/api/breeds/image/random"

# # 2. Hacemos la petición a la API
# respuesta = requests.get(url)

# # 3. Convertimos la respuesta a un formato que Python entiende (JSON)
# datos = respuesta.json()

# # 4. Mostramos el resultado en la consola
# print("¡Aquí tienes un perrito!")
# print("Enlace de la imagen:", datos["message"])


# --- CÓDIGO DE POKÉMON (ACTIVO) ---
# pokemon = "pikachu"
# url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
# respuesta = requests.get(url)

# if respuesta.status_code == 200:
#     datos = respuesta.json()
#     nombre = datos["name"]
#     id_pokedex = datos["id"]
#     altura = datos["height"] 
#     peso = datos["weight"]
    
#     print("--- DATOS DEL POKÉMON ---")
#     print(f"Nombre: {nombre.capitalize()}")
#     print(f"Número en la Pokédex: {id_pokedex}")
#     print(f"Altura: {altura / 10} metros")
#     print(f"Peso: {peso / 10} kg")
# else:
#     print("Hubo un error o el Pokémon no existe.")

# %%
import requests
import json

# 1. Configuración inicial
# Debes registrarte en football-data.org para obtener este código y reemplazar "TU_CLAVE_AQUI"
api_key = "65104bce29144179b5b85d53cf565eaa" 

# Para esta API, la clave se envía de forma oculta en algo llamado "Headers" (Cabeceras)
cabeceras = {
    "X-Auth-Token": api_key
}

# 2. Definimos la URL (usando uno de los ejemplos que me pasaste)
# "See all upcoming matches for Real Madrid"
url = "https://api.football-data.org/v4/teams/86/matches"

# 3. Definimos los filtros (Filters)
# En lugar de poner ?status=SCHEDULED en la URL, en Python lo ponemos en un diccionario.
# ¡Es mucho más ordenado!
filtros = {
    "status": "SCHEDULED" 
    # Podrías agregar más filtros de tu tabla aquí, por ejemplo:
    # "limit": 5 
}

# 4. Hacemos la petición enviando la URL, los filtros y nuestra llave de acceso
respuesta = requests.get(url, headers=cabeceras, params=filtros)

# ... (tu código anterior de configuración y requests)

if respuesta.status_code == 200:
    datos = respuesta.json()
    
    # 1. Guardamos la lista de partidos en una variable
    partidos = datos["matches"]
    
    print("--- PRÓXIMOS PARTIDOS ---")
    
    # 2. Usamos un bucle 'for' para analizar cada partido individualmente
    for partido in partidos:
        
        # 3. Extraemos la fecha.
        # La fecha viene como "2026-03-17T20:00:00Z". 
        # Usamos [:10] para recortar el texto y quedarnos solo con los primeros 10 caracteres (YYYY-MM-DD)
        fecha = partido["utcDate"][:10] 
        
        # 4. Extraemos los nombres de los equipos. 
        # Fíjate cómo entramos primero a "homeTeam" y luego a "name"
        equipo_local = partido["homeTeam"]["name"]
        equipo_visitante = partido["awayTeam"]["name"]
        
        # 5. Imprimimos el resultado limpio
        print(f"Fecha: {fecha} |  {equipo_local} vs {equipo_visitante}")
        
else:
    print(f"Error al conectar. Código de estado: {respuesta.status_code}")
# %%