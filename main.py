#Sentencia Break Ejemplo

print("While con la secuencia break \n")
contador = 0
while contador < 10:
    contador += 1

    if contador == 5:
        break

    print("Valor actual de la variable: ", contador)
    
print("\nFin del programa, la sentencia break se ha ejecutado.")

#Sentencia Continue ejemplo

print("\nWhile con la secuencia Continue \n")
contador = 0
while contador < 10:
    contador += 1

    if contador == 5:
        continue

    print("Valor actual de la variable: ", contador)
    
print("\nFin del programa, la sentencia break se ha ejecutado.")


#Condicionales Multiples

print("=====================================")
print(" ¡¡Convertidor de números a letras!! ")
print("=====================================")

num_uno = int(input("¿Cual es el número que deseas convertir?: "))

if num_uno == 1:
    print("El número es: 'UNO'")
elif num_uno == 2:
    print("El número es: 'DOS'")
elif num_uno == 3:
    print("El número es: 'TRES'")
elif num_uno == 4:
    print("El número es: 'CUATRO'")
elif num_uno == 5:
    print("El número es: 'CINCO'")
else:
    print("Este programa solo puede convertir hasta el número 5")
    
print("=====================================")
print("Fin.")
print("=====================================")


#esto es un comentario
print ("Hola")

"Esto es otro Comentario"

print ("Hola")

""" Hola esto
es un
comentario
multilinea
"""

print ("Hola")

#Condicionales Anidadas

print("=========== \n")
print(" Conversor \n")
print("=========== \n")


print(" Menu de Opciones: \n")

print("Presiona 1 para convertir de número a palabra.")
print("Presiona 2 para convertir de palabra a número. \n")

opcion = int(input("¿Cuál es tu opción deseada?: "))

if opcion == 1:
    print("\n Conversor de número a palabra. \n")

    opcion_uno = int(input("¿Cúal es el número que desea convertir a palabra?: "))

    if opcion_uno == 1:
        print ("El número es 'UNO'")
    elif opcion_uno == 2:
        print("El número es 'DOS'")
    elif opcion_uno == 3:
        print("El número es 'TRES'")
    elif opcion_uno == 4:
        print("El número es 'CUATRO'")
    elif opcion_uno == 5:
        print("El número es 'CINCO'")
    else:
        print("El número seleccionado no esta registrado")

elif opcion == 2:
    print("\n Conversor de palabra a número. \n")

    opcion_dos = input("¿Cúal es la palabra que deseas covertir a número?: ")
    opcion_dos = opcion_dos.lower()

    if opcion_dos == "uno":
        print ("El número es '1'")
    elif opcion_dos == "dos":
        print("El número es '2'")
    elif opcion_dos == "tres":
        print("El número es '3'")
    elif opcion_dos == "cuatro":
        print("El número es '4'")
    elif opcion_dos == "cinco":
        print("El número es '5'")
    else:
        print("El número seleccionada no esta registrado")

else:
    print("Opción no disponible.")

print("Fin.")

#Condicionales Compuestas

print ("Sistema para carcular el promedio de un alumno.")

nombre = input("Para comenza, Cual es tu nombre?: ")

matematicas = float(input(nombre + " Cual es tu calificaión en matemática?: "))
quimica = float(input(nombre + " Cual es tu calificaón en quimica?: "))
biologia = float(input(nombre + " Cual es tu calificación en biologia?: "))

promedio = (matematicas + quimica + biologia) /3

if promedio>= 6:
    print('Felicidades ' + nombre + ' "APROBASTE" com un promedio de: ', promedio )
    print('Felicidades ' + nombre + ' "APROBASTE" com un promedio de: ', round(promedio, 2))

else:
    print('Lo sentimos ' + nombre + ' has "REPROBADO" com un promedio de: ',  promedio )
    print('Lo sentimos ' + nombre + ' has "REPROBADO" com un promedio de: ',  round(promedio, 2) )

print("Fin.")

#Ejercicio Practico 4

print("\nCalculadora en un Sistema Python, con una sola variable. \n")

print("**********************")
print('* "Menu de Opciones" *')
print("********************** \n")

print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. División Entera")
print("6. Exponente")
print("7. Modulo o Resto \n")

