#https://github.com/denulemos/logicaProgramacion


"""
Ejercicio 1
Dado un numero devolver su tabla de multiplicar completa. Por ejemplo:

Input: 5
Output:
	
Tabla del 5
5 x 1 = 5
5 x 2 = 10
(...)
"""

"""
numero = int (input("ingrese numero a multiplicar: "))
contador = 0

for contador in range (0,11):
	resultado = contador * numero
	print (f"{contador} x {numero} = {resultado}")
"""
























"""
Ejercicio 2
Dado un String comprobar si es un palindromo o no
 (se leen igual del derecho y del revés), 
 por ejemplo Bob, Pop, etc... No tener en cuenta espacios ni simbolos.

Input: "otto"
Output: true

"""


"""
cadenadecaracteres = input ("Ingrese una cadena de caracteres: ")
validez = False

if (cadenadecaracteres == cadenadecaracteres[::-1]):
	validez = True
else:
	validez = False
	
print (validez)
"""




















"""
Ejercicio 3
Dado un String y una frase decir cuantas veces se repite la palabra en esa frase dada.

Input: ("Hola", "Hola cómo andas?")
Output: 1
"""

"""
palabra = input ("Ingrese palabra: ").upper()

frase = input ("Ingrese una frase: ").upper()

quitar = ",;:.!¿?"
for caracter in quitar:
	frase = frase.replace(caracter, " ")

print (frase)

listapalabras = []

listapalabras = frase.split() #este metodo divide en vectores cada palabra separada por un espacio

repeticion = 0

print (listapalabras)

for indice in listapalabras:
	if (indice == palabra):
		repeticion+=1
		
print (f"La palabra ingresada fue: {palabra}, y se repite:  {repeticion} vez/veces.")
"""























"""
Ejercicio 4
Dado un String, darle la vuelta, invertir el orden de sus caracteres. 
No se pueden usar metodos del lenguaje, solo estructuras de control.

Input: "hola"
Output: aloh
"""

"""
texto = input ("Ingrese cadena de caracteres: ")
print (texto[::-1])

"""




















"""
Ejercicio 5
Sacar el porcentaje de un numero. Mandamos tanto el porcentaje como el numero por parametros.

Input: (20, 100) -- El 20% de 100
Output: 20
"""

"""
primernumero = int(input("Ingrese numero entero: "))

porcentaje = int (input("ingrese porcentaje 1 al 100: "))

calculo = (primernumero * porcentaje ) / 100

print (f"El {porcentaje}% del numero {primernumero}, es: {calculo} ")
"""




"""
Ejercicio 6
Dibujar un cuadrado hueco con astericos en consola con el tamaño de lados que definamos nosotros

Input: 4
Output:
  * ** *
  *    *
  *    * 
  *    * 
  * ** *
"""

# ~ filas = int(input("Cantidad de filas: "))
# ~ columnas = int (input ("Cantidad de columnas: "))






"""
lado = 4

for fila in range (lado):
  for columna in range (lado):
    if fila == 0 or fila == lado-1 or columna == 0 or columna == lado-1:
      print ("* ", end="")
      
    else:
        print ("  ", end="")
        
  print ()
"""



















"""
Dados dos numeros, devolver cuantos numeros impares hay ENTRE ellos

Input: (1, 100)
Output: 49
"""

"""
desde = int(input("Ingrese numero inicial: "))
hasta = int(input("Ingrese numero final: "))

contadorimpares = 0
contadorpares = 0

if (desde < hasta):

	for indice in range (desde,hasta):
		if indice %2 != 0:
			contadorimpares = contadorimpares + 1
		elif indice %2 == 0:
			contadorpares = contadorpares + 1

	print (f"La cantidad de numeros impares es de: {contadorimpares} ")

else:
	print ("El numero inicial es mayor o igual al numero final. \nError! \nProcure poner el numero inicial como menor que el numero final ")
"""	


















