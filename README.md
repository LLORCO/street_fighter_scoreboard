# Street Fighter Scoreboard

Un tablero de puntuación interactivo para torneos de Street Fighter, desarrollado con Python, Flask y Tkinter.

## Características

- Interfaz gráfica intuitiva para mostrar y actualizar puntuaciones
- Servidor Flask para manejar actualizaciones en tiempo real
- Botones para incrementar y decrementar puntuaciones
- Diseño moderno y responsive
- Lanzador automático que inicia tanto el servidor como la GUI

## Requisitos

- Python 3.8 o superior
- Dependencias listadas en `requirements.txt`

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/LLORCO/street_fighter_scoreboard.git
cd street_fighter_scoreboard
```

2. Crea un entorno virtual e instala las dependencias:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Uso

Para iniciar la aplicación, simplemente ejecuta:
```bash
python launcher.py
```

Esto iniciará automáticamente el servidor Flask y la interfaz gráfica.

## Estructura del Proyecto

- `launcher.py`: Script principal que inicia tanto el servidor como la GUI
- `server.py`: Servidor Flask para manejar actualizaciones
- `gui.py`: Interfaz gráfica desarrollada con Tkinter
- `requirements.txt`: Lista de dependencias del proyecto

## Contribuir

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir los cambios propuestos.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles. 