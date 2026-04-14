import secrets
import string
import os
from cryptography.fernet import Fernet

# Función para solicitar y validar la longitud de la contraseña
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

# --- INICIO DEL PROGRAMA ---

# 1. Obtener la longitud deseada
leng = setleng()
print("Longitud elegida: ", leng)

# Función para generar la contraseña aleatoria segura
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

# 2. Generar la contraseña base
generatedPass = passwordGenerator(leng)

# Función para gestionar la llave de cifrado (Cargar o crear nueva)
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

# 3. Obtener la llave necesaria para el cifrado
mi_key = genkey()

# Función para cifrar el texto usando la llave Fernet
def encrypt(password, mi_key):
    padlock = Fernet(mi_key)
    # Fernet necesita los datos en formato bytes
    plaintext = password.encode('utf-8')
    ciphertext = padlock.encrypt(plaintext)
    print(f"Token cifrado generado con éxito.")
    return ciphertext

# 4. Cifrar la contraseña generada
token_final = encrypt(generatedPass, mi_key)

# Función para guardar el token cifrado en un archivo externo
def guardar_en_archivo(token):
    with open("token.txt", "wb") as f:
        f.write(token)
    print("El resultado se ha guardado en token.txt")

# 5. Ejecutar el guardado final
guardar_en_archivo(token_final)