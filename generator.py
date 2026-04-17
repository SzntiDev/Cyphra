import secrets
import string
import os
from cryptography.fernet import Fernet
import csv

# Función para solicitar y validar la longitud de la contraseña
flag = True
opc = 0
def passwordGenerator(leng):
                contra = []
                # Definimos los caracteres posibles (letras, números, símbolos y espacio)
                caracteres = string.ascii_letters + string.digits + string.punctuation + " "
                
                for l in range(leng):
                    # Usamos secrets para una aleatoriedad segura (CSPRNG)
                    digit = secrets.choice(caracteres)
                    contra.append(digit)
                
                password = "".join(contra)
                
                # Opción para visualizar lo que se generó
                sino = input("¿Desea mostrar la contraseña? (y/n)").lower()
                if sino == "y":
                    print("La contraseña es: " + password)
                else:
                    print("Contraseña oculta.")
                    
                return password
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
def genkey():
        # Si ya existe la llave, la leemos para poder descifrar después
        if os.path.exists("key.txt"):
            with open("key.txt", "rb") as archivo:
                mi_key = archivo.read()
        else:
            # Si no existe, creamos una llave única y la guardamos en un archivo
            mi_key = Fernet.generate_key()
            with open("key.txt", "wb") as archivo:
                archivo.write(mi_key)
        return mi_key
def guardar_en_archivo(servicio, usuario, token_final):
        with open("token.txt", "wb") as f:
            f.write(token_final)
        with open("vault.csv", "a", newline='') as archivo:  ### newline='' evita que se creen filas vacías
            escritor = csv.writer(archivo)
            escritor.writerow([servicio, usuario, token_final.decode()])
        print("El resultado se ha guardado en vault.csv")
def encrypt(password, mi_key):
        padlock = Fernet(mi_key)
        # Fernet necesita los datos en formato bytes
        plaintext = password.encode('utf-8')
        ciphertext = padlock.encrypt(plaintext)
        print(f"Token cifrado generado con éxito.")
        return ciphertext
def ver_contraseñas():
                with open("vault.csv", "r") as archivo:
                    lector = csv.reader(archivo)
                    for fila in lector:
                        if fila[0].lower() == servicio_a_buscar:
                            token_en_bytes = fila[2].encode()

                            padlock = Fernet(mi_key)
                            passwordRecuperada = padlock.decrypt(token_en_bytes).decode()
                            print(f"El servicio es: {fila[0]}")
                            print(f"El usuario es: {fila[1]}")
                            print(f"La contraseña es: {passwordRecuperada}")
menu = """
1. Generar contraseña
2. Ver contraseñas
3. Salir
"""
mi_key = genkey()
while flag: 
    print(menu)
    try:
        opc = int(input("Selecciona una opción: "))
    except ValueError:
        print("Error: Debes introducir un número entero válido.")
        continue
    match opc:
        case 1:     
            leng = setleng()
            print("Longitud elegida: ", leng)
            servicio = input("¿Para qué sitio/app es esta contraseña? (ej: Instagram): ")
            usuario = input("Introduce el nombre de usuario o email: ")
            generatedPass = passwordGenerator(leng)
            token_final = encrypt(generatedPass, mi_key)

            guardar_en_archivo(servicio, usuario, token_final)
        case 2:
            servicio_a_buscar =(input("¿Qué servicio quieres buscar? ")).lower()              
            ver_contraseñas()                    
        case 3:
            flag = False
            print("Adiós")