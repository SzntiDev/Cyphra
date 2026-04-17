# Cyphra | High-End Digital Vault

Professional password management and security dashboard implementation.

## Overview

Cyphra is a high-performance desktop application designed for secure password generation and credential management. It bridges a robust Python-based cryptographic engine with a modern Electron frontend to provide a production-grade security experience. The project prioritizes local data sovereignty, utilizing zero-knowledge principles where encryption keys and vault data never leave the user's machine.

## Features

- **Advanced Cryptography**: Implements AES-256 bit encryption via the Fernet specification for secure data at rest.
- **Secure Generation**: Utilizes Python's `secrets` module (CSPRNG) for generating cryptographically strong passwords.
- **Emerald Vault UI**: A high-fidelity, professional dashboard built with Tailwind CSS, featuring dark mode and refined micro-interactions.
- **Dynamic Vault Management**: Real-time Master-Detail interface for organizing and retrieving credentials from local storage.
- **Security Audit Logs**: Automated activity history tracking for monitoring vault access and credential updates.
- **Data Portability**: Built-in support for importing and exporting encrypted vault structures.

## Technologies Used

- **Frontend**: Electron, Tailwind CSS, Lucide Icons.
- **Backend**: Python 3.x.
- **Security**: Cryptography (Fernet), Secrets (CSPRNG).
- **Integration**: Python-Shell (Node.js to Python bridge).

## Installation

### Prerequisites

