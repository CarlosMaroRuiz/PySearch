from flask import Flask,render_template
from src.search.search_route import search_router

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("views/index.html")
app.register_blueprint(search_router)
if __name__ == '__main__':
    app.run()