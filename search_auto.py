import pyautogui as p
import keyboard as k
import random
import time

pesquisas = [
    'iPhone 15', 'Samsung Galaxy S24', 'Xiaomi Redmi Note 13', 'Motorola Edge 50', 'Google Pixel 8',
    'MacBook Air M3', 'Dell XPS 13', 'Lenovo ThinkPad X1', 'ASUS ROG Strix', 'Acer Nitro 5',
    'Apple Watch Series 9', 'Samsung Galaxy Watch 6', 'Garmin Forerunner 965', 'Amazfit GTR 4', 'Huawei Watch GT 4',
    'AirPods Pro 2', 'Galaxy Buds 2 Pro', 'Sony WH-1000XM5', 'JBL Tune 770NC', 'Beats Studio Pro',
    'Logitech MX Master 3S', 'Razer DeathAdder V3', 'SteelSeries Rival 5', 'Corsair Harpoon RGB', 'HyperX Pulsefire Haste',
    'Logitech G915', 'Keychron K8', 'Razer BlackWidow V4', 'Corsair K70 RGB', 'HyperX Alloy Origins',
    'Samsung Odyssey G7', 'LG UltraGear 27', 'Dell UltraSharp U2723QE', 'ASUS ProArt Display', 'AOC Hero 24G2',
    'PlayStation 5', 'Xbox Series X', 'Nintendo Switch OLED', 'Steam Deck OLED', 'Meta Quest 3',
    'Canon EOS R10', 'Sony Alpha A6400', 'Nikon Z50', 'Fujifilm X-T30 II', 'GoPro Hero 12',
    'DJI Mini 4 Pro', 'DJI Air 3', 'Autel EVO Lite+', 'Holy Stone HS720E', 'Potensic Atom',
    'Kindle Paperwhite', 'Kindle Scribe', 'Kobo Libra 2', 'PocketBook InkPad', 'Onyx Boox Note Air',
    'Samsung Galaxy Tab S9', 'iPad Air M2', 'Lenovo Tab P12', 'Xiaomi Pad 6', 'Huawei MatePad 11.5',
    'Echo Dot 5', 'Google Nest Audio', 'Amazon Fire TV Stick 4K', 'Chromecast with Google TV', 'Apple TV 4K',
    'TP-Link Archer AX55', 'ASUS RT-AX58U', 'Mercusys MR70X', 'Intelbras RX1500', 'Linksys Hydra Pro',
    'HP Smart Tank 581', 'Epson EcoTank L3250', 'Canon MegaTank G3110', 'Brother DCP-T420W', 'Xerox B225',
    'Philips Walita Air Fryer', 'Mondial Air Fryer Oven', 'Electrolux Air Fryer EAF90', 'Oster OFRT780', 'Britânia Air Fryer BFR50',
    'Samsung Smart TV 55', 'LG OLED C4', 'TCL P755', 'Philips Ambilight TV', 'Hisense U7K',
    'Geladeira Brastemp Frost Free', 'Geladeira Electrolux Inverter', 'Geladeira Consul Duplex', 'Geladeira Panasonic Econavi', 'Geladeira Samsung Bespoke',
    'Micro-ondas LG NeoChef', 'Micro-ondas Electrolux ME36S', 'Micro-ondas Panasonic NN-ST27', 'Micro-ondas Consul CMS46', 'Micro-ondas Brastemp BMS46',
    'Cafeteira Nespresso Vertuo', 'Cafeteira Dolce Gusto Genio S', 'Cafeteira Oster PrimaLatte', 'Cafeteira Philco Coffee Express', 'Cafeteira Electrolux ECM25'
]

rodando = True

def encerrar_loop():
    global rodando
    rodando = False


k.on_press_key("q", lambda _: encerrar_loop())

def search_auto():
    try:
        p.press('win')
        time.sleep(1)

        p.write('edge')
        time.sleep(1)

        p.press('enter')
        time.sleep(5)

        for termo in pesquisas:
            if not rodando:
                break

            try:
                p.hotkey('ctrl', 'l')
                time.sleep(1)

                p.write(termo)
                time.sleep(1)

                p.press('enter')
                time.sleep(5)

            except Exception as e:
                print(f"Erro ao pesquisar '{termo}': {e}")
                continue

    except Exception as e:
        print(f"Erro fatal: {e}")

    finally:
        print("Finalizado")

if __name__ == "__main__":
    search_auto()
