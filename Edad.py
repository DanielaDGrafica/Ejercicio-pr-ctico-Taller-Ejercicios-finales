edad = int(input("Por favor, ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
elif 16 <= edad < 18:
    print("Eres menor de edad.")
elif 6 <= edad < 16:
    print("Eres un joven o una joven.")
else:
    print("Eres un niño o una niña.")

