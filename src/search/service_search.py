from  .decoder import decodificar_url_duckduckgo
import requests
import json
from  .link import Link
def obtener_resultados_busqueda(query):
    url = f"http://localhost:8000/search?q={query}"
    result_send = []
    try:
        response = requests.get(url)
        response.raise_for_status()
        resultados = response.json()

        for r in resultados["results"]:
            url = decodificar_url_duckduckgo(r["links"])
            if url:
                result_send.append(Link(url, title=r["titles"]))



        return result_send
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la petición: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error al decodificar la respuesta JSON: {e}. Respuesta del servidor: {response.text}")
        return None
