from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from tkinter import filedialog
# import TesteCodigo

import psycopg2
import sys
import os
import geopandas as gpd

class SybiomaDB:

    _sslmode = "require"

    def __init__(self,host,dbname,user,password):
        self._host = host
        self._dbname = dbname
        self._user = user
        self._password = password
        con_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(self._host, self._user, self._dbname, self._password, self._sslmode)
        self._connection = psycopg2.connect(con_string) 
        self._cursor = self._connection.cursor()
    
    def __del__(self):
        self._cursor.close()
        self._connection.close()
    
    def criarTabelaAPP(self):
        with open("commandApp.txt","r") as arquivo:
            comando = arquivo.read()
        self._cursor.execute(comando)
    
    def criarTabelaAreaImovel(self):
        with open("commandAreaImovel.txt","r") as arquivo:
            comando = arquivo.read()
        self._cursor.execute(comando)
    
    def insertApp(self, cod_cidade, IDF, NOM_TEMA, NUM_AREA, geometry):
        NOM_TEMA = NOM_TEMA.replace("\'","")
        with open("commandInsertApp.txt","r") as arquivo:
            comando = arquivo.read().format(cod_cidade, IDF, NOM_TEMA, NUM_AREA, geometry)
        self._cursor.execute(comando)
    
    def insertAreaImovel(self, COD_IMOVEL,NUM_AREA, COD_ESTADO, NOM_MUNICI, NUM_MODULO, TIPO_IMOVE, SITUACAO, CONDICAO_I, geometry):
        with open("commandInsertAreaImovel.txt","r") as arquivo:
            comando = arquivo.read().format(COD_IMOVEL,NUM_AREA, COD_ESTADO, NOM_MUNICI, NUM_MODULO, TIPO_IMOVE, SITUACAO, CONDICAO_I, geometry)
        self._cursor.execute(comando)
    
    def percorreShapesApp(self,diretorio):
        lista_dir_atual = os.listdir(diretorio)

        for shapes in lista_dir_atual:
            if f'APP.shp' in os.listdir(f'{diretorio}/{shapes}'):
                table = gpd.read_file(f'{diretorio}/{shapes}/APP.shp' , encoding='utf-8',char_decode_errors='ignore')
                quant = table.shape[0]
                i = 0
                while i<quant :
                    self.insertApp(shapes.split("E_")[1], table.IDF[i], str(table.NOM_TEMA[i]), table.NUM_AREA[i], table.geometry[i])
                    i+=1

    
    def percorreShapesAreaImovel(self,diretorio):
        lista_dir_atual = os.listdir(diretorio)

        for shapes in lista_dir_atual:
            if os.path.isdir(f'{diretorios}/{shapes}'):
                if f'AREA_IMOVEL.shp' in os.listdir(f'{diretorio}/{shapes}'):
                    table = gpd.read_file(f'{diretorio}/{shapes}/AREA_IMOVEL.shp' , encoding='utf-8',char_decode_errors='ignore')
                    quant = table.shape[0]
                    i = 0
                    while i<quant :
                        self.insertAreaImovel(shapes.split("E_")[1],table.COD_IMOVEL[i],table.NUM_AREA[i], table.COD_ESTADO[i], table.NOM_MUNICI[i], table.NUM_MODULO[i], table.TIPO_IMOVE[i], table.SITUACAO[i], table.CONDICAO_I[i], table.geometry[i])
                        i+=1


class CreateTela: 
    def __init__(self):
        self.TelaLogin()
        self.TelaGerenciamento()



    def TelaLogin(self):
        #colors
        co1 = "white"
        co2 = "black"
        co3 = "#6074FF"


        def check_login():
            name = e_name.get()
            password = str(e_password.get())
            try:
                self.banco = SybiomaDB('localhost','teste',name, password)
            except:
                messagebox.showwarning('Error', 'Senha ou login invalidos')
                return
            window.destroy()


        window = Tk()
        window.title("")
        window.geometry('310x300')
        window.resizable(width=False, height=False)
        window.configure(bg=co1)

        # frames
        frame_up = Frame(window, width=310, height=50, bg=co1)
        frame_up.grid(row=0, column=0)

        frame_down = Frame(window, width=310, height=300, bg=co1)
        frame_down.grid(row=1, column=0)

        # frame_up widgets
        heading = Label(frame_up, text = "LOGIN", bg = co1, font=('Poppins 23'))
        heading.place(x=5, y=5)

        line = Label(frame_up, width=40, text="", height=1, bg=co3, anchor=NW)
        line.place(x=10, y=45)

        # frame_down widgets
        username = Label(frame_down, text="username *", height=1, anchor=NW, bg=co1, fg=co2, font=('Poppins 12'))
        username.place(x=10, y=10)

        e_name = Entry(frame_down, width=25, justify='left', font=("", 15), highlightthickness=1)
        e_name.place(x=14, y=48)

        password = Label(frame_down, text="password *", height=1, anchor=NW, bg=co1, fg=co2, font=('Poppins 12'))
        password.place(x=10, y=95)

        e_password = Entry(frame_down, width=25, justify='left',show = '*', font=("", 15), highlightthickness=1)
        e_password.place(x=14, y=130)

        #button
        button_confirm = Button(frame_down, text="Login", bg=co3, fg=co1, width=39, height=2, font=("Ivy 9 bold"))
        button_confirm.place(x=15, y=180)




        #button
        button_confirm = Button(frame_down, text="Login", bg=co3, fg=co1, width=39, height=2, font=("Ivy 9 bold"), command=check_login)
        button_confirm.place(x=15, y=180)

        

        window.mainloop()

    
    def TelaGerenciamento(self):
        window1 = Tk()
        window1.title("Inset Sybioma")
        window1.configure(background='#3F79F2')
        window1.geometry("500x500")
        window1.resizable(True,True)
        window1.minsize(width = 300, height = 300)

        #auxiliary functions
        def criaApp():
            self.banco.criarTabelaAPP
        
        def criaAreaImovel():
            self.banco.criarTabelaAreaImovel

        def inserirApp():
            diretorio = filedialog.askdirectory()
            self.banco.percorreShapesApp(diretorio)
        
        def inserirAreaImovel():
            diretorio = filedialog.askdirectory()
            self.banco.percorreShapesAreaImovel(diretorio)

        #Buttons

        search_file = Button(window1,text = "Criar tabela App", command = criaApp )
        search_file.place(relx = 0.3,rely=0.1, relwidth=0.35,relheight = 0.1)

        search_file1 = Button(window1,text = "Criar tabela Area Imovel", command = criaAreaImovel)
        search_file1.place(relx = 0.3,rely=0.3, relwidth=0.35,relheight = 0.1)

        search_file2 = Button(window1,text = "Inserir shapes APP", command = inserirApp)
        search_file2.place(relx = 0.3,rely=0.5, relwidth=0.35,relheight = 0.1)

        search_file3 = Button(window1,text = "Inserir shapes Area Imovel", command = inserirAreaImovel)
        search_file3.place(relx = 0.3,rely=0.7, relwidth=0.35,relheight = 0.1)


        window1.mainloop()


        


teste = CreateTela()
        