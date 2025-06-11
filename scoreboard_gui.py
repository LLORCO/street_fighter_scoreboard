import tkinter as tk
import json

DATA_FILE = "scoreboard_data.json"

def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def guardar():
    try:
        data = {
            "player1": entry_player1.get(),
            "player2": entry_player2.get(),
            "score1": int(entry_score1.get()),
            "score2": int(entry_score2.get()),
            "match_info": entry_match_info.get(),
            "team1": entry_team1.get(),
            "team2": entry_team2.get(),
            "team_score1": int(entry_team_score1.get()),
            "team_score2": int(entry_team_score2.get())
        }
        save_data(data)
        status_label.config(text="✅", fg="green")
        root.after(2000, lambda: status_label.config(text=""))
    except ValueError:
        status_label.config(text="❌", fg="red")
        root.after(2000, lambda: status_label.config(text=""))

def incrementar_score(entry):
    try:
        valor = int(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(valor + 1))
        guardar()
    except ValueError:
        status_label.config(text="❌", fg="red")
        root.after(2000, lambda: status_label.config(text=""))

def decrementar_score(entry):
    try:
        valor = int(entry.get())
        if valor > 0:
            entry.delete(0, tk.END)
            entry.insert(0, str(valor - 1))
            guardar()
    except ValueError:
        status_label.config(text="❌", fg="red")
        root.after(2000, lambda: status_label.config(text=""))

def intercambiar_jugadores():
    # Intercambiar nombres
    p1 = entry_player1.get()
    p2 = entry_player2.get()
    entry_player1.delete(0, tk.END)
    entry_player1.insert(0, p2)
    entry_player2.delete(0, tk.END)
    entry_player2.insert(0, p1)
    # Intercambiar puntajes
    s1 = entry_score1.get()
    s2 = entry_score2.get()
    entry_score1.delete(0, tk.END)
    entry_score1.insert(0, s2)
    entry_score2.delete(0, tk.END)
    entry_score2.insert(0, s1)
    # Intercambiar equipos
    t1 = entry_team1.get()
    t2 = entry_team2.get()
    entry_team1.delete(0, tk.END)
    entry_team1.insert(0, t2)
    entry_team2.delete(0, tk.END)
    entry_team2.insert(0, t1)
    # Intercambiar puntajes de equipo
    ts1 = entry_team_score1.get()
    ts2 = entry_team_score2.get()
    entry_team_score1.delete(0, tk.END)
    entry_team_score1.insert(0, ts2)
    entry_team_score2.delete(0, tk.END)
    entry_team_score2.insert(0, ts1)
    guardar()

data = load_data()

root = tk.Tk()
root.title("Editor de Scoreboard")
root.geometry("420x350")

main_frame = tk.Frame(root, padx=10, pady=10)
main_frame.pack()

# Fila 0: Jugador 1
label_player1 = tk.Label(main_frame, text="Jugador 1:", anchor="e", width=12)
label_player1.grid(row=0, column=0, sticky="e", pady=2)
entry_player1 = tk.Entry(main_frame, width=18)
entry_player1.grid(row=0, column=1, columnspan=3, sticky="w", pady=2)
entry_player1.insert(0, data["player1"])

# Fila 1: Puntaje Jugador 1
label_score1 = tk.Label(main_frame, text="Puntaje J1:", anchor="e", width=12)
label_score1.grid(row=1, column=0, sticky="e", pady=2)
btn_score1_minus = tk.Button(main_frame, text="-", width=2, command=lambda: decrementar_score(entry_score1))
btn_score1_minus.grid(row=1, column=1, sticky="w", padx=1)
entry_score1 = tk.Entry(main_frame, width=5)
entry_score1.grid(row=1, column=2, sticky="w", padx=1)
entry_score1.insert(0, str(data["score1"]))
btn_score1_plus = tk.Button(main_frame, text="+", width=2, command=lambda: incrementar_score(entry_score1))
btn_score1_plus.grid(row=1, column=3, sticky="w", padx=1)

# Fila 2: Jugador 2
label_player2 = tk.Label(main_frame, text="Jugador 2:", anchor="e", width=12)
label_player2.grid(row=2, column=0, sticky="e", pady=2)
entry_player2 = tk.Entry(main_frame, width=18)
entry_player2.grid(row=2, column=1, columnspan=3, sticky="w", pady=2)
entry_player2.insert(0, data["player2"])

