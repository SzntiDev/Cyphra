# Cyphra

Cyphra is a secure, lightweight password generator and vault utility written in Python. It provides cryptographically secure password generation paired with a robust encryption layer to keep your sensitive data safe.

## Features

- **Secure Generation**: Uses Python's `secrets` module (CSPRNG) for high-entropy password generation.
- **Customizable Length**: Tailor your passwords from 8 to 32 characters.
- **Persistent Encryption**: Automatically encrypts generated passwords using the Fernet (symmetric) algorithm.
- **Key Management**: Generates and manages a persistent `key.txt` to ensure you can decrypt your tokens later.
- **Privacy First**: Optional password masking during the generation process.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SzntiDev/Cyphra.git
   cd Cyphra
   ```

2. **Install dependencies**:
   Cyphra requires the `cryptography` library for its encryption features.
   ```bash
   pip install cryptography
   ```

## Usage

Run the script and follow the on-screen prompts:

```bash
python generator.py
```

- **Step 1**: Choose a length (8-32).
- **Step 2**: Decide if you want to see the password on screen.
- **Step 3**: The encrypted token will be saved to `token.txt`.
- **Step 4**: Your unique encryption key is stored in `key.txt` (keep this safe!).

## Security Warning ⚠️

- **Never share your `key.txt`**: This file is needed to decrypt any tokens stored in `token.txt`. If lost, your passwords cannot be recovered.
- **Avoid public repositories**: Do not commit your `key.txt` or `token.txt` to version control.

---

# Cyphra (Español)

Cyphra es un generador de contraseñas seguro y ligero escrito en Python. Proporciona una generación de contraseñas criptográficamente seguras junto con una capa de cifrado robusta para mantener tus datos a salvo.

## Características

- **Generación Segura**: Utiliza el módulo `secrets` de Python para una generación de alta entropía.
- **Longitud Personalizable**: Ajusta tus contraseñas entre 8 y 32 caracteres.
- **Cifrado Persistente**: Cifra automáticamente las contraseñas generadas usando el algoritmo Fernet (simétrico).
- **Gestión de Llaves**: Genera y administra un archivo `key.txt` persistente para asegurar que puedas descifrar tus tokens.
- **Privacidad Ante Todo**: Opción de ocultar la contraseña durante el proceso de generación.

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/SzntiDev/Cyphra.git
   cd Cyphra
   ```

2. **Instalar dependencias**:
   Cyphra requiere la librería `cryptography`.
   ```bash
   pip install cryptography
   ```

## Uso

Ejecuta el script y sigue las instrucciones:

```bash
python generator.py
```

- **Paso 1**: Elige la longitud (8-32).
- **Paso 2**: Decide si quieres visualizar la contraseña.
- **Paso 3**: El token cifrado se guardará en `token.txt`.
- **Paso 4**: Tu llave única se guarda en `key.txt` (¡protégela!).

## Advertencia de Seguridad ⚠️

- **Nunca compartas tu `key.txt`**: Este archivo es necesario para descifrar los tokens. Si se pierde, no podrás recuperar tus contraseñas.
- **Evita repositorios públicos**: No subas tus archivos `key.txt` o `token.txt` a sistemas de control de versiones.
