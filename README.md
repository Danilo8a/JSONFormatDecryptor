# JSONFormatDecryptor

This is a small Python utility that allows you to save and read information in JSON format from a file whose contents are encrypted.

The encryption is symmetric, so you must first generate a key for encryption. The module provides a function called **generate_password_txt**, which generates the key in a txt file in the root of the project. You can then retrieve it and use it in your project to encrypt and decrypt the content. Of course, after generating the key and copying it into your script, you must delete the file so that no one else can access it.

The object that will allow you to encrypt and decrypt the content is instantiated with the key. Then, you can use the **encrypt_file** method to encrypt a dictionary or a list (everything always compatible with the JSON format) in a file whose patch must be passed as a parameter.

To retrieve the information, you can use the **decrypt_file** method, which takes the content of the file whose patch is passed as parameter, decrypts it and returns a list or a dictionary (depending on how you have previously saved the content in JSON format), to use it in your program.
