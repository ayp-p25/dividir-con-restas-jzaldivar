"""
ANGELICA ELIZABETH IBARRA DIAZ
DIAZARTURO ARJONA HERMOSILLOA
CHRISTIAN ALONSO FLORES BURGOS
MARCO FABRIZIO AZPEITIA CASTELLANOS
10 de octubre 2025
Calcular el cociente y residuo de una división usando sólo sumas y restas
"""
#Entradas
#Se pide un número dividendo y un número divisor
dividendo = int(input("Introduzca el dividendo:"))
divisor = int(input("Introduzca el divisor"))
cociente_división=0 #Establecemos que el valor inicial del conciente de la división es cero
residuo_división = dividendo #Así establecemos que la cantidad del dividendo seconvierte en residui
# Proceso
while residuo_división >= divisor: #Con el while indicamos que esto pasará sólamente mientras
#el resiudo sea mayor o igual al divisor
 residuo_división = residuo_división - divisor # con esta lpinea se efectúa la resta
 cociente_división= cociente_división + 1 #Y si fué posible la resta, entonces el conciente aumenta una vez más
# Salidas
print("El cociente",cociente_división) #para que nos muestre el cociente
print("El residuo:", residuo_división) #Para que nos muestre el residuio

