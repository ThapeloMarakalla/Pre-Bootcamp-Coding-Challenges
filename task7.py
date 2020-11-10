def celsius_to_fahrenheit(celsuis):
    """Converts celsuis to fahrenheit, and returns it.
    """
    fahrenheit = (9/5) * celsuis + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Converts fahrenheit to celsuis, and returns it.
    """
    celsuis = 5 / 9 * (fahrenheit - 32)
    return celsuis

if __name__ == "__main__":
    fahrenheit = 110
    celsuis = fahrenheit_to_celsius(fahrenheit)
    print(f'{fahrenheit} F = {celsuis:.2f} C')
    print()

    celsuis = 25
    fahrenheit = celsius_to_fahrenheit(celsuis)
    print(f'{celsuis} C = {fahrenheit} F')