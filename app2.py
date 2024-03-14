import sqlite3
import tkinter as tk
from tkinter import ttk
# from tkinter.ttk import Treeview
# from tkinter.ttk import Label
# "https://drive.google.com/file/d/1vCAOqLPDK4p1483FndCnOqBPuOzbmOOd/view?usp=sharing"

def create_database():
    global db_name, table_name
    db_name = "DB/primatips.sqlite"
    table_name = "primatips_table"
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    conn.commit()
    conn.close()

def search_BET():
    global count1
    search_BET1 = search_entry_BET1.get()
    search_BETX = search_entry_BETX.get()
    search_BET2 = search_entry_BET2.get()
    conn = sqlite3.connect(db_name)

    c = conn.cursor()
    c2 = conn.cursor()

    query = f"SELECT PAYS,TEAMS,BET1,BETX,BET2,SCORE,BUT1,BUT2,RESULTAT,PM,BUT FROM {table_name} WHERE 1=1"
    query2 =f"SELECT COUNT(*) FROM {table_name} WHERE 1=1"
    parameters = []

    if search_entry_BET1:
        query += " AND BET1 LIKE ?"
        query2 += " AND BET1 LIKE ?"
        parameters.append(search_BET1 + '%')

    if search_entry_BETX:
        query += " AND BETX LIKE ?"
        query2 += " AND BETX LIKE ?"
        parameters.append(search_BETX + '%')

    if search_entry_BET2:
        query += " AND BET2 LIKE ?"
        query2 += " AND BET2 LIKE ?"
        parameters.append(search_BET2 + '%')
    
    c.execute(query, parameters)
    c2.execute(query2, parameters)

    rows = c.fetchall()
    count1 = c2.fetchone()[0]

    conn.close()
    update_treeview(rows)

    print("Nombre de lignes dans la colonne 'ID':", count1)
    

def update_treeview(rows):
    for i in data_tree.get_children():
        data_tree.delete(i)
    for row in rows:
        data_tree.insert('', 'end', values=row)

create_database()

# Fonction pour créer un label avec un contour
def create_label_with_border(parent, text, row, column):
    labelBET = tk.Label(parent, text=text, relief="solid", borderwidth=1, width=10, height=2)
    labelBET.grid(row=row, column=column, padx=1, pady=1)
    return labelBET

conn = sqlite3.connect(db_name)
c = conn.cursor()
c.execute(f"SELECT PAYS,TEAMS,BET1,BETX,BET2,SCORE,BUT1,BUT2,RESULTAT,PM,BUT FROM {table_name} ORDER BY ID DESC")
rows = c.fetchall()

# Exécutez la requête SELECT pour compter le nombre de lignes
c.execute(f"SELECT COUNT(*) FROM {table_name}")

# Récupérez le résultat de la requête
count = c.fetchone()[0]

conn.close()

print("Nombre de lignes dans la colonne 'ID':", count)

# Création de la fenêtre principale
root = tk.Tk()
root.title("PRIMATIPS BET")
#largeur_fenetre = root.winfo_screenwidth() // 2   # Largeur de la moitié de l'écran
largeur_fenetre = root.winfo_screenwidth()   # Largeur de la moitié de l'écran
hauteur_fenetre = root.winfo_screenheight()   # hauteur de la moitié de l'écran
root.geometry(f"{largeur_fenetre}x{hauteur_fenetre}")  # Taille de la fenêtre
root.iconbitmap("IMG/PRIMATIPS_ICO.ico")
root.config(background="#002f5e")

# Frame 1 : Logo et Titre
frame1 = tk.Frame(root, bg="#007acc")
frame1.pack(fill="x")  # Remplir horizontalement
# Ajout du logo au premier frame
logo = tk.PhotoImage(file="IMG/PRIMATIPS_LOGO.png")
label_logo = tk.Label(frame1, image=logo, bg="#007acc")
label_logo.pack()

