

# Bool contiene los valores de True y false
# Los tipos numéricos es false para el 0 (cero), true para los demás valores
valor = 0
resultado = bool(valor)
print(f'valor: {valor}, restultado: {resultado}')

valor = 0.1
resultado = bool(valor)
print(f'valor: {valor}, restultado: {resultado}')

# Tipo string -> False '', True demás valores
valor = ''
resultado = bool(valor)
print(f'valor: {valor}, restultado: {resultado}')

valor = 'Hola'
resultado = bool(valor)
print(f'valor: {valor}, restultado: {resultado}')

# Tipo colecciones --> False para colecciones vacias
# Tipo colecciones --> True para todas las demás
# Lista
valor = []
resultado = bool(valor)
print(f'valor de una lista vacia: {valor }, restultado: {resultado}')

valor = [2, 3, 4]
resultado = bool(valor)
print(f'valor de un alista llena: {valor}, restultado: {resultado}')

# Tupla
valor = ()
resultado = bool(valor)
print(f'valor de una tupla vacia: {valor}, restultado: {resultado}')

valor = (5,)
resultado = bool(valor)
print(f'valor de una tupla llena: {valor}, restultado: {resultado}')

# Diccionario
valor = {}
resultado = bool(valor)
print(f'valor de un diccionario vacio: {valor}, restultado: {resultado}')

valor = {'Nombre': 'Juan', 'Apellido': 'Perez'}
resultado = bool(valor)
print(f'valor de un diccionario lleno: {valor}, restultado: {resultado}')

# Sentencias de control con bool
if (1,):
    print('Regresa verdadero')
else:
    print('Regresa falso')

#Ciclos
variable = 17
while variable:
    print('Regresa verdadero')
    break
else:
    print('Regresa falso')
