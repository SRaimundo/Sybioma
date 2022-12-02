from tkinter import *
from tkinter import filedialog
import sys
import os
import zipfile


# root = Tk()

# class Funcs():
def descompactar():
    nome_arquivo = filedialog.askdirectory()
    # print(filename)
    lista_dir = os.listdir(nome_arquivo)
    # print(nome_arquivo)
    for diretorios in lista_dir:
        if '.zip' in diretorios or '.rar' in diretorios:
        # print(diretorios)
            nome_pasta = f'{nome_arquivo}/' + str(diretorios)[0:len(str(diretorios))-4]
            os.mkdir(nome_pasta)
            extrair = zipfile.ZipFile(f'{nome_arquivo}/{diretorios}')
            extrair.extractall(nome_pasta)
            os.remove(f'{nome_arquivo}/{diretorios}')

    lista_dir = os.listdir(nome_arquivo)

    for diretorios in lista_dir:
        if os.path.isdir(f'{nome_arquivo}/{diretorios}'):
            lista_shapes = os.listdir(f'{nome_arquivo}/{diretorios}')
            for shapes in lista_shapes:
                if '.zip' in shapes or '.rar' in shapes:
                    extrair = zipfile.ZipFile(f'{nome_arquivo}/{diretorios}/{shapes}')
                    extrair.extractall(f'{nome_arquivo}/{diretorios}')
                    os.remove(f'{nome_arquivo}/{diretorios}/{shapes}')
    extrair.close()


# class Application(Funcs):
#     def __init__(self):
#         self.root = root
#         self.tela()
#         self.create_button()
#         root.mainloop()
#     def tela(self):
#         self.root.title("Descompactador CAR")
#         self.root.configure(background='#3F79F2')
#         self.root.geometry("500x500")
#         self.root.resizable(True,True)
#         self.root.minsize(width = 300, height = 300)
#     def create_button(self):
#         self.search_file = Button(self.root,text = "Descompactar", command = self.descompactar)
#         self.search_file.place(relx = 0.35,rely=0.5, relwidth=0.3,relheight = 0.1)


# Application()
