import sqlite3, os, json

diretorio_atual = os.getcwd()

# Lê arquivo:
arqv = open(diretorio_atual+'\\data.json',encoding='utf-8')
dados = json.load(arqv)

lista_carga = []

for chave in dados:
    lista_carga.append((int(chave['cpf']), chave['nome'], chave['data_nasc'], chave['celular'], chave['email'], chave['cep']))

con = sqlite3.connect(diretorio_atual+'\\aula8.db')
cur = con.cursor()

try:
    cur.execute('''CREATE TABLE "TB_Cliente"( "CPF" INTEGER NOT NULL UNIQUE, "Nome_Completo" TEXT NOT NULL, "Data_Nascimento" TEXT NOT NULL, "Telefone" TEXT, "Email" TEXT, "CEP" TEXT NOT NULL, PRIMARY KEY("CPF"));''')
except:
    ...

cur.executemany("INSERT INTO TB_Cliente VALUES (?, ?, ?, ?, ?, ?)", lista_carga)

con.commit()

con.close()
