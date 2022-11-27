from tkinter import *
from PIL import ImageTk, Image  # type "Pip install pillow" in your terminal to install ImageTk and Image module
# import sqlite3
from tkinter import messagebox
from SybiomaDB import *


window = Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.attributes('-zoomed', True)
# window.configure(background='#3F79F2')
# window.state('zoomed')
window.resizable(0, 0)
window.title('Sybioma System')


# Window Icon Photo
icon = PhotoImage('images/pic_icon.png')
window.iconphoto(True, icon)

CommandPage = Frame(window)
LoginPage = Frame(window)

for frame in (CommandPage, LoginPage):
    frame.grid(row=0, column=0, sticky='nsew')


def show_frame(frame):
    frame.tkraise()


show_frame(LoginPage)


# ========== DATABASE  ============
Conta = StringVar()
DataBaseName = StringVar()
Password = StringVar()
ConfirmPassword = StringVar()
banco = SybiomaDB()

def connection():
    NomeBanco = database_name.get()
    conta = user_name.get()
    senha = str(password_entry.get())
    try:
        banco.setConnection('localhost',NomeBanco,conta, senha)
        show_frame(CommandPage)
    except:
        messagebox.showwarning('Error', 'Senha ou login invalidos')
        return

def CriaApp():
    banco.criarTabelaAPP()

def CriaAreaImovel():
    banco.criarTabelaAreaImovel

def InsereApp():
    banco.percorreShapesApp()

def InsereAreaImovel():
    banco.percorreShapesAreaImovel

# =====================================================================================================================
# =====================================================================================================================
# ==================== LOGIN PAGE =====================================================================================
# =====================================================================================================================
# =====================================================================================================================

# COMANDOS

#fundo da paginda de Comandos
design_frame1 = Listbox(CommandPage, bg='#0c71b9', highlightthickness=0, borderwidth=0)
design_frame1.place(relx=0, rely=0,relwidth = 1, relheight = 1)

