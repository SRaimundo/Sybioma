from tkinter import *
from PIL import ImageTk, Image  # type "Pip install pillow" in your terminal to install ImageTk and Image module
# import sqlite3
from tkinter import messagebox
from SybiomaDB import *
from descompactador import descompactar


window = Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
# window.attributes('-zoomed', True)
window.state('zoomed')
window.resizable(0, 0)
window.title('Sybioma System')


# Window Icon Photo
icon = PhotoImage(file='images/pic_icon.png')
window.iconphoto(True, icon)

CommandPage = Frame(window)
LoginPage = Frame(window)
LoadingPage = Frame(window)

for frame in (CommandPage, LoginPage, LoadingPage):
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
        messagebox.showinfo(title='', message='Conexao bem sucedida')
        show_frame(CommandPage)
    except:
        messagebox.showwarning('Error', 'Senha ou login invalidos')
        return

def CriaApp():
    try:
        show_frame(LoadingPage)
        banco.criarTabelaAPP()
        messagebox.showinfo(title='', message='Tabela App criada com sucesso')
        show_frame(CommandPage)
    except:
        messagebox.showwarning('Error', 'Erro ao criar Tabela App')
        show_frame(CommandPage)
        return

def CriarAppRecompor():
    try:
        show_frame(LoadingPage)
        banco.criarTabelaAPPRecompor()
        messagebox.showinfo(title='', message='Tabela AppRecompor criada com sucesso')
        show_frame(CommandPage)
    except:
        messagebox.showwarning('Error', 'Erro ao criar Tabela App Recompor')
        show_frame(CommandPage)
        return

def CriarImovApp():
    try:
        show_frame(LoadingPage)
        banco.criarTabelaImovApp()
        messagebox.showinfo(title='', message='Tabela ImovApp criada com sucesso')
        show_frame(CommandPage)
    except:
        messagebox.showwarning('Error', 'Erro ao criar Tabela Imovel App')
        show_frame(CommandPage)
        return

def populaImovApp():
    try:
        show_frame(LoadingPage)
        banco.populaImovApp()
        messagebox.showinfo(title='', message='ImovApp populada com sucesso')
        show_frame(CommandPage)
    except:
        messagebox.showwarning('Error', 'Erro ao popular tabela Imovel App')
        show_frame(CommandPage)
        return


def CriaAreaImovel():
    try:
        show_frame(LoadingPage)
        banco.criarTabelaAreaImovel()
        messagebox.showinfo(title='', message='Tabela Area Imovel criada com sucesso')
        show_frame(CommandPage)
    except:
        messagebox.showwarning('Error', 'Erro ao criar Tabela Area Imovel')
        show_frame(CommandPage)
        return

def InsereApp():
    try:
        show_frame(LoadingPage)
        banco.percorreShapesApp()
        messagebox.showinfo(title='Concluido', message='Shapes inseridos na tabela App')
        show_frame(CommandPage)
    except:
        messagebox.showwarning('Error', 'Erro ao inserir dados na tabela App')
        show_frame(CommandPage)
        return

def InsereAreaImovel():
    try:
        show_frame(LoadingPage)
        banco.percorreShapesAreaImovel()
        messagebox.showinfo(title='Concluido', message='Shapes inseridos na tabela Area Imovel')
        show_frame(CommandPage)
    except:
        messagebox.showwarning('Error', 'Erro ao inserir dados na tabela Area Imovel')
        show_frame(CommandPage)
        return

def corrigirTextoApp():
    try:
        show_frame(LoadingPage)
        banco.corrigirTextoApp()
        show_frame(CommandPage)
    except:
        messagebox.showwarning('Error', 'Erro ao corrigir formatacao da App')
        show_frame(CommandPage)
        return

def corrigirTextoAppRecompor():
    try:
        show_frame(LoadingPage)
        banco.corrigirTextoAppRecompor()
        show_frame(CommandPage)
    except:
        messagebox.showwarning('Error', 'Erro ao corrigir formatacao da App Recompor')
        show_frame(CommandPage)
        return