numero = int(input("Introduce la opcion deseada: "))

if numero == 1:
    print("Elegiste suma \n")
    numero = int(input("Introduce el primer número: "))
    numero += int(input("Introduce el segundo número: "))
    print("\nEl resultado de la suma es: ", numero)

elif numero == 2:
    print("Elegiste resta \n")
    numero = int(input("Introduce el primer número: "))
    numero -= int(input("Introduce el segundo número: "))
    print("\nEl resultado de la resta es: ", numero)

elif numero == 3:
    print("Elegiste multiplicación \n")
    numero = int(input("Introduce el primer número: "))
    numero *= int(input("Introduce el segundo número: "))
    print("\nEl resultado de la multiplicación es: ", numero)

elif numero == 4:
    print("Elegiste división \n")
    numero = float(input("Introduce el primer número: "))
    numero /= float(input("Introduce el segundo número: "))
    print("\nEl resultado de la división es: ", round(numero, 2))
    
elif numero == 5:
    print("Elegiste división entera \n")
    numero = int(input("Introduce el primer número: "))
    numero //= int(input("Introduce el segundo número: "))
    print("\nEl resultado de la división entera es: ", numero)

elif numero == 6:
    print("Elegiste expontente \n")
    numero = int(input("Introduce el primer número: "))
    numero **= int(input("Introduce el segundo número: "))
    print("\nEl resultado del exponente es: ", numero)

elif numero == 7:
    print("Elegiste modulo o resto \n")
    numero = int(input("Introduce el primer número: "))
    numero %= int(input("Introduce el segundo número: "))
    print("\nEl resultado de la modulo o resto es: ", numero)
else:
    print("La opcion elegida no esta disponible")

#Ejercicio Practico 5

#idea mia! mas simple

print("0","1","1","2","3","5","8","13","21","34","55","89","144","233","377","610","987","1597 ", sep=" ")

#Sucesión Fibonacci

print("Sucesión Fibonacci \n")

num_uno, num_dos = 0, 1

while num_dos <=1597:
    print(num_uno, num_dos, end=" ")
    num_uno = num_uno + num_dos
    num_dos = num_uno + num_dos


#Ejercicio 1

print("Sistema para calcular el promedio de un alumno em Anatomia e Fisiologia Humana.")

nombre =  input("Para comenza, Cual es tu nombre?: ")

matematicas = int(input(nombre + " Cual es tu calificacion en atividade?: "))
quimica = int(input(nombre + " Cual es tu calificacion en prova final?: "))
biologia = int(input(nombre + " Cual es tu calificacion en laboratorio?: "))

promedio = (matematicas + quimica + biologia) / 3
promedio = int(promedio)

if promedio >= 6:
    print('Felicidades ' +  nombre + ' "APROBASTES" con un promedio de: ', promedio)

if promedio<= 5.9:
    print('Infelizmente ' +  nombre + ' "Reprobaste" con un promedio de: ', promedio)


   
    

print("Fin.")

#Ejercicio Practico 1
print("==============================")
print('Compañia Multinacional "Rappi"')
print("==============================")
print('"Sistema vacional de Rappi"')
print("==============================\n")

nombre = input('Para comenza, ¿Cual es el "nombre del empleado"?: ')

print("\n", nombre, ", a ¿cual departemento pertenece? \n")

print('Presiona 1 para el "Departamento de Atención al Cliente", empleado con "clave 1"')
print('Presiona 2 para el "Departamento de Logística", empleado con "clave 2"')
print('Presiona 3 para "Gerencia", empleado con "clave 3"')

clave = int(input("\n ¿Cual es la clave del empleado: "))

#end

print("Esto es un", end=" ")
print("ejemplo")

#Entrada de Datos

palabra = input("Introduce una Palabra: ")
num_int = int(input("Introduce un Número Entero: "))
num_float = float(input("Introduce un Número Flotante: "))
num_complex = complex(input("Introduce un Número Complejo: "))

print("String: ", palabra)
print("Entero: ", num_int)
print("Float: ", num_float)
print("Número Complejo: ", num_complex)

#Entrada de Datos continuacion

