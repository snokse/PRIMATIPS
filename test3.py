import tkinter as tk

# Fonction pour créer un label avec un contour
def create_label_with_border(parent, text, row, column):
    labelBET = tk.Label(parent, text=text, relief="solid", borderwidth=1, width=10, height=2)
    labelBET.grid(row=row, column=column, padx=1, pady=1)
    return labelBET

# Création de la fenêtre principale
root = tk.Tk()
root.title("Tableau de Labels avec Contour")

# Création des labels dans un tableau 8x7
label_texts = [
    "COTE", "1", "X", "2", "PM", "B/SB", "TOTAL",
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
        label = create_label_with_border(root, label_text, i, j)
        row_labels.append(label)
    labels.append(row_labels)

# Lancement de la boucle principale
root.mainloop()
