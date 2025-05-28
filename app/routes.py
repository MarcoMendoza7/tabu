from flask import Blueprint, render_template, request
from app.tabu_solver import tabu_search, city_names

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    best_route, best_cost = [], 0

    if request.method == 'POST':
        origin = request.form.get("origin")  
        destination = request.form.get("destination")  
        temp_ini = float(request.form.get("temp_ini", 1000))  
        temp_min = float(request.form.get("temp_min", 10))  
        tabu_size = int(request.form.get("speed", 50))  

        # Obtener índices de origen y destino
        origin_index = city_names.index(origin)
        destination_index = city_names.index(destination)

        best_route, best_cost = tabu_search(temp_ini, temp_min, tabu_size, origin_index, destination_index)

        print("Ruta generada en índices:", best_route)

    ruta_ciudades = [city_names[i] for i in best_route] if best_route else ["Ruta no generada"]

    return render_template('index.html', result={"ruta_optimizada": ruta_ciudades, "distancia": best_cost}, city_names=city_names)
