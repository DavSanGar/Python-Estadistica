import pandas as pd
import numpy as np



def calculo(vector):

    #Media
    suma = 0
    n = 0

    for elemento in vector:
        suma += elemento
        n += 1

    media = (1/n)*suma

    print("media:", media)
 
    #Alternativas

    suma = sum(vector)
    n = len(vector)

    media_2 = suma / n

    print("media_2:", media_2)


    moda = 0
    repeticiones = 0

    diccionario = {}

    for elemento in vector:
        if not diccionario.get(elemento):
            diccionario[elemento] = 1
        else:
            diccionario[elemento] += 1

        if diccionario[elemento]> repeticiones:
            moda = elemento    

    print("moda:", moda)

    #Mediana

    vector.sort(reverse = False) #Así ordenamos de menor a mayor

    punto_medio = int(len(vector)/2)


    if len(vector) % 2 == 0:
        mediana = (vector[punto_medio] + vector[punto_medio+1])/2
    else:
        mediana = vector[punto_medio]

    print("mediana:", mediana)


vector = [1,2,3,4,5,6,7,8,9,8,6,5,7,5]

# calculo(vector)

df = pd.read_csv("salary_data.csv", sep=";")

print(df.head())

print(df.age.mean())
print(df.age.mode())


v = np.array(vector)
print(v.mean())