"""
Ejercicio 8
Con un numero entero, invertirlo y devolverlo dado vuelta.

Input: 56
Output: 65
"""

"""
numero = int (input("Ingrese un numero entero:"))
print (type(numero))
numero = str (numero)
print (type(numero))
print (numero[::-1])
"""























"""
Ejercicio 9
Dados dos array devolver una lista o array con los elementos comunes entre ambos sin duplicados

Input: ([1,2,3], [3,2,5,6])
Output: [2,3]
"""


"""
from random import *

#declaro la primer matriz
primermatriz = [ 	[0,0,0],
					[0,0,0],
					[0,0,0]
				]

#declaro la segunda matriz
segundamatriz = [ 	[0,0,0],
					[0,0,0],
					[0,0,0]
				]

#relleno la primera matriz con numeros al azar
for contador1 in range (len(primermatriz)):
	
	for contador2 in range (len(primermatriz[contador1])):
		
		primermatriz[contador1][contador2] = randint (1,9)

#relleno la segunda matriz con numeros al azar
for contador1 in range (len(segundamatriz)):
	
	for contador2 in range (len(segundamatriz[contador1])):
		
		segundamatriz[contador1][contador2] = randint (1,9)

#impresion
print ("primer matriz al azar")
for fila in primermatriz:
	print (fila)
	
#impresion
print ("segunda matriz")
for fila in segundamatriz:
	print (fila)

#declaro una lista donde se guardan los datos duplicados
duplicados = []
dato = 0

for filas in range (len(primermatriz)):
	
	for columnas in range (len(primermatriz[filas])):
		
		for vectores in range (len(primermatriz)):
		
			if primermatriz[filas][columnas] in segundamatriz [vectores]:
		
			
				duplicados.append(primermatriz[filas][columnas]) #segundo intento
			
print (f"Los numeros duplicados son: {duplicados}")
duplicados = set(duplicados) #set es para trabajar con conjuntos, sin duplicados. Los borra automaticamente
print (f"Estructura set: {duplicados}")
"""




























"""
Ejercicio 10
Dado un numero mostrar una escalera con escalones de guiones usando el numero para los niveles de la escalera.

Input: 4
Output:
  [-]
  [-][-]
  [-][-][-]
  [-][-][-][-]
"""

"""
numero = int (input("Ingrese un numero: "))

#primera forma
for contador1 in range (numero):
	
	for contador2 in range (contador1+1):
		
		print ("[-]", end = "")
	print (" ")



#segunda forma
altura = numero

for fila in range (altura):
  for columna in range (fila+1):
    print ("[-]", end ="")
  print (" ")

"""



























"""
Ejercicio 11
Dado un String y una busqueda, censurar las coincidencias de la busqueda en el String con [-CENSURADO-]
 Si ambos llegan vacios, devolver un "No se puede leer el texto y la busqueda". 
 Y si llega un solo parametro, devolver "No se puede hacer la busqueda"

Input: ('holi como va', 'holi) -- Frase y palabra a censurar
Output: [-CENSURADO-] como va
"""


"""
palabra = input ("Palabra a censurar: ").lower()
frase = input ("Ingrese frase: ").lower()

if palabra in frase:
	frase = frase.replace((palabra), "-CENSURADO-")

print (frase)
"""
	
	
	
	

	



















"""
Ejercicio 12
Dado un numero mostrar todos los numeros desde ese al 0 de 8 en 8 en una lista con guiones 
y cada numero debe empezar por "n"

Input: 100
Output:
-n 100
-n 92
-n 84
etc..
"""

"""
numero = int (input("Ingrese numero: "))

for contador in range (numero, 0, -8):
	print (f"-n {contador}")
"""





















"""
Ejercicio 14
Dado un String y un numero, repetir el String las veces que diga el numero
"""

"""
cadenadecaracteres = input ("Ingrese texto: ")
repeticion = int(input("¿Ingrese la cantidad de veces que desea repetirlo?"))


for contador in range (repeticion):
	print (f"N°{contador+1}: {cadenadecaracteres}")
"""









