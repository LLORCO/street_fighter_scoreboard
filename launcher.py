import subprocess
import sys
import time
import os
import signal
import psutil

def kill_process_tree(pid):
    parent = psutil.Process(pid)
    children = parent.children(recursive=True)
    for child in children:
        child.kill()
    parent.kill()

# Iniciar el servidor Flask en segundo plano
server_process = subprocess.Popen([sys.executable, 'server.py'])

try:
    # Esperar un poco para asegurarse de que el servidor arranque
    time.sleep(1)
    # Iniciar la interfaz gráfica
    gui_process = subprocess.Popen([sys.executable, 'scoreboard_gui.py'])
    gui_process.wait()  # Esperar a que el GUI se cierre
finally:
    # Al cerrar el GUI, terminar el servidor y todos sus procesos hijos
    kill_process_tree(server_process.pid)
    
    # Terminar el proceso de Python
    os.kill(os.getpid(), signal.SIGTERM) 