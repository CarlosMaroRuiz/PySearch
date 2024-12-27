import http.server
import socketserver
import json
import urllib.parse
from search_engine_parser import DuckDuckGoSearch


def get_results(text: str):
    ddg_search = DuckDuckGoSearch()
    search = ddg_search.search(text, pages=1)
    results = list(search)
    return results


PORT = 8000


class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/search"):
            parsed_url = urllib.parse.urlparse(self.path)
            query_params = urllib.parse.parse_qs(parsed_url.query)
            termino_busqueda_query = query_params.get('q', [None])[0]
            print(termino_busqueda_query)
            result = get_results(termino_busqueda_query)

            # Constructing the response
            response_data = {
                'query': termino_busqueda_query,
                'results': result if result else 'No results found.'
            }

            # Send JSON response
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "404 Not Found"}).encode('utf-8'))


with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"Servidor escuchando en el puerto {PORT}")
    httpd.serve_forever()