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

#   --- Parte B: Lógica proporcional ---

# FUNCION LOGICA
def usuario_critico(usuario):

    p = usuario in A # Usuario activo en API
    q = usuario in B # Usuario activo en Web
    r = usuario in C # Usuario con errores
    return r and (p or q) # Me devuelve usuario crítico si tiene errores y está activo en al menos una plataforma

# CLASIFICACIÓN
usuarios = set(A+B+C) # Todos los usuarios únicos

print("Clasificación de usuarios:")

for usuario in usuarios:
    if usuario_critico(usuario): # Si el usuario es crítico, lo clasifico como tal
        print(usuario,"-> Crítico")
    else:
        print(usuario,"-> No crítico")

print()

#   --- Parte C: Interpretacion ---

#   ¿Qué tipo de usuarios representa mayor riesgo?
#   Los usuarios críticos representan un mayor riesgo, ya que tienen errores (r es verdadero) y
#   están activos en al menos una plataforma (p o q es verdadero).
#   Esto significa que estos usuarios pueden estar experimentando problemas que afectan su experiencia, lo
#   que podría llevar a una mayor insatisfacción y abandono de la plataforma. Además, si estos usuarios 
#   son activos en ambas plataformas, el impacto negativo podría ser aún mayor, ya que podrían estar 
#   enfrentando problemas en ambos entornos.

#   ¿Qué significa que el usuario este en C pero no en A U B?
#   Significa que el sistema detectó errores asociados a un usuario que no aparece registrado utilizando
#   ninguna plataforma. Puede representar intentos de acceso ilegitimos, errores de logging,
#   inconsistencias en la base de datos, problemas de sincronizacion entre sistemas, o incluso actividades
#   maliciosas. 

#  ¿Qué decisiones se deberian tomar como equipo programador?
#   Revisar logss del usuario 109. Validar autenticaciones. Mejorar controles de consistencia. Implementar
#   alertas automaticas. Analizar usuarios críticos para reducir errores.

