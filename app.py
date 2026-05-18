def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

if __name__ == "__main__":
    print("--- Probando Calculadora ---")
    print(f"Suma: 5 + 3 = {sumar(5, 3)}")
    print(f"Resta: 10 - 4 = {restar(10, 4)}")