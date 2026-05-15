#       ---------- TRABAJO PRÁCTICO INTEGRADOR MATEMATICA Y PROGRAMACIÓN ----------



#   ----- CONSIGNA 1- Validación de usuarios y análisis de consistencia del sistema -----


# --- Parte A: Analisis con conjuntos ---

# Defino los datos utilizando listas ya que son estructuras básicas
A = [101, 102, 103, 104, 105, 106]  # API
B = [104, 105, 106, 107, 108]       # WEB
C = [102, 105, 109]                 # ERRORES

# CONVERTIR A CONJUNTOS
setA = set(A)
setB = set(B)
setC = set(C)

# AMBAS PLATAFORMAS
ambas = setA & setB # Utilizo & ya que es el operador de intersección
print("Usuarios que usan ambas plataformas:")
print()

# AL MENOS UNA PLATAFORMA (A U B)
al_menos_una = setA | setB # Utilizo | ya que es el operador de unión
print("Usuarios que usan al menos una plataforma:",al_menos_una)
print()

# SIN ERRORES (A U B) - C

sin_errores = (setA | setB) - setC # - es el operador de diferencia

print("Usuarios sin errores:",sin_errores)
print()

# EXCLUSIVOS DE ERRORES (C - (A U B))

solo_A = setA - setB
solo_B = setB - setA
exclusivos = solo_A | solo_B

print("Usuarios exclusivos:", exclusivos)
print()

# USUARIOS EN C PERO NO EN A U B

inconsistentes = setC - (setA | setB)

print("Usuarios en C pero no en A U B:", inconsistentes)
print()
