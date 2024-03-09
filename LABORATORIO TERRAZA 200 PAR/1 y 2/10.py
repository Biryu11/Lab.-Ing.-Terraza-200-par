def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fibonacci_series = [0, 1]
    
    while len(fibonacci_series) < n:
        next_term = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_term)
    
    return fibonacci_series

numero = int(input("Ingresa el valor de n: "))
fibonacci_numero = fibonacci(numero)
print("La serie de Fibonacci hasta el término", numero, "es:", fibonacci_numero)
