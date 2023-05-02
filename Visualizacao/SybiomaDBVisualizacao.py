import psycopg2
import psycopg2.extras
import geopandas as gpd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine


class SybiomaDB:
        
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
        #conecta pelo geopandas
        engine_string = "postgresql://{0}:{1}@{2}/{3}".format(self._user, self._password, self._host, self._dbname)
        self.engine = create_engine(engine_string)

        
    
    def __del__(self):
        self._cursor.close()
        self._connection.close()
        
    
    def criarTabelaAPP(self):
        with open("commandApp.txt","r") as arquivo:
            comando = arquivo.read()
        self._cursor.execute(comando)

    def plotImovel(self,codimov):

        ci = "'" + codimov + "'"
        sql= "SELECT geom, gid FROM public.area_imovel WHERE cod_imovel = {0};".format(ci)
        gdf_imov = gpd.read_postgis(sql, con=self.engine)

        sql = "select ap.gid, ap.geom from public.area_imovel im, public.imovel_app ia, public.app_recompor ap where im.cod_imovel ={0} and ia.idimovel = im.gid and ia.idapp = ap.gid;".format(ci)
        gdf_app = gpd.read_postgis(sql, con=(self.engine))

        shape_01 = gdf_imov
        shape_02 = gdf_app
        g1 = gpd.GeoDataFrame(shape_01).geom
        g2 = gpd.GeoDataFrame(shape_02).geom
        ax = g1.plot(color='red')
        g2.plot(ax=ax, color='green', alpha=0.5)
        plt.show()
    

    def plotImovelVizinhos(self,codimov,raio):
        ci = "'" + codimov + "'"
        sql= "SELECT geom, gid FROM public.area_imovel WHERE cod_imovel = {0};".format(ci)
        gdf_imov = gpd.read_postgis(sql, con=self.engine)

        sql = "select ap.gid, ap.geom from public.area_imovel im, public.imovel_app ia, public.app_recompor ap where im.cod_imovel ={0} and ia.idimovel = im.gid and ia.idapp = ap.gid;".format(ci)
        gdf_app = gpd.read_postgis(sql, con=(self.engine))

        sql = "select b.gid,b.geom from area_imovel a, area_imovel b, app_recompor c where ST_DWithin(a.geom,b.geom,{0}) and a.cod_imovel={1} and st_intersects(b.geom,c.geom);".format(raio,ci)
        gdf_imov_vizinho = gpd.read_postgis(sql, con=self.engine)

        sql = "select app.gid, app.geom from app_recompor app, imovel_app ip where app.gid= ip.idapp and ip.idimovel in(select b.gid from area_imovel a, area_imovel b, app_recompor c where ST_DWithin(a.geom,b.geom,{0}) and a.cod_imovel={1} and st_intersects(b.geom,c.geom))".format(raio,ci)
        gdf_app_vizinho = gpd.read_postgis(sql, con=self.engine)

        shape_01 = gdf_imov
        shape_02 = gdf_app
        shape_03 = gdf_imov_vizinho
        shape_04 = gdf_app_vizinho

        g1 = gpd.GeoDataFrame(shape_01).geom
        g2 = gpd.GeoDataFrame(shape_02).geom
        g3 = gpd.GeoDataFrame(shape_03).geom
        g4 = gpd.GeoDataFrame(shape_04).geom
        
        ax = g1.plot(color='red')
        g2.plot(ax=ax, color='green', alpha=0.5)
        g3.plot(ax=ax, color='blue', alpha=0.5)
        g4.plot(ax=ax, color='yellow', alpha=0.5)
        plt.show()
        
