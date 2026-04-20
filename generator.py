import secrets
import string
import os
from cryptography.fernet import Fernet
import csv
import datetime

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
    yaGuardado = [] 
    
    actualizado = False 
    # ^^^ Un "interruptor". Empieza apagado (False) porque al principio asumimos que NO hemos encontrado aún ninguna cuenta repetida. Sirve para avisarnos si pisamos un duplicado o si es cuenta nueva.
    with open("token.txt", "wb") as f:
        f.write(token_final)
    # ^^^ Abre (o crea) 'token.txt' en modo escritura de Bytes ('wb'). Sobrescribe lo viejo y le graba el último token.
    
    if os.path.exists("vault.csv"):
    # ^^^ PREGUNTA INICIAL: ¿Ya existe el archivo maestro 'vault.csv' en esta compu? 
    # Validamos esto porque intentar ordenarle a Python leer un archivo que no existe tiraría un "Error 404".
        
        with open("vault.csv", "r", newline='') as archivo_lectura:
        # ^^^ Si existe, lo abrimos en modo lectura ('r'). 
            
            lector = csv.reader(archivo_lectura)
            # ^^^ Preparamos la herramienta mágica capaz de leer formato de Excel/CSV separando las columnas correctamente.
            
            for fila in lector:
            # ^^^ Entramos al bucle: "Por cada una de las líneas leídas en el documento, vamos a hacer lo siguiente..."
                
                if len(fila) < 3: 
                    continue
                # ^^^ 'Seguro anti-crasheos'. A veces al final de los archivos quedan líneas en blanco o "basura". Si la fila de turno tiene menos de 3 columnas (Servicio, Usr y Token), la saltamos (con 'continue').
                
                if fila[0].lower() == servicio.lower() and fila[1].lower() == usuario.lower():
                # ^^^ AQUÍ PASA LA MAGIA ANTI-DUPLICADOS. Comparamos la columna 0 y 1 del Excel actual, contra el servicio y usuario que nos pasó Electron. 
                # .lower() pasa todo temporalmente a letras minúsculas para que "Instagram" e "instagram" sean tomados como el mismo.
                    
                    fila[2] = token_final.decode()
                    # ^^^ ¡Premio, encontramos repetido! Sobreescribimos la columna 2 de ESA fila (donde va el token viejo) y lo cambiamos por el nuevo token convertido a texto simple con .decode().
                    
                    actualizado = True
                    # ^^^ "Encendemos el interruptor" avisando: ("¡Ojo, sí encontré un duplicado y lo pisé! No lo agregues de vuelta").
                yaGuardado.append(fila)
                # ^^^ Finalmente, guardamos la fila completa en la lista en memoria `yaGuardado`. 
                # (Esa fila que agregamos ya es la versión modificada si había match repetido, ¡o la versión sin cambios si no importaba!).
        # ----- FIN DE LA LECTURA R (Aquí cierra automáticamente tras leer todo el Excel) -----
        
        if not actualizado:
        # ^^^ Una vez revisamos todo, miramos nuestro interruptor: ¿Siguió apagado (not actualizado)? 
        # Si la respuesta es sí, es porque ese usuario/servicio era totalmente nuevo y virgen.
            
            yaGuardado.append([servicio, usuario, token_final.decode()])
            # ^^^ Como es nuevo, simplemente empujamos al final de la lista los 3 datos limpios juntos en una fila fresca.
        with open("vault.csv", "w", newline='') as archivo_escritura:
        # ^^^ Ahora ABRIMOS DE NUEVO EL EXCEL en modo escritura total y destructiva ('w'). 
        # Esto significa que borrará por completo lo que el archivo tenía adentró al instante.
            
            escritor = csv.writer(archivo_escritura)
            escritor.writerows(yaGuardado)
            # ^^^ Usando 'writerows' en plural, incrustamos toda nuestra super lista guardada en la RAM (`yaGuardado`) devuelta al CSV al instante. Lo hemos salvado limpiamente sin duplicados.
    else:
    # ^^^ "PLAN B". Esto solo entra si el 'vault.csv' sencillamente NO existía inicialmente en la compu.
        
        with open("vault.csv", "w", newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([servicio, usuario, token_final.decode()])
        # ^^^ Creamos e inauguramos el nuevo 'vault.csv' grabando la primera fila la historia y listo.
            
    print("El resultado se ha guardado en vault.csv")
    # ^^ Recordatorio: Este print() ensucia la llegada a Electron JavaScript, capaz lo vas a querer borrar para curar el 'bug' visual ;)
def encrypt(password, mi_key):
        padlock = Fernet(mi_key)
        # Fernet necesita los datos en formato bytes
        plaintext = password.encode('utf-8')
        ciphertext = padlock.encrypt(plaintext)
        print(f"Token cifrado generado con éxito.")
        return ciphertext
def ver_contraseñas(servicio_a_buscar, mi_key):
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
def ver_todo(mi_key):
    lista_completa = []
    if os.path.exists("vault.csv"):
        with open("vault.csv", "r") as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                if len(fila) < 3: continue
                try:
                    token_en_bytes = fila[2].encode()
                    padlock = Fernet(mi_key)
                    decrypted = padlock.decrypt(token_en_bytes).decode()
                    lista_completa.append({
                        "servicio": fila[0],
                        "usuario": fila[1],
                        "password": decrypted
                    })
                except Exception:
                    continue
    return lista_completa
def registrar_evento (titulo, descripcion, tipo="SECURE"):
    fecha_hora = datetime.datetime.now().strftime ("%b %d, %Y • %I:%M %p").upper()
    with open("events.csv", "a", newline='', encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([titulo, descripcion, tipo, fecha_hora])
def ver_eventos():
    lista_eventos = []
    if os.path.exists("events.csv"):
        with open("events.csv", "r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                if len(fila) < 4: continue
                lista_eventos.append({
                    "titulo": fila[0],
                    "descripcion": fila[1],
                    "tipo": fila[2],
                    "fecha": fila[3]
                })
    return lista_eventos
menu = """
1. Generar contraseña
2. Ver contraseñas
3. Salir
"""
mi_key = genkey()
if __name__ == "__main__":
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
                ver_contraseñas(servicio_a_buscar, mi_key)                    
            case 3:
                flag = False
                print("Adiós")