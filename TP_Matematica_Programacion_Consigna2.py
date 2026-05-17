#   ----- CONSIGNA 2 - Análisis y optimización de costos de desarrollo -----

# para instalar la libreria ingresar en el terminal
#  --> pip install matplotlib <--
import matplotlib.pyplot as plt        #Importo la biblioteca para graficar

# DEFINO LAS FUNCIONES
def A_f(x):
    return 40*x + 200

def B_f(x):
    return 70 * x + 50

def C_f(x):
    return -2 * (x**2) + 80 * x + 100

# DEFINO VALORES DE X 
valores_x = [0, 5, 10, 15, 20, 25, 30, 40, 50]

# A continuacion se muestra la tabla de valores de cada funcion para cada valor de x
for x in valores_x:

    print("x =",x)
    print("A(x) =",A_f(x))
    print("B(x) =",B_f(x))
    print("C(x) =",C_f(x))
    print()

# GRAFICO LAS FUNCIONES

x_grafico = list(range(0,51))       #utilizo list para convertir el rango en una lista de valores de x para graficar

# Posteriormente se crean listas vacías para almacenar los valores de cada función correspondientes a cada
#valor de x en el dominio definido para el gráfico. Estas listas se llenarán con los resultados de evaluar
# cada función en cada valor de x, lo que permitirá graficar las funciones correctamente.
valores_A = []
valores_B = []
valores_C = []

# Se recorre cada valor de la lista x_grafico
for x in x_grafico: #for x in x_grafico → va tomando uno por uno los valores de x_grafico
    #Ejecuta la función usando ese valor de x A_f(x) y guarda el resultado en la lista valores_A,
    #lo mismo se hace con B y C
    valores_A.append(A_f(x))        #el .append() es para agregar el valor de A_f(x) a la lista valores_A
    valores_B.append(B_f(x))
    valores_C.append(C_f(x))

# Se grafican los valores de cada plan usando:
# x_grafico como eje X y valores_A como eje Y 
# label='Plan A' sirve para ponerle nombre a la línea del gráfico y que después aparezca 
plt.plot(x_grafico, valores_A, label='Plan A')
plt.plot(x_grafico, valores_B, label='Plan B')
plt.plot(x_grafico, valores_C, label='Plan C')

plt.xlabel('Horas de desarrollo')   # Coloca un nombre al eje X del gráfico
plt.ylabel('Costo total')           # Coloca un nombre al eje Y del gráfico
plt.title("Comparacion de planes")  # Coloca un título al gráfico

#Eje horizontal
plt.axhline(0, color = 'black')     # Es utilizado para agregar una línea horizontal en la posición y=0. 
                                    # El argumento color='black' se utiliza para establecer el color
#Eje vertical
plt.axvline(0, color = 'black')     # Es utilizado para agregar una línea horizontal en la posición x=0.
                                    # El argumento color='black' se utiliza para establecer el color

plt.legend() #Se utiliza para mostrar una leyenda en la gráfica, que ayuda a identificar qué línea 
#corresponde a cada plan.

#plt.grid(True) Se utiliza en el caso de que se quiera mostrar una cuadrícula en la gráfica,
#lo que facilita la lectura de los valores y la comparación entre las funciones. 
#El argumento TRUE indica que se desea mostrar la cuadrícula. En este caso no se utiliza porque el 
#gráfico ya es claro sin ella.

plt.show() #Se utiliza para mostrar la gráfica en pantalla





