import psutil
import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def afficher_infos_systeme():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disque = psutil.disk_usage('/')
    
    print("---- Infos système ----")
    print(f"CPU utilisé : {cpu}%")
    print(f"RAM utilisée : {ram.percent}%")
    print(f"Disque utilisé : {disque.percent}%")
    print("GPU: Pas d'affichage GPU pour le moment (à ajouter)")

if __name__ == "__main__":
    try:
        while True:
            clear_console()
            afficher_infos_systeme()
            print("\nAppuie sur Ctrl+C pour quitter.")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nBye !")