# Fila 3: Puntaje Jugador 2
label_score2 = tk.Label(main_frame, text="Puntaje J2:", anchor="e", width=12)
label_score2.grid(row=3, column=0, sticky="e", pady=2)
btn_score2_minus = tk.Button(main_frame, text="-", width=2, command=lambda: decrementar_score(entry_score2))
btn_score2_minus.grid(row=3, column=1, sticky="w", padx=1)
entry_score2 = tk.Entry(main_frame, width=5)
entry_score2.grid(row=3, column=2, sticky="w", padx=1)
entry_score2.insert(0, str(data["score2"]))
btn_score2_plus = tk.Button(main_frame, text="+", width=2, command=lambda: incrementar_score(entry_score2))
btn_score2_plus.grid(row=3, column=3, sticky="w", padx=1)

# Fila 4: Match Info
label_match = tk.Label(main_frame, text="Match Info:", anchor="e", width=12)
label_match.grid(row=4, column=0, sticky="e", pady=2)
entry_match_info = tk.Entry(main_frame, width=18)
entry_match_info.grid(row=4, column=1, columnspan=3, sticky="w", pady=2)
entry_match_info.insert(0, data["match_info"])

# Fila 5: Equipo 1
label_team1 = tk.Label(main_frame, text="Equipo 1:", anchor="e", width=12)
label_team1.grid(row=5, column=0, sticky="e", pady=2)
entry_team1 = tk.Entry(main_frame, width=18)
entry_team1.grid(row=5, column=1, columnspan=3, sticky="w", pady=2)
entry_team1.insert(0, data["team1"])

# Fila 6: Puntaje Equipo 1
label_team_score1 = tk.Label(main_frame, text="Puntaje E1:", anchor="e", width=12)
label_team_score1.grid(row=6, column=0, sticky="e", pady=2)
btn_team_score1_minus = tk.Button(main_frame, text="-", width=2, command=lambda: decrementar_score(entry_team_score1))
btn_team_score1_minus.grid(row=6, column=1, sticky="w", padx=1)
entry_team_score1 = tk.Entry(main_frame, width=5)
entry_team_score1.grid(row=6, column=2, sticky="w", padx=1)
entry_team_score1.insert(0, str(data["team_score1"]))
btn_team_score1_plus = tk.Button(main_frame, text="+", width=2, command=lambda: incrementar_score(entry_team_score1))
btn_team_score1_plus.grid(row=6, column=3, sticky="w", padx=1)

# Fila 7: Equipo 2
label_team2 = tk.Label(main_frame, text="Equipo 2:", anchor="e", width=12)
label_team2.grid(row=7, column=0, sticky="e", pady=2)
entry_team2 = tk.Entry(main_frame, width=18)
entry_team2.grid(row=7, column=1, columnspan=3, sticky="w", pady=2)
entry_team2.insert(0, data["team2"])

# Fila 8: Puntaje Equipo 2
label_team_score2 = tk.Label(main_frame, text="Puntaje E2:", anchor="e", width=12)
label_team_score2.grid(row=8, column=0, sticky="e", pady=2)
btn_team_score2_minus = tk.Button(main_frame, text="-", width=2, command=lambda: decrementar_score(entry_team_score2))
btn_team_score2_minus.grid(row=8, column=1, sticky="w", padx=1)
entry_team_score2 = tk.Entry(main_frame, width=5)
entry_team_score2.grid(row=8, column=2, sticky="w", padx=1)
entry_team_score2.insert(0, str(data["team_score2"]))
btn_team_score2_plus = tk.Button(main_frame, text="+", width=2, command=lambda: incrementar_score(entry_team_score2))
btn_team_score2_plus.grid(row=8, column=3, sticky="w", padx=1)

# Fila 9: Botón intercambiar, guardar y estado
swap_button = tk.Button(main_frame, text="Intercambiar jugadores", command=intercambiar_jugadores, bg="#2196F3", fg="white")
swap_button.grid(row=9, column=0, columnspan=2, pady=12, sticky="e")
save_button = tk.Button(main_frame, text="Guardar Cambios", command=guardar, bg="#4CAF50", fg="white")
save_button.grid(row=9, column=2, sticky="e")
status_label = tk.Label(main_frame, text="", font=("Arial", 14))
status_label.grid(row=9, column=3, sticky="w")

root.mainloop()
