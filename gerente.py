from re import template
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import banco

class Gerente:
    def __init__(self):

        self.cor1 = "#DEDEDE"

        self.janela = Toplevel()
        self.janela.title("Gerente")
        self.janela.resizable(False,False)
        ### Centralizando janela na tela
        self.largura = 1000
        self.altura = 535

        self.largura_screen = self.janela.winfo_screenwidth()
        self.altura_screen = self.janela.winfo_screenheight()

        self.posx = self.largura_screen/2 - self.largura/2
        self.posy = self.altura_screen/2 - self.altura/2

        self.janela.geometry("%dx%d+%d+%d" % (self.largura,self.altura,self.posx,self.posy))

        self.icon = PhotoImage(file="img/mecanico.png")
        self.janela.iconphoto(False, self.icon)

        self.nb = ttk.Notebook(self.janela)
        self.nb.place(x=0,y=0, width=self.largura,height=self.altura)

        self.aba1 = Frame(self.nb, bg=self.cor1)
        self.aba2 = Frame(self.nb)
        self.aba3 = Frame(self.nb)
       
        self.nb.add(self.aba1, text="Gerenciar Funcionarios")
        self.nb.add(self.aba2, text="Ver Clientes")
        self.nb.add(self.aba3, text="Ver Ordems de serviço")


        ######################################### Configurações e Widgets da primeira ABA ###################################

        self.container_EsquerdaAba1 = Frame(self.aba1, width=380, height=505, bg=self.cor1, bd=1, relief="solid")
        self.container_EsquerdaAba1.place(x=0,y=0)

        self.label_procurarAba1 = LabelFrame(self.container_EsquerdaAba1,text="Procurar", bd=1, relief="solid", font="Arial 15", bg=self.cor1)
        self.label_procurarAba1.place(x=10,y=0, width=360, height=80)

        self.entrada_pesquisarAba1 = Entry(self.label_procurarAba1, bd=1,relief="solid", font="Arial 14")
        self.entrada_pesquisarAba1.place(x=10,y=15, width=250)

        self.btn_procurarAba1 = Button(self.label_procurarAba1, command=self.pesquisarAba1)
        self.imgBAba1 = PhotoImage(file="img/lupa.png")
        self.btn_procurarAba1.config(image=self.imgBAba1)
        self.btn_procurarAba1.imagem = self.imgBAba1
        self.btn_procurarAba1.place(x=270,y=15, width=30, height=28)

        self.btn_apagarAba1 = Button(self.label_procurarAba1, command=self.limparAba1)
        self.imgBFAba1 = PhotoImage(file='img/botao-fechar.png')
        self.btn_apagarAba1.config(image=self.imgBFAba1)
        self.btn_apagarAba1.imagem = self.imgBFAba1
        self.btn_apagarAba1.place(x=315,y=15, width=30, height=28)

        ###################################################################################################################

        nomeFuncionario = StringVar()
        senhaFuncionario = StringVar()
        cpfFuncionario = StringVar()
        cargoFuncionario = StringVar() 

        self.label_nomeAba1 = Label(self.container_EsquerdaAba1, text="Nome", font="Arial 16", bg=self.cor1)
        self.label_nomeAba1.place(x=10,y=110)
        self.entrada_NomeAba1 = Entry(self.container_EsquerdaAba1, font="Arial 14", bd=1,relief="solid", textvariable=nomeFuncionario)
        self.entrada_NomeAba1.place(x=90,y=112, width=250)
    
        self.label_senhaAba1 = Label(self.container_EsquerdaAba1, text="Senha", font="Arial 16", bg=self.cor1)
        self.label_senhaAba1.place(x=10,y=160)
        self.entrada_SenhaAba1 = Entry(self.container_EsquerdaAba1, font="Arial 14", bd=1,relief="solid", textvariable=senhaFuncionario)
        self.entrada_SenhaAba1.place(x=90,y=162, width=250)

        self.label_cpfAba1 = Label(self.container_EsquerdaAba1, text="Cpf", font="Arial 16", bg=self.cor1)
        self.label_cpfAba1.place(x=10,y=210)
        self.entrada_CpfAba1 = Entry(self.container_EsquerdaAba1, font="Arial 14", bd=1, relief="solid", textvariable=cpfFuncionario)
        self.entrada_CpfAba1.place(x=90, y=212, width=250)

        self.label_cargoAba1 = Label(self.container_EsquerdaAba1, text="Cargo", font="Arial 16", bg=self.cor1)
        self.label_cargoAba1.place(x=10,y=260)
        self.entrada_CargoAba1 = Entry(self.container_EsquerdaAba1, font="Arial 14", bd=1, relief="solid", textvariable=cargoFuncionario)
        self.entrada_CargoAba1.place(x=90, y=262, width=250)

        #################################################################################################################

        self.btn_CadastrarAba1 = Button(self.container_EsquerdaAba1, text="Cadastrar", font="Arial 16", bd=1, relief="solid", command=self.insertFuncionario)
        self.btn_CadastrarAba1.place(x=20, y=340, width=150)

        self.btn_DeletarAba1 = Button(self.container_EsquerdaAba1, text="Deletar", font="Arial 16", bd=1, relief="solid", command=self.deletarFuncionario)
        self.btn_DeletarAba1.place(x=190, y=340, width=150)

        self.btn_EditarAba1 = Button(self.container_EsquerdaAba1, text="Editar", font="Arial 16", bd=1, relief="solid",command=self.editarFuncionario)
        self.btn_EditarAba1.place(x=20, y=410, width=150)

        self.btn_LimparAba1 = Button(self.container_EsquerdaAba1, text="Limpar", font="Arial 16", bd=1, relief="solid", command=self.limparFuncionario)
        self.btn_LimparAba1.place(x=190, y=410, width=150)
  
        ####################################################################################################################

        def getDataAba1(event):
            selected_row = self.tvAba1.focus()
            data = self.tvAba1.item(selected_row)
            global row 
            row = data["values"]
            nomeFuncionario.set(row[1])
            senhaFuncionario.set(row[2])
            cpfFuncionario.set(row[3])
            cargoFuncionario.set(row[4])

        ####################################################################################################################

        self.tvAba1= ttk.Treeview(self.aba1, columns=('id', 'nome', 'senha','cpf','cargo'), show='headings', height=24)

        self.tvAba1.column('id', width=50)
        self.tvAba1.column('nome', width=130)
        self.tvAba1.column('senha', width=150)
        self.tvAba1.column('cpf', width=133)
        self.tvAba1.column('cargo', width=150)

        self.tvAba1.heading('id', text="ID")
        self.tvAba1.heading('nome', text="NOME")
        self.tvAba1.heading('senha', text="SENHA")
        self.tvAba1.heading('cpf', text="CPF")
        self.tvAba1.heading('cargo', text="CARGO")

        self.tvAba1.bind("<ButtonRelease-1>", getDataAba1)
        self.tvAba1.place(x=380,y=0)
        self.mostrarFuncionario()

        ############################### Configuração do Treeview e Widget da segunda ABA ####################################

        self.container_EsquerdaAba2 = Frame(self.aba2, width=380, height=505, bg=self.cor1, bd=1, relief="solid")
        self.container_EsquerdaAba2.place(x=0,y=0)

        self.label_procurarAba2 = LabelFrame(self.container_EsquerdaAba2,text="Procurar", bd=1, relief="solid", font="Arial 15", bg=self.cor1)
        self.label_procurarAba2.place(x=10,y=0, width=360, height=80)

        self.entrada_pesquisarAba2 = Entry(self.label_procurarAba2, bd=1,relief="solid", font="Arial 14")
        self.entrada_pesquisarAba2.place(x=10,y=15, width=250)

        self.btn_procurarAba2 = Button(self.label_procurarAba2, command=self.pesquisarAba2)
        self.imgBAba2 = PhotoImage(file="img/lupa.png")
        self.btn_procurarAba2.config(image=self.imgBAba2)
        self.btn_procurarAba2.imagem = self.imgBAba2
        self.btn_procurarAba2.place(x=270,y=15, width=30, height=28)

        self.btn_apagarAba2 = Button(self.label_procurarAba2, command=self.limparAba2)
        self.imgBFAba2 = PhotoImage(file='img/botao-fechar.png')
        self.btn_apagarAba2.config(image=self.imgBFAba2)
        self.btn_apagarAba2.imagem = self.imgBFAba2
        self.btn_apagarAba2.place(x=315,y=15, width=30, height=28)

        #####################################################################################################################

        nomeCliente = StringVar()
        cpfCliente = StringVar()
        foneCliente = StringVar()
        emailCliente =StringVar()
        enderecoCliente = StringVar()
        placaCliente = StringVar()
        

        self.label_nomeAba2 = Label(self.container_EsquerdaAba2, text="Nome", font="Arial 16", bg=self.cor1)
        self.label_nomeAba2.place(x=10,y=90)
        self.entrada_NomeAba2 = Entry(self.container_EsquerdaAba2, font="Arial 14", bd=1,relief="solid", textvariable=nomeCliente)
        self.entrada_NomeAba2.place(x=90,y=92, width=250)

        self.label_cpfAba2 = Label(self.container_EsquerdaAba2, text="Cpf", font="Arial 16", bg=self.cor1)
        self.label_cpfAba2.place(x=10,y=140)
        self.entrada_CpfAba2 = Entry(self.container_EsquerdaAba2, font="Arial 14", bd=1, relief="solid", textvariable=cpfCliente)
        self.entrada_CpfAba2.place(x=90, y=142, width=250)
    
        self.label_foneAba2 = Label(self.container_EsquerdaAba2, text="Fone", font="Arial 16", bg=self.cor1)
        self.label_foneAba2.place(x=10,y=190)
        self.entrada_FoneAba2 = Entry(self.container_EsquerdaAba2, font="Arial 14", bd=1,relief="solid", textvariable=foneCliente)
        self.entrada_FoneAba2.place(x=90,y=192, width=250)

        self.label_emailAba2 = Label(self.container_EsquerdaAba2, text="Email", font="Arial 16", bg=self.cor1)
        self.label_emailAba2.place(x=10,y=240)
        self.entrada_EmailAba2 = Entry(self.container_EsquerdaAba2, font="Arial 14", bd=1, relief="solid", textvariable=emailCliente)
        self.entrada_EmailAba2.place(x=90, y=242, width=250)

        self.label_placaAba2 = Label(self.container_EsquerdaAba2, text="Placa", font="Arial 16", bg=self.cor1)
        self.label_placaAba2.place(x=10,y=290)
        self.entrada_PlacaAba2 = Entry(self.container_EsquerdaAba2, font="Arial 14", bd=1, relief="solid", textvariable=placaCliente)
        self.entrada_PlacaAba2.place(x=90, y=292, width=250)

        self.label_enderecoAba2 = Label(self.container_EsquerdaAba2, text="Endereço", font="Arial 16", bg=self.cor1)
        self.label_enderecoAba2.place(x=10,y=340)
        self.entrada_EnderecoAba2 = Entry(self.container_EsquerdaAba2, font="Arial 14", bd=1, relief="solid", textvariable=enderecoCliente)
        self.entrada_EnderecoAba2.place(x=110, y=342, width=250)


        #####################################################################################################################

        self.btn_CadastrarAba2 = Button(self.container_EsquerdaAba2, text="Cadastrar", font="Arial 16", bd=1, relief="solid", command=self.cadastrarCliente)
        self.btn_CadastrarAba2.place(x=20, y=390, width=150)
      
        self.btn_DeletarAba2 = Button(self.container_EsquerdaAba2, text="Deletar", font="Arial 16", bd=1, relief="solid", command=self.deletarCliente)
        self.btn_DeletarAba2.place(x=190, y=390, width=150)

        self.btn_EditarAba2 = Button(self.container_EsquerdaAba2, text="Editar", font="Arial 16", bd=1, relief="solid", command=self.editarCliente)
        self.btn_EditarAba2.place(x=20, y=440, width=150)

        self.btn_LimparAba2 = Button(self.container_EsquerdaAba2, text="Limpar", font="Arial 16", bd=1, relief="solid", command=self.limparCliente)
        self.btn_LimparAba2.place(x=190, y=440, width=150)

        ###################################################################################################################

        def getDataAba2(event):
            selected_row = self.tvAba2.focus()
            data = self.tvAba2.item(selected_row)
            global rowAba2 
            rowAba2 = data["values"]
            nomeCliente.set(rowAba2[1])
            cpfCliente.set(rowAba2[2])
            foneCliente.set(rowAba2[3])
            emailCliente.set(rowAba2[4])
            placaCliente.set(rowAba2[5])
            enderecoCliente.set(rowAba2[6])

        #####################################################################################################################

        self.tvAba2= ttk.Treeview(self.aba2, columns=('id', 'nome', 'cpf','fone','email','placa','endereco'), show='headings', height=24)

        self.tvAba2.column('id', width=30)
        self.tvAba2.column('nome', width=100)
        self.tvAba2.column('cpf', width=100)
        self.tvAba2.column('fone', width=90)
        self.tvAba2.column('email', width=100)
        self.tvAba2.column('placa', width=90)
        self.tvAba2.column('endereco', width=100)

        self.tvAba2.heading('id', text="ID")
        self.tvAba2.heading('nome', text="NOME")
        self.tvAba2.heading('cpf', text="CPF")
        self.tvAba2.heading('fone', text="FONE")
        self.tvAba2.heading('email', text="EMAIL")
        self.tvAba2.heading('placa', text="PLACA")
        self.tvAba2.heading('endereco', text="ENDEREÇO")

        self.tvAba2.bind("<ButtonRelease-1>", getDataAba2)
        self.tvAba2.place(x=380,y=0)
        self.mostrarCliente()

        #################################################################################################################

        self.container_EsquerdaAba3 = Frame(self.aba3, width=380, height=505, bg=self.cor1, bd=1, relief="solid")
        self.container_EsquerdaAba3.place(x=0,y=0)

        self.label_procurarAba3 = LabelFrame(self.container_EsquerdaAba3,text="Procurar", bd=1, relief="solid", font="Arial 15", bg=self.cor1)
        self.label_procurarAba3.place(x=10,y=0, width=360, height=80)

        self.entrada_pesquisarAba3 = Entry(self.label_procurarAba3, bd=1,relief="solid", font="Arial 14")
        self.entrada_pesquisarAba3.place(x=10,y=15, width=250)

        self.btn_procurarAba3 = Button(self.label_procurarAba3, command=self.pesquisarAba3)
        self.imgBAba3 = PhotoImage(file="img/lupa.png")
        self.btn_procurarAba3.config(image=self.imgBAba3)
        self.btn_procurarAba3.imagem = self.imgBAba3
        self.btn_procurarAba3.place(x=270,y=15, width=30, height=28)

        self.btn_apagarAba3 = Button(self.label_procurarAba3, command=self.limparAba3)
        self.imgBFAba3 = PhotoImage(file='img/botao-fechar.png')
        self.btn_apagarAba3.config(image=self.imgBFAba3)
        self.btn_apagarAba3.imagem = self.imgBFAba3
        self.btn_apagarAba3.place(x=315,y=15, width=30, height=28)

        #####################################################################################################################

        self.btn_ConcluirOr = Button(self.container_EsquerdaAba3, text="Concluir Ordem", font="Arial 16", bd=1, relief="solid", command=self.concluirOrdem)
        self.btn_ConcluirOr.place(x=40, y=120, width=300, height=50)

        self.btn_DeletarOr = Button(self.container_EsquerdaAba3, text="Deletar Ordem", font="Arial 16", bd=1, relief="solid", command=self.deletarOrdem)
        self.btn_DeletarOr.place(x=40, y=220, width=300,height=50)

        self.btn_MostrarOrAti= Button(self.container_EsquerdaAba3, text="Mostrar Ordems Ativas", font="Arial 16", bd=1, relief="solid", command=self.mostrarOrdemAtiva)
        self.btn_MostrarOrAti.place(x=40, y=320, width=300,height=50)

        self.btn_MostrarOrCon = Button(self.container_EsquerdaAba3, text="Mostrar Ordems Concluidas", font="Arial 16", bd=1, relief="solid", command=self.mostrarOrdemConcluida)
        self.btn_MostrarOrCon.place(x=40, y=420, width=300,height=50)

        ################################# Criação do tree view  da terceira ABA #########################################

        def getDataAba3(event):
            selected_row = self.tvAba3.focus()
            data = self.tvAba3.item(selected_row)
            global rowAba3
            rowAba3 = data["values"]


        self.tvAba3= ttk.Treeview(self.aba3, columns=('id', 'cpfcliente', 'cpfmecanico','valor','descricao'), show='headings', height=24)

        self.tvAba3.column('id', width=60)
        self.tvAba3.column('cpfcliente', width=130)
        self.tvAba3.column('cpfmecanico', width=130)
        self.tvAba3.column('valor', width=140)
        self.tvAba3.column('descricao', width=150)
        

        self.tvAba3.heading('id', text="ID")
        self.tvAba3.heading('cpfcliente', text="CPFCLIENTE")
        self.tvAba3.heading('cpfmecanico', text="CPFMECÂNICO")
        self.tvAba3.heading('valor', text="VALOR")
        self.tvAba3.heading('descricao', text="DESCRIÇÃO")
    
        self.tvAba3.bind("<ButtonRelease-1>", getDataAba3)
        self.tvAba3.place(x=380,y=0)
        self.mostrarOrdem()

        mainloop()

    #########################################################################################################################

    def limparFuncionario(self):
        self.entrada_NomeAba1.delete(0,END)
        self.entrada_SenhaAba1.delete(0,END)
        self.entrada_CpfAba1.delete(0,END)
        self.entrada_CargoAba1.delete(0,END)

    def mostrarFuncionario(self):
        self.tvAba1.delete(*self.tvAba1.get_children())
        sql = "SELECT * FROM funcionarios"
        linhas = banco.mostrarDados(sql)
        for i in linhas:
            self.tvAba1.insert("", "end", values=i)
    
    def insertFuncionario(self):
        if self.entrada_NomeAba1.get() == "" or self.entrada_SenhaAba1.get() == "" or self.entrada_CpfAba1.get() == "" or self.entrada_CargoAba1.get() == "":
            messagebox.showinfo(title="ERRO", message="Digite todos os dados")
            return
        try:
            sql = "INSERT INTO funcionarios (nome,senha,cpffun,cargo) VALUES ('{}','{}','{}','{}')".format(self.entrada_NomeAba1.get(), self.entrada_SenhaAba1.get(),self.entrada_CpfAba1.get(), self.entrada_CargoAba1.get())
            banco.Dados(sql)
        except:
            messagebox.showinfo(title="ERRO", message="Erro ao inserir novos dados")
            return
        self.mostrarFuncionario()
        self.limparFuncionario()

    def editarFuncionario(self):
        if self.entrada_NomeAba1.get() == "" or self.entrada_SenhaAba1.get() == "" or self.entrada_CpfAba1.get() == "" or self.entrada_CargoAba1.get() == "":
            messagebox.showinfo(title="ERRO", message="Digite todos os dados")
            return
        try:
            sql = "UPDATE funcionarios SET nome = '{}', senha = '{}', cpffun = '{}', cargo = '{}' WHERE idfuncionario = '{}'" .format(self.entrada_NomeAba1.get(), self.entrada_SenhaAba1.get(), self.entrada_CpfAba1.get(), self.entrada_CargoAba1.get(), row[0])
            banco.Dados(sql)
        except:
            messagebox.showinfo(title="ERRO", message=("Erro ao editar os dados"))
        self.mostrarFuncionario()
        self.limparFuncionario()

    def deletarFuncionario(self):
        sql = "DELETE FROM funcionarios WHERE idfuncionario = '{}'".format(row[0])
        banco.Dados(sql)
        self.limparFuncionario()
        self.mostrarFuncionario()

    ########################################################################################################################

    def limparCliente(self):
        self.entrada_NomeAba2.delete(0,END)
        self.entrada_CpfAba2.delete(0,END)
        self.entrada_FoneAba2.delete(0,END)
        self.entrada_EmailAba2.delete(0,END)
        self.entrada_PlacaAba2.delete(0,END)
        self.entrada_EnderecoAba2.delete(0,END)

    def mostrarCliente(self):
        self.tvAba2.delete(*self.tvAba2.get_children())
        sql = "SELECT * FROM cliente"
        linhas = banco.mostrarDados(sql)
        for i in linhas:
            self.tvAba2.insert("", "end", values=i)

    def cadastrarCliente(self):
        if self.entrada_NomeAba2.get() == "" or self.entrada_CpfAba2.get() == "" or self.entrada_FoneAba2.get() == "" or self.entrada_EmailAba2.get() == "" or self.entrada_PlacaAba2.get() == "" or self.entrada_EnderecoAba2.get() == "":
            messagebox.showinfo(title="ERRO", message="Digite todos os dados")
        try:
            sql = "INSERT INTO cliente (nome,cpf,telefone,email, placa,endereco) VALUES ('{}','{}','{}','{}','{}','{}')".format(self.entrada_NomeAba2.get(), self.entrada_CpfAba2.get(), self.entrada_FoneAba2.get(), self.entrada_EmailAba2.get(),self.entrada_PlacaAba2.get(), self.entrada_EnderecoAba2.get())
            banco.Dados(sql)
        except:
            messagebox.showinfo(title="ERRO", message="Erro ao cadastrar novo cliente")
        self.mostrarCliente()
        self.limparCliente()
    
    def editarCliente(self):
        if self.entrada_NomeAba2.get() == "" or self.entrada_CpfAba2.get() == "" or self.entrada_FoneAba2.get() == "" or self.entrada_EmailAba2.get() == ""   or self.entrada_PlacaAba2.get() == "" or self.entrada_EnderecoAba2.get() == "":
            messagebox.showinfo(title="ERRO", message="Digite todos os dados")
        try:
            sql = "UPDATE cliente SET nome = '{}', cpf = '{}', telefone = '{}', email = '{}' , placa = '{}', endereco = '{}' WHERE idcliente = {}".format(self.entrada_NomeAba2.get(),self.entrada_CpfAba2.get(),self.entrada_FoneAba2.get(),self.entrada_EmailAba2.get(),self.entrada_PlacaAba2.get(),self.entrada_EnderecoAba2.get(), rowAba2[0])
            banco.Dados(sql)
        except:
            messagebox.showinfo(title="ERRO", message="Erro ao editar dados")
        self.mostrarCliente()
        self.limparCliente()

    def deletarCliente(self):
        sql = "DELETE FROM cliente WHERE idcliente = '{}'".format(rowAba2[0])
        banco.Dados(sql)
        self.limparCliente()
        self.mostrarCliente()

    ########################################################################################################################

    def mostrarOrdem(self):
        self.tvAba3.delete(*self.tvAba3.get_children())
        sql = "SELECT * FROM ordem WHERE status LIKE 'Ativa'"
        linhas = banco.mostrarDados(sql)
        for i in linhas:
            self.tvAba3.insert("", "end", values=i)

    def concluirOrdem(self):
        sql = "UPDATE ordem SET status = 'concluida' WHERE idordem = {}".format(rowAba3[0]) 
        banco.Dados(sql)
        self.item = self.tvAba3.selection()[0]
        self.tvAba3.delete(self.item)

    def deletarOrdem(self):
        sql = "DELETE FROM ordem WHERE idordem = '{}'".format(rowAba3[0])
        banco.Dados(sql)
        self.mostrarOrdem()

    def mostrarOrdemAtiva(self):
        self.mostrarOrdem()

    def mostrarOrdemConcluida(self):
        sql = "SELECT * FROM ordem WHERE status LIKE 'concluida'"
        linhas = banco.mostrarDados(sql)
        self.tvAba3.delete(*self.tvAba3.get_children())
        for i in linhas:
            self.tvAba3.insert("", "end", values=i)
        
    #########################################################################################################################
    def pesquisarAba1(self):
        self.tvAba1.delete(*self.tvAba1.get_children())
        sql = "SELECT * FROM funcionarios WHERE nome LIKE '%{}%'".format(self.entrada_pesquisarAba1.get())
        linhas = banco.mostrarDados(sql)
        for i in linhas:
            self.tvAba1.insert("", "end", values=i)

    def pesquisarAba2(self):
        self.tvAba2.delete(*self.tvAba2.get_children())
        sql = "SELECT * FROM cliente WHERE nome LIKE '%{}%'".format(self.entrada_pesquisarAba2.get())
        linhas = banco.mostrarDados(sql)
        for i in linhas:
            self.tvAba2.insert("", "end", values=i)
        
    def pesquisarAba3(self):
        self.tvAba3.delete(*self.tvAba3.get_children())
        sql = "SELECT * FROM ordem WHERE cpfmecanico LIKE '%{}%'".format(self.entrada_pesquisarAba3.get())
        linhas = banco.mostrarDados(sql)
        for i in linhas:
            self.tvAba3.insert("", "end", values=i)

    ########################################################################################################################
    def limparAba1(self):
        self.entrada_pesquisarAba1.delete(0,END)
        self.mostrarFuncionario()

    def limparAba2(self):
        self.entrada_pesquisarAba2.delete(0,END)
        self.mostrarCliente()

    def limparAba3(self):
        self.entrada_pesquisarAba3.delete(0,END)
        self.mostrarOrdem()
