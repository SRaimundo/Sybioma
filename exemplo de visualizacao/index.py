from tkinter import *
from PIL import ImageTk, Image  # type "Pip install pillow" in your terminal to install ImageTk and Image module
from tkinter import messagebox
from SybiomaDB import *


window = Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
# window.attributes('-zoomed', True) #Habilitar em caso de sistema linux
window.state('zoomed') #Desabilitar em caso de sistema linux
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
codigo = StringVar()
codigo_raio = StringVar()

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

def Reconnection():
    NomeBanco = database_name.get()
    conta = user_name.get()
    senha = str(password_entry.get())
    try:
        banco.setConnection('localhost',NomeBanco,conta, senha)
    except:
        messagebox.showwarning('Error', 'Senha ou login invalidos')
        return


def Plotar_Imovel():
    try:
        show_frame(design_frame12)
        imovel_buscado = str(codigo_busca.get() )
        banco.plotImovel(imovel_buscado)
        show_frame(CommandPage)
    except:
        messagebox.showwarning('Error', 'Erro ao plotar imovel')
        Reconnection()
        show_frame(CommandPage)
        return
    
def Plotar_Imovel_Vizinhos():
    try:
        show_frame(design_frame12)
        imovel_buscado = str(codigo_busca.get() )
        raio_de_busca = str(codigo_raio.get() )
        banco.plotImovelVizinhos(imovel_buscado,raio_de_busca)
        show_frame(CommandPage)
    except:
        messagebox.showwarning('Error', 'Erro ao plotar imovel')
        Reconnection()
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


# # ===== Utilitarios Label ==============
# utilitario_label =  Label(design_frame4, text='Utilitarios', font=('Arial', 15, 'bold'), bg='#f8f8f8')
# utilitario_label.place(x=10, y=15) #105 25

# # ===== App Label ==============
# app_label = Label(design_frame4, text='App', font=('Arial', 15, 'bold'), bg='#f8f8f8')
# app_label.place(x=10, y=100)

# # ===== Area Imovel Label ==============
# areaImovel_label = Label(design_frame4, text='Area Imovel', font=('Arial', 15, 'bold'), bg='#f8f8f8')
# areaImovel_label.place(x=10, y=185)

# # ===== App Recompor Label ==============
# AppRecompor = Label(design_frame4, text='App Recompor', font=('Arial', 15, 'bold'), bg='#f8f8f8')
# AppRecompor.place(x=10, y=270)

# # ===== Imovel App Label ==============
# AppRecompor = Label(design_frame4, text='Imovel App', font=('Arial', 15, 'bold'), bg='#f8f8f8')
# AppRecompor.place(x=10, y=415)



# ======= account ===========
codigo_label = Label(design_frame4, text='•Insira o codigo do imovel ou da cidade para consulta', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
codigo_label.place(x=170, y=70)
codigo_busca = Entry(design_frame4, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2,
                    textvariable=codigo)
codigo_busca.place(x=150, y=100, width=486, height=34)
codigo_busca.config(highlightbackground="black", highlightcolor="black")


raio_label = Label(design_frame4, text='•Insira o raio para pesquisar imoveis vizinhos na consulta', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
raio_label.place(x=170, y=150)
codigo_raio = Entry(design_frame4, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2,
                    textvariable=codigo_raio)
codigo_raio.place(x=293, y=180, width=200, height=34)
codigo_raio.config(highlightbackground="black", highlightcolor="black")



# ==== Commands buttons  down button ============


# plotar codImovel
Command1 = Button(design_frame4, fg='#f8f8f8', text='Plotar Imovel', bg='#1b87d2', font=("yu gothic ui bold", 11),
                   cursor='hand2', activebackground='#1b87d2', command=Plotar_Imovel)
Command1.place(x=10, y=255, width=200, height=50)

# plotar codImovel e vizinhos
Command1 = Button(design_frame4, fg='#f8f8f8', text='Plotar Imovel e vizinhos', bg='#1b87d2', font=("yu gothic ui bold", 11),
                   cursor='hand2', activebackground='#1b87d2', command=Plotar_Imovel_Vizinhos)
Command1.place(x=240, y=255, width=200, height=50)




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
