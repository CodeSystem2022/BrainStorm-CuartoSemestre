#Profundizamos en el tipo float

a = 3.0
print(f"El valor de a es: {a:.2f}")

#Constructor de tipo float -> puede recibir un valor entero o un valor de tipo string

b = float(10) # Le pasamos un valor entero
c= float("10") # Le pasamos un valor de tipo string
print(f"El valor de b es: {b:.2f}")
print(f"El valor de c es: {c:.2f}")

#Notacion exponencial (valores positivos y negativos)
a = 3e5
print(f'a: {a:.2f}')

b = 3e-5
print(f'b: {b:.2f}')

#Cualquier calculo que incluye un float, todo cambia a float
a = 3.0 + 2
print(f'a: {a:.2f}')
print(f'El tipo de a es: {type(a)}')
