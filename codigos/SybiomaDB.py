import psycopg2
import sys
import os
import csv
import geopandas as gpd
from tkinter import filedialog, Label
from tkinter import messagebox
from shapely.geometry import MultiPolygon
from shapely.geometry import Polygon
from tkinter.ttk import Progressbar

class SybiomaDB:

    # _sslmode = "require"

    # def __init__(self):
        
    def setConnection(self,host,dbname,user,password):
        self._host = host
        self._dbname = dbname
        self._user = user
        self._password = password
        con_string = "host={0} user={1} dbname={2} password={3}".format(self._host, self._user, self._dbname, self._password)
        self._connection = psycopg2.connect(con_string) 
        self._cursor = self._connection.cursor()
        self.criarPrepareApp = True
        self.criarPrepareAreaImovel = True

        
    
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
    
    def criarTabelaAPPRecompor(self):
        with open("commandAppRecompor.txt","r") as arquivo:
            comando = arquivo.read()
        self._cursor.execute(comando)
    
    def criarTabelaImovApp(self):
        with open("commandImovApp.txt","r") as arquivo:
            comando = arquivo.read()
        self._cursor.execute(comando)

    def populaImovApp(self):
        with open("commandInsertImovApp.txt","r") as arquivo:
            comando = arquivo.read()
        self._cursor.execute(comando)
 
    
    def percorreShapesApp(self,root):            
        
        progress = Progressbar(root,lengt=400, mode = "determinate",maximum = 10, value = 0)
        progress.place(x=826, y=406,width = 400, height= 30)
        self._cursor.execute("select distinct cod_cidade from app;")
        resultado = self._cursor.fetchall()
        cidadesInseridas = []
        for cod in resultado:
            cidadesInseridas.append(str(cod[0]))

        if self.criarPrepareApp == True:
                self._cursor.execute("prepare planoInsertApp as INSERT INTO APP(cod_cidade, idf, nom_tema, num_area, geom) VALUES ($1,$2,$3,$4,st_makevalid($5))")
                self.criarPrepareApp = False
        
        diretorio = filedialog.askdirectory()
        lista_dir_atual = os.listdir(diretorio)
        quantShapes = 0
        repetidas = []
        for shapes in lista_dir_atual:
            if f'APP.shp' in os.listdir(f'{diretorio}/{shapes}'):
                quantShapes+=1
                cidade=shapes.split("SHAPE_")[1]
                if str(cidade) in cidadesInseridas:
                    repetidas.append(cidade)

        
        res = True
        if len(repetidas) != 0:
            f = open("log.txt","wt")
            for city in repetidas:
                f.write(city+"\n")
            
            f.close()
            res = messagebox.askyesnocancel("Cidades já inseridas","Existem cidades que já foram inseridas no banco de dados (codigo delas está no arquivo log.txt na pasta do programa), deseja apagar os dados delas e reinseri-las ?")
        
        if res == None:
            progress.destroy()
            return


        progress["maximum"] = quantShapes
        progress["value"] = 0.5

        quantCarregadas = 0
        quantTotal = quantShapes

        if(res==False):
            quantTotal-=len(repetidas)

        
        load_label = Label(root, text="{0}/{1} cidades carregadas".format(quantCarregadas,quantTotal), font=('Arial', 12, 'bold'), bg='#f8f8f8')
        load_label.place(x=826, y=440)
        
        
        
        for shapes in lista_dir_atual:
            if f'APP.shp' in os.listdir(f'{diretorio}/{shapes}'):
                table = gpd.read_file(f'{diretorio}/{shapes}/APP.shp' , encoding='utf-8',char_decode_errors='ignore')
                table.geometry = [MultiPolygon([feature]) if isinstance(feature, Polygon) else feature for feature in table.geometry ]
                quant = table.shape[0]
                cidade=shapes.split("SHAPE_")[1]
                if cidade in repetidas:
                    if(res == False):
                        progress["value"]+=1
                        root.update_idletasks()
                        continue

                    if(res == True):
                        commandDelete = "DELETE FROM app WHERE cod_cidade={0};".format(cidade)
                        self._cursor.execute(commandDelete)
                        self._connection.commit()
                
                table = gpd.read_file(f'{diretorio}/{shapes}/APP.shp' , encoding='utf-8',char_decode_errors='ignore') #.to_wkb()
                table.geometry = [MultiPolygon([feature]) if isinstance(feature, Polygon) else feature for feature in table.geometry ]
                i = 0
                while i<quant :
                    self._cursor.execute("execute planoInsertApp (%s, %s, %s, %s,%s)",  (cidade, str(table.IDF[i]), str(table.NOM_TEMA[i]), table.NUM_AREA[i],str(table.geometry[i])))
                    i+=1
                    if i%200 ==0:
                        self._connection.commit()
                self._connection.commit()
                progress["value"]+=1
                quantCarregadas+=1
                load_label["text"] = "{0}/{1} cidades carregadas".format(quantCarregadas,quantTotal)
                root.update_idletasks()
        
        progress.destroy()
        load_label.destroy()

    
    def percorreShapesAreaImovel(self,root):

        progress = Progressbar(root,lengt=400, mode = "determinate",maximum = 10, value = 0)
        progress.place(x=826, y=406,width = 400, height= 30)
        self._cursor.execute("select distinct cod_cidade from area_imovel;")
        resultado = self._cursor.fetchall()
        cidadesInseridas = []
        for cod in resultado:
            cidadesInseridas.append(str(cod[0]))

        if self.criarPrepareAreaImovel:
            self._cursor.execute("prepare planoInsertAreaImovel as INSERT INTO area_imovel(cod_cidade,cod_imovel, num_area, cod_estado, nom_munici, num_modulo, tipo_imove, situacao, condicao_i, geom)VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,st_makevalid($10))")
            self.criarPrepareAreaImovel = False
        
        diretorio = filedialog.askdirectory()
        lista_dir_atual = os.listdir(diretorio)

        quantShapes = 0
        repetidas = []
        for shapes in lista_dir_atual:
            if f'AREA_IMOVEL.shp' in os.listdir(f'{diretorio}/{shapes}'):
                quantShapes+=1
                cidade=shapes.split("SHAPE_")[1]
                if str(cidade) in cidadesInseridas:
                    repetidas.append(cidade)
        
        res = True
        if len(repetidas) != 0:
            f = open("log.txt","wt")
            for city in repetidas:
                f.write(city+"\n")
            
            f.close()
            res = messagebox.askyesnocancel("Cidades já inseridas","Existem cidades que já foram inseridas no banco de dados (codigo delas está no arquivo log.txt na pasta do programa), deseja apagas os dados delas e reinseri-las ?")
        
        if res == None:
            progress.destroy()
            return


        progress["maximum"] = quantShapes
        progress["value"] = 0.5

        quantCarregadas = 0
        quantTotal = quantShapes

        if(res==False):
            quantTotal-=len(repetidas)

        
        load_label = Label(root, text="{0}/{1} cidades carregadas".format(quantCarregadas,quantTotal), font=('Arial', 12, 'bold'), bg='#f8f8f8')
        load_label.place(x=826, y=440)

        for shapes in lista_dir_atual:
            if os.path.isdir(f'{diretorio}/{shapes}'):
                if f'AREA_IMOVEL.shp' in os.listdir(f'{diretorio}/{shapes}'):
                    table = gpd.read_file(f'{diretorio}/{shapes}/AREA_IMOVEL.shp' , encoding='utf-8',char_decode_errors='ignore')
                    quant = table.shape[0]
                    cidade=shapes.split("SHAPE_")[1]

                    if cidade in repetidas:
                        if(res == False):
                            progress["value"]+=1
                            root.update_idletasks()
                            continue
                        if(res == True):
                            commandDelete = "DELETE FROM area_imovel WHERE cod_cidade={0};".format(cidade)
                            self._cursor.execute(commandDelete)
                            self._connection.commit()
                                                
                    table = gpd.read_file(f'{diretorio}/{shapes}/AREA_IMOVEL.shp' , encoding='utf-8',char_decode_errors='ignore') #.to_wkb()
                    table.geometry = [MultiPolygon([feature]) if isinstance(feature, Polygon) else feature for feature in table.geometry ]
                    i = 0
                    
                    while i<quant :
                        self._cursor.execute("execute planoInsertAreaImovel (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)", (cidade,table.COD_IMOVEL[i],table.NUM_AREA[i], table.COD_ESTADO[i], table.NOM_MUNICI[i], table.NUM_MODULO[i], table.TIPO_IMOVE[i], table.SITUACAO[i], table.CONDICAO_I[i], str(table.geometry[i])))
                        i+=1
                        if i%200 ==0:
                            self._connection.commit()
                    self._connection.commit()
                    progress["value"]+=1
                    quantCarregadas+=1
                    load_label["text"] = "{0}/{1} cidades carregadas".format(quantCarregadas,quantTotal)
                    root.update_idletasks()
        
        progress.destroy()
        load_label.destroy()
    
    def corrigirTextoApp(self):
        self._cursor.execute("update app set nom_tema=lower(convert_from(convert(SUBSTRING(nom_tema,0,99)::bytea, 'UTF8', 'LATIN1'), 'UTF8'));Commit;")
    
    def corrigirTextoAppRecompor(self):
        self._cursor.execute("update app_recompor set nom_tema=lower(convert_from(convert(SUBSTRING(nom_tema,0,99)::bytea, 'UTF8', 'LATIN1'), 'UTF8'));Commit;")
    
    def corrigirTextoAreaImovelCond(self):
        self._cursor.execute("update area_imovel set condicao_i=lower(convert_from(convert(condicao_i::bytea, 'UTF8', 'LATIN1'), 'UTF8'));Commit;")
    
    def corrigirTextoAreaImovelNom(self):
        self._cursor.execute("update area_imovel set nom_munici=lower(convert_from(convert(nom_munici::bytea, 'UTF8', 'LATIN1'), 'UTF8'));Commit;")
    
    def criaGeoIndiceRecompor(self):
        with open("CommandAppRecomporGeoIndex.txt","r") as arquivo:
            comando = arquivo.read()
        self._cursor.execute(comando)
    
    def criaGidIndiceRecompor(self):
        with open("CommandAppRecomporGidIndex.txt","r") as arquivo:
            comando = arquivo.read()
        self._cursor.execute(comando)
    
    def criaCodImovelIndiceRecompor(self):
        with open("CommandAppRecomporCodImovelIndex.txt","r") as arquivo:
            comando = arquivo.read()
        self._cursor.execute(comando)
    

    def padronizacaoCondicao(self):
        arquivo = filedialog.askopenfile(mode = "r", title = "Selecione o arquivo CSV", filetypes = (
            ('CSV files', '*.csv'),
        ) )

        sqlDelete = "DROP TABLE IF EXISTS padronizacao_condicao_i;"
        self._cursor.execute(sqlDelete)
        self._connection.commit()
        print(1)


        sqlCreate = 'CREATE TABLE "padronizacao_condicao_i" ("idp" integer, "original" text,"nova" text); ALTER TABLE "padronizacao_condicao_i" ADD PRIMARY KEY (idp); '
        self._cursor.execute(sqlCreate)
        print(2)
        self._connection.commit()

        with open(arquivo.name, 'r') as f:
            reader = csv.reader(f)
            next(reader) # Skip the header row.
            for row in reader:
                self._cursor.execute("INSERT INTO padronizacao_condicao_i(idp,original,nova) VALUES (%s, %s, %s)", row)
        
        self._connection.commit()
        print(3)
        
        sqlPadronizacao = "UPDATE area_imovel SET condicao_i = padr.nova from padronizacao_condicao_i as padr where condicao_i = padr.original"
        self._cursor.execute(sqlPadronizacao)
        self._connection.commit()
        
    





# teste = SybiomaDB('localhost','teste', 'samuel','986082Sr')
# print("Conectou")

# # teste.criarTabelaAPP()
# # print("Criou tabela app")

# # teste.criarTabelaAreaImovel()
# # print("Criou tabela area imovel")

# teste.percorreShapesApp("/home/alunos/Desktop/sybioma/testeCodigos/samuel")
# print("Shapes inseridos")
# # teste.percorreShapesAreaImovel("/home/alunos/Desktop/sybioma/testeCodigos/samuel")