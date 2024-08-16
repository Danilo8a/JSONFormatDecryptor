import cryptography.fernet as fernet
import json
import datetime
import re
import os


def generate_password_txt():
    password = str(fernet.Fernet.generate_key())
    file_name = str(datetime.datetime.now())
    pattern = r"[-\s:.]"
    file_name = re.sub(pattern, "_", file_name) + "_password.txt"
    with open(file_name, "w") as archivo:
        archivo.write(password)


class JSONFormatDecryptor:
    my_decryptor = None
    my_password = None
    last_json_decrypted = {}
    last_json_encrypted = {}

    def __init__(self, my_password):
        self.my_password = my_password
        self.my_decryptor = fernet.Fernet(self.my_password)

    # Funcion para desencriptar el contenido de un archivo
    def decrypt_file(self, file_patch):
        # Comprobacion de que el archivo existe
        if not os.path.isfile(file_patch):
            raise FileNotFoundError("The path assigned for the file to decrypt is incorrect.")
        else:
            content = ""
            # Abrir el documento para leer el contenido
            with open(file_patch, 'r') as file:
                content = file.read()

            # Se desencripta el contenido
            content = self.my_decryptor.decrypt(content)

            # Se intenta convertir el contenido a formato JSON
            # Si el formato no es correcto, deja que se genere la excepcion correspondiente
            self.last_json_decrypted = json.loads(content)
            return self.last_json_decrypted

    # Funcion para encriptar el contenido en formato JSON a un archivo
    def encrypt_file(self, file_patch, content):
        # Comprobacion de que el contenido sea correcto
        if type(content) is not dict or type(content) is not list:
            raise ValueError("The content to be encrypted must be in the correct JSON format: a list or a dictionary.")

        self.last_json_encrypted = content

        # Se convierte en una cadena de bytes el contenido
        json_content = json.dumps(content).encode()

        # Se encripta el contenido
        en_content = self.my_decryptor.encrypt(json_content)

        # Se guarda en un documento el contenido
        with open(file_patch, 'w') as file:
            file.write(en_content.decode())


if __name__ == "__main__":
    my_decrypter = JSONFormatDecryptor(b'HZqEJTbGEXnCp8NCK6LsM0p-MVaRoXUxYZsLPdXBxeg=')
    to_encrypt = {
        'nombre': 'Danilo',
        'Apellido': 'Ochoa',
        'Edad': '27'
    }

    # my_decrypter.encrypt_file('encriptado.txt', to_encrypt)
    decrypt = my_decrypter.decrypt_file('encriptado.txt')
    print(decrypt)
