import sys
import os
import geopandas as gpd
# Necessario instalar geopandas para rodar o programa

#arq = 'APP' #arquivo que será procurado

arq = sys.argv[1]


lista_dir_atual = os.listdir()
temas = {}

for diretorios in lista_dir_atual:
    if os.path.isdir(diretorios):
        lista_shapes = os.listdir(diretorios)
        for shapes in lista_shapes:
            if os.path.isdir(f'{diretorios}/{shapes}'):
                
                # if os.path.isdir(f'{diretorios}/{shapes}/{arq}'):    
                #     table = DBF(f'{diretorios}/{shapes}/{arq}/{arq}.dbf' , encoding='utf-8',char_decode_errors='ignore')
                #     quant = table.shape[0]
                #     print(table.shape)
                    # for record in table:
                    #     print(record['NOM_TEMA'])

                if f'{arq}.dbf' in os.listdir(f'{diretorios}/{shapes}'):
                    table = gpd.read_file(f'{diretorios}/{shapes}/{arq}.shp' , encoding='utf-8',char_decode_errors='ignore')
                    quant = table.shape[0]
                    # print(table.header())
                    for aux in table:
                        print(aux)
                    # i = 0
                    # while i<quant :
                    #     print(f'{table.IDF[i]} - {table.NOM_TEMA[i]} - {table.NUM_AREA[i]} - {table.geometry[i]}')
                    #     i+=1
                    


