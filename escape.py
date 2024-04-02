r = float(input("Ingrese el radio en Kilómetros: "))
g = float(input("Ingrese la constante g: "))

ve = (2 * g * r * 1000) ** (1 / 2)

print(f"La velocidad de Escape es {round(ve, 1)}")
