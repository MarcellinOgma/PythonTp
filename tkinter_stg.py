from tkinter import *


# Fonction register
def register():
    winReg = Toplevel(windows)
    windows.withdraw()
    winReg.title("REGISTER")
    winReg.config(bg="#717113")
    winReg.geometry('600x400')
    canevas = Canvas(winReg, width=600, height=400, bg="#717113")
    image = PhotoImage(file="C:\\Users\\Utilisateur\\Desktop\\ANACONDA\\TUTO\\sources\\giphy.gif")
    canevas.create_image(90, 50, anchor=NW, image=image)
    canevas.place(x=0, y=0)
    # Creation des labels
    labelEmail = Label(canevas, text="Email: ", font=("Times New Roman", 15, "bold"),
                       bg="#717113", fg="white")
    labelEmail.place(x=10, y=60)

    labelFirstname = Label(canevas, text="Firstname: ", font=fonts, bg="#717113", fg="white")
    labelFirstname.place(x=10, y=110)

    labelUsername = Label(canevas, text="Username: ", font=fonts, bg="#717113", fg="white")
    labelUsername.place(x=10, y=170)

    labelPassword = Label(canevas, text="Password: ", font=fonts, bg="#717113", fg="white")
    labelPassword.place(x=10, y=230)

    labelCfPass = Label(canevas, text='Conf.Pass: ', font=fonts, bg="#717113", fg="white")
    labelCfPass.place(x=10, y=280)

    # Creation des entry
    entryEmail = Entry(canevas, font=("Times New Roman", 15, "bold"), width=32,
                       bg="#aed0a4", fg="#e8063b",
                       justify="center")
    entryEmail.focus_set()
    entryEmail.place(x=150, y=60)

    entryFirstname = Entry(canevas, font=fonts, width=30, bg="#aed0a4", fg="#e8063b",
                           justify="center")
    entryFirstname.place(x=150, y=110)

    entryUser = Entry(canevas, font=fonts, width=30, bg="#aed0a4", fg="#e8063b",
                      justify="center")
    entryUser.place(x=150, y=170)

    entryPassword = Entry(canevas, font=fonts, width=30, bg="#aed0a4", fg="#e8063b",
                          justify="center", show="*")
    entryPassword.place(x=150, y=230)

    entryCfPassword = Entry(canevas, font=fonts, width=30, bg="#aed0a4", fg="#e8063b",
                            justify='center', show="*")
    entryCfPassword.place(x=150, y=280)

    # Creation du bouton de confirmation

    buttonRegister = Button(canevas, text="Submit", font=fonts, padx=6, bg="#717113", fg="white" )
    buttonRegister.place(x=200, y=330)

    winReg.mainloop()


windows = Tk()
windows.geometry("500x600")
windows.title("Image en fond")
can = Canvas(windows, width=500, height=250, bg="#0ea598")
img = PhotoImage(file="C:\\Users\\Utilisateur\\Desktop\\ANACONDA\\TUTO\\sources\\background.gif")
can.create_image(140, 20, anchor=NW, image=img)
can.place(x=0, y=0)

# Creation des labels
fonts = ("Time New Roman", 15, "bold")
labelUser = Label(can, text='Username', font=fonts, bg="#717113", fg="white")
labelUser.place(x=45, y=40)

labelpass = Label(can, text='Password', font=fonts, bg="#717113", fg="white")
labelpass.place(x=45, y=100)

# Champs de saisie
entryUser = Entry(can, font=fonts, bg="#aed0a4", fg="#e8063b", justify="center")
entryUser.place(x=160, y=40)

entryPass = Entry(can, font=fonts, show="*", bg="#aed0a4", fg="#e8063b", justify="center")
entryPass.place(x=150, y=100)

# Buttons
buttonValid = Button(can, text="valid", font=fonts, padx=20, pady=0, bg="#717113", fg="white")
buttonValid.place(x=110, y=170)

buttonPF = Button(can, text="Password forgot", font=fonts, padx=20, pady=0, bg="#717113", fg="white")
buttonPF.place(x=250, y=170)

# Deuxiemme image


can1 = Canvas(windows, width=500, height=350, bg="#717113")
img1 = PhotoImage(file="C:\\Users\\Utilisateur\\Desktop\\ANACONDA\\TUTO\\sources\\giphy.gif")
can1.create_image(50, 20, anchor=NW, image=img1)
can1.place(x=0, y=250)

# BUTTON D'ENREGITREMENT


buttonPF = Button(can1, text="Sign in", font=fonts, padx=20, pady=0, bg="#717113", fg="white"
                  , command=register)
buttonPF.place(x=190, y=170)

windows.mainloop()
