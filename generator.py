import random
import string
from cryptography.fernet import Fernet

def setleng():
    while True:
        try:
            leng = int(input("¿De cuánto debe ser la contraseña? (8 a 32): "))

            if 8 <= leng <= 32:
                return leng
            else:
                print("Error: Debe estar entre 8 y 32.")

        except ValueError:
            print("Error: Debes introducir un número entero válido.")

leng = setleng()

print("Longitud elegida: ",leng)
def passwordGenerator(leng):
    contra = []
    for l in range(leng):
        digit = random.choice(string.ascii_letters + string.digits + string.punctuation + " ")
        
        contra.append(digit)
    password = "".join(contra)
    sino = input("Desea mostrar la contraseña? (y/n)")
    
    if sino == "y" or sino == "n":
        
        if sino == "y":

            print("La contraseña es: " + password)

    else:
        print("Contraseña oculta")
    return password

generatedPass = passwordGenerator(leng)
