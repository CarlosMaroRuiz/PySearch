import urllib.parse

def decodificar_url_duckduckgo(url_redireccion):

    try:
        parsed_url = urllib.parse.urlparse(url_redireccion)
        query_params = urllib.parse.parse_qs(parsed_url.query)
        url_codificada = query_params.get('uddg', [None])[0]
        if url_codificada:
            url_decodificada = urllib.parse.unquote(url_codificada)
            return url_decodificada
        else:
            return None
    except:
        return None