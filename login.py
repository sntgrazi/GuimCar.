from tkinter import *
import banco
from mecanico import Mecanico
from gerente import Gerente
from recepcionista import Recepcionista

class Login:
    def __init__(self):

        self.cor1 = "#485055"
        self.cor2 = "#ffffff"

        self.janela = Tk()
        self.janela.title("Login")
        self.janela.resizable(False,False)

        self.background = Label(self.janela)
        self.backgroundImg = PhotoImage(file="img/bg.png")
        self.background['image'] = self.backgroundImg
        self.background.place(x=0,y=0)

        ### Centralizando janela na tela
        self.largura = 1000
        self.altura = 550

        self.largura_screen = self.janela.winfo_screenwidth()
        self.altura_screen = self.janela.winfo_screenheight()

        self.posx = self.largura_screen/2 - self.largura/2
        self.posy = self.altura_screen/2 - self.altura/2


        self.janela.geometry("%dx%d+%d+%d" % (self.largura,self.altura,self.posx,self.posy))

        self.icon = PhotoImage(file="img/user.png")
        self.janela.iconphoto(False, self.icon)

        self.container01 = Frame(self.janela, width=450, height=330, bg=self.cor1)
        self.container01.place(x=290,y=110)

        self.titulo = Label(self.container01, text="GUIMCAR", font="Arial 16", bg=self.cor1, fg=self.cor2)
        self.titulo.place(x=175,y=20)

        self.label_usuario = Label(self.container01, text="Usuario", font="Arial 16", bg=self.cor1, fg=self.cor2)
        self.label_usuario.place(x=60,y=90)

        self.label_senha = Label(self.container01, text="Senha", font="Arial 16", bg=self.cor1, fg=self.cor2)
        self.label_senha.place(x=60, y=150)
        
        self.entrada_usuario = Entry(self.container01, font="Arial 15")
        self.entrada_usuario.place(x=150, y=90, width=250)

        self.entrada_senha = Entry(self.container01, font="Arial 15", show='*')
        self.entrada_senha.place(x=150, y=150, width=250)

        self.btnEntrar = Button(self.container01, text="Entrar", font="Arial 16", command=self.Entrar)
        self.btnEntrar.place(x=180,y=215, width=100, height=50)
    
        self.msg = Label(self.container01, text="", font="Arial 16", bg=self.cor1, fg=self.cor2)
        self.msg.place(x=115,y=285)

        self.janela.mainloop()

    def Entrar(self):
        nome = self.entrada_usuario.get()
        senha = self.entrada_senha.get()
        try:
            sql="SELECT senha FROM funcionarios WHERE nome = '{}'".format(nome)
            senhadb = banco.mostrarDados(sql)
            if senha == senhadb[0][0]:
                sql2 = "SELECT nome FROM funcionarios WHERE nome LIKE '%Mec%'"
                linha = banco.mostrarDados(sql2)
                for i in linha:
                    if nome in i:
                        conect = "UPDATE funcionarios SET status = 'Logado' WHERE nome = '{}'".format(nome)
                        banco.Dados(conect)
                        tela = Mecanico()
                sql3 = "SELECT nome FROM funcionarios WHERE nome LIKE '%Ger%'"
                linhaG = banco.mostrarDados(sql3)
                for G in linhaG:
                    if nome in G:
                        tela = Gerente()
                sql4 = "SELECT nome FROM funcionarios WHERE nome LIKE '%Recep%'"
                linhaR = banco.mostrarDados(sql4)
                for R in linhaR:
                    if nome in R:
                        tela = Recepcionista()
        except:
            self.msg["text"] = "Usuario/Senha incorretos"
        

tela = Login()