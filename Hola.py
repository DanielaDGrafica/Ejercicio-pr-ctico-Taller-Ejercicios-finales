def saludar(nombre):
    print("¡Hola, " + nombre + "! ¿Cómo estás?")
saludar("Daniela")

def saludar_p(nombre, saludo="Hello"):
    print(f"{saludo}, {nombre}!")

saludar_p("Mafe")
saludar_p("Juan Gi", saludo="¡Saludos")
saludar_p(f"James")
saludar_p("Pepe",saludo="¡Hi!")