"""
Ejercicio 15
Dado un String devolver el caracter mas usado.

Input: denuuu
Output: u
"""

"""
miprimerdiccionario = {}

alfabeto = "abcdefghijklmnñopqrstuvwxyz"

for contador in alfabeto:
	miprimerdiccionario[contador] = 0 


frase = input("Ingrese una cadena de caracteres: ").lower()


for caracter in frase:
	if caracter not in miprimerdiccionario.keys():
		miprimerdiccionario[caracter] = 1
	else:
		miprimerdiccionario[caracter]+=1
		

for key, valor in miprimerdiccionario.items():
	print (f"{key}:{valor}")

mayor = 0

for caracter, valor in miprimerdiccionario.items():
	if (miprimerdiccionario[caracter] > mayor):
		letra = caracter
		mayor = miprimerdiccionario[caracter]
		
print (f"La letra que mas se repite es: {letra}, con un total de: {mayor}")
"""
	
	
























"""
Ejercicio 16
Dado una cadena de texto, devolver cuantas vocales tiene la misma.

Input: denu
Output: 2
"""

"""
vocales = "aeiou"
frase = input ("Ingrese frase: ").lower()
contadorvocales = 0

for indice in frase:
	if indice in vocales:
		contadorvocales+=1
		
print (f"La cantidad de vocales es de: {contadorvocales}")
"""





















"""
Ejercicio 18
Dado un numero, mostrar sus divisores (hasta el número)

Input: 5
Output: 1 5
"""

"""
numero = int (input ("Ingrese numero: "))

for contador in range (1, numero+1):
	if (numero % contador == 0):	
		print (contador, "es divisor")
"""






"""
Ejercicio 20
Dados dos String crear un algoritmo que compruebe si son anagramas entre si 
(Si ambos usan los mismos caracteres en una misma cantidad) 
ejemplo: roma - mora - amor 
ejemplo: vino - ovni
"""

"""
frase1 = (input("Ingrese primera frase: ")).upper()
frase2= (input("Ingrese segunda frase: ")).upper()
print (f"Usted ingreso las frases: {frase1} & {frase2} ")

listaletra1 = []
listaletra2 = []

#paso 1) las palabras van dentro de listas sin los espacios.	
for letra in frase1:
	if letra != " ":
		listaletra1.append(letra)	

for letra in frase2:
	if letra != " ":
		listaletra2.append(letra)
			
print (f"Las listas en caracteres quedaron de la siguiente forma: \n{listaletra1}\n & \n{listaletra2}\n ")	

#verifico si las 2 palabras son del mismo tamaño			
if (len(listaletra1)) == (len(listaletra2)): 
	print (f"Las listas tienen la misma cantidad de vectores.\n\n")
			
			
else:
	print ("Las palabras ingresadas en las listas, no tienen el mismo tamaño, y como tal, NO son anagramas")
	exit ()

#paso 2) ordeno todo los vectores de la lista por abecedario, de esta forma, si las letras son las mismas, las listas que comparo tambien lo seran
listaletra1.sort () 
listaletra2.sort ()
if (listaletra1 == listaletra2):
	print ("Las palabras ingresadas son anagramas")
else:
	print ("No son anagramas, fin del programa")
"""
	














"""
Ejercicio 21

Dada un String y un numero, cortar el string mostrando X cantidad de caracteres dependiendo del numero enviado.

Input: (Denu, 2)
Output: De

"""

"""
cadena = input ("Ingrese una cadena de caracteres: ")

cortar = int (input ("Indique N° de caracter de donde cortara la palabra: "))

print (cadena[0:(cortar)])
"""




























"""
Ejercicio 22
Dados dos numeros indicar cual es mayor y cual es menor.

Input: (2, 5)
Output: 2 is less than 5
"""

