print('Bienvenido al programa "emprendedor3" \n*Ingrese solamente números, los separadores decimales se escriben con el "."')

p = float(input("Ingrese el precio de suscripción: "))
u = float(input("Ingrese el número de usuarios: "))
gt = float(input("Ingrese el gasto total: "))

utilidades_actual = p * u - gt

print(f"Sus utilidades son {round(utilidades_actual,2)}")

utilidades_anterior = float(input("Ingrese las utilidades del año anterior: "))

print(f"La razón entre las utilidades actuales y las del año anterior son: {round(utilidades_actual/utilidades_anterior, 2)}")