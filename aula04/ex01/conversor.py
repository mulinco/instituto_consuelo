def celsius_para_fahrenheit(celsius):
    """Essa função nos retorna o valor convertido de celsius para fahrenheit de acordo com o valor do parâmetro"""
    return celsius * 1.8 + 32   

def fahrenheit_para_celsius(fahrenheit):
    """Essa função nos retorna o valor convertido de fahrenheit para celsius de acordo com o valor do parâmetro"""
    return (((fahrenheit - 32) / 9) * 5)   

def celsius_para_kelvin(celsius):
    """Converte uma temperatura de Celsius para Kelvin."""
    return celsius + 273.15

def kelvin_para_celsius(kelvin):
    """Converte uma temperatura de Kelvin para Celsius."""
    if kelvin < 0:
        raise ValueError("A temperatura em Kelvin não pode ser negativa.")
    return kelvin - 273.15