def corrigirTextoAreaImovelCond():
    try:
        show_frame(LoadingPage)
        banco.corrigirTextoAreaImovelCond()
        show_frame(CommandPage)
    except:
        messagebox.showwarning('Error', 'Erro ao corrigir formatacao da Condicao em Area Imovel')
        show_frame(CommandPage)
        return

def corrigirTextoAreaImovelNom():
    try:
        show_frame(LoadingPage)
        banco.corrigirTextoAreaImovelNom()
        show_frame(CommandPage)
    except:
        messagebox.showwarning('Error', 'Erro ao corrigir formatacao de Nom_Tema em Area Imovel')
        show_frame(CommandPage)
        return

def criaGeoIndiceRecompor():
    try:
        show_frame(LoadingPage)
        banco.criaGeoIndiceRecompor()
        messagebox.showinfo(title='Concluido', message='Geo indice criado com sucesso na tabela App Recompor')
        show_frame(CommandPage)
    except:
        messagebox.showwarning('Error', 'Erro ao criar indice Geometrico em App Recompor')
        show_frame(CommandPage)
        return

def criaGidIndiceRecompor():
    try:
        show_frame(LoadingPage)
        banco.criaGidIndiceRecompor()
        messagebox.showinfo(title='Concluido', message='Indice no GID criado com sucesso na tabela App Recompor')
        show_frame(CommandPage)
    except:
        messagebox.showwarning('Error', 'Erro ao criar indice do GID em App Recompor')
        show_frame(CommandPage)
        return

def criaCodImovelIndiceRecompor():
    try:
        show_frame(LoadingPage)
        banco.criaCodImovelIndiceRecompor()
        messagebox.showinfo(title='Concluido', message='Indice codigo imovel criado com sucesso na tabela App Recompor')
        show_frame(CommandPage)
    except:
        messagebox.showwarning('Error', 'Erro ao criar indice do codigo imovel em App Recompor')
        show_frame(CommandPage)
        return

def descompacta():
    try:
        show_frame(LoadingPage)
        descompactar()
        messagebox.showinfo(title='Concluido', message='Itens descompatados com sucesso')
        show_frame(CommandPage)
    except:
        messagebox.showwarning('Error', 'Erro ao descompactar arquivos')
        show_frame(CommandPage)
        return




 

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


# ===== Utilitarios Label ==============
utilitario_label = Label(design_frame4, text='Utilitarios', font=('Arial', 15, 'bold'), bg='#f8f8f8')
utilitario_label.place(x=10, y=15) #105 25

# ===== App Label ==============
app_label = Label(design_frame4, text='App', font=('Arial', 15, 'bold'), bg='#f8f8f8')
app_label.place(x=10, y=120)

# ===== Area Imovel Label ==============
areaImovel_label = Label(design_frame4, text='Area Imovel', font=('Arial', 15, 'bold'), bg='#f8f8f8')
areaImovel_label.place(x=10, y=225)

# ===== App Recompor Label ==============
AppRecompor = Label(design_frame4, text='App Recompor', font=('Arial', 15, 'bold'), bg='#f8f8f8')
AppRecompor.place(x=10, y=330)

# ===== Imovel App Label ==============
AppRecompor = Label(design_frame4, text='Imovel App', font=('Arial', 15, 'bold'), bg='#f8f8f8')
AppRecompor.place(x=10, y=485)



# ==== Commands buttons  down button ============

# Comando 18
Command18 = Button(design_frame4, fg='#f8f8f8', text='Descompactar pasta', bg='#1b87d2', font=("yu gothic ui bold", 11),
                   cursor='hand2', activebackground='#1b87d2', command=descompacta)
Command18.place(x=10, y=40, width=195, height=50)

# APP
Command1 = Button(design_frame4, fg='#f8f8f8', text='Criar tabela App', bg='#1b87d2', font=("yu gothic ui bold", 11),
                   cursor='hand2', activebackground='#1b87d2', command=CriaApp)
Command1.place(x=10, y=145, width=200, height=50)

