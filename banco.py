import os
import sqlite3
from sqlite3 import Error

pastaApp = os.path.dirname(__file__)
nomeBanco = pastaApp+"\\banco.db"

def conexaoBanco():
    conect = None
    try:
        conect = sqlite3.connect(nomeBanco)
    except Error as ex:
        print(ex)
    return conect
      

def mostrarDados(query):
    conect = conexaoBanco()
    cursor = conect.cursor()
    cursor.execute(query)
    resultado = cursor.fetchall()
    conect.close
    return resultado

def Dados(query):
    try:
        conect = conexaoBanco()
        cursor = conect.cursor()
        cursor.execute(query)
        conect.commit()
        conect.close()
    except Error as ex:
        print(ex)