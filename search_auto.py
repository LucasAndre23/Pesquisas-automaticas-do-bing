import pyautogui as p
import keyboard as k
import random
import time

pesquisas = [
    'laptop', 'smartphone', 'headphones', 'monitor', 'keyboard', 'mouse', 'printer', 'webcam', 'speakers', 'router',
    'tablet', 'camera', 'microphone', 'charger', 'battery', 'cable', 'projector', 'scanner', 'drone', 'console',
    'television', 'fridge', 'oven', 'toaster', 'blender', 'fan', 'lamp', 'watch', 'clock', 'radio',
    'book', 'pen', 'pencil', 'notebook', 'paper', 'eraser', 'marker', 'ruler', 'bag', 'wallet',
    'shirt', 'pants', 'jacket', 'shoes', 'socks', 'hat', 'gloves', 'belt', 'dress', 'skirt',
    'car', 'bus', 'train', 'bicycle', 'motorcycle', 'truck', 'boat', 'ship', 'airplane', 'subway',
    'apple', 'banana', 'orange', 'grape', 'pear', 'peach', 'plum', 'kiwi', 'mango', 'pineapple',
    'dog', 'cat', 'bird', 'fish', 'horse', 'cow', 'sheep', 'goat', 'lion', 'tiger',
    'gold', 'silver', 'diamond', 'iron', 'copper', 'steel', 'bronze', 'platinum', 'coal', 'oil'
]

rodando = True

def encerrar_loop():
    global rodando
    rodando = False


k.on_press_key("q", lambda _: encerrar_loop())

def search_auto():
    
    p.press('win')
    time.sleep(2)
    p.write('edge')
    p.press('enter')
    time.sleep(3)

    while rodando:
        termo = random.choice(pesquisas)
        p.write(termo)
        time.sleep(2)
        p.press('enter')
        time.sleep(5)
        p.hotkey('ctrl', 't')
        time.sleep(2)

if __name__ == "__main__":
    search_auto()