# Comando 2
Command2 = Button(design_frame4, fg='#f8f8f8', text='Inserir shapes App', bg='#1b87d2', font=("yu gothic ui bold", 11),
                   cursor='hand2', activebackground='#1b87d2', command=InsereApp)
Command2.place(x=215, y=145, width=200, height=50)

# AREA IMOVEL
#Comando 3
Command3 = Button(design_frame4, fg='#f8f8f8', text='Inserir shapes AreaImovel', bg='#1b87d2', font=("yu gothic ui bold", 11),
                   cursor='hand2', activebackground='#1b87d2', command=InsereAreaImovel)
Command3.place(x=215, y=250, width=200, height=50)

# Comando 4
Command4 = Button(design_frame4, fg='#f8f8f8', text='Criar tabela AreaImovel', bg='#1b87d2', font=("yu gothic ui bold", 11),
                   cursor='hand2', activebackground='#1b87d2', command=CriaAreaImovel)
Command4.place(x=10, y=250, width=200, height=50)

# APP RECOMPOR
# Comando 5
Command5 = Button(design_frame4, fg='#f8f8f8', text='Criar App Recompor', bg='#1b87d2', font=("yu gothic ui bold", 11),
                   cursor='hand2', activebackground='#1b87d2', command=CriarAppRecompor)
Command5.place(x=10, y=355, width=200, height=50)

# Comando 6
Command6 = Button(design_frame4, fg='#f8f8f8', text='Criar Geo indice App Recompor', bg='#1b87d2', font=("yu gothic ui bold", 9),
                   cursor='hand2', activebackground='#1b87d2', command=criaGeoIndiceRecompor)
Command6.place(x=215, y=355, width=200, height=50)

# Comando 7

Command7 = Button(design_frame4, fg='#f8f8f8', text='Criar indice gid App Recompor', bg='#1b87d2', font=("yu gothic ui bold", 9),
                   cursor='hand2', activebackground='#1b87d2', command=criaGidIndiceRecompor)
Command7.place(x=420, y=355, width=195, height=50)

# Comando 8
Command8 = Button(design_frame4, fg='#f8f8f8', text='Criar CodImovel indice Recompor', bg='#1b87d2', font=("yu gothic ui bold", 8),
                   cursor='hand2', activebackground='#1b87d2', command=criaCodImovelIndiceRecompor)
Command8.place(x=10, y=405, width=200, height=50)

# IMOVEL APP

# Comando 9

Command9 = Button(design_frame4, fg='#f8f8f8', text='Criar tabela Imovel App', bg='#1b87d2', font=("yu gothic ui bold", 11),
                cursor='hand2', activebackground='#1b87d2', command=CriarImovApp)
Command9.place(x=10, y=510, width=200, height=50)

# Comando 10
Command10 = Button(design_frame4, fg='#f8f8f8', text='Popular Imovel App com os dados', bg='#1b87d2', font=("yu gothic ui bold",8),
                cursor='hand2', activebackground='#1b87d2', command=populaImovApp)
Command10.place(x=215, y=510, width=200, height=50)



# # Comando 11
# Command11 = Button(design_frame4, fg='#f8f8f8', text='Corrigir formatacao App', bg='#1b87d2', font=("yu gothic ui bold", 11),
#                    cursor='hand2', activebackground='#1b87d2', command=corrigirTextoApp)
# Command11.place(x=470, y=260, width=215, height=50)

# #Comando 12


# Command12 = Button(design_frame4, fg='#f8f8f8', text='Corrigir formatacao App Recompor', bg='#1b87d2', font=("yu gothic ui bold", 9),
#                    cursor='hand2', activebackground='#1b87d2', command=corrigirTextoAppRecompor)
# Command12.place(x=10, y=330, width=215, height=50)

# # Comando 13
# Command13 = Button(design_frame4, fg='#f8f8f8', text='Corrigir Condicao Area Imovel', bg='#1b87d2', font=("yu gothic ui bold", 9),
#                    cursor='hand2', activebackground='#1b87d2', command=corrigirTextoAreaImovelCond)
# Command13.place(x=235, y=330, width=215, height=50)

