# %% [markdown]
# ## Ejercicio 6: Empaquetado y desempaquetado

# %%
dia = 25
mes = "Septiembre"
anio = 2026
fecha = dia, mes, anio

diaN, mesN, anioN = fecha

# %% [markdown]
# ### a) Expliquen por qué fecha es una tupla aun sin paréntesis.
# 
# Cuando estamos en python lo que defenie una tupla no son los parentessis, si no la coma. Cuando escribimos `dia, mes, año` (valores separados por comas sin ningun otro contenedor como `[]` o `{}`), el interprete los empaqueta directamente en una tupla. Esto se llama *tuple packing*. Los parentensis son solo una ayuda visual opcional. 

# %%
print(type(fecha)) # <class 'tuple'

# %% [markdown]
# ### b) Muestren cada variable obtenida mediante desempaquetado.
# 
# Al hacer `diaN, mesN, anioN = fecha`, Python reparte cada elemento 
# de la tupla en una variable, en orden. Esto se llama *tuple unpacking*.

# %%
diaN, mesN, anioN = fecha

print(diaN)
print(mesN)
print(anioN)

# %% [markdown]
# ### c) Intenten desempaquetar fecha en dos variables y analicen el ValueError.
# Al intentar `a , b = fecha` se produce un error ValueError, porque `fecha` tiene 3 elementos y le pedimos  solamente 2 automaticamente python lo rechaza pero no es como que lo acepta en silencio, si no que te avisa.

# %%
a, b = fecha
#ValueError: too many values to unpack 

# %% [markdown]
# ### d) Indiquen qué condición debe cumplirse entre la cantidad de elementos y la cantidad de variables. 
# La cantidad de elementos del lado izquierdo debe ser exactamente iguall de iterable que del lado derecho. Si hay menos o mas variables que elementos, python lanza ValueError 