nombre =  input("Cual es tu nombre?: ")
print("Hola " + nombre + ", vamos a realizar una suma")

num_uno = int(input("Por Favor Introduce el primer valor: "))
num_dos = int(input("Por Favor Introduce el segundo valor: "))

resultado = num_uno + num_dos

print(nombre + " el resultado de la suma es: ", resultado)

#Función Len()

#Opción 1

print("\nHola tiene", len("Hola"), "caracteres.")

#Opción 2

longitud = len("La Geekipedia")
print("\nLa Geekipedia tiene", longitud, "caracteres.") #No precisa hacer espacio porque los agrega por si solo.

# Meme de Procesos Selectivos

print ('Proceso Selectivo, de la "Empresa Pico PicoPicó"')

nombre = input("Digite el nombre del seleccionado, Cual es el nombre?: ")

matematicas = float(input(nombre + " Cual es su calificación en la Prueba Lógica?: "))
quimica = float(input(nombre + " Cual es su calificaón en el Teste Comportamental?: "))
biologia = float(input(nombre + ' Cual es su calificación en la "ENTREVISTA"?: '))

promedio = (matematicas + quimica + biologia) /3

if promedio>= 1100:
    print('Felicidades ' + nombre + ' "APROBASTE" com un promedio de: ', promedio )
    print('Felicidades ' + nombre + ' "APROBASTE" com un promedio de: ', round(promedio, 2))

else:
    print('Lo sentimos ' + nombre + ' há "REPROBADO NUESTRO PROCESO SELECTIVO" con un promedio de: ',  promedio, ' "SUERTE SIGUE INTENTANDO"' )
    print('Lo sentimos ' + nombre + ' há "REPROBADO NUESTRO PROCESO SELECTIVO " con un promedio de: ',  round(promedio, 2), ' "SUERTE SIGUE INTENTANDO"' )

print("Fin.")
print('Paz "Empresa Pico PicoPicó"')

#Operadores

print ("Suma:")

numero_uno = 5
numero_dos = 4

resultado = numero_uno  +  numero_dos

print ("El resultado de la suma es: " + str(resultado))


print ("Resta:")

numero_uno = 5
numero_dos = 4

resultado = numero_uno  -  numero_dos

print ("El resultado de la resta es: " + str(resultado))


print ("Multiplicación:")

numero_uno = 5
numero_dos = 4

resultado = numero_uno  *  numero_dos

print ("El resultado de la multiplicación es: " + str(resultado))



print ("Exponente:")

numero_uno = 2
exponente = 5

resultado = numero_uno  **  exponente

print ("El resultado del Exponente es: " + str(resultado))


print ("División:")

numero_uno = 4
numero_dos = 2

resultado = numero_uno  /  numero_dos

print ("El resultado de la División es: " + str(resultado))


print ("Módulo:")

numero_uno = 30
numero_dos = 8

resultado = numero_uno  %  numero_dos

print ("El resultado del Módulo es: " + str(resultado))


print ("División Entera:")

numero_uno = 4
numero_dos = 2

resultado = numero_uno  //  numero_dos

print ("El resultado de la División Entera es: " + str(resultado))




print ("División Entera:")

numero_uno = 10
numero_dos = 3

resultado = numero_uno  //  numero_dos

print ("El resultado de la División Entera es: " + str(resultado))

#Operadores Asignación

nombre = "Hola "
nombre += input(" Escribe tu nombre: ")
print (nombre, ", este es el incremento y decremento de una variable. \n")

print("Incremento o Aumento: ")
x=1
print ("El valor inicial de x es: ", x)

x+=1
x+=1
x+=1
x+=1
x+=1
print("el valor final de x es: ", x, "\n")

print("Decremento o Disminucion: ")
print ("El valor inicial de x es: ", x)

x-=1
x-=1
x-=1
x-=1
x-=1
print("el valor final de x es: ", x, "\n")

#Oeradores Racionales

print("Introduce dos números a comparar: \n")

num_uno = int(input("Intruduce el primer número: "))
num_dos = int(input("Intruduce el segundo número: "))

print("\n Los números a comparar son: ", num_uno, " y ", num_dos, "\n")

if num_uno == num_dos:
    print("Es igual... \n")
