 
import random

from config import (
    COLORES,
    TAMANO_CODIGO,
    MAX_FITNESS,
    POBLACION_INICIAL,
    GENERACIONES,
    TASA_MUTACION,
    TASA_CRUZA,
    NUM_ELITE
)

def generar_individuo():
    """
    Genera un individuo aleatorio sin colores repetidos.

    El individuo es una lista de TAMANO_CODIGO colores únicos,
    seleccionados aleatoriamente de la lista COLORES.

    Returns
    -------
    list of str
        Individuo generado, representado como una lista de colores únicos.
    """

    return random.sample(COLORES, TAMANO_CODIGO)

def calcular_fitness(individuo, codigo_objetivo):
    """
    Calcula el fitness de un individuo comparado con el código objetivo.

    Se otorgan:
    - +1.0 puntos por cada color en la posición correcta.
    - +0.5 puntos por cada color presente pero en una posición incorrecta.

    Parameters
    ----------
    individuo : list of str
        Combinación candidata generada por el algoritmo.
    codigo_objetivo : list of str
        Combinación secreta a adivinar.

    Returns
    -------
    float
        Valor de fitness del individuo.
    """

    correctos = sum(i == j for i, j in zip(individuo, codigo_objetivo))
    comunes = len(set(individuo) & set(codigo_objetivo))
    mal_posicionados = comunes - correctos
    return correctos * 1.0 + mal_posicionados * 0.5


def seleccion(poblacion, fitnesses):
    """
    Selecciona un individuo de la población usando selección por ruleta (fitness proporcional).

    Si todos los fitness son cero, selecciona un individuo aleatorio.

    Parameters
    ----------
    poblacion : list of list of str
        Lista de individuos actuales.
    fitnesses : list of float
        Lista de valores de fitness correspondientes a la población.

    Returns
    -------
    list of str
        Individuo seleccionado para cruce.
    """

    total = sum(fitnesses)
    if total == 0:
        return random.choice(poblacion)
    probabilidades = [f / total for f in fitnesses]
    return random.choices(poblacion, weights=probabilidades, k=1)[0]


def cruzar(padre1, padre2):
    """
    Crea un hijo a partir de dos padres mediante recombinación sin repeticiones.

    Para cada posición, se elige aleatoriamente el gen del padre1 o padre2
    sin duplicar colores. Si faltan colores, se completan al azar con colores
    no usados.

    Parameters
    ----------
    padre1 : list of str
        Primer individuo progenitor.
    padre2 : list of str
        Segundo individuo progenitor.

    Returns
    -------
    list of str
        Hijo generado por cruce entre los padres.
    """

    hijo = []
    usados = set()
    for i in range(TAMANO_CODIGO):
        gene = padre1[i] if random.random() < 0.5 else padre2[i]
        if gene not in usados:
            hijo.append(gene)
            usados.add(gene)
    faltantes = [c for c in COLORES if c not in usados]
    random.shuffle(faltantes)
    hijo += faltantes[:TAMANO_CODIGO - len(hijo)]
    return hijo


def mutar(individuo):
    """
    Aplica mutación sobre un individuo con una probabilidad dada.

    La mutación puede ser:
    - "swap": intercambio de dos colores del individuo.
    - "replace": sustitución de un color por otro no presente.

    La mutación mantiene la unicidad de los colores.

    Parameters
    ----------
    individuo : list of str
        Individuo a mutar.

    Returns
    -------
    list of str
        Individuo mutado (puede ser igual si no se aplica mutación).
    """

    if random.random() < TASA_MUTACION:
        nuevo = individuo.copy()
        tipo = random.choice(["swap", "replace"])

        if tipo == "swap":
            i, j = random.sample(range(TAMANO_CODIGO), 2)
            nuevo[i], nuevo[j] = nuevo[j], nuevo[i]

        elif tipo == "replace":
            actuales = set(nuevo)
            posibles = [c for c in COLORES if c not in actuales]
            if posibles:
                i = random.randint(0, TAMANO_CODIGO - 1)
                nuevo[i] = random.choice(posibles)

        return nuevo

    return individuo


def algoritmo_genetico(codigo_objetivo):
    """
    Ejecuta un algoritmo genético para resolver el juego Mastermind.

    En cada generación:
    - Se evalúan los individuos.
    - Se seleccionan padres proporcionalmente a su fitness.
    - Se cruzan y mutan para generar nuevos individuos.
    - Se aplica elitismo para conservar los mejores.

    El proceso se repite hasta alcanzar MAX_FITNESS o agotar GENERACIONES.

    Parameters
    ----------
    codigo_objetivo : list of str
        Combinación secreta que se desea descubrir.

    Returns
    -------
    list of str or None
        Solución encontrada con fitness máximo, o None si no se alcanzó.
    """

    poblacion = [generar_individuo() for _ in range(POBLACION_INICIAL)]

    for gen in range(GENERACIONES):
        fitnesses = [calcular_fitness(ind, codigo_objetivo) for ind in poblacion]

        print(f"\n--- Generación {gen} ---")
        poblacion_ordenada = sorted(zip(poblacion, fitnesses), key=lambda x: x[1], reverse=True)
        for ind, fit in poblacion_ordenada:
            print(f"{ind} -> fitness: {fit:.2f}")

        if any(f == MAX_FITNESS for f in fitnesses):
            solucion = poblacion[fitnesses.index(MAX_FITNESS)]
            print(f"\n✅ ¡Solución encontrada en la generación {gen}: {solucion}")
            return solucion

        nueva_poblacion = poblacion_ordenada[:NUM_ELITE]  # elitismo

        while len(nueva_poblacion) < POBLACION_INICIAL:
            padre1 = seleccion(poblacion, fitnesses)
            padre2 = seleccion(poblacion, fitnesses)
            hijo = cruzar(padre1, padre2) if random.random() < TASA_CRUZA else padre1.copy()
            hijo = mutar(hijo)
            fit_hijo = calcular_fitness(hijo, codigo_objetivo)
            nueva_poblacion.append((hijo, fit_hijo))

        poblacion = [ind for ind, _ in nueva_poblacion]

    print("\n⛔ No se encontró solución en el número máximo de generaciones.")
    return None


# Ejemplo de uso
if __name__ == "__main__":
    codigo_secreto = generar_individuo()
    print(f"🎯 Código secreto: {codigo_secreto}")
    algoritmo_genetico(codigo_secreto)
