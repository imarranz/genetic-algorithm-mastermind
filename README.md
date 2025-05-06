
## 🧠 Introducción

<p align="center">
  <img src="https://repository-images.githubusercontent.com/978594808/a7188d90-0f10-4267-9b4b-7c7b03b98a0c" alt="Genetic Algorithm Mastermind">
</p>

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://www.python.org/)
[![Genetic Algorithm Mastermind](https://img.shields.io/badge/Genetic%20Algorithm-Mastermind-blueviolet.svg)](https://github.com/imarranz/genetic-algorithm-mastermind)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.md)

**Mastermind** es un juego clásico de lógica y deducción entre dos jugadores. Uno de ellos elige una combinación secreta de colores (sin repeticiones), y el otro intenta adivinarla proponiendo distintas combinaciones. Después de cada intento, el jugador que conoce la solución proporciona una pista:

  * Cuántos colores están en la **posición correcta**.
  * Cuántos colores están **presentes pero en la posición incorrecta**.

El objetivo es deducir la combinación exacta con el menor número posible de intentos.

---

### 🧬 ¿Por qué usar Algoritmos Genéticos?

Un **Algoritmo Genético (GA)** es una técnica de optimización inspirada en los procesos de selección natural. En este enfoque, una población de soluciones candidatas evoluciona generación tras generación mediante operadores como:

  * **Selección** https://img.shields.io/badge/Selección-yellow.svg: Preferencia por los mejores individuos.
  * **Cruce**: Combinación de soluciones.
  * **Mutación**: Exploración aleatoria del espacio de búsqueda.
  * **Elitismo**: Preservación de los individuos con mejor rendimiento entre generaciones.

El juego de _Mastermind_ representa un problema ideal para ser abordado mediante algoritmos genéticos, debido a que::

1. **Existe una función de ajuste (fitness)** que nos permite evaluar cada intento. Mi propuesta es puntuar de la siguiente manera:

  * +1 punto por cada color en su posición correcta.
  * +0.5 puntos por cada color correcto en posición incorrecta.

Dado que el código objetivo contiene cinco colores únicos, la solución se considera correcta únicamente cuando la función de ajuste alcanza exactamente 5.0, lo que indica que todos los colores están en la posición correcta.

2. **El espacio de soluciones (fenotipos)** —es decir, las combinaciones de colores válidas— se puede codificar de forma simple como listas de letras.

3. **El espacio de representación (genotipos)** es directamente computacional: cada individuo puede representarse como una lista de caracteres sin repeticiones, lo que permite definir mutaciones, cruces y comparaciones de forma eficiente.

---

Este proyecto explora dos enfoques diferentes:

  * Un algoritmo genético **clásico**, con población, cruce, mutación y elitismo.

  * Una versión **simplificada**, que mantiene un solo individuo y lo mejora iterativamente (búsqueda local evolutiva).

---

## 🛠️ Instalación

Este proyecto está desarrollado en **Python 3.8+** y no requiere dependencias externas.

Puedes clonar el repositorio con el siguiente comando:

```bash
git clone https://github.com/imarranz/genetic-algorithm-mastermind.git
cd genetic-algorithm-mastermind
```

---

## 🚀 Uso

Hay dos scripts principales que puedes ejecutar directamente:

### :dna: Algoritmo Genético Clásico

Ejecuta el enfoque tradicional con población, cruce, mutación y elitismo:

```bash
python genetic-algoritm-mastermind-full.py
```

Este script mostrará en consola la evolución generación a generación hasta encontrar la solución o agotar el número de generaciones.

---

### :repeat: Búsqueda Evolutiva con un Solo Individuo

Ejecuta el enfoque simplificado con mutaciones progresivas:

```bash
python genetic-algorithm-mastermind-single.py
```

Y obtendremos una salida como la siguiente:

```bash
🎯 Código secreto: ['Y', 'C', 'R', 'P', 'M']
🔁 Solución inicial: ['G', 'Y', 'O', 'R', 'B'] -> fitness: 1.0
----------------------------------------------
✅ Gen 1: ['G', 'Y', 'O', 'R', 'C'] -> fitness: 1.5
✅ Gen 4: ['G', 'Y', 'O', 'R', 'M'] -> fitness: 2.0
✅ Gen 5: ['G', 'Y', 'R', 'O', 'M'] -> fitness: 2.5
✅ Gen 10: ['Y', 'G', 'R', 'O', 'M'] -> fitness: 3.0
✅ Gen 18: ['Y', 'G', 'R', 'P', 'M'] -> fitness: 4.0
✅ Gen 21: ['Y', 'C', 'R', 'P', 'M'] -> fitness: 5.0
```

Este script parte de una única solución aleatoria e intenta mejorarla con mutaciones que se aceptan solo si mejoran el fitness.

---

### :gear: Parámetros configurables

Este proyecto permite ajustar varios parámetros que afectan al comportamiento del algoritmo genético y la estrategia evolutiva. Estos parámetros se definen en el archivo `config.py` y pueden modificarse fácilmente según el tipo de ejecución (`genetic-algorithm-mastermind-full.py` o `genetic-algorithm-mastermind-single.py`). La siguiente tabla resume los principales parámetros disponibles:

| Parámetro           | Descripción                                                              | Se aplica en               |
| ------------------- | ------------------------------------------------------------------------ | -------------------------- |
| `COLORES`           | Lista de colores posibles que forman las combinaciones                   | `-single` y `-full`        |
| `TAMANO_CODIGO`     | Número de colores que tiene el código secreto                            | `-single` y `-full`        |
| `MAX_FITNESS`       | Valor de la función de ajuste que indica solución perfecta (`=5.0`)      | `-single` y `-full`        |
| `GENERACIONES`      | Número máximo de generaciones o iteraciones permitidas                   | `-single` y `-full`        |
| `TASA_MUTACION`     | Probabilidad de aplicar mutación a un individuo                          | `-single` y `-full`        |
| `POBLACION_INICIAL` | Número de individuos por generación                                      | `-full`                    |
| `TASA_CRUZA`        | Probabilidad de que dos padres se crucen en lugar de copiar uno de ellos | `-full`                    |
| `NUM_ELITE`         | Número de mejores individuos que se preservan sin cambios (elitismo)     | `-full`                    |


---

## 📁 Estructura del Repositorio

```
genetic-algorithm-mastermind/
├── genetic-algorithm-mastermind-full.py         # Algoritmo genético clásico (población + cruce)
├── genetic-algorithm-mastermind-single.py       # Versión simplificada con un solo individuo
├── config.py                                    # Parámetros globales de configuración
├── utils.py                                     # Funciones comunes (fitness, mutación, etc.)
├── README.md                                    # Documentación del proyecto
```

--

## :books: References

  * **Martínez-Arranz I**, Alonso C, Mayo R, Mincholé I, Mato JM, Lee DJ. _Genetic algorithms applied to translational strategy in metabolic-dysfunction associated steatohepatitis (MASH). Learning from mouse models_. Comput Methods Programs Biomed. 2024 Oct;255:108346. doi: [10.1016/j.cmpb.2024.108346](https://doi.org/10.1016/j.cmpb.2024.108346). Epub 2024 Jul 26. PMID: 39089186.

