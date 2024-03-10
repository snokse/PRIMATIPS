import tkinter as tk
import mysql.connector
import tkinter.ttk as ttk


# MySQL connection details (replace with your credentials)
db_host = "localhost"
db_user = "root"
db_password = ""
db_name = "primatips"
table_name = "primatips_table"
# Connect to MySQL database
def connect_to_database():
    global connection, cursor
    try:
        connection = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name)
        cursor = connection.cursor()
        print("Connected to MySQL database successfully!")
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL database: {err}")

# Fetch data from MySQL table
def fetch_data():
    global data
    try:
        # Replace "your_table_name" and "your_columns" with your actual table and columns
        requete1 = "SELECT PAYS,TEAMS,BET1,BETX,BET2,SCORE,RESULTAT,PM,BUT FROM primatips_table"
        cursor.execute(requete1)
        data = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error fetching data from MySQL table: {err}")

def rechercher():
    global resultats
    # Récupérer la valeur saisie dans l'entrée
    valeur_recherchee = entry1.get()

    # Créer un curseur
    cursor = connection.cursor()

    # Exécuter la requête SQL
    requete1 = "SELECT PAYS,TEAMS,BET1,BETX,BET2,SCORE,RESULTAT,PM,BUT FROM primatips_table WHERE BET1 LIKE '%s%%'" % valeur_recherchee
    cursor.execute(requete1)
    # Récupérer les résultats
    resultats = cursor.fetchall()

    # Afficher les résultats
    for resultat in resultats:
        print(resultat)

    # Fermer le curseur
    cursor.close()

# Création de la fenêtre principale
root = tk.Tk()
root.title("PRIMATIPS BET")
largeur_fenetre = root.winfo_screenwidth() // 2  # Largeur de la moitié de l'écran
root.geometry(f"{largeur_fenetre}x600")  # Taille de la fenêtre
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
frame2 = tk.Frame(root, bg="#007acc", width=largeur_fenetre // 2)
frame2.pack(padx=10, pady=5, fill="y")  # Remplir horizontalement avec un padding
# Labels
label1 = tk.Label(frame2, text="1")
label1.grid(row=0, column=1, padx=5, pady=5)
label2 = tk.Label(frame2, text="X")
label2.grid(row=0, column=2, padx=5, pady=5)
label3 = tk.Label(frame2, text="2")
label3.grid(row=0, column=3, padx=5, pady=5)
# Entries
entry1 = tk.Entry(frame2)
entry1.grid(row=1, column=1, padx=5, pady=5)
entry2 = tk.Entry(frame2)
entry2.grid(row=1, column=2, padx=5, pady=5)
entry3 = tk.Entry(frame2)
entry3.grid(row=1, column=3, padx=5, pady=5)
# Button
button = tk.Button(frame2, text="Valider", command=rechercher)
button.grid(row=3, columnspan=4, pady=10)

# Frame 3 : Vide de couleur rouge
frame3 = tk.Frame(root, bg="#007acc", width=largeur_fenetre // 2)  # Largeur de moitié de la fenêtre
frame3.pack(side="left", fill="y")  # Remplir verticalement

# Frame 4 : Affichage des données MySQL
frame4 = tk.Frame(root)
frame4.pack(fill="both", expand=True)  # Remplir et étendre dans toutes les directions
# Créer un Treeview (remplacer les exemples par vos propres données)
data_tree = ttk.Treeview(frame4, columns=("PAYS", "TEAMS", "1","X", "2", "SCORE","RESULTAT", "PM", "BUT"))
data_tree.heading("PAYS", text="PAYS")
data_tree.heading("TEAMS", text="TEAMS")
data_tree.heading("1", text="1")
data_tree.heading("X", text="X")
data_tree.heading("2", text="2")
data_tree.heading("SCORE", text="SCORE")
data_tree.heading("RESULTAT", text="RESULTAT")
data_tree.heading("PM", text="PM")
data_tree.heading("BUT", text="BUT")
data_tree.pack(fill="both", expand=True)  # Remplir et étendre dans toutes les directions
# Charger les données MySQL fictives
# donnees_mysql = charger_donnees_mysql()
# for row in donnees_mysql:
# data_tree.insert("", "end", text=row["ID"], values=(row["Nom"], row["Age"]))

# Populate the Treeview with fetched data
def populate_treeview():
    for row in resultats:
        data_tree.insert("", tk.END, values=row)

# Ajouter une barre de défilement horizontal
scrollbar_x = ttk.Scrollbar(frame4, orient="horizontal", command=data_tree.xview)
scrollbar_x.pack(side="bottom", fill="x")
data_tree.configure(xscrollcommand=scrollbar_x.set)

# Main program loop
def main():
    connect_to_database()
    rechercher()
    fetch_data()
    populate_treeview()
    root.mainloop()


if __name__ == "__main__":
    main()
