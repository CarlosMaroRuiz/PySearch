
from flask import Blueprint, request,render_template,render_template_string
from .service_search import obtener_resultados_busqueda

search_router = Blueprint('search', __name__)

@search_router.route('/search')
def buscar():
    query = request.args.get('query', '')
    print(f"La búsqueda recibida es: {query}")

    if not query:
        return render_template_string("""
            <div class="text-red-500">Por favor, introduce un término de búsqueda.</div>
        """), 400

    try:
        result =obtener_resultados_busqueda(query)
        if not result:
            return render_template_string("""
                <div class="text-gray-500">No se encontraron resultados.</div>
            """), 200
        return render_template("views/result.html",results=result)

    except Exception as e:
        print(f"Error detallado: {str(e)}")
        return render_template_string("""
            <div class="text-red-500">Error: {{ error }}</div>
        """, error=str(e)), 500