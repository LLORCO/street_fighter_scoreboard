import json

DATA_FILE = "scoreboard_data.json"

def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def update_scoreboard():
    data = load_data()
    print("Valores actuales del scoreboard:")
    for key, value in data.items():
        print(f"{key}: {value}")
    
    print("\nDeja vacío si no quieres cambiar un campo.")
    for key in data:
        nuevo = input(f"{key} [{data[key]}]: ").strip()
        if nuevo:
            if "score" in key or "score" in key.lower():
                try:
                    data[key] = int(nuevo)
                except ValueError:
                    print("Valor inválido. Se mantiene el anterior.")
            else:
                data[key] = nuevo

    save_data(data)
    print("\n✅ Scoreboard actualizado.")

if __name__ == "__main__":
    update_scoreboard()
