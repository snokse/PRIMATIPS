import tkinter as tk

# Définition de la fenêtre principale
fenetre = tk.Tk()
fenetre.geometry("780x580")
fenetre.title("PRIMATIPS BET")
fenetre.config(background="#165e8e")
fenetre.iconbitmap("IMG/PRIMATIPS_ICO.ico")

# Création du premier frame pour le logo
frame_logo = tk.Frame(fenetre, bg="white", borderwidth=2, relief="groove")
frame_logo.pack(fill="y")

# Ajout du logo au premier frame
logo = tk.PhotoImage(file="IMG/PRIMATIPS_LOGO.png")
label_logo = tk.Label(frame_logo, image=logo, bg="#165e8e")
label_logo.pack()

# Création des 4 autres frames LEFT TOP RIGHT BOTTOM
frame_1 = tk.Frame(fenetre, bg="red", borderwidth=2, relief="groove")
frame_1.pack(fill="both", expand=True, side=tk.LEFT)

frame_2 = tk.Frame(fenetre, bg="green", borderwidth=2, relief="groove")
frame_2.pack(fill="both", expand=True, side=tk.TOP)

frame_3 = tk.Frame(fenetre, bg="blue", borderwidth=2, relief="groove")
frame_3.pack(fill="both", expand=True, side=tk.BOTTOM)

frame_4 = tk.Frame(fenetre, bg="yellow", borderwidth=2, relief="groove")
frame_4.pack(fill="both", expand=True, side=tk.LEFT)

# Personnalisation des frames (optionnel)
# Ajout de widgets, boutons, etc.

# Lancement de la boucle principale
fenetre.mainloop()
