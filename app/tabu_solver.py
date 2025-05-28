import random
import math

cities = {
    'Jiloyork': (19.916012, -99.580580),
    'Toluca': (19.289165, -99.655697),
    'Atlacomulco': (19.799520, -99.873844),
    'Guadalajara': (20.677754, -103.346254),
    'Monterrey': (25.691611, -100.321838),
    'QuintanaRoo': (21.163112, -86.802315),
    'Michohacan': (19.701400, -101.208297),
    'Aguascalientes': (21.876410, -102.264387),
    'CDMX': (19.432713, -99.133183),
    'QRO': (20.597194, -100.386670)
}

city_names = list(cities.keys())
coordinates = list(cities.values())

def euclidean(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def total_distance(route):
    dist = sum(euclidean(coordinates[route[i]], coordinates[route[i+1]]) for i in range(len(route)-1))
    dist += euclidean(coordinates[route[-1]], coordinates[route[0]])  # Regresa al inicio
    return dist

def tabu_search(temp_ini, temp_min, tabu_size):
    current = random.sample(range(len(cities)), len(cities))  # Ruta inicial aleatoria
    best = current[:]
    best_cost = total_distance(best)
    tabu_list = []
    T = temp_ini

    while T > temp_min:
        neighbors = [current[:i] + [current[j]] + current[i+1:j] + [current[i]] + current[j+1:] 
                     for i in range(len(cities)) for j in range(i+1, len(cities))]

        candidates = [n for n in neighbors if n not in tabu_list]
        if not candidates:
            break

        next_route = min(candidates, key=total_distance)
        cost = total_distance(next_route)

        if cost < best_cost:
            best, best_cost = next_route[:], cost

        tabu_list.append(next_route)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

        current = next_route
        T *= 0.99  # Enfriamiento más lento para mayor exploración

        print(f"Iteración con T={T:.2f} | Mejor ruta hasta ahora: {best} | Distancia: {best_cost:.2f}")

    return best, best_cost
