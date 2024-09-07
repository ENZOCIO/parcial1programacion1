
from models.cliente import Cliente
from models.vidrio import Vidrio
from models.acabado import Acabado
from models.nave import Nave
from models.ventana import Ventana
from models.cotizacion import Cotizacion
from main import seleccionar_vidrio, seleccionar_acabado, seleccionar_tipo_ventana, crear_cliente, crear_ventana, crear_nave

def test_seleccionar_vidrio(monkeypatch):
    inputs = iter(['1'])  # Mocking user input
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    vidrio = seleccionar_vidrio()
    assert vidrio.nombre == "Transparente"
    assert vidrio.precio == 8.25

def test_seleccionar_acabado(monkeypatch):
    inputs = iter(['2'])  # Mocking user input
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    acabado = seleccionar_acabado()
    assert acabado.nombre == "Lacado Brillante"
    assert acabado.precio == 54.2

def test_seleccionar_tipo_ventana(monkeypatch):
    inputs = iter(['O'])  # Mocking user input
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    tipo = seleccionar_tipo_ventana()
    assert tipo == 'O'

def test_crear_cliente(monkeypatch):
    inputs = iter(['Juan Pérez', 'Constructora ABC', 'Calle Falsa 123'])  # Mocking user input
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    cliente = crear_cliente()
    assert cliente.nombre == 'Juan Pérez'
    assert cliente.tipo == 'Constructora ABC'
    assert cliente.direccion == 'Calle Falsa 123'

def test_crear_ventana():
    vidrio = Vidrio('Transparente', 8.25)
    acabado = Acabado('Pulido', 50.7)
    nave = Nave('O', 50, 150, vidrio, acabado, False)
    ventana = crear_ventana('O', 120, 150, [nave])
    assert ventana.tipo == 'O'
    assert ventana.ancho == 120
    assert ventana.alto == 150
    assert len(ventana.naves) == 1

def test_crear_nave():
    vidrio = Vidrio('Transparente', 8.25)
    acabado = Acabado('Pulido', 50.7)
    nave = crear_nave('O', 50, 150, vidrio, acabado, False)
    assert nave.tipo == 'O'
    assert nave.vidrio.nombre == 'Transparente'
    assert nave.acabado.nombre == 'Pulido'
    assert not nave.esmerilado

# Para correr las pruebas, ejecuta `pytest` en la línea de comandos
