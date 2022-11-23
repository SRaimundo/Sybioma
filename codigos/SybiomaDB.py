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




teste = SybiomaDB('localhost','teste', 'samuel','986082Sr')
print("Conectou")

# teste.criarTabelaAPP()
# print("Criou tabela app")

# teste.criarTabelaAreaImovel()
# print("Criou tabela area imovel")

teste.percorreShapesApp("/home/alunos/Desktop/sybioma/testeCodigos/samuel")
print("Shapes inseridos")
# teste.percorreShapesAreaImovel("/home/alunos/Desktop/sybioma/testeCodigos/samuel")