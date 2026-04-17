import sys
import generator 
import json

# 1 = Generar, 2 = Buscar, 3 = Listar Todo
modo = sys.argv[1]

# Necesitamos la llave para cualquier operación
mi_key = generator.genkey()

if modo == "1":
    # Electron nos enviará: [modo, longitud, sitio, usuario]
    leng = int(sys.argv[2])
    sitio = sys.argv[3]
    user = sys.argv[4]
    
    # Ejecutamos las herramientas en orden
    password = generator.passwordGenerator(leng)
    token = generator.encrypt(password, mi_key)
    
    generator.guardar_en_archivo(sitio, user, token)
    
    # Esto es lo que Electron recibirá y mostrará en pantalla
    print(password) # Primero la contraseña para mostrarla en el resultado
    print(f"ÉXITO: Contraseña para {sitio} guardada correctamente.")

elif modo == "2":
    # Electron nos enviará: [modo, sitio_a_buscar]
    sitio = sys.argv[2]
    generator.ver_contraseñas(sitio, mi_key)

elif modo == "3":
    # Modo para obtener TODO el listado en formato JSON
    datos = generator.ver_todo(mi_key)
    print(json.dumps(datos))