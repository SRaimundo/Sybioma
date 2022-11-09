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
        with open("commandInsertApp.txt","r") as arquivo:
            comando = arquivo.read().format(cod_cidade, IDF, NOM_TEMA, NUM_AREA, geometry)
        self._cursor.execute(comando)
    
    def insertAreaImovel(self, COD_IMOVEL,NUM_AREA, COD_ESTADO, NOM_MUNICI, NUM_MODULO, TIPO_IMOVE, SITUACAO, CONDICAO_I, geometry):
        with open("commandInsertAreaImovel.txt","r") as arquivo:
            comando = arquivo.read().format(COD_IMOVEL,NUM_AREA, COD_ESTADO, NOM_MUNICI, NUM_MODULO, TIPO_IMOVE, SITUACAO, CONDICAO_I, geometry)
        self._cursor.execute(comando)
    
    def percorreShapesApp(self,diretorio):
        lista_dir_atual = os.listdir(diretorio)

        for diretorios in lista_dir_atual:
            if os.path.isdir(diretorios):
                lista_shapes = os.listdir(diretorios)
                for shapes in lista_shapes:
                    if os.path.isdir(f'{diretorios}/{shapes}'):
                        if f'{arq}.dbf' in os.listdir(f'{diretorios}/{shapes}'):
                            table = gpd.read_file(f'{diretorios}/{shapes}/APP.shp' , encoding='utf-8',char_decode_errors='ignore')
                            quant = table.shape[0]
                            i = 0
                            while i<quant :
                                self.insertApp(shapes.split("E_")[1], table.IDF[i], table.NOM_TEMA[i], table.NUM_AREA[i], table.geometry[i])
                                i+=1

    
    def percorreShapesApp(self,diretorio):
        lista_dir_atual = os.listdir(diretorio)

        for diretorios in lista_dir_atual:
            if os.path.isdir(diretorios):
                lista_shapes = os.listdir(diretorios)
                for shapes in lista_shapes:
                    if os.path.isdir(f'{diretorios}/{shapes}'):
                        if f'{arq}.dbf' in os.listdir(f'{diretorios}/{shapes}'):
                            table = gpd.read_file(f'{diretorios}/{shapes}/AREA_IMOVEL.shp' , encoding='utf-8',char_decode_errors='ignore')
                            quant = table.shape[0]
                            i = 0
                            while i<quant :
                                self.insertAreaImovel(table.COD_IMOVEL[i],table.NUM_AREA[i], table.COD_ESTADO[i], table.NOM_MUNICI[i], table.NUM_MODULO[i], table.TIPO_IMOVE[i], table.SITUACAO[i], table.CONDICAO_I[i], table.geometry[i])
                                i+=1




teste = SybiomaDB('localhost','sybioma', 'postgres','986082Sr')
teste.criarTabelaAPP()