from calculadora import suma

def test_suma_positivo():
    assert suma(3, 4) == 7
    
def test_suma_negativos():
    assert suma(-2, -3) == -5
    
def test_suma_positivo_negativo():
    assert suma(10, -3) == 7    