- [Node.js](https://nodejs.org/) (Latest LTS version recommended)
- [Python 3.x](https://www.python.org/)
- [Pip](https://pip.pypa.io/en/stable/)

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/SzntiDev/Cyphra.git
   cd Cyphra
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Install Python dependencies:
   ```bash
   pip install cryptography python-shell
   ```

4. Initialize the application:
   ```bash
   npm start
   ```

## Usage Examples

### Generating a Credential
1. Navigate to the "Pass Generator" section.
2. Enter the target Service (e.g., "GitHub") and your Username.
3. Select the desired password length using the slider.
4. Click "Generar y Proteger" to encrypt and save the credential to your local vault.

### Accessing the Vault
1. Navigate to the "Vault" section.
2. Select an entry from the list to view its decrypted details.
3. Use the "Copy" icon to secure the password to your clipboard.

## Project Structure

```text
Cyphra/
├── main.js           # Electron main process and window configuration
├── index.html        # Main application entry point and UI structure
├── index.css         # Global design system and custom styling
├── renderer.js       # Frontend logic and Python bridge communication
├── generator.py      # Core security engine (Encryption & Generation)
├── script.py         # Command-line API for Electron integration
├── package.json      # Node.js project metadata and dependencies
└── .gitignore        # Security configuration to protect keys and vault data
```

## Configuration

The application operates entirely locally. Upon first run, a `key.txt` file is generated. This file contains the master decryption key and must be stored securely. Loss of this file results in the permanent loss of all vault data.

## API Documentation

The `script.py` acts as an internal API bridge:
- **Mode 1**: Generation and encryption (`[1, length, site, user]`).
- **Mode 2**: Targeted search and decryption (`[2, site]`).
- **Mode 3**: Full vault retrieval in JSON format (`[3]`).

## Roadmap

- Implement PBKDF2 Master Password authentication.
- Migrate local CSV storage to an encrypted SQLite database.
- Add biometric authentication support for Windows Hello.

## Contributing Guidelines

Contributions are welcome. Please ensure that all security logic remains concentrated in the Python backend and that no sensitive files (keys, logs, vaults) are ever staged for commit.

## License

Personal project by SzntiDev. All rights reserved.

---

# Cyphra | Bóveda Digital de Alto Nivel

Implementación profesional de gestión de contraseñas y panel de seguridad.

## Resumen

Cyphra es una aplicación de escritorio de alto rendimiento diseñada para la generación segura de contraseñas y la gestión de credenciales. Une un robusto motor criptográfico basado en Python con una interfaz moderna en Electron para proporcionar una experiencia de seguridad de grado de producción. El proyecto prioriza la soberanía de los datos locales, utilizando principios de conocimiento cero donde las llaves de cifrado y los datos de la bóveda nunca salen del equipo del usuario.

## Características

- **Criptografía Avanzada**: Implementa cifrado AES-256 bits a través de la especificación Fernet para la seguridad de datos en reposo.
- **Generación Segura**: Utiliza el módulo `secrets` de Python (CSPRNG) para generar contraseñas criptográficamente fuertes.
- **Interfaz Emerald Vault**: Un panel profesional de alta fidelidad construido con Tailwind CSS, con modo oscuro y micro-interacciones refinadas.
- **Gestión Dinámica de Bóveda**: Interfaz Maestro-Detalle en tiempo real para organizar y recuperar credenciales del almacenamiento local.
- **Registros de Auditoría**: Seguimiento automatizado del historial de actividad para monitorear el acceso a la bóveda y las actualizaciones de credenciales.
- **Portabilidad de Datos**: Soporte integrado para importar y exportar estructuras de bóveda cifradas.

## Tecnologías Utilizadas

- **Frontend**: Electron, Tailwind CSS, Lucide Icons.
- **Backend**: Python 3.x.
- **Seguridad**: Cryptography (Fernet), Secrets (CSPRNG).
- **Integración**: Python-Shell (puente de Node.js a Python).

## Instalación

### Requisitos Previos

- [Node.js](https://nodejs.org/) (Se recomienda la última versión LTS)
- [Python 3.x](https://www.python.org/)
- [Pip](https://pip.pypa.io/en/stable/)

### Instrucciones de Configuración

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/SzntiDev/Cyphra.git
   cd Cyphra
   ```

2. Instalar dependencias de Node.js:
   ```bash
   npm install
   ```

3. Instalar dependencias de Python:
   ```bash
   pip install cryptography python-shell
   ```

4. Iniciar la aplicación:
   ```bash
   npm start
   ```

## Ejemplos de Uso

### Generar una Credencial
1. Navegue a la sección "Pass Generator".
2. Ingrese el Servicio objetivo (ej. "GitHub") y su nombre de Usuario.
3. Seleccione la longitud de contraseña deseada usando el control deslizante.
4. Haga clic en "Generar y Proteger" para cifrar y guardar la credencial en su bóveda local.

### Acceder a la Bóveda
1. Navegue a la sección "Vault".
2. Seleccione una entrada de la lista para ver sus detalles descifrados.
3. Use el icono de "Copiar" para asegurar la contraseña en su portapapeles.

## Estructura del Proyecto

```text
Cyphra/
├── main.js           # Proceso principal de Electron y configuración de ventana
├── index.html        # Punto de entrada principal y estructura de la interfaz
├── index.css         # Sistema de diseño global y estilos personalizados
├── renderer.js       # Lógica de frontend y comunicación con el puente Python
├── generator.py      # Motor central de seguridad (Cifrado y Generación)
├── script.py         # API de línea de comandos para la integración con Electron
├── package.json      # Metadatos del proyecto Node.js y dependencias
└── .gitignore        # Configuración de seguridad para proteger llaves y datos
```

## Configuración

La aplicación funciona íntegramente de forma local. Al ejecutarse por primera vez, se genera un archivo `key.txt`. Este archivo contiene la llave de descifrado maestra y debe guardarse de forma segura. La pérdida de este archivo resulta en la pérdida permanente de todos los datos de la bóveda.

## Documentación de la API

El archivo `script.py` actúa como un puente de API interno:
- **Modo 1**: Generación y cifrado (`[1, longitud, sitio, usuario]`).
- **Modo 2**: Búsqueda dirigida y descifrado (`[2, sitio]`).
- **Modo 3**: Recuperación completa de la bóveda en formato JSON (`[3]`).

## Hoja de Ruta

- Implementar autenticación de contraseña maestra con PBKDF2.
- Migrar el almacenamiento CSV local a una base de datos SQLite cifrada.
- Agregar soporte de autenticación biométrica para Windows Hello.

## Guías de Contribución

Las contribuciones son bienvenidas. Por favor, asegúrese de que toda la lógica de seguridad permanezca concentrada en el backend de Python y que ningún archivo sensible (llaves, registros, bóvedas) sea incluido en los commits.

## Licencia

Proyecto personal de SzntiDev. Todos los derechos reservados.
