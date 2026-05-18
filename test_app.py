from app import sumar, restar, multiplicar, dividir

def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0

def test_restar():
    assert restar(5, 2) == 3
    assert restar(1, 5) == -4

def test_multiplicar():
    assert multiplicar(3, 4) == 12
    assert multiplicar(5, 0) == 0

def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(5, 0) == "Error: No se puede dividir por cero"