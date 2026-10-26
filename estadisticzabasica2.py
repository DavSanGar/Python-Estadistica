import pandas as pd
import numpy as np

df = pd.read_csv("salary_data.csv", sep=";")

Rango = df.income.max()-df.income.min()
print("rango ingresos ",Rango)

ragno_numpy = np.max(df.age)-np.min(df.age)
print("rango edad: ",ragno_numpy)

#Varianza = df.age.var()
#print("media edad", df.age.mean())
#print("Varianza edad:", Varianza)

#varianza_numpy = np.var(df.age)
#print("varianza edad", varianza_numpy)

print("VARIANZAS POBLACIONALES")
Varianza = df.age.var(ddof=0)
print("Varianza edad", Varianza)
Varianza_np = np.var(df.age,ddof=0)
print("Varianza_np edad: ", Varianza_np)


#Desviacion estandar

ds = df.age.std()
print("Desviacion estandar", ds)
ds_np = np.std(df.age)
print("Desviacion estandar con np", ds_np)