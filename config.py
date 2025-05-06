# === CONFIGURACIÓN DEL ALGORITMO GENÉTICO PARA MASTERMIND ===

# Lista de colores disponibles para formar combinaciones.
# Cada letra representa un color único, sin repeticiones dentro de una combinación.
COLORES = ['R', 'G', 'B', 'Y', 'O', 'P', 'C', 'M']
# R = Red (Rojo)
# G = Green (Verde)
# B = Blue (Azul)
# Y = Yellow (Amarillo)
# O = Orange (Naranja)
# P = Purple (Púrpura o Violeta)
# C = Cyan (Cian o celeste)
# M = Magenta (Magenta o fucsia)

# Número de posiciones del código secreto (y de cada candidato).
# Los colores seleccionados deben ser únicos y estar en COLORES.
TAMANO_CODIGO = 5

# Tamaño de la población inicial (número de individuos por generación).
# Cada individuo es una posible combinación candidata.
POBLACION_INICIAL = 10

# Número máximo de generaciones que ejecutará el algoritmo genético.
# En cada generación se evalúan los individuos, se seleccionan los mejores,
# se cruzan y se mutan para formar la nueva población.
GENERACIONES = 1000

# Valor máximo que puede alcanzar la función de ajuste (fitness).
# Representa una solución perfecta: los 5 colores correctos en la posición correcta.
MAX_FITNESS = 5.0

# Probabilidad de mutación aplicada a cada individuo tras la reproducción.
# Controla la exploración aleatoria del espacio de soluciones.
TASA_MUTACION = 0.2  # (20%)

# Probabilidad de cruce entre dos individuos para generar descendencia.
# Si no se aplica cruce, se copia uno de los padres directamente.
TASA_CRUZA = 0.7  # (70%)

# Número de individuos de mayor fitness que se conservan directamente
# en la siguiente generación sin cambios (elitismo).
NUM_ELITE = 2