# Frame 2 : Labels, Entries et Button
frame2 = tk.Frame(root, bg="#007acc", width=largeur_fenetre)
frame2.pack(padx=5, pady=5, fill="x")  # Remplir horizontalement avec un padding
# Labels
label1 = tk.Label(frame2, text="1")
label1.grid(row=0, column=1, padx=5, pady=5)
label2 = tk.Label(frame2, text="X")
label2.grid(row=0, column=2, padx=5, pady=5)
label3 = tk.Label(frame2, text="2")
label3.grid(row=0, column=3, padx=5, pady=5)
# Entries

search_entry_BET1 = tk.Entry(frame2)
search_entry_BET1.grid(row=1, column=1, padx=5, pady=5)
search_entry_BETX = tk.Entry(frame2)
search_entry_BETX.grid(row=1, column=2, padx=5, pady=5)
search_entry_BET2 = tk.Entry(frame2)
search_entry_BET2.grid(row=1, column=3, padx=5, pady=5)
# Button
button = tk.Button(frame2, text="Valider", command=search_BET)
button.grid(row=3, columnspan=4, pady=10)

# Frame 3 : Vide de couleur rouge
frame3 = tk.Frame(root, bg="#007acc", width=largeur_fenetre // 2)  # Largeur de moitié de la fenêtre
frame3.pack(side="left", fill="y")  # Remplir verticalement

# Création des labels dans un tableau 8x7
label_texts = [
    count, "1", "X", "2", "PM", "B/SB", "TOTAL",
    "1", "Label 9", "Label 10", "Label 11", "Label 12", "Label 13", "Label 14",
    "X", "Label 16", "Label 17", "Label 18", "Label 19", "Label 20", "Label 21",
    "2", "Label 23", "Label 24", "Label 25", "Label 26", "Label 27", "Label 28",
    "1X", "Label 30", "Label 31", "Label 32", "Label 33", "Label 34", "Label 35",
    "12", "Label 37", "Label 38", "Label 39", "Label 40", "Label 41", "Label 42",
    "X2", "Label 44", "Label 45", "Label 46", "Label 47", "Label 48", "Label 49",
    "1X2", "Label 51", "Label 52", "Label 53", "Label 54", "Label 55", "Label 56"
]

labels = []
for i in range(8):
    row_labels = []
    for j in range(7):
        label_text = label_texts[i * 7 + j]
        label = create_label_with_border(frame3, label_text, i, j)
        row_labels.append(label)
    labels.append(row_labels)


# Frame 4 : Affichage des données MySQL
frame4 = tk.Frame(root)
frame4.pack(fill="both", expand=True)  # Remplir et étendre dans toutes les directions
# Créer un Treeview (remplacer les exemples par vos propres données)
data_tree = ttk.Treeview(frame4, columns=("PAYS", "TEAMS", "1","X", "2", "SCORE", "BUT1", "BUT2","RESULTAT", "PM", "BUT"), show='headings')
# Use integer values for alignment

data_tree.heading("PAYS", text="PAYS")
data_tree.heading("TEAMS", text="TEAMS")
data_tree.heading("1", text="1")
data_tree.heading("X", text="X")
data_tree.heading("2", text="2")
data_tree.heading("SCORE", text="SCORE")
data_tree.heading("BUT1", text="BUT1")
data_tree.heading("BUT2", text="BUT2")
data_tree.heading("RESULTAT", text="RESULTAT")
data_tree.heading("PM", text="PM")
data_tree.heading("BUT", text="BUT")
data_tree.pack(fill="both", expand=True)  # Remplir et étendre dans toutes les directions



# Ajouter une barre de défilement horizontal
scrollbar_x = ttk.Scrollbar(frame4, orient="horizontal", command=data_tree.xview)
scrollbar_x.pack(side="bottom", fill="x")
data_tree.configure(xscrollcommand=scrollbar_x.set)


update_treeview(rows)

root.mainloop()