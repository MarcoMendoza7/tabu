from flask import Flask, render_template, request
from app.tabu_solver import tabu_search, city_names

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    best_route, best_cost = [], 0  # Inicializar variables

    if request.method == 'POST':
        best_route, best_cost = tabu_search(1000, 1, 50)

    # Convertir índices a nombres de ciudades
    ruta_ciudades = [city_names[i] for i in best_route] if best_route else []

    return render_template('index.html', ruta=ruta_ciudades, distancia=best_cost)

if __name__ == '__main__':
    app.run(debug=True)
