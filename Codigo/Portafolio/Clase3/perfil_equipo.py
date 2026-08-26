"""
Desarrollen perfil_equipo.py dentro de la carpeta codigo del repositorio. El programa deberá solicitar el nombre del
equipo, comisión, nombre de cada integrante y rol inicial en el proyecto.
El programa deberá:
• Normalizar los nombres con title().
• Convertir el nombre del equipo a mayúsculas.
• Informar la cantidad de caracteres del nombre del equipo.
• Generar una sigla con la inicial de cada palabra.
• Verificar si el nombre del equipo contiene al menos un dígito recorriendo sus caracteres y utilizando isdigit().
• Mostrar toda la información mediante f-strings.
• Mantener las operaciones de procesamiento dentro de funciones y la entrada/salida general en el programa principal.
def contiene_digitos(texto):
 val= False
 for caracter in texto:
 if caracter.isdigit():
 val= True
 return val
 """

 #===============================
 #P
#===============================
def RecorrerListaIntegrantes(IntegrantesLista, nombre):
    for i in range(len(IntegrantesLista)):
        if IntegrantesLista[i] == nombre:
            return nombre
    return -1

def RecorrerListaRol(RolLista, nombre, IntegrantesLista):
   nombreEncontrado = RecorrerListaIntegrantes(IntegrantesLista, nombre)
   if nombreEncontrado == -1: 
       return False
   posicion = IntegrantesLista.index(nombre)
   Rol = RolLista[posicion]
   return Rol

def TodoRol(RolLista):
    for i in range(len(RolLista)):
      
        print(f"ROL {RolLista[i]} del integrante")

def TodoIntegrante(IntegrantesLista):
    for i in range(len(IntegrantesLista)):
   
        print(f"INTEGRANTE {IntegrantesLista[i]}")


def asignarIntegrante(nombreIntegrante, ListaIntegrantes):
    if RecorrerListaIntegrantes(ListaIntegrantes, nombreIntegrante) == -1: 
        ListaIntegrantes.append(nombreIntegrante)
        return f"Se agrego satifactoriamente al integrante {nombreIntegrante}"
    else:
        return f"El integrante {nombreIntegrante} ya existe, por lo cual no se agrego a la lista. "
    

def asignarRol(RolLista,nombre,IntegrantesLista, Rol, nombreEquipo): 
    if RecorrerListaIntegrantes(IntegrantesLista, nombre) == -1:
        return "El integrante no se encuentra en la lista"
    else:
        RolLista.append(Rol)
        return f"El integrante {nombre} del equipo {nombreEquipo} fue asignado con el ROL {Rol} "

def procesar_alta_integrante(nombreIntegrante, ListaIntegrantes, RolLista, rolIntegrante, nombreEquipo):
    if RecorrerListaIntegrantes(ListaIntegrantes, nombreIntegrante) != -1:
        return f"El integrante {nombreIntegrante} ya existe, no se agregó ni se le asignó rol."
    else:
        ListaIntegrantes.append(nombreIntegrante)
        RolLista.append(rolIntegrante)
        return f"El integrante {nombreIntegrante} del equipo {nombreEquipo} fue asignado con el ROL {rolIntegrante}"



   
   



def normalizar(IntegrantesLista, nombre):
    Integrante = RecorrerListaIntegrantes(IntegrantesLista, nombre)
    if Integrante == -1:
        return "El integrante no esta en la lista: "
    else: 
        return Integrante.title()


def EquipoM(nombreEquipo):
    return nombreEquipo.upper()

def Cara(nombreEquipo):
    return len(nombreEquipo)
        
def Siglas(nombreEquipo):
    listaPalabras = nombreEquipo.split()
    sigla= ""
    for palabra in listaPalabras:
        sigla = sigla + palabra[0]
    sigla = sigla.upper()
    return sigla

def UnDigito(nombreEquipo):
    val = False
    for caracter in nombreEquipo:
        if caracter.isdigit():
            val= True
    return val

    
    


    

def main():
 #===============================
 #S
#===============================
    nombreEquipo = ""
    comision = ""
    Integrantes = []
    Rol = []




 #===============================
 #I
#===============================
 
    nombreEquipoI = input("Ingrese el nombre del equipo: ")
    nombreEquipo = nombreEquipoI
    comisionI = input("Ingrese la comision: ")
    cantidadI = int(input("Ingrese la cantidad de integrantes en el equipo: "))
    while cantidadI <= 0:
        print("Ingresa una cantidad mayor a 0")
        cantidadI = int(input("Ingrese la cantidad de integrantes en el equipo: "))


    for i in range(cantidadI):
        i = i + 1 
        nombreIntegrante = input(f"Ingrese el nombre del integrante del equipo:   integrante n{i}")
        RolIntegrante = input(f"Del integrante {nombreIntegrante} n {i} Ingrese su rol: ")
        mensaje = procesar_alta_integrante(nombreIntegrante, Integrantes, Rol, RolIntegrante, nombreEquipo)
        print(mensaje)


 #===============================
 #O
#===============================
    print("Salida")
    print(f"Equipo: {nombreEquipo} - Comisión: {comision}")
    print("Todo")
    TodoIntegrante(Integrantes)
    TodoRol(Rol)
   
    print("Normalizar")

    for integrante in Integrantes:
        print(normalizar(Integrantes,integrante))

    print("Nombre del equipo en mayuscula")
    print(EquipoM(nombreEquipo))

    print(f"Cantidad de caracteres del equipo {nombreEquipo}")
    print(Cara(nombreEquipo))

    print("Nombre del equipo en siglas")
    print(Siglas(nombreEquipo))

    print("Verificar si al menos el nombre del equipo tiene un digito")
    if UnDigito(nombreEquipo):
        print("Tiene un digito al menos en su nombre")
    else:
        print("No tiene ningun digito en el nombre del equipo")
    

if __name__ == '__main__':
    main()