from flask import Blueprint, render_template, request
from app.tabu_solver import tabu_search, city_names

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    best_route, best_cost = [], 0

    if request.method == 'POST':
        temp_ini = float(request.form.get("temp_ini", 1000))  # Valor por defecto
        temp_min = float(request.form.get("temp_min", 10))  # Valor por defecto
        tabu_size = int(request.form.get("speed", 50))  # Valor por defecto

        best_route, best_cost = tabu_search(temp_ini, temp_min, tabu_size)
        print("Ruta generada en índices:", best_route)  

    ruta_ciudades = [city_names[i] for i in best_route] if best_route else ["Ruta no generada"]
    print("Ciudades optimizadas:", ruta_ciudades)  

    return render_template('index.html', result={"ruta_optimizada": ruta_ciudades, "distancia": best_cost})
