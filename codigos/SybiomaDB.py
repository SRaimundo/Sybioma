import psycopg2
import sys
import os
import geopandas as gpd
from tkinter import filedialog
from shapely.geometry import MultiPolygon
from shapely.geometry import Polygon

class SybiomaDB:

    _sslmode = "require"

    # def __init__(self):
        
    def setConnection(self,host,dbname,user,password):
        self._host = host
        self._dbname = dbname
        self._user = user
        self._password = password
        con_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(self._host, self._user, self._dbname, self._password, self._sslmode)
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
    
    
    def percorreShapesApp(self):            
        
        if self.criarPrepareApp == True:
                self._cursor.execute("prepare planoInsertApp as INSERT INTO APP(cod_cidade, idf, nom_tema, num_area, geom) VALUES ($1,$2,$3,$4,$5)")
                self.criarPrepareApp = False
        
        diretorio = filedialog.askdirectory()
        lista_dir_atual = os.listdir(diretorio)
        
        for shapes in lista_dir_atual:
            if f'APP.shp' in os.listdir(f'{diretorio}/{shapes}'):
                table = gpd.read_file(f'{diretorio}/{shapes}/APP.shp' , encoding='utf-8',char_decode_errors='ignore')
                table.geometry = [MultiPolygon([feature]) if isinstance(feature, Polygon) else feature for feature in table.geometry ]
                quant = table.shape[0]
                cidade=shapes.split("SHAPE_")[1]
                table = gpd.read_file(f'{diretorio}/{shapes}/APP.shp' , encoding='utf-8',char_decode_errors='ignore') #.to_wkb()
                table.geometry = [MultiPolygon([feature]) if isinstance(feature, Polygon) else feature for feature in table.geometry ]
                i = 0
                while i<quant :
                    self._cursor.execute("execute planoInsertApp (%s, %s, %s, %s,%s)",  (cidade, str(table.IDF[i]), str(table.NOM_TEMA[i]), table.NUM_AREA[i],str(table.geometry[i])))
                    i+=1
                    if i%200 ==0:
                        self._connection.commit()
                self._connection.commit()

    
    def percorreShapesAreaImovel(self):

        if self.criarPrepareAreaImovel:
            self._cursor.execute("prepare planoInsertAreaImovel as INSERT INTO area_imovel(cod_cidade,cod_imovel, num_area, cod_estado, num_munici, num_modulo, tipo_imove, situacao, condicao_i, geom)VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10)")
            self.criarPrepareAreaImovel = False
        
        diretorio = filedialog.askdirectory()
        lista_dir_atual = os.listdir(diretorio)

        for shapes in lista_dir_atual:
            if os.path.isdir(f'{diretorios}/{shapes}'):
                if f'AREA_IMOVEL.shp' in os.listdir(f'{diretorio}/{shapes}'):
                    table = gpd.read_file(f'{diretorio}/{shapes}/AREA_IMOVEL.shp' , encoding='utf-8',char_decode_errors='ignore')
                    quant = table.shape[0]
                    cidade=shapes.split("SHAPE_")[1]
                    table = gpd.read_file(f'{diretorio}/{shapes}/AREA_IMOVEL.shp' , encoding='utf-8',char_decode_errors='ignore') #.to_wkb()
                    table.geometry = [MultiPolygon([feature]) if isinstance(feature, Polygon) else feature for feature in table.geometry ]
                    i = 0
                    
                    while i<quant :
                        self._cursor.execute("execute planoInsertAreaImovel (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)", (cidade,table.COD_IMOVEL[i],table.NUM_AREA[i], table.COD_ESTADO[i], table.NOM_MUNICI[i], table.NUM_MODULO[i], table.TIPO_IMOVE[i], table.SITUACAO[i], table.CONDICAO_I[i], str(table.geometry[i])))
                        i+=1
                        if i%200 ==0:
                            self._connection.commit()
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