import psycopg2
import psycopg2.extras
import sys
import os
import csv
import geopandas as gpd
from tkinter import filedialog, Label
from tkinter import messagebox
from shapely.geometry import MultiPolygon
from shapely.geometry import Polygon
from tkinter.ttk import Progressbar
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

import time

_host = "localhost"
_dbname = "sybioma"
_user = "postgres"
_password = "986082Sr"
# con_string = "host={0} user={1} dbname={2} password={3}".format(self._host, self._user, self._dbname, self._password)
# self._connection = psycopg2.connect(con_string) 
# self._cursor = self._connection.cursor()
# self.criarPrepareApp = True
# self.criarPrepareAreaImovel = True
# #conecta pelo geopandas
engine_string = 'postgresql://{0}:{1}@{2}/{3}'.format(_user, _password, _host, _dbname)
engine = create_engine(engine_string)


ci = "'" + "PR-4126678-A33F71B96DEA4B6DA317C1EB559C883F" + "'"
sql= 'SELECT geom, gid FROM public."area_imovel" WHERE cod_imovel = ' + ci + ';'
gdf_imov = gpd.read_postgis(sql, con=engine)

sql = 'select ap.gid, ap.geom from public."area_imovel" im, public."imovel_app" ia, public."app_recompor" ap where im.cod_imovel = ' + ci + ' and ia.idimovel = im.gid and ia.idapp = ap.gid;'
gdf_app = gpd.read_postgis(sql, con=engine)

shape_01 = gdf_imov
shape_02 = gdf_app
g1 = gpd.GeoDataFrame(shape_01).geom
g2 = gpd.GeoDataFrame(shape_02).geom
ax = g1.plot(color='red')
g2.plot(ax=ax, color='green', alpha=0.5)
plt.show()
        
