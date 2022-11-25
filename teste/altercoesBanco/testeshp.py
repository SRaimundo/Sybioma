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
        
    
    def criarTabelaAreaImovel(self):
        
    
    def insertApp(self, cod_cidade, IDF, NOM_TEMA, NUM_AREA, geometry):
    
    
    def insertAreaImovel(self, COD_IMOVEL,NUM_AREA, COD_ESTADO, NOM_MUNICI, NUM_MODULO, TIPO_IMOVE, SITUACAO, CONDICAO_I, geometry):
    
    def percorreShapesApp(self,diretorio):
    
    
    def percorreShapesAreaImovel(self,diretorio):
    


teste = SybiomaDB('localhost','teste', 'samuel','986082Sr')
print("Conectou")

# teste.criarTabelaAPP()
# print("Criou tabela app")

# teste.criarTabelaAreaImovel()
# print("Criou tabela area imovel")

teste.percorreShapesApp("/home/alunos/Desktop/sybioma/testeCodigos/samuel")
print("Shapes inseridos")
# teste.percorreShapesAreaImovel("/home/alunos/Desktop/sybioma/testeCodigos/samuel")