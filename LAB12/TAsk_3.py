import random
import math
import matplotlib.pyplot as plt

def get_sensor_coordinates():
    n = int(input("Enter the number of underwater sensors: "))
    sensors = []
    for i in range(n):
        print(f"Enter coordinates for sensor {i+1}:")
        x = float(input("  x: "))
        y = float(input("  y: "))
        sensors.append((x, y))
    return sensors

def euclidean_distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def total_path_distance(path, sensors):
    distance = 0
    for i in range(len(path)):
        distance += euclidean_distance(sensors[path[i]], sensors[path[(i+1)%len(path)]])
    return distance

def greedy_tsp(sensors):
    n = len(sensors)
    unvisited = set(range(n))
    path = []
    current = 0
    path.append(current)
    unvisited.remove(current)
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(sensors[current], sensors[city]))
        path.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    return path

def random_path(n):
    path = list(range(n))
    random.shuffle(path)
    return path

# --- Genetic Algorithm for TSP ---
def initialize_population(pop_size, n):
    population = []
    for _ in range(pop_size):
        p = list(range(n))
        random.shuffle(p)
        population.append(p)
    return population

def crossover(parent1, parent2):
    # Order crossover (OX)
    size = len(parent1)
    a, b = sorted(random.sample(range(size), 2))
    child = [None]*size
    child[a:b+1] = parent1[a:b+1]
    fill = [item for item in parent2 if item not in child]
    idx = 0
    for i in range(size):
        if child[i] is None:
            child[i] = fill[idx]
            idx += 1
    return child

def mutate(path, mutation_rate=0.1):
    path = path[:]
    for i in range(len(path)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(path)-1)
            path[i], path[j] = path[j], path[i]
    return path

def select(population, sensors, k=3):
    # Tournament selection
    selected = random.sample(population, k)
    selected.sort(key=lambda p: total_path_distance(p, sensors))
    return selected[0]

def genetic_algorithm_tsp(sensors, pop_size=100, generations=500, mutation_rate=0.1):
    n = len(sensors)
    population = initialize_population(pop_size, n)
    best_path = min(population, key=lambda p: total_path_distance(p, sensors))
    best_distance = total_path_distance(best_path, sensors)
    for gen in range(generations):
        new_population = []
        for _ in range(pop_size):
            parent1 = select(population, sensors)
            parent2 = select(population, sensors)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population
        current_best = min(population, key=lambda p: total_path_distance(p, sensors))
        current_distance = total_path_distance(current_best, sensors)
        if current_distance < best_distance:
            best_path = current_best
            best_distance = current_distance
    return best_path

def plot_route(sensors, path, title, color='b'):
    x = [sensors[i][0] for i in path] + [sensors[path[0]][0]]
    y = [sensors[i][1] for i in path] + [sensors[path[0]][1]]
    plt.plot(x, y, marker='o', color=color, label=title)
    for idx, (xi, yi) in enumerate(sensors):
        plt.text(xi, yi, str(idx+1), fontsize=9, ha='right')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(title)
    plt.grid(True)

def main():
    print("SR University AUV Swarm Route Optimization (TSP Simulation)")
    sensors = get_sensor_coordinates()
    n = len(sensors)

    # Random path
    rand_path = random_path(n)
    rand_dist = total_path_distance(rand_path, sensors)
    print(f"\nRandom Path Distance: {rand_dist:.2f}")

    # Greedy path
    greedy_path = greedy_tsp(sensors)
    greedy_dist = total_path_distance(greedy_path, sensors)
    print(f"Greedy Path Distance: {greedy_dist:.2f}")

    # Genetic Algorithm path
    print("\nRunning Genetic Algorithm optimization...")
    ga_path = genetic_algorithm_tsp(sensors, pop_size=100, generations=500, mutation_rate=0.1)
    ga_dist = total_path_distance(ga_path, sensors)
    print(f"Genetic Algorithm Optimized Path Distance: {ga_dist:.2f}")

    # Visualization
    plt.figure(figsize=(10, 6))
    plot_route(sensors, rand_path, f"Random Path ({rand_dist:.2f})", color='gray')
    plot_route(sensors, greedy_path, f"Greedy Path ({greedy_dist:.2f})", color='orange')
    plot_route(sensors, ga_path, f"GA Optimized Path ({ga_dist:.2f})", color='green')
    plt.legend()
    plt.show()

    print("\n--- Distance Comparison ---")
    print(f"Random Path: {rand_dist:.2f}")
    print(f"Greedy Path: {greedy_dist:.2f}")
    print(f"Genetic Algorithm Optimized Path: {ga_dist:.2f}")

if __name__ == "__main__":
    main()
    # The code is correct, but if output is not displaying, it may be due to missing imports or backend issues.
    # Ensure the following imports are present at the top of your file:
    # import random
    # import matplotlib.pyplot as plt
    # import math

    # If you cannot add imports at the top, you can add them here for completeness:
    import random
    import matplotlib.pyplot as plt
    import math

    # If the code still does not display output, check if the functions used in main() are defined:
    # get_sensor_coordinates, random_path, total_path_distance, greedy_tsp, genetic_algorithm_tsp

    # If running in some environments (like some IDEs or notebooks), you may need to call plt.show() explicitly.
    # This is already present in your main().

    # If you want to ensure the script runs and displays output, you can add a print statement here:
    print("Execution complete. If you do not see the plot, check your environment's plot display settings.")
