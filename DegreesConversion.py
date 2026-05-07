#degrees conversion: The temperature xxF in degrees Celsius is (xx - 32) * 5 / 9
while True:
    degree_fahrenheit = float(input("Enter a temperature in degrees Fahrenheit: "))
    print(f"You entered: {degree_fahrenheit}F")
    degree_celsius = (degree_fahrenheit - 32) * 5 / 9
    result = round(degree_celsius, 2)
    print(f"The temperature {degree_fahrenheit}F in degrees Celsius is {result}°C")
