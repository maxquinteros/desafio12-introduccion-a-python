print('Bienvenido al programa "emprendedor1" \n*Ingrese solamente números, los separadores decimales se escriben con el "."')

p = float(input("Ingrese el precio de suscripción: "))
u = float(input("Ingrese el número de usuarios: "))
gt = float(input("Ingrese el gasto total: "))

utilidades = p * u - gt

print(f"Sus utilidades son {round(utilidades, 2)}")