import sqlite3
import tkinter as tk
from tkinter import ttk

def create_database():
    conn = sqlite3.connect('DB/primatips4.sqlite')
    c = conn.cursor()
    conn.commit()
    conn.close()

def search_items():
    search_term = search_entry.get()
    conn = sqlite3.connect('DB/primatips4.sqlite')
    c = conn.cursor()
    c.execute("SELECT PAYS,TEAMS,BET1,BETX,BET2,SCORE,RESULTAT,PM,BUT FROM primatips_table WHERE PAYS LIKE ?", ('%' + search_term + '%',))
    rows = c.fetchall()
    conn.close()
    update_treeview(rows)

def update_treeview(rows):
    for i in data_tree.get_children():
        data_tree.delete(i)
    for row in rows:
        data_tree.insert('', 'end', values=row)

create_database()

root = tk.Tk()
root.title("Database Viewer")

search_label = tk.Label(root, text="Search:")
search_label.grid(row=0, column=0)

search_entry = tk.Entry(root)
search_entry.grid(row=0, column=1)

search_button = tk.Button(root, text="Search", command=search_items)
search_button.grid(row=0, column=2)

data_tree = ttk.Treeview(root, columns=("PAYS", "TEAMS", "1","X", "2", "SCORE","RESULTAT", "PM", "BUT"), show='headings')
data_tree.heading("PAYS", text="PAYS")
data_tree.heading("TEAMS", text="TEAMS")
data_tree.heading("1", text="1")
data_tree.heading("X", text="X")
data_tree.heading("2", text="2")
data_tree.heading("SCORE", text="SCORE")
data_tree.heading("RESULTAT", text="RESULTAT")
data_tree.heading("PM", text="PM")
data_tree.heading("BUT", text="BUT")
data_tree.grid(row=0, column=0, columnspan=3)



conn = sqlite3.connect('DB/primatips4.sqlite')
c = conn.cursor()
c.execute("SELECT PAYS,TEAMS,BET1,BETX,BET2,SCORE,RESULTAT,PM,BUT FROM primatips_table")
rows = c.fetchall()
conn.close()

update_treeview(rows)

root.mainloop()
