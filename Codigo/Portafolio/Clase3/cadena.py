texto = "Programacion en Python"

#5)
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
#6)
#a)
print(texto.upper())
#La salida que esperamos: "PROGRAMACION EN PYTHON"
#b)
print(texto.lower())
#Resultado: "programacion en python"

#c)
print(texto.title())
#Resultado: "Programacion En Python" pasa el "en" a mayuscula solo la letra "e"
#d)
print(texto.capitalize())
#Resultado: "Programacion en python" la letra "P" de python pasa a minuscula 
#e)
print(texto.replace("Python", "IA"))
#Resultado: "Programacion en IA"
#f)
print(texto.count("a"))
#Resultado: 2 (las 'a' presentes en "Programacion")
#g) 
print(texto.find("Python"))
#Resultado: 16 (La "p" de python empieza con el indice 16)
#h) 
print(len(texto))
#Resultado: 22 caracteres que tiene totales 


# --- SEGUNDA PARTE: Métodos de validación (Diapositiva 37) ---

c1 = "Programacion"
c2 = "2026"
c3 = "Python3"
c4 = "Programacion en Python"

print("\n--- Resultados de validación ---")
print(f"'{c1}' -> isalpha: {c1.isalpha()} | isdigit: {c1.isdigit()} | isalnum: {c1.isalnum()}")
print(f"'{c2}' -> isalpha: {c2.isalpha()} | isdigit: {c2.isdigit()} | isalnum: {c2.isalnum()}")
print(f"'{c3}' -> isalpha: {c3.isalpha()} | isdigit: {c3.isdigit()} | isalnum: {c3.isalnum()}")
print(f"'{c4}' -> isalpha: {c4.isalpha()} | isdigit: {c4.isdigit()} | isalnum: {c4.isalnum()}")

"""
isdigit devuelve true solamente si todos los caracteres son digitos , no tiene ningun signo especial y al menos tiene 
un caracter. 
Ejemplo cuando da True:

"123".isdigit() da como salida False

isalnum devuelve true solamente si todos son letras o numeros, si hay un espacio, simbolo o un espacio estaria dando False

isalpha() retorna False en "Programacion en Python" porque el método evalúa 
que absolutamente TODOS los caracteres de la cadena sean letras alfabéticas. 
Como los espacios en blanco (" ") se consideran caracteres dentro de la secuencia 
y no forman parte del abecedario, la condición falla.
"""
