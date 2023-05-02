import sys
import os
from dbfread import DBF
# Necessario instalar dfbread para rodar o programa

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
                #     for record in table:
                #         print(record['NOM_TEMA'])

                if f'{arq}.dbf' in os.listdir(f'{diretorios}/{shapes}'):
                    table = DBF(f'{diretorios}/{shapes}/{arq}.dbf' , encoding='utf-8',char_decode_errors='ignore')
                    for record in table:
                        print(record) #print momentaneo indicando o local onde deve ficar o arquivo inserção


