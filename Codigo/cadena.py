texto = "Programacion en Python"

#a)
print(texto[0])
print(texto[-1])

#b) 
palabra = texto[:12] #doce digitos "Programacion"
print(palabra) #Esperamos como salida programacion 

#Mostrar cadena invertida
invertida = texto[::-1]
print(invertida) # Como salida obtenemos nohtyP ne noicamargorP

#d)

if "Python" in texto:
    print("Se encuentra la palabra Python en la cadena")
else:
    print("No se encuentra la cadena python en la cadena")

# #e) 
# texto[0] = "p" #intentamos modificar

# #Obtenemos:
# """
# y", line 23, in <module>
#     texto[0] = "p" #intentamos modificar
#     ~~~~~^^^
# TypeError: 'str' object does not support item assignment
# """
# #Como indica la diapositiva 32 de la clase 3
# """
# Las cadenas de texto (str) son un tipo de dato inmutable. 
# Esto es porque una ves que se crea la cadena en la memoria de la computadora, su contenido queda fijo y no se puede alterar posicion por posicion
# """
