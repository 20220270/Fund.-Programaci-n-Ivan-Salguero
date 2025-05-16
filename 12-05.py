

#-------------------------------------------------------------------------------------#
cuenta = float(input("Introduce la cantidad de dinero a pagar: "))

propina = float(input("Introduce la propina: Formato decimal (0.1, 0.15, 0.2): "))

total_propina = cuenta * propina

total_a_pagar = cuenta + total_propina
print("La cuenta es: ", cuenta, "y total a pagar es: ", total_a_pagar)