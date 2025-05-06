

## 🧠 Introducción

**Mastermind** es un juego clásico de lógica y deducción entre dos jugadores. Uno de ellos elige una combinación secreta de colores (sin repeticiones), y el otro intenta adivinarla proponiendo distintas combinaciones. Después de cada intento, el jugador que conoce la solución proporciona una pista:

* Cuántos colores están en la **posición correcta**.
* Cuántos colores están **presentes pero en la posición incorrecta**.

El objetivo es deducir la combinación exacta con el menor número posible de intentos.

---

### 🧬 ¿Por qué usar algoritmos genéticos?

Un **algoritmo genético (GA)** es una técnica de optimización inspirada en los procesos de selección natural. En este enfoque, una población de soluciones candidatas evoluciona generación tras generación mediante operadores como:

* **Selección** (preferencia por los mejores individuos),
* **Cruce** (combinación de soluciones),
* **Mutación** (exploración aleatoria del espacio de búsqueda).

Este problema es ideal para aplicar un algoritmo genético porque:

1. **Existe una función de ajuste (fitness)** que nos permite evaluar cada intento:

   * +1 punto por cada color en su posición correcta.
   * +0.5 puntos por cada color correcto en posición incorrecta.

2. **El espacio de soluciones (fenotipos)** —es decir, las combinaciones de colores válidas— se puede codificar de forma simple como listas de letras.

3. **El espacio de representación (genotipos)** es directamente computacional: cada individuo puede representarse como una lista de caracteres sin repeticiones, lo que permite definir mutaciones, cruces y comparaciones de forma eficiente.

---

Este proyecto explora dos enfoques diferentes:

* Un algoritmo genético **clásico**, con población, cruce, mutación y elitismo.
* Una versión **simplificada**, que mantiene un solo individuo y lo mejora iterativamente (búsqueda local evolutiva).

---

## 🛠️ Instalación

Este proyecto está desarrollado en **Python 3.8+** y no requiere dependencias externas.

Puedes clonar el repositorio con:

```bash
git clone https://github.com/tu_usuario/genetic-algorithm-mastermind.git
cd genetic-algorithm-mastermind
```

---

## 🚀 Uso

Hay dos scripts principales que puedes ejecutar directamente:

### Algoritmo Genético Clásico

Ejecuta el enfoque tradicional con población, cruce, mutación y elitismo:

```bash
python genetic-algoritm-mastermind-full.py
```

Este script mostrará en consola la evolución generación a generación hasta encontrar la solución o agotar el número de generaciones.

---

### Búsqueda Evolutiva con un Solo Individuo

Ejecuta el enfoque simplificado con mutaciones progresivas:

```bash
python genetic-algorithm-mastermind-single.py
```

```bash
🎯 Código secreto: ['Y', 'C', 'R', 'P', 'M']
🔁 Solución inicial: ['G', 'Y', 'O', 'R', 'B'] -> fitness: 1.0
----------------------------------------------
✅ Gen 1: ['G', 'Y', 'O', 'R', 'C'] -> fitness: 1.5
✅ Gen 4: ['G', 'Y', 'O', 'R', 'M'] -> fitness: 2.0
✅ Gen 5: ['G', 'Y', 'R', 'O', 'M'] -> fitness: 2.5
✅ Gen 10: ['Y', 'G', 'R', 'O', 'M'] -> fitness: 3.0
✅ Gen 18: ['Y', 'G', 'R', 'P', 'M'] -> fitness: 4.0
✅ Gen 55: ['Y', 'C', 'R', 'P', 'M'] -> fitness: 5.0
```

Este script parte de una única solución aleatoria e intenta mejorarla con mutaciones que se aceptan solo si mejoran el fitness.

---

## 📁 Estructura del repositorio

```
genetic-algorithm-mastermind/
├── genetic-algorithm-mastermind-full.py         # Algoritmo genético clásico (población + cruce)
├── genetic-algorithm-mastermind-single.py       # Versión simplificada con un solo individuo
├── config.py                                    # Parámetros globales de configuración
├── utils.py                                     # Funciones comunes (fitness, mutación, etc.)
├── README.md                                    # Documentación del proyecto
```

Puedes personalizar fácilmente los parámetros del algoritmo (mutación, cruce, población, etc.) editando `config.py`.

---

¿Te gustaría añadir una sección de "📊 Ejemplo de salida" con un fragmento del log típico o un gráfico de evolución del fitness? También puedo ayudarte a preparar una visualización con `matplotlib`.

