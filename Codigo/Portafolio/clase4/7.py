# %% [markdown]
# # 7. Tuplas anidadas

# %%
alumnos = ( 
    ("Ana", (12, "Marzo", 2005)), 
    ("Bruno", (8, "Julio", 2004)), 
    ("Carla", (21, "Enero", 2005)) 
) 

# %% [markdown]
# # a) Mostrar el nombre del segundo alumno.
# Cada alumno es una tupla alumnos, nombre y fecha son tuplas de tuplas. Para llegar al segundo alumnos tenemos que aacceder con el indice [1] (arranca en 0) y dentro de esa tupla el nombre esta en la posicion [0]

# %%
nombreSegundo = alumnos[1][0]
print(nombreSegundo)

# %% [markdown]
# ### b) Mostrar la fecha completa del tercer alumno.
# El tercer alumno esta en el indice [2] y su fecha (que encima es otra tupla) esta en la posicion [1]

# %%
fechaTercero = alumnos[2][1]
print(fechaTercero) 

# %% [markdown]
# ### c) Mostrar únicamente el mes de nacimiento del primer alumno. 
# Primer alumno: indice[0]. Su fecha: indice[1]. dentro de la fecha , el mes esta en la posicion [1] (dia,mes,año).

# %%
mesPrimero = alumnos[0][1][1]
print(mesPrimero)

# %% [markdown]
# ### d) Recorrer la estructura y mostrar nombre, día, mes y año con formato legible. 
# Como cada elemento de alumnos es una tupla nombre, fecha . A su ves fecha es (dia,mes,año), se puede desempaquetar todo directamente en el for, incluso en dos niveles a la vez 

# %%
for nombre, (dia, mes, anio) in alumnos:
    print(f"{nombre} nacio el {dia} de {mes} de {anio}")


