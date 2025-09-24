"""
ga_real.py
Algoritmo Genético simple para optimización sobre variables reales.
- Selección: torneo
- Crossover: BLX-alpha
- Mutación: ruido gaussiano por componente
- El usuario define la función `fitness(individual)`.

Ejecutar: python ga_real.py
"""

import random
import math
from typing import List, Callable, Tuple

# ----------------------------
#  CONFIGURACIÓN / HYPERPARÁMETROS
# ----------------------------
POP_SIZE = 60              # tamaño de la población
GENS = 200                 # generaciones
TOURNAMENT_SIZE = 3        # tamaño del torneo para selección
CROSSOVER_RATE = 0.9       # probabilidad de aplicar crossover
MUTATION_RATE = 0.2        # probabilidad de mutar un individuo
MUTATION_SIGMA = 0.1       # desviación estándar para la mutación gaussiana
ELITISM = 1                # cuántos mejores se preservan
BLX_ALPHA = 0.5            # parámetro alpha para BLX-alpha

# Dominio para cada dimensión: lista de (min, max)
BOUNDS: List[Tuple[float, float]] = [(-5.0, 5.0)] * 5  # ejemplo: 5 dimensiones


# ----------------------------
#  PROBLEMA: define fitness
# ----------------------------
def fitness(ind: List[float]) -> float:
    """
    Ejemplo: función Sphere (minimizar): f(x) = sum(x_i^2)
    Como los GAs que implementaré buscan MAXIMIZAR, devolveremos -f(x).
    > Si quieres maximizar una función directamente, devuelve el valor sin cambiar signo.
    """
    val = sum(x * x for x in ind)
    return -val  # convertimos minimización a maximización


# ----------------------------
#  FUNCIONES AUXILIARES
# ----------------------------
def random_individual(bounds: List[Tuple[float, float]]) -> List[float]:
    return [random.uniform(lo, hi) for lo, hi in bounds]


def clamp_individual(ind: List[float], bounds: List[Tuple[float, float]]):
    for i, (lo, hi) in enumerate(bounds):
        if ind[i] < lo:
            ind[i] = lo
        elif ind[i] > hi:
            ind[i] = hi


# ----------------------------
#  OPERADORES GENÉTICOS
# ----------------------------
def tournament_selection(pop: List[List[float]], fitnesses: List[float], k: int) -> List[float]:
    """Selecciona 1 individuo por torneo de tamaño k (devuelve copia)."""
    selected = random.sample(range(len(pop)), k)
    best = selected[0]
    for idx in selected[1:]:
        if fitnesses[idx] > fitnesses[best]:
            best = idx
    return pop[best][:]


def blx_alpha_crossover(parent1: List[float], parent2: List[float], alpha: float, bounds: List[Tuple[float, float]]) -> Tuple[List[float], List[float]]:
    """BLX-alpha crossover para variables reales."""
    child1 = parent1[:]
    child2 = parent2[:]
    for i in range(len(parent1)):
        cmin = min(parent1[i], parent2[i])
        cmax = max(parent1[i], parent2[i])
        I = cmax - cmin
        lo = cmin - alpha * I
        hi = cmax + alpha * I
        val1 = random.uniform(lo, hi)
        val2 = random.uniform(lo, hi)
        child1[i] = val1
        child2[i] = val2
    clamp_individual(child1, bounds)
    clamp_individual(child2, bounds)
    return child1, child2


def mutate(ind: List[float], mutation_rate: float, sigma: float, bounds: List[Tuple[float, float]]):
    """Mutación gaussiana por componente con probabilidad mutation_rate (por individuo)."""
    if random.random() < mutation_rate:
        for i in range(len(ind)):
            ind[i] += random.gauss(0, sigma)
        clamp_individual(ind, bounds)


# ----------------------------
#  ALGORITMO PRINCIPAL
# ----------------------------
def run_ga(bounds: List[Tuple[float, float]],
           fitness_fn: Callable[[List[float]], float],
           pop_size: int = POP_SIZE,
           gens: int = GENS,
           tournament_k: int = TOURNAMENT_SIZE,
           crossover_rate: float = CROSSOVER_RATE,
           mutation_rate: float = MUTATION_RATE,
           mutation_sigma: float = MUTATION_SIGMA,
           elitism: int = ELITISM,
           blx_alpha: float = BLX_ALPHA):
    # Inicializar población
    population = [random_individual(bounds) for _ in range(pop_size)]
    fitnesses = [fitness_fn(ind) for ind in population]

    best_over_time = []
    for gen in range(gens):
        # Ordenar por fitness (descendente porque maximizamos)
        sorted_idx = sorted(range(pop_size), key=lambda i: fitnesses[i], reverse=True)
        new_pop = []

        # Elitismo: copiar los mejores
        for i in range(elitism):
            new_pop.append(population[sorted_idx[i]][:])

        # Generar nuevos individuos hasta completar población
        while len(new_pop) < pop_size:
            # Selección
            parent1 = tournament_selection(population, fitnesses, tournament_k)
            parent2 = tournament_selection(population, fitnesses, tournament_k)

            # Crossover
            if random.random() < crossover_rate:
                child1, child2 = blx_alpha_crossover(parent1, parent2, blx_alpha, bounds)
            else:
                child1, child2 = parent1[:], parent2[:]

            # Mutación
            mutate(child1, mutation_rate, mutation_sigma, bounds)
            mutate(child2, mutation_rate, mutation_sigma, bounds)

            new_pop.append(child1)
            if len(new_pop) < pop_size:
                new_pop.append(child2)

        population = new_pop
        fitnesses = [fitness_fn(ind) for ind in population]

        # Registrar mejor actual
        best_idx = max(range(pop_size), key=lambda i: fitnesses[i])
        best_over_time.append((gen, fitnesses[best_idx], population[best_idx][:]))

        # Impresión periódica
        if gen % (gens // 10 or 1) == 0 or gen == gens - 1:
            print(f"Gen {gen:4d} | Best fitness: {fitnesses[best_idx]: .6f} | Best individual: {population[best_idx]}")

    return best_over_time


# ----------------------------
#  EJECUCIÓN / EJEMPLO
# ----------------------------
if __name__ == "__main__":
    random.seed(42)
    print("Iniciando GA de ejemplo (función Sphere, 5D).")
    best_hist = run_ga(BOUNDS, fitness, pop_size=POP_SIZE, gens=GENS)

    # Mostrar resultado final
    gen, best_fit, best_ind = best_hist[-1]
    print("\nResultado final:")
    print(f"Generación {gen}, fitness = {best_fit:.6f}, individuo = {best_ind}")
    # Si fitness devuelve -f(x) (minimización), el valor real mínimo es -best_fit
    print(f"Valor objetivo (si Sphere minimizado): { -best_fit :.6f}")
