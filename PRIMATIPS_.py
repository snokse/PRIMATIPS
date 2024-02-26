#Create window 
#Create button 
#Create label 

from tkinter import *
import mysql.connector
import my_fonction

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database= "primatips_db"
    )

    mycursor = mydb.cursor()
    sql_RES_1="SELECT COUNT(RF) FROM primatips_table WHERE BET_1 LIKE '1.7'"
    sql_RES_X="SELECT RF FROM primatips_table WHERE BET_X LIKE '3.2'"
    sql_RES_2="SELECT RF FROM primatips_table WHERE BET_2 LIKE '4.2'"
    
    mycursor.execute(sql_RES_1)
    RES_BET_1 = mycursor.fetchall()
    #print("connected")

    for RF in RES_BET_1:
        print(RF)
    # mydb.commit()
except mysql.connector.Error as r:
    print(r)

Mywindow=Tk()
Mywindow.geometry("780x580")
Mywindow.title("PRIMATIPS BET")
Mywindow.config(background="#165e8e")
Mywindow.iconbitmap("IMG/PRIMATIPS_ICO.ico")


# Label and Entry for Titre 
Titre=Label(Mywindow,text="Welcome to PRIMATIPS BET", fg="#000", bg="#FFF", font=("courrier,52"))
Titre.grid(row=0, columnspan=1, column=3)

# Label and Entry for LOGO 
img= PhotoImage(file="IMG/PRIMATIPS_LOGO.png").zoom(32).subsample(32)
canvas=Canvas(Mywindow,width=132,height=119,bg="#165e8e",bd=0,highlightthickness=0)
canvas.create_image(132/2,119/2,image=img)
canvas.grid(row=1, columnspan=2, column=3)

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

Label(frame, text="1 - X - 2 - 1X2 - 1X - 12 - X2", fg="white", bg="#165e8e", font=("courier", 16)).grid(row=5, column=2)

my_fonction.result_label1 = Label(frame, text="1", font=("Arial", 12))
my_fonction.result_label1.grid(row=6, columnspan=1)

my_fonction.result_labelX = Label(frame, text="X", font=("Arial", 12))
my_fonction.result_labelX.grid(row=7, columnspan=1)

my_fonction.result_label2 = Label(frame, text="2", font=("Arial", 12))
my_fonction.result_label2.grid(row=8, columnspan=1)



frame.grid(row=6, column=2, columnspan=1)


Mywindow.mainloop()