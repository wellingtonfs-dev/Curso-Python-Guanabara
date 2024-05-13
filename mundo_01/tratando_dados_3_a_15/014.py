#14. Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

temperatura_celsius = float(input('Digite a temperatura em Celsius: '))
temperatura_fahrenheit = (temperatura_celsius * 1.8) + 32
print(f'A temperatura de {temperatura_celsius}ºC corresponde a {temperatura_fahrenheit}ºF')