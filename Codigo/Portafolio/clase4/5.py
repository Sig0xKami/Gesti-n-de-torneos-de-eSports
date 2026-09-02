"""
 
Ing Maria Eugenia Varando 
5. Operadores, funciones y métodos 
ventas = (120, 85, 230, 150, 90, 150) 
Resolver: 
a) Informar cantidad, mayor, menor y suma total con len(), max(), min() y sum(). 
b) Verificar pertenencia de 150 y ausencia de 500 con in y not in. 
c) Informar cuántas veces aparece 150 con count(). 
d) Informar la primera posición de 230 con index(). 
e) Concatenar ventas con (300, 250) y comprobar que se obtiene una nueva tupla. 
f) Replicar (0, 1) tres veces mediante el operador *. 
El método index() genera ValueError si el elemento no está presente. Antes de buscar 999, resuelvan el caso mediante una 
validación con in.


"""

ventas = (120, 85, 230, 150, 90, 150)

# A) ======================Infomar 
cantidad = len(ventas)
mayor = max(ventas)
menor = min(ventas)
sumaTotal = sum(ventas)
# B) ======================Verificar
esta150 = 150 in ventas 
noEsta500 = 500 not in ventas 
# C) Cuantas veces aparece 150 
cVeces150 = ventas.count(150)

#D) primra posicion de 230
Posicion230 = ventas.index(230)

#E) concatenenar  y comprobar qu es una tupla 
nueva_tupla = ventas + (300, 250)
esTupla = type(nueva_tupla)

#F) replicar (0,1) tres veces 
replicada = (0,1) * 3

#Validacion antes de buscar 999 (evita el ValueError de index() )
buscando = 999
esta999 = buscando in ventas 

if esta999: 
    posicion999 = ventas.index(buscando)
    print(f"{buscando} esta en la posicion {posicion999}")
else:
    print(f"{buscado} no está presente en la tupla")