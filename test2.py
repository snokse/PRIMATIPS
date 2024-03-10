import tkinter as tk
import mysql.connector
import tkinter.ttk as ttk

# Données MySQL (remplacez par vos données)
db_host = "localhost"
db_user = "root"
db_password = ""
db_name = "primatips"
table_name = "primatips_table"
colonnes = ["colonne1", "colonne2", "colonne3"]  # Ajustez au besoin

# Connexion à la base de données MySQL
def connexion_bdd():
    global connexion, curseur
    try:
        connexion = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name)
        curseur = connexion.cursor()
        print("Connexion à la base de données MySQL réussie !")
    except mysql.connector.Error as err:
        print(f"Erreur de connexion à la base de données MySQL : {err}")

# Récupération des données MySQL
def recuperation_donnees():
    global donnees
    try:
        requete = f"SELECT * FROM {table_name}"
        curseur.execute(requete)
        donnees = curseur.fetchall()
    except mysql.connector.Error as err:
        print(f"Erreur de récupération des données MySQL : {err}")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Fenetre avec 5 frames")

# Frame 1 : Logo et titre
frame_1 = tk.Frame(fenetre, width=fenetre.winfo_width())
frame_1.pack(fill=tk.X)

# Logo (ajustez l'image et la taille)
logo = tk.PhotoImage(file="IMG/PRIMATIPS_LOGO.png")
label_logo = tk.Label(frame_1, image=logo)
label_logo.pack(side=tk.LEFT)

# Titre
label_titre = tk.Label(frame_1, text="Titre de votre application", font=("Arial", 18))
label_titre.pack(side=tk.LEFT)

# Frame 2 : Table Treeview
frame_2 = tk.Frame(fenetre)
frame_2.pack(fill=tk.BOTH, expand=True)

# Fonction pour créer et afficher la Treeview
def affichage_treeview():
    global treeview, scrollbar_x

    # **Call `recuperation_donnees()` to ensure data is fetched before accessing it**
    recuperation_donnees()  # Moved this call inside the function

    treeview = tk.ttk.Treeview(frame_2, columns=colonnes, show="headings")
    treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar_x = tk.Scrollbar(frame_2, orient=tk.HORIZONTAL, command=treeview.xview)
    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

    treeview.configure(xscrollcommand=scrollbar_x.set)

    # Définition des titres des colonnes
    for colonne in colonnes:
        treeview.heading(colonne, text=colonne)

    # Remplissage de la Treeview avec les données
    for ligne in donnees:
        treeview.insert("", tk.END, values=ligne)

# **Call `affichage_treeview()` after data retrieval**
affichage_treeview()  # Moved this call after function definition

# Frames 3, 4 et 5 : Couleurs
frame_3 = tk.Frame(fenetre, bg="red")
frame_3.pack(fill=tk.BOTH, expand=True)

frame_4 = tk.Frame(fenetre, bg="green")
frame_4.pack(fill=tk.BOTH, expand=True)

frame_5 = tk.Frame(fenetre, bg="orange")
frame_5.pack(fill=tk.BOTH, expand=True)

# Lancement de la boucle principale
if __name__ == "__main__":
    connexion_bdd()
    fenetre.mainloop()
