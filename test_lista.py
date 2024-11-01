from lista import elementos_lista

def test_elementos_lista():
    assert elementos_lista(["lobo","conejo","cerdo","huron","ardilla"]) == 5
    assert elementos_lista(["lobo","conejo","cerdo","huron","ardilla","pollo","perro","zorro"]) == 8
    assert elementos_lista(["lobo","conejo","cerdo","huron","ardilla","pollo","perro","zorro","gato"]) == 10
    assert elementos_lista(["lobo","conejo","cerdo","huron","ardilla","pollo","perro","zorro","gato","cisne"]) == 15