def Celsius_para_Fahrenheit(temperatura_celsius):
    temp_fahrenheit = temperatura_celsius * 9 / 5 + 32
    return temp_fahrenheit


def Celsius_para_Kelvin(temperatura_celsius):
    temperatura_kelvin = temperatura_celsius + 273.15
    return temperatura_kelvin


def Fahrenheit_para_Celsius(temperatura_fahrenheit):
    temperatura_celsius = (temperatura_fahrenheit - 32) * 5 / 9
    return temperatura_celsius


def Fahrenheit_para_Kelvin(temperatura_fahrenheit):
    temperatura_kelvin = (temperatura_fahrenheit - 32) * 5 / 9 + 273.15
    return temperatura_kelvin


def Kelvin_para_celsius(temperatura_kelvin):
    temperatura_celsius = temperatura_kelvin - 273.15
    return temperatura_celsius


def Kelvin_para_fahrenheit(temperaruta_kelvin):
    temperaruta_fahrenheit = (temperaruta_kelvin - 273.15) * 9 / 5 + 32
    return temperaruta_fahrenheit