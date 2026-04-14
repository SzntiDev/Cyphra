import flet as ft
def main(page: ft.Page):
    # 1. Configuración de la ventana (El lienzo)
    page.title = "Aprendiendo Flet - Paso 1"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    # 2. Definición de controles (Los objetos)
    # Guardamos los controles en variables para poder usarlos luego
    titulo = ft.Text("Mi Primer Generador", size=30, weight="bold")
    
    caja_longitud = ft.TextField(
        label="Escribe un número", 
        width=200, 
        text_align="center"
    )
    
    texto_resultado = ft.Text(size=18, color="blueaccent")
    # 3. La Función del Evento (¿Qué pasa cuando aprieto el botón?)
    def al_hacer_clic(e):
        # Leemos el valor de la caja de texto
        valor = caja_longitud.value
        
        # Validamos y cambiamos otro control
        if valor:
            texto_resultado.value = f"Has elegido una longitud de: {valor}"
        else:
            texto_resultado.value = "¡Por favor, escribe algo primero!"
        
        # ¡MUY IMPORTANTE! Siempre hay que actualizar la página para ver los cambios
        page.update()
    # 4. El Botón (Con el fix para tu versión)
    # En lugar de 'text', usamos 'content' que es más flexible
    boton_generar = ft.ElevatedButton(
        content=ft.Text("Procesar Datos"), 
        on_click=al_hacer_clic # Aquí conectamos el botón con la función de arriba
    )
    # 5. Dibujar en pantalla
    page.add(
        titulo,
        caja_longitud,
        boton_generar,
        texto_resultado
    )
ft.app(target=main)