# Selection sort  ( seleccion )
    # Este algoritmo va buscando los elementos mas pequeños y los intercambia en orden.
    # Primero busca el mas pequeño y lo intercambia en la primera posicion del array 
    # Luego lo mismo con el segundo y asi 

arr=[1,2,4,5,7,3,98,3,26,33,6,23]       #Array con valores random

def selectionSort(arr):
    if not arr: 
        return arr 
    for i in range(len(arr)- 1):        
        min_i= i            
        for j in range(i+1 , len(arr)):
            if arr[j] < arr[min_i]:
                min_i=j
        arr[i],arr[min_i]=arr [min_i], arr[i]
        print("Vuelta :" , i , arr)

#selectionSort(arr)

# Insertion sort (Ordenacion de insercion)
    """ Parte de una lista de objetos desordenados  . Toma el primer elemento y lo considera
    como una lista de 1 elemento ordenada, toma el segundo elemento y lo inserta en la posicion 
    que corresponda teniendo en cuenta la comparacion realizada
    """


def insertionSort(arr):

    for i in range(len(arr)):
        valor=arr[i]   #Guardamos el valor en la variable valor
        j = i - 1      # J inicia en el elemento anterior al actual 
        while j >= 0  and valor <= arr[j]:  
            arr[j+1] = arr [j]  #desplazamos el elemento en arr[j] una pos a la derecha para hacerle espacio al valor
            j-= 1   #disminuimos j para comparar hacia la izquierda
        arr[j+1]= valor  # insertamos el valor en la posicion que corresponde
        print("Estado actual de la lista :" , arr)


#insertionSort(arr)

# Bubble Sort (Ordenacion de burbuja)

"""
    Es un algoritmo que va comparando la posicion actual y la siguiente  . Si el valor actual 
    es mayor al siguiente los intercambia  y sigue este proceso hasta terminar de ordenar
"""

def bubbleSort(arr):
    n = len(arr) # ponemos en la variable N la longitud de nuestro array
    for i in range(n):  #recorre el array
        for j in range(0,n-1):  # pega toda una vuelta al array 
            if arr[j] > arr[j+1]:       #compara posicion actual con posicion siguiente
                arr[j], arr[j+1] = arr[j+1], arr[j] #swap
        print("vuelta numero :" ,i ,arr)    #impresion para ver el proceso

#bubbleSort(arr)