"""
from random import *

numero1 = float (input("Ingrese el primer numero: "))

numero2 = float (input ("Ingrese el segundo numero: "))

if (numero1 == numero2):
	print ("Ambos numeros son iguales: ")
elif (numero1 > numero2):
	print (f"El numero: {numero1} es mayor que el numero: {numero2} ")
else:
	print (f"El numero: {numero2} es mayor que el numero: {numero1} ")
"""






















"""
Ejercicio 23
Dado un String poner en mayuscula la primera letra de cada palabra en la cadena y devolverla.

Input: hola soy denu lemon
Output: Hola Soy Denu Lemon
"""


"""
cadena = input ("Ingrese cadena de caracteres: ").title()
print (cadena)
"""
























"""
Ejercicio 24
Dado un array de enteros y un numero, detectar si esa lista de numeros es una permutacion del 1 al numero
 aportado.

Permutacion: Secuencia de numeros en orden sin que falte ninguno entre ellos

Input: ([1,2,3,4,5], 5)
Output: true

#la consiga es confusa, nose entiende si realmente es una permutacion matematica, o si por el contrario,
controlar una consecutividad de numeros del 1, hasta el numero que ingresa por teclado
"""

"""
from random import * #ver con ari

milista = [1,2,3,4,5,6]

milista.sort ()
print (milista)
numero = int (input ("Ingrese un numero entero de tope: "))



######## RECORRER MATRIZ POR VALOR, METODO PYTHON ###########


# ~ for contadorindice, dato in enumerate(milista):
	# ~ if dato == contadorindice+1:
		# ~ print (f"El contador vale: {contadorindice+1}  y es igual al  {dato}: {contadorindice+1 == dato}")
		
	# ~ else:
		# ~ print ("No son numeros consecutivos. Fin del programa")
		# ~ break


######## RECORRER MATRIZ CON FOR POR NUMERO DE INDEX: METODO JAVA || C ###########

# ~ contador = 1
# ~ for indice in range (len(milista)):
	# ~ if milista[indice] == contador:
		# ~ print (f"El contador vale: {contador}  y es igual al numero de la lista: {milista[indice]} : {milista[indice] == contador}")
		# ~ contador+=1
	# ~ else:
		# ~ print ("No son numeros consecutivos. Fin del programa")
		# ~ break


"""




























"""
Ejercicio 25
Dado un String, si hay mas mayusculas, pasar todo a mayuscula, y viceversa.

Input: "DENu"
Output: DENU
"""

"""
cadena = input ("Ingrese una palabra: ")

print(cadena.upper())

print(cadena.lower())
"""



















"""
Ejercicio 26
Dado un numero mostrar la serie de fibonacci y el resultado de la misma

Input: 10
Output: Serie completa: 0,1,1,2,3,5,8,13,21,34,55) Resultado: 55
"""


"""
tope = int (input ("Ingrese un numero final: "))

numero1 = 1
numero2 = 1
numero3 = 1

print ("0, 1, ", end="")

while (numero3 <= tope):
	print ((numero3), end =", ")
	numero1 = numero3
	numero3 = numero3 + numero2
	numero2= numero1
"""



print ("Hola mundo")

















"""
Ejercicio 27
Dado un numero mostrar a cuantos años, meses y dias equivale.


Input: 920
Output: 2 años, 6 meses y 2 dias
"""


dias = int (input("Ingrese cantidad de dias a calcular: "))

years = dias // 365 #la parte entera de dias, dividido 365, esto me da solo los años completos


month = (dias-(365*(dias//365)))//30 # del dias - los años completos de 365 da el sobrante de dias que no completan un año
									#esto se divide entero (sin resto) por //30 y me da los meses enteros

# ~ month = (dias-(365*(years)))//30

dias_extras = dias - ((years*365)+(month*30)) #el sobrante de los dias menos los años enteros (365) menos los meses enteros (30) da el resto de los dias que no llegan a formar un mes


print (f"La cantidad de años es de: {years}")

print (f"La cantidad de meses es de: {month}")

print (f"La cantidad de dias es de: {dias_extras}")