design_frame2 = Listbox(CommandPage, bg='#1e85d0', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame2.place(x=676, y=0)

design_frame3 = Listbox(CommandPage, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame3.place(x=75, y=106)

design_frame4 = Listbox(CommandPage, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame4.place(x=676, y=106)

# ====== Email ====================
# user_name = Entry(design_frame4, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2,
#                     textvariable=Email)
# user_name.place(x=134, y=170, width=256, height=34)
# user_name.config(highlightbackground="black", highlightcolor="black")
# email_label = Label(design_frame4, text='• Email account', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
# email_label.place(x=130, y=140)

# ==== Password ==================
# password_entry1 = Entry(design_frame4, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2,
#                         textvariable=Password)
# password_entry1.place(x=134, y=250, width=256, height=34)
# password_entry1.config(highlightbackground="black", highlightcolor="black")
# password_label = Label(design_frame4, text='• Password', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
# password_label.place(x=130, y=220)


# function for show and hide password
# def password_command():
#     if password_entry1.cget('show') == '•':
#         password_entry1.config(show='')
#     else:
#         password_entry1.config(show='•')


# ====== checkbutton ==============
# checkButton = Checkbutton(design_frame4, bg='#f8f8f8', command=password_command, text='show password')
# checkButton.place(x=140, y=288)

# ========= Buttons ===============
# SignUp_button = Button(CommandPage, text='Sign up', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
#                        command=lambda: show_frame(LoginPage), borderwidth=0, activebackground='#1b87d2', cursor='hand2')
# SignUp_button.place(x=1100, y=175)

# ===== Welcome Label ==============
welcome_label = Label(design_frame4, text='Welcome', font=('Arial', 20, 'bold'), bg='#f8f8f8')
welcome_label.place(x=130, y=15)

# ======= top Login Button =========
# login_button = Button(CommandPage, text='Login', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
#                       borderwidth=0, activebackground='#1b87d2', cursor='hand2')
# login_button.place(x=845, y=175)

# login_line = Canvas(CommandPage, width=60, height=5, bg='#1b87d2')
# login_line.place(x=840, y=203)

# ==== Commands buttons  down button ============
Command1 = Button(design_frame4, fg='#f8f8f8', text='Criar tabela App', bg='#1b87d2', font=("yu gothic ui bold", 12),
                   cursor='hand2', activebackground='#1b87d2', command=CriaApp)
Command1.place(x=10, y=120, width=215, height=50)

# Comando 2
Command2 = Button(design_frame4, fg='#f8f8f8', text='Criar tabela AreaImovel', bg='#1b87d2', font=("yu gothic ui bold", 12),
                   cursor='hand2', activebackground='#1b87d2', command=CriaAreaImovel)
Command2.place(x=235, y=120, width=215, height=50)

# Comando 3
Command3 = Button(design_frame4, fg='#f8f8f8', text='Inserir shapes App', bg='#1b87d2', font=("yu gothic ui bold", 12),
                   cursor='hand2', activebackground='#1b87d2', command=InsereApp)
Command3.place(x=470, y=120, width=215, height=50)

#Comando 4


Command4 = Button(design_frame4, fg='#f8f8f8', text='Inserir shapes AreaImovel', bg='#1b87d2', font=("yu gothic ui bold", 12),
                   cursor='hand2', activebackground='#1b87d2', command=InsereAreaImovel)
Command4.place(x=10, y=190, width=215, height=50)

# Comando 5
Command5 = Button(design_frame4, fg='#f8f8f8', text='Command5', bg='#1b87d2', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#1b87d2', command=lambda: login())
Command5.place(x=235, y=190, width=215, height=50)

# Comando 6
Command6 = Button(design_frame4, fg='#f8f8f8', text='Command6', bg='#1b87d2', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#1b87d2', command=lambda: login())
Command6.place(x=470, y=190, width=215, height=50)

# Comando 7

Command7 = Button(design_frame4, fg='#f8f8f8', text='Command7', bg='#1b87d2', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#1b87d2', command=lambda: login())
Command7.place(x=10, y=260, width=215, height=50)

# Comando 8
Command8 = Button(design_frame4, fg='#f8f8f8', text='Command8', bg='#1b87d2', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#1b87d2', command=lambda: login())
Command8.place(x=235, y=260, width=215, height=50)

# Comando 9
Command9 = Button(design_frame4, fg='#f8f8f8', text='Command9', bg='#1b87d2', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#1b87d2', command=lambda: login())
Command9.place(x=470, y=260, width=215, height=50)

#Comando 10


Command10 = Button(design_frame4, fg='#f8f8f8', text='Command10', bg='#1b87d2', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#1b87d2', command=lambda: login())
Command10.place(x=10, y=330, width=215, height=50)

# Comando 11
Command11 = Button(design_frame4, fg='#f8f8f8', text='Command11', bg='#1b87d2', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#1b87d2', command=lambda: login())
Command11.place(x=235, y=330, width=215, height=50)

# Comando 12
Command12 = Button(design_frame4, fg='#f8f8f8', text='Command12', bg='#1b87d2', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#1b87d2', command=lambda: login())
Command12.place(x=470, y=330, width=215, height=50)

# Comando 13

Command13 = Button(design_frame4, fg='#f8f8f8', text='Command13', bg='#1b87d2', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#1b87d2', command=lambda: login())
Command13.place(x=10, y=400, width=215, height=50)

# Comando 14
Command14 = Button(design_frame4, fg='#f8f8f8', text='Command14', bg='#1b87d2', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#1b87d2', command=lambda: login())
Command14.place(x=235, y=400, width=215, height=50)

# Comando 15
Command15 = Button(design_frame4, fg='#f8f8f8', text='Command15', bg='#1b87d2', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#1b87d2', command=lambda: login())
Command15.place(x=470, y=400, width=215, height=50)

#Comando 16

Command16 = Button(design_frame4, fg='#f8f8f8', text='Command16', bg='#1b87d2', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#1b87d2', command=lambda: login())
Command16.place(x=10, y=470, width=215, height=50)

# Comando 17
Command17 = Button(design_frame4, fg='#f8f8f8', text='Command17', bg='#1b87d2', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#1b87d2', command=lambda: login())
Command17.place(x=235, y=470, width=215, height=50)

# Comando 18
Command18 = Button(design_frame4, fg='#f8f8f8', text='Command18', bg='#1b87d2', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#1b87d2', command=lambda: login())
Command18.place(x=470, y=470, width=215, height=50)



# ======= ICONS =================

# ===== Email icon =========
# email_icon = Image.open('images/email_icon.png')
# photo = ImageTk.PhotoImage(email_icon)
# emailIcon_label = Label(design_frame4, image=photo, bg='#f8f8f8')
# emailIcon_label.image = photo
# emailIcon_label.place(x=105, y=174)

# ===== password icon =========
# password_icon = Image.open('images/pass_icon.png')
# photo = ImageTk.PhotoImage(password_icon)
# password_icon_label = Label(design_frame4, image=photo, bg='#f8f8f8')
# password_icon_label.image = photo
# password_icon_label.place(x=105, y=254)

# ===== picture icon =========
picture_icon = Image.open('images/pic_icon.png')
photo = ImageTk.PhotoImage(picture_icon)
picture_icon_label = Label(design_frame4, image=photo, bg='#f8f8f8')
picture_icon_label.image = photo
picture_icon_label.place(x=280, y=5)

# ===== Left Side Picture ============
side_image = Image.open('images/vector.png')
photo = ImageTk.PhotoImage(side_image)
side_image_label = Label(design_frame3, image=photo, bg='#1e85d0')
side_image_label.image = photo
side_image_label.place(x=50, y=10)



# forgotPassword = Button(design_frame4, text='Forgot password', font=("yu gothic ui", 8, "bold underline"), bg='#f8f8f8',
#                         borderwidth=0, activebackground='#f8f8f8', command=lambda: forgot_password(), cursor="hand2")
# forgotPassword.place(x=290, y=290)


# =====================================================================================================================
# =====================================================================================================================
# =====================================================================================================================


# =====================================================================================================================
# =====================================================================================================================
# ==================== CONECTION PAGE =================================================================================
# =====================================================================================================================
# =====================================================================================================================

# fundo_LoginPage = Listbox(LoginPage,bg='#0c71b9')
# fundo_LoginPage.place(relx=0, rely=0,relwidth = 1, relheight = 1)

#fundo da pagina de login
design_frame5 = Listbox(LoginPage, bg='#0c71b9', highlightthickness=0, borderwidth=0)
design_frame5.place(relx=0, rely=0,relwidth = 1, relheight = 1)

design_frame6 = Listbox(LoginPage, bg='#1e85d0', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame6.place(x=676, y=0)

design_frame7 = Listbox(LoginPage, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame7.place(x=75, y=106)

design_frame8 = Listbox(LoginPage, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame8.place(x=676, y=106)

# ==== Full Name =======
database_name = Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2,
                   textvariable=DataBaseName)
database_name.place(x=130, y=150, width=286, height=34)
database_name.config(highlightbackground="black", highlightcolor="black")
name_label = Label(design_frame8, text='•Database Name', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
name_label.place(x=126, y=120)

# ======= account ===========
user_name = Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2,
                    textvariable=Conta)
user_name.place(x=130, y=220, width=286, height=34)
user_name.config(highlightbackground="black", highlightcolor="black")
email_label = Label(design_frame8, text='•User account', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
email_label.place(x=120, y=190)

# ====== Password =========
password_entry = Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2,
                       textvariable=Password)
password_entry.place(x=130, y=295, width=286, height=34)
password_entry.config(highlightbackground="black", highlightcolor="black")
password_label = Label(design_frame8, text='• Password', fg="#89898b", bg='#f8f8f8',
                       font=("yu gothic ui", 11, 'bold'))
password_label.place(x=126, y=265)


def password_command2():
    if password_entry.cget('show') == '•':
        password_entry.config(show='')
    else:
        password_entry.config(show='•')


checkButton = Checkbutton(design_frame8, bg='#f8f8f8', command=password_command2, text='show password')
checkButton.place(x=290, y=330)


# ========= Buttons ====================
# SignUp_button = Button(LoginPage, text='Sign up', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
#                        command=lambda: show_frame(CommandPage), borderwidth=0, activebackground='#1b87d2', cursor='hand2')
# SignUp_button.place(x=1100, y=175)

# SignUp_line = Canvas(LoginPage, width=60, height=5, bg='#1b87d2')
# SignUp_line.place(x=1100, y=203)

# ===== Welcome Label ==================
welcome_label = Label(design_frame8, text='Welcome', font=('Arial', 20, 'bold'), bg='#f8f8f8')
welcome_label.place(x=130, y=15)

# ========= Login Button =========
# login_button = Button(LoginPage, text='Login', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
#                       borderwidth=0, activebackground='#1b87d2', command=lambda: show_frame(CommandPage), cursor='hand2')
# login_button.place(x=845, y=175)

# ==== SIGN UP down button ============
Enter_button = Button(design_frame8, fg='#f8f8f8', text='Enter', bg='#1b87d2', font=("yu gothic ui bold", 15),
                 cursor='hand2', activebackground='#1b87d2', command=connection)
Enter_button.place(x=130, y=435, width=286, height=50)

# ===== password icon =========
password_icon = Image.open('images/pass_icon.png')
photo = ImageTk.PhotoImage(password_icon)
password_icon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
password_icon_label.image = photo
password_icon_label.place(x=100, y=300)


# ===== DataBase icon =========
email_icon = Image.open('images/email_icon.png')
photo = ImageTk.PhotoImage(email_icon)
emailIcon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
emailIcon_label.image = photo
emailIcon_label.place(x=100, y=225)

# ===== User icon =========
name_icon = Image.open('images/name_icon.png')
photo = ImageTk.PhotoImage(name_icon)
nameIcon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
nameIcon_label.image = photo
nameIcon_label.place(x=100, y=153)

# ===== picture icon =========
picture_icon = Image.open('images/pic_icon.png')
photo = ImageTk.PhotoImage(picture_icon)
picture_icon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
picture_icon_label.image = photo
picture_icon_label.place(x=280, y=5)

# ===== Left Side Picture ============
side_image = Image.open('images/vector.png')
photo = ImageTk.PhotoImage(side_image)
side_image_label = Label(design_frame7, image=photo, bg='#1e85d0')
side_image_label.image = photo
side_image_label.place(x=50, y=10)


window.mainloop()
