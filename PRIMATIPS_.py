#Create window 
#Create button 
#Create label 

from tkinter import *
import mysql.connector
import my_fonction
import tkinter as tk

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database= "primatips"
    )

    mycursor = mydb.cursor()
    sql_RES_1_1=f"SELECT COUNT(RESULTAT) FROM primatips_table WHERE BET1 LIKE '1.9' AND RESULTAT LIKE '1'"
    sql_RES_1_X=f"SELECT COUNT(RESULTAT) FROM primatips_table WHERE BET1 LIKE '1.9' AND RESULTAT LIKE 'X'"
    sql_RES_1_2=f"SELECT COUNT(RESULTAT) FROM primatips_table WHERE BET1 LIKE '1.9' AND RESULTAT LIKE '2'"
    sql_RES_1_1X2=f"SELECT COUNT(RESULTAT) FROM primatips_table WHERE BET1 LIKE '1.9' AND BETX LIKE '3.4'  AND BET2 LIKE '4' AND RESULTAT LIKE '1'"
    sql_RES_2="SELECT RESULTAT FROM primatips_table WHERE BET2 LIKE '4.2'"
    
    mycursor.execute(sql_RES_1_1)
    RES_BET_1_1 = mycursor.fetchone()
    mycursor.execute(sql_RES_1_X)
    RES_BET_1_X = mycursor.fetchone()
    mycursor.execute(sql_RES_1_2)
    RES_BET_1_2 = mycursor.fetchone()
    mycursor.execute(sql_RES_1_1X2)
    RES_BET_1_1X2 = mycursor.fetchone()
    # print("connected")

    for RF in RES_BET_1_1:
        print(RF)
    # mydb.commit()
except mysql.connector.Error as r:
    print(r)
# Créer la fenêtre principale
Mywindow = tk.Tk()
Mywindow.geometry("780x580")
Mywindow.title("PRIMATIPS BETT")
Mywindow.config(background="#165e8e")
Mywindow.iconbitmap("IMG/PRIMATIPS_ICO.ico")



# Label and Entry for Titre 
Titre=Label(Mywindow,text="Welcome to PRIMATIPS BET", fg="#000", bg="#FFF", font=("courrier,52"))
Titre.grid(row=0, columnspan=1, column=2)

# Label and Entry for LOGO 
img= PhotoImage(file="IMG/PRIMATIPS_LOGO.png").zoom(32).subsample(32)
canvas=Canvas(Mywindow,width=132,height=119,bg="#165e8e",bd=0,highlightthickness=0)
canvas.create_image(132/2,119/2,image=img)
canvas.grid(row=1, columnspan=2, column=2)

# Label and Entry for 1
Label(Mywindow, text="1", fg="white", bg="#165e8e", font=("courier", 16)).grid(row=2, column=1)
my_fonction.entry_Bet1 = Entry(Mywindow)
my_fonction.entry_Bet1.grid(row=2, column=2)

# Label and Entry for X
Label(Mywindow, text="X", fg="white", bg="#165e8e", font=("courier", 16)).grid(row=3, column=1)
my_fonction.entry_BetX = Entry(Mywindow)
my_fonction.entry_BetX.grid(row=3, column=2)

# Label and Entry for 2
Label(Mywindow, text="2", fg="white", bg="#165e8e", font=("courier", 16)).grid(row=4, column=1)
my_fonction.entry_Bet2 = Entry(Mywindow)
my_fonction.entry_Bet2.grid(row=4, column=2)

# Button to display the entered values
Button(text="Afficher", command=my_fonction.afficher).grid(row=5, columnspan=1, column=2)

# Label to display the entered values
frame=Frame(Mywindow, bg="#FFF" ,width=300, height=300)

cadre = tk.Frame(frame, borderwidth=5, relief="groove")
cadre.grid(row=9, column=2, padx=2, pady=2)

for i in range(4):
    for j in range(8):
        if i==0 and j==1:
            my_fonction.result_label1 = Label(cadre, text="1",
                                                  font=("Arial", 12),relief="groove", borderwidth=10) 
            my_fonction.result_label1.grid(row=i, column=j, padx=2, pady=2, columnspan=1)    
        if i==0 and j==2:
            my_fonction.result_labelX = Label(cadre, text="X",
                                                  font=("Arial", 12),relief="groove", borderwidth=10) 
            my_fonction.result_labelX.grid(row=i, column=j, padx=2, pady=2, columnspan=1)  
        if i==0 and j==3:
            my_fonction.result_label2 = Label(cadre, text="2",
                                                  font=("Arial", 12),relief="groove", borderwidth=10) 
            my_fonction.result_label2.grid(row=i, column=j, padx=2, pady=2, columnspan=1)  
        if i==1 and j==0:
            label = tk.Label(cadre, text="1",
                       relief="groove", borderwidth=10)
            label.grid(row=i, column=j, padx=2, pady=2)  
        if i==2 and j==0:
            label = tk.Label(cadre, text="X",
                       relief="groove", borderwidth=10)
            label.grid(row=i, column=j, padx=2, pady=2)  
        if i==3 and j==0:
            label = tk.Label(cadre, text="2",
                       relief="groove", borderwidth=10)
            label.grid(row=i, column=j, padx=2, pady=2)  
        if i==0 and j==4:
            label = tk.Label(cadre, text="1X2",
                       relief="groove", borderwidth=10)
            label.grid(row=i, column=j, padx=2, pady=2)  
        if i==0 and j==5:
            label = tk.Label(cadre, text="1X",
                       relief="groove", borderwidth=10)
            label.grid(row=i, column=j, padx=2, pady=2)  
        if i==0 and j==6:
            label = tk.Label(cadre, text="12",
                       relief="groove", borderwidth=10)
            label.grid(row=i, column=j, padx=2, pady=2)  
        if i==0 and j==7:
            label = tk.Label(cadre, text="X2",
                       relief="groove", borderwidth=10)
            label.grid(row=i, column=j, padx=2, pady=2) 
        if i==1 and j==1:
            label = tk.Label(cadre, text=f"{RES_BET_1_1}",
                       relief="groove", borderwidth=10)
            label.grid(row=i, column=j, padx=2, pady=2) 
        if i==2 and j==1:
            label = tk.Label(cadre, text=f"{RES_BET_1_X}",
                       relief="groove", borderwidth=10)
            label.grid(row=i, column=j, padx=2, pady=2) 
        if i==3 and j==1:
            label = tk.Label(cadre, text=f"{RES_BET_1_2}",
                       relief="groove", borderwidth=10)
            label.grid(row=i, column=j, padx=2, pady=2) 
        if i==1 and j==4:
            label = tk.Label(cadre, text=f"{RES_BET_1_1X2}",
                       relief="groove", borderwidth=10)
            label.grid(row=i, column=j, padx=2, pady=2) 
frame.grid(row=10, column=2, columnspan=1)

Mywindow.mainloop()