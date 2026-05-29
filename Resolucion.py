# Parte A: Análisis con Conjuntos
print("Parte A — Análisis con Conjuntos:")

# Los conjuntos de usuarios que tenemos son:

A = [101, 102, 103, 104, 105, 106] # API
B = [104, 105, 106, 107, 108] # Web
C = [102, 105, 109] # Errores

# Los imprimimos
print("Conjunto A (API):", A)
print("Conjunto B (Web):", B)
print("Conjunto C (Errores):", C)

print() # Salto de línea para mejor lectura


# 1 Cálculos e Interpretación
print("1. Cálculos e Interpretación:")
print() # Salto de línea para mejor lectura


# Intersección (A∩B): Usuarios que usan ambas plataformas.
interseccion = [] # vector vacío para almacenar la intersección
for id_a in A: # para id_a recorremos el vector A posicion por posición
    for id_b in B: # para id_b recorremos el vector B  posición por posición
        if id_a == id_b: # Si encontramos un ID que está en A y B osea ambos
            interseccion.append(id_a) # Lo agregamos al vector intersección
            # Utilizamos append porque lo vimos en clases
print("Intersección (A ∩ B):", interseccion) # Imprimimos la intersección

print() # Salto de línea para mejor lectura


# Unión (A ∪ B): Total de usuarios activos en el sistema.
union = [] # vector vacío para almacenar la unión
for id_a in A: # Recorremos cada id_a en A
    if id_a not in union: # Si el id_a no está ya en la unión, lo agregamos
        union.append(id_a) # Agregamos el id_a a la unión
for id_b in B: # Recorremos cada id_b en B
    if id_b not in union: # Si el id_b no está en la unión
        union.append(id_b) # Agregamos el id_b a la unión
print("Unión (A ∪ B):", union)

print() # Salto de línea para mejor lectura


# Diferencia ((A ∪ B)−C): Usuarios activos que no tuvieron errores.
diferencia = [] # vector vacía para almacenar la diferencia
for id_union in union: # Recorremos cada id_union en la unión del vector union anterior
    if id_union not in C: # Si el id_union no está en el conjunto de errores
        diferencia.append(id_union) # Lo agregamos a la diferencia
print("Diferencia ((A ∪ B)−C):", diferencia) # Imprimimos la diferencia

print() # Salto de línea para mejor lectura

# Diferencia Simétrica (AΔB): Usuarios que usan solo una plataforma (API o Web, pero no ambas).

diferencia_simetrica = [] # vector vacío para almacenar la diferencia simétrica
for id_a in A: # Recorremos cada id_a en A
    if id_a not in B: # Si el id_a no está en B, es decir, solo está en A
        diferencia_simetrica.append(id_a) # Lo agregamos a la diferencia simétrica
for id_b in B: # Recorremos cada id_b en B
    if id_b not in A: # Si el id_b no está en A, es decir, solo está en B
        diferencia_simetrica.append(id_b) # Lo agregamos a la diferencia simétrica
print("Diferencia Simétrica (A Δ B):", diferencia_simetrica) # Imprimimos la diferencia simétrica

print() # Salto de línea para mejor lectura

# 3. Usuarios que aparecen en C pero no en A ∪ B:
print("3. Usuarios que aparecen en C pero no en A ∪ B:")
print() # Salto de línea para mejor lectura
# Usuarios que generaron errores pero no están registrados como usuarios activos en ninguna plataforma.

usuarios_errores_no_activos = [] # vector vacío para almacenar los usuarios que están en C pero no en la unión de A y B
for id_c in C: # Recorremos cada id_c en C
    if id_c not in union: # Si el id_c no está en la unión de A y B
        usuarios_errores_no_activos.append(id_c) # Lo agregamos a la lista de usuarios con errores pero no activos
print("Usuarios en C pero no en A ∪ B:", usuarios_errores_no_activos) # Imprimimos los usuarios que están en C pero no en la unión de A y B

print() # Salto de línea para mejor lectura

# Parte B: Lógica Proposicional
print("Parte B — Lógica Proposicional:")
print() # Salto de línea para mejor lectura

