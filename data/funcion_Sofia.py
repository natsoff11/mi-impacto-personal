# Escribe una funcion llamada fibonacci que reciba un numero
# entero n y devuelva una lista con los primeros n terminos
# de la sucesion de Fibonacci.
# La sucesion empieza con 0 y 1: [0, 1, 1, 2, 3, 5, 8, ...]
# Incluye docstring y comentarios en espanol. 
def fibonacci(n):
    # Inicializar la lista con los primeros dos terminos
    fib = [0, 1]
    
    # Calcular los siguientes terminos
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    # Devolver los primeros n terminos
    return fib[:n]

# Explica paso a paso que hace esta funcion
# 1. Inicializa una lista con los primeros dos terminos de la sucesion de Fibonacci (0 y 1)
# 2. Usa un bucle for para calcular los siguientes terminos sumando los dos terminos anteriores
# 3. Devuelve los primeros n terminos de la lista

# añade un bloque de prueba
if __name__ == "__main__":
    print(fibonacci(10))  # Debería imprimir [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]