from tkinter import *
from tkinter import filedialog
import sys
import os
import zipfile


def descompactar():
    nome_arquivo = filedialog.askdirectory()
    lista_dir = os.listdir(nome_arquivo)
    for diretorios in lista_dir:
        if '.zip' in diretorios or '.rar' in diretorios:
            nome_pasta = f'{nome_arquivo}/' + str(diretorios)[0:len(str(diretorios))-4]
            os.mkdir(nome_pasta)
            extrair = zipfile.ZipFile(f'{nome_arquivo}/{diretorios}')
            extrair.extractall(nome_pasta)
            # os.remove(f'{nome_arquivo}/{diretorios}')
    
    for diretorios in lista_dir:
        if '.zip' in diretorios or '.rar' in diretorios:
            os.remove(f'{nome_arquivo}/{diretorios}')

    lista_dir = os.listdir(nome_arquivo)

    for diretorios in lista_dir:
        if os.path.isdir(f'{nome_arquivo}/{diretorios}'):
            lista_shapes = os.listdir(f'{nome_arquivo}/{diretorios}')
            for shapes in lista_shapes:
                if '.zip' in shapes or '.rar' in shapes:
                    extrair = zipfile.ZipFile(f'{nome_arquivo}/{diretorios}/{shapes}')
                    extrair.extractall(f'{nome_arquivo}/{diretorios}')
                    # os.remove(f'{nome_arquivo}/{diretorios}/{shapes}')
    

    for diretorios in lista_dir:
        if os.path.isdir(f'{nome_arquivo}/{diretorios}'):
            lista_shapes = os.listdir(f'{nome_arquivo}/{diretorios}')
            for shapes in lista_shapes:
                if '.zip' in shapes or '.rar' in shapes:
                    os.remove(f'{nome_arquivo}/{diretorios}/{shapes}')
    
    extrair.close()