print("Definición de proposiciones:")
print("p: pertenece a A (usuario accede por API)")
p = A
print("q: pertenece a B (usuario accede por Web)")
q = B
print("r: pertenece a C (usuario ha generado errores)")
r = C
print() # Salto de línea para mejor lectura

print("Definición de usuario crítico:")
print("(p ∨ q) ∧ r")
print() # Salto de línea para mejor lectura

# 5. Construcción de la tabla de verdad

#Ejemplo sin usar el append

tabla_verdad = [None] * 5
# Inicializamos cada fila de la tabla de verdad con una lista de 9 elementos (1 para el nombre y 8 para las combinaciones de p, q, r)
for filas in range(5):
    tabla_verdad[filas] = [0] * 9

# Nombres de cada fila
tabla_verdad[0][0] = "p (API)"
tabla_verdad[1][0] = "q (Web)"
tabla_verdad[2][0] = "r (Errores)"
tabla_verdad[3][0] = "(p v q)"
tabla_verdad[4][0] = "(p v q) ^ r"

columna_actual = 1 # Empezamos en la columna 1 porque la columna 0 está reservada para los nombres de las filas

for p in [1, 0]:
    for q in [1, 0]:
        for r in [1, 0]:

            # Calculamos los resultados
            p_o_q = p or q
            resultado = p_o_q and r

            # Convertimos cada valor a "V" o "F" por separado
            if p == 1:
                tabla_verdad[0][columna_actual] = "V"
            else:
                tabla_verdad[0][columna_actual] = "F"

            if q == 1:
                tabla_verdad[1][columna_actual] = "V"
            else:
                tabla_verdad[1][columna_actual] = "F"

            if r == 1:
                tabla_verdad[2][columna_actual] = "V"
            else:
                tabla_verdad[2][columna_actual] = "F"

            if p_o_q == 1:
                tabla_verdad[3][columna_actual] = "V"
            else:
                tabla_verdad[3][columna_actual] = "F"

            if resultado == 1:
                tabla_verdad[4][columna_actual] = "V"
            else:
                tabla_verdad[4][columna_actual] = "F"

            columna_actual += 1

# Imprimimos la tabla
print("Tabla de verdad:")
print()

for i in range(9):
    for j in range(5):
        print(tabla_verdad[j][i], end="\t\t ")  # Imprimimos cada elemento con tabulación y sin salto de línea
    print()

print() # Salto de línea para mejor lectura

#6. Implementación de la función en Python que evalúe la expresión (p ∨ q) ∧ r
print("6. funcion")
def es_usuario_critico(usuario_id):
    p = usuario_id in A  # Verifica si el usuario pertenece a A
    q = usuario_id in B  # Verifica si el usuario pertenece a B
    r = usuario_id in C  # Verifica si el usuario pertenece a C

    return (p or q) and r  # Retorna True si es crítico, False en caso contrario
print("Ejemplo de uso de la función es_usuario_critico:")
print("Usuario 105 es crítico:", es_usuario_critico(105)) # Ejemplo de uso de la función para el usuario 105, que pertenece a A, B y C, por lo tanto es crítico
print()


print("7. Clasificación de usuarios:")

# 1. Creamos una lista de usuarios únicos sin usar set()
usuarios_unicos = []
for usuario in (A + B + C):
    if usuario not in usuarios_unicos:
        usuarios_unicos.append(usuario)

# 2. Clasificamos los usuarios
usuarios_criticos = []
usuarios_no_criticos = []

for usuario_id in usuarios_unicos: 
    if es_usuario_critico(usuario_id):
        usuarios_criticos.append(usuario_id)
    else:
        usuarios_no_criticos.append(usuario_id)

print("Usuarios críticos:", usuarios_criticos)
print("Usuarios no críticos:", usuarios_no_criticos)
print() # Salto de línea para mejor lectura

print("Parte C — Interpretación:")
print() # Salto de línea para mejor lectura

# 8. Responder:
# o ¿Qué tipo de usuario representa mayor riesgo?
# o ¿Qué significa que un usuario esté en 𝐶 pero no en 𝐴 ∪ 𝐵?
# o ¿Qué decisión tomarían como equipo programador?

