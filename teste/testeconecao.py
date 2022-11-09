import psycopg2

class SybiomaDB:
    # _host
    # _user
    # _dbname
    # _password
    _sslmode = "require"
    # _connection
    # _cursor

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
    
    def criarTabela(self,nome):
        self._cursor.execute('CREATE TABLE public."IMOV_APP"(idi integer NOT NULL,idapp integer NOT NULL,CONSTRAINT "IMOV_APP_pkey" PRIMARY KEY (idi,idapp));')
        self._connection.commit()


# teste = SybiomaDB('localhost','sybioma', 'postgres','986082Sr')
# teste.criarTabela('testeTabela')

with open("commandApp.txt","r") as arquivo:
    comando = arquivo.read().format("teste")
comando.format("teste")
print(comando)

