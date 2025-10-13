import pytest 
from conversor import *

# Eu também poderia ter escrito from conversor import + o nome de todas as funções. Mas como eu usaria todas as funções do módulo mesmo, apenas usei *.


def test_celsius_para_fahrenheit():
    """Testa a conversão de uma temperatura positiva de Celsius para Fahrenheit."""
    celsius = 40
    resultado = celsius_para_fahrenheit(celsius)
    assert resultado == 104

def test_fahrenheit_para_celsius():
    """Testa a conversão de uma temperatura quente de Fahrenheit para Celsius."""
    fahrenheit = 104
    resultado = fahrenheit_para_celsius(fahrenheit)
    assert resultado == 40

def test_celsius_para_kelvin():
    """Testa a conversão de uma temperatura de Celsius para Kelvin."""
    celsius = 40
    resultado = celsius_para_kelvin(celsius)
    assert resultado == 313.15

def test_kelvin_para_celsius():
    """Testa a conversão de uma temperatura de Kelvin para Celsius."""
    kelvin = 313.15
    resultado = kelvin_para_celsius(kelvin)
    assert resultado == pytest.approx(40)

def test_kelvin_para_celsius_com_valor_negativo():
    """
    Testa se a função kelvin_para_celsius levanta um ValueError
    quando recebe uma temperatura Kelvin negativa.
    """
    with pytest.raises(ValueError):
        kelvin_para_celsius(-10)