# # Comando 14
# Command14 = Button(design_frame4, fg='#f8f8f8', text='Corrigir NOM_TEMA Area Imovel', bg='#1b87d2', font=("yu gothic ui bold", 9),
#                    cursor='hand2', activebackground='#1b87d2', command=corrigirTextoAreaImovelNom)
# Command14.place(x=470, y=330, width=215, height=50)


# # Comando 15
# Command15 = Button(design_frame4, fg='#f8f8f8', text='Command15', bg='#1b87d2', font=("yu gothic ui bold", 15),
#                    cursor='hand2', activebackground='#1b87d2', command=lambda: login())
# Command15.place(x=470, y=400, width=215, height=50)

# #Comando 16

# Command16 = Button(design_frame4, fg='#f8f8f8', text='Command16', bg='#1b87d2', font=("yu gothic ui bold", 15),
#                    cursor='hand2', activebackground='#1b87d2', command=lambda: login())
# Command16.place(x=10, y=470, width=215, height=50)

# # Comando 17
# Command17 = Button(design_frame4, fg='#f8f8f8', text='Command17', bg='#1b87d2', font=("yu gothic ui bold", 15),
#                    cursor='hand2', activebackground='#1b87d2', command=lambda: login())
# Command17.place(x=235, y=470, width=215, height=50)

# # Comando 18
# Command18 = Button(design_frame4, fg='#f8f8f8', text='Command18', bg='#1b87d2', font=("yu gothic ui bold", 15),
#                    cursor='hand2', activebackground='#1b87d2', command=lambda: login())
# Command18.place(x=470, y=470, width=215, height=50)



# # ===== picture icon =========
# picture_icon = Image.open('images/pic_icon.png')
# photo = ImageTk.PhotoImage(picture_icon)
# picture_icon_label = Label(design_frame4, image=photo, bg='#f8f8f8')
# picture_icon_label.image = photo
# picture_icon_label.place(x=280, y=5)

# ===== Left Side Picture ============
side_image = Image.open('images/vector.png')
photo = ImageTk.PhotoImage(side_image)
side_image_label = Label(design_frame3, image=photo, bg='#1e85d0')
side_image_label.image = photo
side_image_label.place(x=50, y=10)




# =====================================================================================================================
# =====================================================================================================================
# =====================================================================================================================


# =====================================================================================================================
# =====================================================================================================================
# ==================== CONECTION PAGE =================================================================================
# =====================================================================================================================
# =====================================================================================================================

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


# ===== Welcome Label ==================
welcome_label = Label(design_frame8, text='Welcome', font=('Arial', 20, 'bold'), bg='#f8f8f8')
welcome_label.place(x=130, y=15)


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




# =====================================================================================================================
# =====================================================================================================================
# ==================== LOADING PAGE =================================================================================
# =====================================================================================================================
# =====================================================================================================================

#fundo da pagina de Carregamento
design_frame9 = Listbox(LoadingPage, bg='#0c71b9', highlightthickness=0, borderwidth=0)
design_frame9.place(relx=0, rely=0,relwidth = 1, relheight = 1)

design_frame10 = Listbox(LoadingPage, bg='#1e85d0', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame10.place(x=676, y=0)

design_frame11 = Listbox(LoadingPage, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame11.place(x=75, y=106)

design_frame12 = Listbox(LoadingPage, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame12.place(x=676, y=106)


# ===== Loading Label ==================
loading_label = Label(design_frame12, text='Carregando. Por favor aguarde!', font=('Arial', 20, 'bold'), bg='#f8f8f8')
loading_label.place(x=150, y=250)

# ===== Left Side Picture ============
side_image = Image.open('images/vector.png')
photo = ImageTk.PhotoImage(side_image)
side_image_label = Label(design_frame11, image=photo, bg='#1e85d0')
side_image_label.image = photo
side_image_label.place(x=50, y=10)




window.mainloop()
