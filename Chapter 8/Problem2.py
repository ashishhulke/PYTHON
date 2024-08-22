# 2. Write a python program using function to convert Celsius to Fahrenheit.

def convert(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = convert(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F.")