if num_uno != num_dos:
    print("Son diferentes... \n")
if num_uno < num_dos:
    print("Es menor... \n")
if num_uno > num_dos:
    print("Es mayor... \n")
if num_uno <= num_dos:
    print("Es menor o igual... \n")
if num_uno >= num_dos:
    print("Es mayor o igual... \n")

print("Fin...")

#Operadores Lógico

#Conjucióm

print("\n ^^^^^^^^^^^^^^^^^")
print("  Conjucion (and) ")
print(" ----------------- \n")

num_uno = int(input("Escribe un número mayor a 2 y menor a 5: "))

if num_uno > 2 and num_uno < 5:
    print("El número ", num_uno, " Cumple con la comdición. \n")
else:
    print("El número ", num_uno, " NO cumple con la condición. \n" )


#Disyuncióm

print("^^^^^^^^^^^^^^^^^")
print(" Disyunción (or) ")
print("----------------- \n")    

palabra = input("Para cumplir con la condicion escribe 'Si' o 'Yes': ")
if palabra == "Si" or palabra == "Yes":
    print("La condición se ha cumplido. \n")
else:
    print("La condición No se ha cumplido. \n")


#Negación

print("^^^^^^^^^^^^^^^^")
print(" Negación (not) ")
print("---------------- \n")

num_uno = int(input("Introduce un número igual a 5: "))

if not num_uno == 5:
    print("\n El número es diferente de cinco y 'SI' cumple con la condición. \n")
else:
    print("\n El número es igual a cinco y 'NO' cumple con la condición. \n")

print("--------Fin-------- \n")


#sep

print("1","2","3","4","5","fin")

print("1","2","3","4","5","fin", sep="")

print("1","2","3","4","5","fin", sep="-")

print("1","2","3","4","5","fin", sep=", ")

#Suma

print ("Esto es una suma")
numero_uno = 2
numero_dos = 4
resultado = numero_uno + numero_dos
print (resultado)

#Texto

mensaje = "Hola"
mensaje += " "
mensaje += "Ernesto"
print (mensaje)

print ("concatenación:")

mensaje = "Hola"
espacio = " "
nombre = "Ernesto"
print(mensaje + espacio + nombre)


numero_uno = 4
numero_dos = 6
resultado = numero_uno + numero_dos
resultado = str(resultado)
print("El resultado de la suma es:" + resultado)


print ("Busqueda:")
mensaje = "Hola Ernesto"
buscar_subcadena = mensaje.find("Ernesto")
print (buscar_subcadena)

print("Extracción:")
mensaje = "Hola Ernesto"
extraer_subcadena = mensaje[1:8]
print(extraer_subcadena)

print("Comparacion:")

mensaje_uno = "Hola"
mensaje_dos = "Hola"
print(mensaje_uno == mensaje_dos)

mensaje_uno = "Hola"
mensaje_dos = "Ernesto"
print(mensaje_uno == mensaje_dos)

#Texto simple base concanetación 

mensaje = "Hola"
espacio = " "
nombre = "Ernesto"
print(mensaje + espacio + nombre)

#Texto simple base concanetación 2

mensaje = "Hola Ernesto"
extraer_subcadena = mensaje[1:8]
print(extraer_subcadena)

#Tipo de Dato Entero o Largo
numero = 15
print (numero, type(numero))

#Tipo de Dato Flotante

numero_flotante = 15.5
print (numero_flotante, type(numero_flotante))

#Tipo de dato Numero Complejo
numero_complejo = 5 + 6j
print(numero_complejo, type(numero_complejo))

#Tipo de Dato scring
nombre = "Ernesto"
print(nombre, type(nombre))

#Tipo de Dato Booleano
verdadero_falso = 3 == 3
print(verdadero_falso, type(verdadero_falso))

verdadero_falso = 3 == 35
print(verdadero_falso, type(verdadero_falso))

#while función


x=1

while x<3:
    print(x)
    x+=1

print("Fin.")


#Ejemplo 2

x=1

while x<11:
    print("Ernesto")
    x+=1

print("Fin.")


#Ejemplo 3

x=0

while x<1000:
    print("Ivanna")
    x+=1

print("Fin.")
