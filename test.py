import tkinter as tk

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.geometry("780x580")
# Créer 4 frames
cadre1 = tk.Frame(fenetre, borderwidth=2, relief="groove")
cadre2 = tk.Frame(fenetre, borderwidth=2, relief="groove")
cadre3 = tk.Frame(fenetre, borderwidth=2, relief="groove")
cadre4 = tk.Frame(fenetre, borderwidth=2, relief="groove")

# Disposer les frames en grille
cadre1.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
cadre2.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
cadre3.pack(side=tk.LEFT, fill=tk.Y, expand=True)
cadre4.pack(side=tk.RIGHT, fill=tk.Y, expand=True)

# ... (ajouter des widgets aux frames)

# Démarrer la boucle principale
fenetre.mainloop()