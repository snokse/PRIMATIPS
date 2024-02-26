import tkinter as tk

# Créer la fenêtre principale
fenetre = tk.Tk()

# Définir la taille de la fenêtre
fenetre.geometry("400x200")

# Créer un cadre
cadre = tk.Frame(fenetre, borderwidth=5, relief="groove")
cadre.pack(padx=30, pady=10)

for i in range(4):
    for j in range(8):
        label = tk.Label(cadre, text=f"{i+1}x{j+1}",
                       relief="groove", borderwidth=5)
        label.grid(row=i, column=j, padx=2, pady=2)

# Démarrer la boucle principale
fenetre.mainloop()