# Valor por hora normal y por hora extra (ejemplo)
valor_hora_normal = 10000
valor_hora_extra = 15000

# Solicitar al usuario que ingrese el número de horas extras trabajadas
horas_extras = int(input("Ingresa el número de horas extras trabajadas: "))

# Calcular el pago por horas extras
pago_horas_extras = horas_extras * valor_hora_extra

# Mostrar el resultado
print(f"El pago por {horas_extras} horas extras trabajadas es: ${pago_horas_extras}")