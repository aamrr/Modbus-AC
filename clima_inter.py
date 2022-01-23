from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkcalendar import *
from datetime import date

#definition de fentre
fenetre = Tk()
fenetre.title("Insurability")
fenetre.geometry('520x820')

#insert data label
label = Label(fenetre, text="Inserer les temperatures")
label.grid(column=1,row=1,pady=30,columnspan=3)

#TEMP1 line
TEMP1_LABEL = Label(fenetre, text="TEMP1: ")
TEMP1_LABEL.grid(column=1,row=2,pady=10)
TEMP1 = Entry(fenetre,width=10)
TEMP1.grid(column=2, row=2,columnspan=2)

#TEMP2 line
TEMP2_label = Label(fenetre, text="TEMP2: ")
TEMP2_label.grid(column=2,row=3,pady=10)
TEMP2 = Entry(fenetre,width=10)
TEMP2.grid(column=2, row=3,columnspan=2)

#Prenom line
TEMP3_label = Label(fenetre, text="TEMP3: ")
TEMP3_label.grid(column=2,row=4,pady=10)
TEMP3 = Entry(fenetre,width=10)
TEMP3.grid(column=2, row=4,columnspan=2)


result = Label(fenetre, text="")
result.grid(column=2,row=11,columnspan=2)

def clicked():

	tmp2 = int(TEMP1.get())
	tmp2 = int(TEMP2.get())
	tmp3 = int(TEMP3.get())

	



bt = Button(fenetre,text="Transfer",command=clicked)
bt.grid(column=1,row=11,pady=10)



fenetre.mainloop()