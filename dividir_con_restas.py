"""
Alumnos:
Leonardo Jesús Álvarez Fernández
Bruce de Bary Hernández Robles
José María Meléndrez Varela
Akemi Clarissa Olvera Arao
Fecha:10/10/25
Calcular el cociente y residuo de una división usando sólo sumas y
restas
"""
dividendo = float(input("Ingrese un dividendo: "))
divisor = float(input("Ingrese un divisor: "))
cociente = 0
residuo = 0
f2 = 0
f1 = 0
if divisor < 0:
 divisor = abs(divisor)
 f2 = 1
if dividendo < 0:
 dividendo = abs(dividendo)
 f1 = 1
while dividendo >= divisor:
 dividendo -= divisor
 cociente +=1
if dividendo == divisor:
 cociente +=1
 residuo = 0
if f2 == 0 and f1 == 1 or f2 == 1 and f1 == 0:
 cociente = -cociente
residuo = dividendo
print("El cociente es: ",cociente)
print("El residuo es: ",residuo)
