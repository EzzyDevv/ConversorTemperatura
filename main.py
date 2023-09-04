import formulas


print("-=-" * 10)
print("|  CONVERSOR DE TEMPERATURA  |")
print("-=-" * 10)

value = float(input("Digite a temperatura : "))
print("Insira a unidade de medida de temperatura abaixo.")
answer = int(input("""[1] Celsius
[2] Fahrenheit
[3] Kelvin\n>>> """))

if answer == 1:
    print("Deseja converter para qual outra unidade de medida ?")
    c = int(input("""[1] Fahrenheit
[2] Kelvin\n>>> """))
    if c == 1:
        temperatura_fahrenheit = formulas.Celsius_para_Fahrenheit(value)
        print(f"Celsius : {value:.2f}°C | Fahrenheit : {temperatura_fahrenheit:.2f}°F")
    if c == 2:
        temperatura_kelvin = formulas.Celsius_para_Kelvin(value)
        print(f"Celsius : {value:.2f}°C | Kelvin : {temperatura_kelvin:.2f}°K")
elif answer == 2:
    print("Deseja converter para qual outra unidade de medida ?")
    c = int(input("""[1] Celsius
[2] Kelvin\n>>> """))
    if c == 1:
        temperatura_celsius = formulas.Fahrenheit_para_Celsius(value)
        print(f"Fahrenheit : {value}°F | Celsius : {temperatura_celsius:.2f}°C")
    if c == 2:
        temperatura_kelvin = formulas.Fahrenheit_para_Kelvin(value)
        print(f"Fahrenheit : {value}°F | Kelvin : {temperatura_kelvin:.2f}°K")
elif answer == 3:
    print("Deseja converter para qual outra unidade de medida ?")
    c = int(input("""[1] Celsius
[2] Fahrenheit\n>>> """))
    if c == 1:
        temperatura_celsius = formulas.Kelvin_para_celsius(value)
        print(f"Kelvin : {value:.2f}°K | Celsius : {temperatura_celsius:.2f}°C")
    if c == 2:
        temperatura_kelvin = formulas.Kelvin_para_fahrenheit(value)
        print(f"Kelvin : {value:.2f}°K | Fahrenheit : {temperatura_kelvin:.2f}°F")
else:
    print("Insira uma alternativa correspondente!")