def GeneradorLFSR(bitsIniciales, valores):
    generacion  = bitsIniciales
    salida_xor = 0
    contador = 1
    aux = 0

    while True:
        for valor in valores:
            salida_xor += int(generacion[valor-1])
        if salida_xor%2 == 0.0:
            salida_xor = 0
        else:
            salida_xor = 1
        print('Iteracion # ', contador)

        generacion, salida_xor = str(salida_xor) + generacion[:-1], 0
        print('Bits Generados : ' , generacion)
        print('')
        contador+=1

        if generacion == bitsIniciales:
            aux+=1
            print('Generado hasta el inicial')
            break

GeneradorLFSR('1010', (3,4))