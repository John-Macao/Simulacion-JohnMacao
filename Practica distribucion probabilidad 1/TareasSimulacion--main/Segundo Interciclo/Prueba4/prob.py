import numpy as np 
import random
import math 

random.seed(1234)


for x in range(random.randint(1,3)):
    mu, sigma = 20, 10 # media y desvio estandar
    datos = abs(math.ceil(np.random.normal(mu, sigma, 1))) #creando muestra de datos con una distribución normal
    print(datos)

