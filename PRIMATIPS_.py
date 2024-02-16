#Create window 
#Create button 
#Create label 

from tkinter import *
import my_fonction
   
Mywindow=Tk()
Mywindow.geometry("780x580")
Mywindow.title("PRIMATIPS BET")
Mywindow.config(background="#165e8e")
Mywindow.iconbitmap("IMG/PRIMATIPS_ICO.ico")


"""
frame=Frame(Mywindow, bg="#fff")

Bet1=Label(frame,text="1", fg="#edf0f2", bg="#165e8e", font=("courrier",24))
Bet1.pack()
zone_1=Entry(frame)
zone_1.pack()

BetX=Label(frame,text="X", fg="#edf0f2", bg="#165e8e", font=("courrier",24))
BetX.pack()
zone_X=Entry(frame)
zone_X.pack()

Bet2=Label(frame,text="2", fg="#edf0f2", bg="#165e8e", font=("courrier",24))
Bet2.pack()
zone_2=Entry(frame)
zone_2.pack()

But_Valide=Button(frame,text="Validé", command=Valide)
But_Valide.pack()

frame.pack(expand=YES)
"""
# Label and Entry for Titre 
Titre=Label(Mywindow,text="Welcome to PRIMATIPS BET", fg="#000", bg="#FFF", font=("courrier,52"))
Titre.grid(row=0, columnspan=2, column=3)

# Label and Entry for LOGO 
img= PhotoImage(file="IMG/PRIMATIPS_LOGO.png").zoom(32).subsample(32)
canvas=Canvas(Mywindow,width=132,height=119,bg="#165e8e",bd=0,highlightthickness=0)
canvas.create_image(132/2,119/2,image=img)
canvas.grid(row=1, columnspan=2, column=3)

# Label and Entry for 1
Label(Mywindow, text="1", fg="white", bg="#165e8e", font=("courier", 16)).grid(row=2, column=0)
my_fonction.entry_Bet1 = Entry(Mywindow)
my_fonction.entry_Bet1.grid(row=2, column=1)

# Label and Entry for X
Label(Mywindow, text="X", fg="white", bg="#165e8e", font=("courier", 16)).grid(row=3, column=0)
my_fonction.entry_BetX = Entry(Mywindow)
my_fonction.entry_BetX.grid(row=3, column=1)

# Label and Entry for 2
Label(Mywindow, text="2", fg="white", bg="#165e8e", font=("courier", 16)).grid(row=4, column=0)
my_fonction.entry_Bet2 = Entry(Mywindow)
my_fonction.entry_Bet2.grid(row=4, column=1)

# Button to display the entered values
Button(text="Afficher", command=my_fonction.afficher).grid(row=5, columnspan=1)

# Label to display the entered values
my_fonction.result_label = Label(Mywindow, text="", font=("Arial", 12))
my_fonction.result_label.grid(row=6, columnspan=1)


Mywindow.mainloop()