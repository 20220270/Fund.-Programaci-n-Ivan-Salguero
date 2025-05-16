contrasena = input("Introduce la contraseña: ")
 # Si es menor a 8 caracteres, no es valida
if len(contrasena) < 8 :
    print("La contraseña no es válida")
    # Si no tiene al menos una mayúscula, no es válida
elif not any(c.isupper() for c in contrasena): # Recorre todos los caracteres de la contraseña para ver si hay una mayuscula
    print("La contraseña no es válida")
    # Si no tiene al menos un número, no es válida
elif not any(c.isdigit() for c in contrasena): # Recorre todos los caracteres de la contraseña para ver si hay un numero
    print("La contraseña no es válida")
    # Si no tiene al menos un carácter especial, no es válida
else:
    print("La contraseña es válida")


#-------------------------------------------------------------------------------------#

# Calcular el impuesto a pagar por el consumo de energia

u_consumidas = int(input("Introduce el número de unidades consumidas: "))

if u_consumidas >= 0 and u_consumidas <= 100:
    impuesto = 0
    print("El impuesto a pagar es: ", impuesto)
elif u_consumidas > 100 and u_consumidas <= 200:
    impuesto = 0.5 * u_consumidas
    print("El impuesto a pagar es: ", impuesto)
elif( u_consumidas > 200):
    impuesto = 0.7 *u_consumidas
    print("El impuesto a pagar es: ", impuesto)
else:
    print("El número de unidades consumidas no es válido")
    impuesto = 0
#-------------------------------------------------------------------------------------#

# Programa para saber si un numero es magico o no
# Para que sea maguico es numero debe ser divisible entre 7 pero no entre 5

numero = int(input("Introduce un numero: "))
if numero % 7 == 0 and numero % 5 != 0:
    print("El numero es magico")
else:
    print("El numero no es magico")