print("8. Respuestas:")
print("¿Qué tipo de usuario representa mayor riesgo?") 
print("Los usuarios críticos representan el mayor riesgo, ya que acceden a la plataforma (ya sea por API o Web) y han generado errores. Estos usuarios podrían estar causando problemas en el sistema o podrían ser víctimas de ataques, por lo que requieren atención prioritaria.")
print("Ejemplo", usuarios_criticos) # Ejemplo de usuarios críticos para ilustrar la respuesta
print() # Salto de línea para mejor lectura
print("¿Qué significa que un usuario esté en C pero no en A ∪ B?")
print("Un usuario que está en C pero no en A ∪ B es un usuario que ha generado errores pero no está registrado como activo en ninguna de las plataformas (API o Web). Esto podría indicar que el usuario ha intentado acceder al sistema de manera no autorizada, o que ha generado errores sin haber accedido correctamente a través de las plataformas, lo cual es un comportamiento sospechoso y potencialmente peligroso.")
print("Ejemplo", usuarios_errores_no_activos) # Ejemplo de usuarios que están en C pero no en A ∪ B para ilustrar la respuesta
print() # Salto de línea para mejor lectura
print("¿Qué decisión tomarían como equipo programador?")
print("Como equipo programador, se recomendaría implementar medidas de seguridad adicionales para los usuarios críticos, como monitoreo más estricto, autenticación multifactor o incluso bloqueo temporal si se detectan comportamientos anómalos. Para los usuarios que están en C pero no en A ∪ B, se debería investigar su actividad para determinar si se trata de intentos de acceso no autorizados o errores legítimos, y tomar medidas en consecuencia, como reforzar la seguridad del sistema o mejorar la gestión de errores.")


# Consigna 2 — Análisis y optimización de costos de desarrollo
print()
print("Consigna 2 — Análisis y optimización de costos de desarrollo")

print() # Salto de línea para mejor lectura
print("Parte A — Análisis matemático")
print("Funciones implementadas:")
print("A(x) = 40x + 200")
print("B(x) = 70x + 50")
print("C(x) = -2x^2 + 80x + 100")
print() # Salto de línea para mejor lectura
print() # Salto de línea para mejor lectura

print("Parte B — Implementación en Python")
print("5. programar las funciones en Python.")
a = 40 # Coeficiente de x en A(x)
b = 200 # Término independiente en A(x)
c = 70 # Coeficiente de x en B(x)
d = 50 # Término independiente en B(x)
e = -2 # Coeficiente de x^2 en C(x)
f = 80 # Coeficiente de x en C(x)
g = 100 # Término independiente en C(x)
def A(x):
    return a * x + b # Función A(x) que calcula el costo del plan A para una cantidad de horas x
def B(x):
    return c * x + d # Función B(x) que calcula el costo del plan B para una cantidad de horas x
def C(x):
    return e * x**2 + f * x + g # Función C(x) que calcula el costo del plan C para una cantidad de horas x
print("Costo del plan A para 10 horas:", A(10)) # Costo del plan A para 10 horas
print("Costo del plan B para 10 horas:", B(10)) # Costo del plan B para 10 horas
print("Costo del plan C para 10 horas:", C(10)) # Costo del plan C para 10 horas


print("6. Programar las funciones en Python.")
print() # Salto de línea para mejor lectura

print("Para esta consigna, se recomienda usar Matplotlib para graficar las funciones A(x), B(x) y C(x) en el intervalo dado. La implementación de las funciones y la lógica para determinar el plan más económico se realizará utilizando estructuras básicas de programación, asegurando que la librería se utilice únicamente para la visualización, tal como lo establece la rúbrica de evaluación.")
print("se instala con el comando en terminal: pip install matplotlib")

print() # Salto de línea para mejor lectura
print("Generar gráfico de las funciones en el intervalo dado utilizando Matplotlib")
#importamos la librería para graficar y visualización de datos 
import matplotlib.pyplot as plt
import numpy as np # Importamos numpy para manejar arrays y generar el intervalo de x de manera eficiente
# Definimos el intervalo de x
x = np.linspace(0, 50, 100) # Generamos 100 puntos entre 0 y 50 con numpy porque para la libreria matplotlib se maneja numpy 

