# Primer ejercicio:
key = "Contraseña"
password = input ("Ingrese la contraseña: ")
if key == password.lower():
    print ("La contraseña coincide")
else:
    print ("La contraseña no coincide")


# Segundo ejercicio:

nombre = input ("¿Cómo te llamas? ")
genero = input ("¿Cuál es tu sexo (M o H)? ")
if genero == "M":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"
print ("Tu grupo es " + grupo)