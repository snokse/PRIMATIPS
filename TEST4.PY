import tkinter as tk
from tkinter import ttk
import sqlite3
db_name = "DB/primatips.sqlite"
table_name = "primatips_table"
def remplir_treeview(tv, connexion, table_name):
    # Récupération des noms des colonnes
    curseur = connexion.cursor()
    curseur.execute(f"PRAGMA table_info({table_name})")
    noms_colonnes = [colonne[1] for colonne in curseur.fetchall()]

    # Insertion des noms des colonnes dans le Treeview
    for colonne in noms_colonnes:
        tv.heading(colonne, text=colonne)

    # Récupération des données
    curseur.execute("SELECT * FROM ?", (table_name,))
    données = curseur.fetchall()

    # Insertion des données dans le Treeview
    for ligne in données:
        tv.insert('', 'end', values=ligne)

# Connexion à la base de données
connexion = sqlite3.connect(db_name)

root = tk.Tk()
# Création du Treeview
tv = ttk.Treeview(root, columns=[], show='headings')

# Remplissage du Treeview
remplir_treeview(tv, connexion, table_name)

# Affichage du Treeview
tv.pack()

# Fermeture de la connexion à la base de données
connexion.close()

root.mainloop()
