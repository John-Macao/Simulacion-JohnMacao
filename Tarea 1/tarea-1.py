
import random

import matplotlib.pyplot as plt

valor2 = 0
valor3 = 0
valor4 = 0
valor5 = 0
valor6 = 0
valor7 = 0
valor8 = 0
valor9 = 0
valor10 = 0
valor11 = 0
valor12 = 0
aux = 0

for i in range(100):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma = dado1 + dado2
    aux = aux + 1
    
    if suma == 2:
        valor2 = valor2 + 1
    elif suma ==3:
        valor3 = valor3 + 1
    elif suma ==4:
        valor4 = valor4 + 1
    elif suma ==5:
        valor5 = valor5 + 1
    elif suma ==6:
        valor6 = valor6 + 1
    elif suma ==7:
        valor7 = valor7 + 1
    elif suma ==8:
        valor8 = valor8 + 1
    elif suma ==9:
        valor9 = valor9 + 1
    elif suma ==10:
        valor10 = valor10 + 1
    elif suma ==11:
        valor11 = valor11 + 1
    elif suma ==12:
        valor12 = valor12 + 1
        
print('valor 2: ' + str(valor2))
print('valor 3: ' + str(valor3))
print('valor 4: ' + str(valor4))
print('valor 5: ' + str(valor5))
print('valor 6: ' + str(valor6))
print('valor 7: ' + str(valor7))
print('valor 8: ' + str(valor8))
print('valor 9: ' + str(valor9))
print('valor 10: ' + str(valor10))
print('valor 11: ' + str(valor11))
print('valor 12: ' + str(valor12))

valores = [2, 3,4,5,6,7,8,9,10,11,12]
datos = [valor2, valor3, valor4, valor5, valor6, valor7, valor8, valor9, valor10, valor11, valor12]

fig, ax = plt.subplots()
ax.set_ylabel('Num. Repetición')
ax.set_xlabel('Escala 2-12')
ax.set_title('Probabilidad de que se repita el 7')
plt.bar(valores , datos)
plt.savefig('grafico_probabilidad_7.png')
plt.show()
#datos.plot.hist()
#plt.show()


#sns.histplot(data=datos, x="xxxxx" , y= "yyyyyy")