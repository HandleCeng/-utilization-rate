import psutil
import GPUtil

def afficher_infos_systeme():
    # Informations sur le CPU
    cpu_info = f"CPU: {psutil.cpu_percent()}% utilisé"
    
    # Informations sur la RAM
    ram = psutil.virtual_memory()
    ram_info = f"RAM: {ram.percent}% utilisé"
    
    # Informations sur le disque
    disque = psutil.disk_usage('/')
    disque_info = f"Disque: {disque.percent}% utilisé"
    
    # Informations sur le GPU
    gpus = GPUtil.getGPUs()
    for gpu in gpus:
        gpu_info = f"GPU {gpu.id}: {gpu.name}, Mémoire Utilisée: {gpu.memoryUsed} MB, Charge: {gpu.load * 100}%"
        print(gpu_info)
    
    # Affichage des informations
    print(cpu_info)
    print(ram_info)
    print(disque_info)

# Appel de la fonction pour afficher les informations
afficher_infos_systeme()
