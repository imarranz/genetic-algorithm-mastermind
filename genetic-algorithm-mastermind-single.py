import random

from config import (
    COLORES,
    TAMANO_CODIGO,
    MAX_FITNESS,
    GENERACIONES,
)

def generar_individuo():
    """
    Genera un individuo aleatorio.

    El individuo es una lista de TAMANO_CODIGO colores distintos,
    seleccionados aleatoriamente de la lista COLORES sin repeticiones.

    Returns
    -------
    list of str
        Lista con una combinación aleatoria de colores únicos.
    """

    return random.sample(COLORES, TAMANO_CODIGO)

def calcular_fitness(individuo, codigo_objetivo):
    """
    Calcula el valor de fitness de un individuo comparado con el código objetivo.

    El fitness se calcula como:
    - +1.0 por cada color en la posición correcta.
    - +0.5 por cada color presente pero en posición incorrecta.

    Parameters
    ----------
    individuo : list of str
        Combinación propuesta (longitud TAMANO_CODIGO).
    codigo_objetivo : list of str
        Combinación secreta a adivinar.

    Returns
    -------
    float
        Valor de fitness entre 0 y MAX_FITNESS.
    """

    correctos = sum(i == j for i, j in zip(individuo, codigo_objetivo))
    comunes = len(set(individuo) & set(codigo_objetivo))
    mal_posicionados = comunes - correctos
    return correctos * 1.0 + mal_posicionados * 0.5

def mutar(individuo):
    """
    Realiza una mutación sobre un individuo.

    Hay dos tipos posibles de mutación:
    - "swap": intercambia dos colores del individuo.
    - "replace": reemplaza un color por otro que no esté ya en el individuo,
      seleccionado de la lista COLORES.

    La mutación garantiza que los colores del individuo siguen siendo únicos.

    Parameters
    ----------
    individuo : list of str
        Individuo a mutar (longitud TAMANO_CODIGO, colores únicos).

    Returns
    -------
    list of str
        Nuevo individuo mutado.
    """

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

def busqueda_evolutiva(codigo_objetivo):
    """
    Ejecuta un algoritmo evolutivo simple con un solo individuo.

    A partir de una solución inicial aleatoria, se realizan mutaciones.
    Si una mutación mejora el fitness del individuo, se acepta.
    El proceso se repite hasta alcanzar el fitness máximo o agotar las generaciones.

    Parameters
    ----------
    codigo_objetivo : list of str
        Combinación secreta que se intenta adivinar.

    Returns
    -------
    list of str
        Mejor solución encontrada (puede ser óptima o no).
    """

    actual = generar_individuo()
    fitness_actual = calcular_fitness(actual, codigo_objetivo)

    print(f"\n🎯 Código secreto: {codigo_objetivo}")
    print(f"🔁 Solución inicial: {actual} -> fitness: {fitness_actual:.1f}")
    print("----------------------------------------------")

    for gen in range(1, GENERACIONES + 1):
        candidato = mutar(actual)
        fitness_candidato = calcular_fitness(candidato, codigo_objetivo)

        if fitness_candidato > fitness_actual:
            actual = candidato
            fitness_actual = fitness_candidato
            print(f"✅ Gen {gen}: {actual} -> fitness: {fitness_actual:.1f}")

        if fitness_actual == MAX_FITNESS:
            print(f"\n🎉 ¡Solución perfecta encontrada en la iteración {gen}: {actual}")
            return actual

    print("\n⛔ No se alcanzó el fitness máximo.")
    return actual


# Ejemplo de uso
if __name__ == "__main__":
    codigo_secreto = generar_individuo()
    busqueda_evolutiva(codigo_secreto)
    #busqueda_evolutiva(['O','B','M','P','Y'])

