# Autor: Juan Carlos Flores García, A01376511. Grupo 4.

# Descripción: Programa que recibe listas y regresa una nueva lista o modifica una lista existente dependiendo del
# ejercicio.


# Función que recibe una lista y luego regresa una lista nueva únicamente con los valores pares.
def extraerPares(lista):
    listaDePares = []

    for valor in lista:
        if valor % 2 == 0:
            listaDePares.append(valor)

    return listaDePares


# Función que recibe una lista y regresa una lista nueva con valores mayores a un elemento previo.
def extraerMayoresPrevio(lista):
    listaMayoresPrevio = []

    for valor in range(1, len(lista)):
        if lista[valor] > lista[valor - 1]:
            listaMayoresPrevio.append(lista[valor])

    return listaMayoresPrevio


# Función que recibe una lista y luego regresa una lista nueva con las parejas de números en lugares intercambiados.
def intercambiarParejas(lista):
    listaDeParejas = []

    for valor in range(1, len(lista), 2):
        listaDeParejas.append(lista[valor])
        listaDeParejas.append(lista[valor - 1])

        if valor % 2 == 1:
            listaDeParejas.append(lista[-1])

    return listaDeParejas


# Función que recibe una lista y luego la regresa modificada con el número mayor y menor cambiados de lugar.
def intercambiarMM(lista):
    if len(lista) > 0:
        numeroMayor = max(lista)
        numeroMenor = min(lista)

        nMayor = lista.index(numeroMayor)
        nMenor = lista.index(numeroMenor)

        lista[nMayor] = numeroMenor
        lista[nMenor] = numeroMayor

        return lista

    else:

        return lista


# Función que recibe una lista, después saca el promedio de los números sin contar el número mayor y el número menor y
# luego regresa el promedio.
def promediarCentro(lista):
    if len(lista) > 2:
        lista.sort()
        promedioDelCentro = sum(lista[1:len(lista) - 1]) // len(lista[1:len(lista) - 1])

        return promedioDelCentro

    else:
        if len(lista) == 0:
            return lista
        else:
            return 0


# Función que recibe una lista y calcula su media y desvicación.
def calcularEstadistica(lista):
    if len(lista)>0:
        mediaDeLista = sum(lista) / len(lista)
    else:
        mediaDeLista = 0

    if len(lista)>0:
        acumular = 0
        for valor in lista:
            acumular += (valor - mediaDeLista) ** 2
        desviacionDeLista = ((acumular / (len(lista) - 1))) ** 0.5
    else:
        desviacionDeLista = 0

    return (mediaDeLista, "%.6f" % desviacionDeLista)





