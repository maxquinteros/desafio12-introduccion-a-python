print('Bienvenido al programa "emprendedor2" \n*Ingrese solamente números, los separadores decimales se escriben con el "."')

p_normal = float(input("Ingrese el precio de suscripción normal: "))
p_premium = 1.5 * p_normal
u_normal = float(input("Ingrese el número de usuarios normales: "))
u_premium = float(input("Ingrese el número de usuarios premium: "))
gt = float(input("Ingrese el gasto total: "))

utilidades = p_normal * u_normal + p_premium * u_premium - gt

print(f"Sus utilidades son {round(utilidades, 2)}")