# Calculamos los valores de y para cada función
y_A = A(x) # Calculamos A(x) para cada valor de x
y_B = B(x) # Calculamos B(x) para cada valor de x
y_C = C(x) # Calculamos C(x) para cada valor de x


# Graficamos las funciones
plt.figure(figsize=(10, 6)) # Configuramos el tamaño de la figura
plt.plot(x, y_A, label='Plan A (A(x))', color='blue') # Graficamos A(x) con color azul
plt.plot(x, y_B, label='Plan B (B(x))', color='orange') # Graficamos B(x) con color naranja
plt.plot(x, y_C, label='Plan C (C(x))', color='green') # Graficamos C(x) con color verde
plt.title('Costo de los Planes de Contratación') # Título del gráfico
plt.xlabel('Horas utilizadas (x)') # Etiqueta del eje x segun eje carteceano
plt.ylabel('Costo (y)') # Etiqueta del eje y segun eje carteceano
plt.legend() # Mostramos la leyenda para identificar cada función por su color
plt.grid() # Agregamos una cuadrícula
plt.xlim(0, 50) # Limitamos el eje x 
plt.ylim(-20, max(max(y_A), max(y_B), max(y_C))-2400) # Limitamos el eje y 
plt.show() # Mostramos el gráfico    

print() # Salto de línea para mejor lectura

print("7. Evaluar las funciones para los valores dados.")
valores_x = [0, 5, 10, 15, 20, 25, 30, 40, 50] # Lista de valores de x para evaluar las funciones
print("Evaluación de las funciones para los valores de x:")
for x in valores_x:
    print(f"x = {x}: A(x) = {A(x)}, B(x) = {B(x)}, C(x) = {C(x)}") # Evaluamos y mostramos el costo de cada plan para cada valor de x   
print() # Salto de línea para mejor lectura
print("8. Crear una función que determine el plan más económico para un valor de x.")
def plan_mas_economico(x):
    costo_A = A(x) # Calculamos el costo del plan A para x horas
    costo_B = B(x) # Calculamos el costo del plan B para x horas
    costo_C = C(x) # Calculamos el costo del plan C para x horas

    costos = {'Plan A': costo_A, 'Plan B': costo_B, 'Plan C': costo_C} # Creamos un diccionario con los costos de cada plan
    # Encontramos el plan con el costo mínimo utilizando la función min y la clave del diccionario
    if costo_A < costo_B and costo_A < costo_C:
        plan_economico = 'Plan A' # Si el costo del plan A es el menor, lo asignamos como el plan más económico
    elif costo_B < costo_A and costo_B < costo_C:
        plan_economico = 'Plan B' # Si el costo del plan B es el menor, lo asignamos como el plan más económico
    else:
        plan_economico = 'Plan C' # Si el costo del plan C es el menor, lo asignamos como el plan más económico
        
    return plan_economico, costos[plan_economico] # Retornamos el nombre del plan más económico y su costo
# Ejemplo de uso de la función para x = 10 horas
plan, costo = plan_mas_economico(10) # Determinamos el plan más económico para 10 horas
print(f"Ej: para x = 10 horas, el plan más económico es {plan} con un costo de {costo}.") # Mostramos el resultado del plan más económico para 10 horas
print() # Salto de línea para mejor lectura
print("Parte C — Análisis")
print("9. Determinar para qué valores conviene cada plan.")
print("Para determinar para qué valores de x conviene cada plan, podemos evaluar la función plan_mas_economico para un rango de valores de x y observar cuál plan es el más económico en cada caso. A continuación, se muestra un análisis general basado en la evaluación de los costos para los valores de x dados anteriormente:")
for x in valores_x:
    plan, costo = plan_mas_economico(x) # Determinamos el plan más económico para cada valor de x
    print(f"x = {x} horas: Plan más económico = {plan} con costo = {costo}") # Mostramos el plan más económico para cada valor de x 
