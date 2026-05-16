#   ----- CONSIGNA 2 - Análisis y optimización de costos de desarrollo -----

# para instalar la libreria en la terminal ingresar en el terminal
#  --> pip install matplotlib <--

import matplotlib.pyplot as plt # Importo la biblioteca para graficar

# DEFINO LAS FUNCIONES

def A_f(x):
    return 40*x + 200

def B_f(x):
    return 70 * x + 50

def C_f(x):
    return -2 * (x**2) + 80 * x + 100

# DEFINO VALORES DE X 

valores_x = [0, 5, 10, 15, 20, 25, 30, 40, 50]
