import os
import sys
import time
import psutil
import platform
from datetime import datetime

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    COLOR_AVAILABLE = True
except ImportError:
    COLOR_AVAILABLE = False


class ConsoleUtils:
    @staticmethod
    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def print_colored(text, color=None, style=None):
        if COLOR_AVAILABLE:
            color_code = getattr(Fore, color.upper(), "") if color else ""
            style_code = getattr(Style, style.upper(), "") if style else ""
            print(f"{style_code}{color_code}{text}{Style.RESET_ALL}")
        else:
            print(text)


class SystemMonitor:
    def __init__(self, refresh_rate=2):
        self.refresh_rate = refresh_rate
        self.hostname = platform.node()
        self.os_info = f"{platform.system()} {platform.release()} ({platform.version()})"
        self.start_time = datetime.now()

    def get_cpu_usage(self):
        return psutil.cpu_percent(interval=1)

    def get_ram_usage(self):
        ram = psutil.virtual_memory()
        return ram.percent, ram.total, ram.used, ram.available

    def get_disk_usage(self, path="/"):
        disk = psutil.disk_usage(path)
        return disk.percent, disk.total, disk.used, disk.free

    def uptime(self):
        delta = datetime.now() - self.start_time
        return str(delta).split('.')[0]

    def display_system_info(self):
        ConsoleUtils.clear_console()
        ConsoleUtils.print_colored("=== System Monitoring ===", color="cyan", style="BRIGHT")
        print(f"Machine      : {self.hostname}")
        print(f"System       : {self.os_info}")
        print(f"Script uptime: {self.uptime()}")

        cpu = self.get_cpu_usage()
        ConsoleUtils.print_colored(f"\nCPU usage    : {cpu}%", color="yellow")

        ram_percent, ram_total, ram_used, ram_available = self.get_ram_usage()
        ConsoleUtils.print_colored(f"RAM usage    : {ram_percent}% "
                                   f"({self._bytes_to_human(ram_used)}/{self._bytes_to_human(ram_total)})",
                                   color="magenta")

        disk_percent, disk_total, disk_used, disk_free = self.get_disk_usage()
        ConsoleUtils.print_colored(f"Disk usage   : {disk_percent}% "
                                   f"({self._bytes_to_human(disk_used)}/{self._bytes_to_human(disk_total)})",
                                   color="green")

        ConsoleUtils.print_colored("GPU: Not implemented yet", color="red")
        print("\nPress Ctrl+C to exit.")

    @staticmethod
    def _bytes_to_human(n):
        symbols = ('B', 'KB', 'MB', 'GB', 'TB', 'PB')
        i = 0
        while n >= 1024 and i < len(symbols) - 1:
            n /= 1024.
            i += 1
        return f"{n:.2f} {symbols[i]}"

    def run(self):
        try:
            while True:
                self.display_system_info()
                time.sleep(self.refresh_rate)
        except KeyboardInterrupt:
            ConsoleUtils.print_colored("\nStopping monitoring", color="cyan")
            sys.exit(0)
        except Exception as e:
            ConsoleUtils.print_colored(f"\nCritical error: {e}", color="red", style="BRIGHT")
            sys.exit(1)


if __name__ == "__main__":
    monitor = SystemMonitor(refresh_rate=2)
    monitor.run()