print() # Salto de línea para mejor lectura

print("Consigna 3 — Análisis de rendimiento en un sistema distribuido")

print() # Salto de línea para mejor lectura
print("Parte B — Implementación en Python")
print("3. Calcular el tiempo promedio de ejecución por función y por servidor.")
# Matriz de tiempos promedio de ejecución (en milisegundos)
M = [
    [120, 150, 100], # Función 1: Autenticación
    [200, 180, 220], # Función 2: Procesamiento de datos
    [90, 110, 95]    # Función 3: Generación de reportes
]
# Matriz de cantidad de ejecuciones
C = [
    [30, 20, 10], # Función 1: Autenticación
    [15, 25, 20], # Función 2: Procesamiento de datos
    [40, 10, 30]  # Función 3: Generación de reportes
]
# Calcular el tiempo promedio de ejecución por función
tiempo_promedio_funcion = [] # vector vacío para almacenar el tiempo promedio por función
for i in range(0,3,1): # Recorremos cada función (fila de M)
    suma_tiempos = 0 # Variable para acumular la suma de los tiempos de ejecución de la función i
    for j in range(0,3,1): # Recorremos cada servidor (columna de M)
        suma_tiempos += M[i][j] # Sumamos el tiempo de ejecución de la función i en el servidor j
    promedio = suma_tiempos / 3 # Calculamos el promedio dividiendo la suma por el número de servidores (3)
    tiempo_promedio_funcion.append(promedio) # Agregamos el promedio al vector de tiempos promedio por función
print("Tiempo promedio de ejecución por función:")
for i in range(0,3,1):
    print(f"Función {i+1}: {tiempo_promedio_funcion[i]} ms") # Imprimimos el tiempo promedio de ejecución para cada función
print() # Salto de línea para mejor lectura
# Calcular el tiempo promedio de ejecución por servidor
tiempo_promedio_servidor = [] # vector vacío para almacenar el tiempo promedio por servidor
for j in range(0,3,1): # Recorremos cada servidor (columna de M)
    suma_tiempos = 0 # Variable para acumular la suma de los tiempos de ejecución en el servidor j
    for i in range(0,3,1): # Recorremos cada función (fila de M)
        suma_tiempos += M[i][j] # Sumamos el tiempo de ejecución de la función i en el servidor j
    promedio = suma_tiempos / 3 # Calculamos el promedio dividiendo la suma por el número de funciones (3)
    tiempo_promedio_servidor.append(promedio) # Agregamos el promedio al vector de tiempos promedio por servidor
print("Tiempo promedio de ejecución por servidor:")
for j in range(0,3,1):
    print(f"Servidor {j+1}: {tiempo_promedio_servidor[j]} ms") # Imprimimos el tiempo promedio de ejecución para cada servidor
print() # Salto de línea para mejor lectura
print("4. Calcular la matriz transpuesta de M y explicar qué representa en este contexto.")
# Calcular la matriz transpuesta de M
M_transpuesta = [] # vector vacío para almacenar la matriz transpuesta
for j in range(0,3,1): # Recorremos cada columna de M
    fila_transpuesta = [] # Lista para almacenar la fila de la matriz transpuesta correspondiente a la columna j de M
    for i in range(0,3,1): # Recorremos cada fila de M
        fila_transpuesta.append(M[i][j]) # Agregamos el elemento M[i][j] a la fila transpuesta
    M_transpuesta.append(fila_transpuesta) # Agregamos la fila transpuesta a la matriz transpuesta
print("Matriz transpuesta de M:")
for fila in M_transpuesta:
    print(fila) # Imprimimos cada
# fila de la matriz transpuesta
print() # Salto de línea para mejor lectura
print("El resto de las consignas se encuentran en el PDF adjunto, debido a su tipo de resolucion que requiere un análisis más detallado y una explicación extensa, lo cual es más adecuado para un formato escrito. En el PDF se incluyen las respuestas a las preguntas de interpretación crítica, análisis mediante producto matricial, propiedades de la matriz y análisis aplicado, siguiendo la estructura y criterios establecidos en la rúbrica de evaluación.")
