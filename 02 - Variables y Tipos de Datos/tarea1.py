#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

from xml.etree.ElementTree import PI


a= 356
print(a)


#2) Imprimir el tipo de dato de la constante 8.5

print(type(8.5))

#3) Imprimir el tipo de dato de la variable creada en el punto 1

print(type (a))

#4) Crear una variable que contenga tu nombre

mi_nombe = "Marcelo"

print(mi_nombe)

#5) Crear una variable que contenga un número complejo

complejo = 65j

#6) Mostrar el tipo de dato de la variable crada en el punto 5

print(type(complejo))   

#7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

Pi = 3.1421
print(Pi)



#8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?


var1= True
var2=False

#9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

print('la variable 1 es ', type(var1), 'la variable 2 tambien es', type(var2))

#10) Asignar a una variable, la suma de un número entero y otro decimal

var_suma = 36 + 45.78
print (var_suma)

#11) Realizar una operación de suma de números complejos

b= 3 + 45j
d= 21j

print(b + d)

#12) Realizar una operación de suma de un número real y otro complejo

j= 25 + 21j

print(j)
#13) Realizar una operación de multiplicación

f = 5
g = 9
print ( f * g)
#14) Mostrar el resultado de elevar 2 a la octava potencia

print( 2**8)

#15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

m= 27/4
print (m)

#16) De la división anterior solamente mostrar la parte entera

m= 27//4
print (m)

#17) De la división de 27 entre 4 mostrar solamente el resto

m= 27%4
print (m)

#18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

print(6 * 4 + 3) 
#19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

var3= 'hola '
var4= 'mundo'

print(var3 + var4)

#20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

print(2 == '2')

#21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

print(2 == int('2'))
#22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

#a = float('3,8')

#23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido


var5= 3 
var5 -= 1
print(var5)

a = -3
a -= 1
print(a)
#24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

print(1<<2) 

#25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

#print (2+'2')

print(float(2) + float('2'))

print(int(2) + int('2'))

print(str(2) + str('2'))
#26) Realizar una operación válida entre valores de tipo entero y string """

var1 = 'este texto se repite '
var2 = 3
print(var1 * var2 + str(var2) + ' veces'