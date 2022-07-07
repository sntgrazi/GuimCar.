from tkinter import *
from tkinter import ttk
import banco
from tkinter import messagebox

class Recepcionista:
    def __init__(self):

        self.cor1 = "#DEDEDE"

        self.janela = Toplevel()
        self.janela.title("Recepcionista")
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

        self.nb.add(self.aba1, text="Cadastrar Clientes")
        self.nb.add(self.aba2, text="Ver Orçamentos")
        
        ####################################################################################################################

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

        ####################################################################################################################

        nomeCliente = StringVar()
        cpfCliente = StringVar()
        foneCliente = StringVar()
        emailCliente =StringVar()
        enderecoCliente = StringVar()
        placaCliente = StringVar()

        self.label_nomeAba1 = Label(self.container_EsquerdaAba1, text="Nome", font="Arial 16", bg=self.cor1)
        self.label_nomeAba1.place(x=10,y=90)
        self.entrada_NomeAba1 = Entry(self.container_EsquerdaAba1, font="Arial 14", bd=1,relief="solid", textvariable=nomeCliente)
        self.entrada_NomeAba1.place(x=90,y=92, width=250)

        self.label_cpfAba1 = Label(self.container_EsquerdaAba1, text="Cpf", font="Arial 16", bg=self.cor1)
        self.label_cpfAba1.place(x=10,y=140)
        self.entrada_CpfAba1 = Entry(self.container_EsquerdaAba1, font="Arial 14", bd=1, relief="solid", textvariable=cpfCliente)
        self.entrada_CpfAba1.place(x=90, y=142, width=250)
    
        self.label_foneAba1 = Label(self.container_EsquerdaAba1, text="Fone", font="Arial 16", bg=self.cor1)
        self.label_foneAba1.place(x=10,y=190)
        self.entrada_FoneAba1 = Entry(self.container_EsquerdaAba1, font="Arial 14", bd=1,relief="solid", textvariable=foneCliente)
        self.entrada_FoneAba1.place(x=90,y=192, width=250)

        self.label_emailAba1 = Label(self.container_EsquerdaAba1, text="Email", font="Arial 16", bg=self.cor1)
        self.label_emailAba1.place(x=10,y=240)
        self.entrada_EmailAba1 = Entry(self.container_EsquerdaAba1, font="Arial 14", bd=1, relief="solid", textvariable=emailCliente)
        self.entrada_EmailAba1.place(x=90, y=242, width=250)

        self.label_enderecoAba1 = Label(self.container_EsquerdaAba1, text="Placa", font="Arial 16", bg=self.cor1)
        self.label_enderecoAba1.place(x=10,y=290)
        self.entrada_EnderecoAba1 = Entry(self.container_EsquerdaAba1, font="Arial 14", bd=1, relief="solid", textvariable=enderecoCliente)
        self.entrada_EnderecoAba1.place(x=90, y=292, width=250)

        self.label_placaAba1 = Label(self.container_EsquerdaAba1, text="Endereço", font="Arial 16", bg=self.cor1)
        self.label_placaAba1.place(x=10,y=340)
        self.entrada_PlacaAba1 = Entry(self.container_EsquerdaAba1, font="Arial 14", bd=1, relief="solid", textvariable=placaCliente)
        self.entrada_PlacaAba1.place(x=110, y=342, width=250)

        ###################################################################################################################

        self.btn_CadastrarAba1 = Button(self.container_EsquerdaAba1, text="Cadastrar", font="Arial 16", bd=1, relief="solid", command=self.cadastrarCliente)
        self.btn_CadastrarAba1.place(x=20, y=390, width=150)
      
        self.btn_DeletarAba1 = Button(self.container_EsquerdaAba1, text="Deletar", font="Arial 16", bd=1, relief="solid", command=self.deletarCliente)
        self.btn_DeletarAba1.place(x=190, y=390, width=150)

        self.btn_EditarAba1 = Button(self.container_EsquerdaAba1, text="Editar", font="Arial 16", bd=1, relief="solid", command=self.editarCliente)
        self.btn_EditarAba1.place(x=20, y=440, width=150)

        self.btn_LimparAba1 = Button(self.container_EsquerdaAba1, text="Limpar", font="Arial 16", bd=1, relief="solid", command=self.limparCliente)
        self.btn_LimparAba1.place(x=190, y=440, width=150)

        #####################################################################################################################

        def getDataAba1(event):
            selected_row = self.tvAba1.focus()
            data = self.tvAba1.item(selected_row)
            global rowAba1 
            rowAba1 = data["values"]
            nomeCliente.set(rowAba1[1])
            cpfCliente.set(rowAba1[2])
            foneCliente.set(rowAba1[3])
            emailCliente.set(rowAba1[4])
            placaCliente.set(rowAba1[5])
            enderecoCliente.set(rowAba1[6])

        #####################################################################################################################

        self.tvAba1= ttk.Treeview(self.aba1, columns=('id', 'nome', 'cpf','fone','email','placa','endereco'), show='headings', height=24)

        self.tvAba1.column('id', width=30)
        self.tvAba1.column('nome', width=100)
        self.tvAba1.column('cpf', width=100)
        self.tvAba1.column('fone', width=90)
        self.tvAba1.column('email', width=100)
        self.tvAba1.column('placa', width=90)
        self.tvAba1.column('endereco', width=100)

        self.tvAba1.heading('id', text="ID")
        self.tvAba1.heading('nome', text="NOME")
        self.tvAba1.heading('cpf', text="CPF")
        self.tvAba1.heading('fone', text="FONE")
        self.tvAba1.heading('email', text="EMAIL")
        self.tvAba1.heading('placa', text="PLACA")
        self.tvAba1.heading('endereco', text="ENDEREÇO")

        self.tvAba1.bind("<ButtonRelease-1>", getDataAba1)
        self.tvAba1.place(x=380,y=0)
        self.mostrarCliente()

        ################################################ SEGUNDA ABA ########################################################

        self.container_EsquerdaAba2 = Frame(self.aba2, width=380, height=505, bg=self.cor1, bd=1, relief="solid")
        self.container_EsquerdaAba2.place(x=0,y=0)

        self.label_procurarAba2 = LabelFrame(self.container_EsquerdaAba2,text="Procurar", bd=1, relief="solid", font="Arial 15", bg=self.cor1)
        self.label_procurarAba2.place(x=10,y=30, width=360, height=80)

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

        self.imagem_ButtonAceit = PhotoImage(file="img/aceitar.png")
        self.imagem_ButtonAceitar = self.imagem_ButtonAceit.subsample(1,1)
        self.btn_AceitarOr = Button(self.container_EsquerdaAba2, text="   Aceitar Orçamento", image=self.imagem_ButtonAceitar, compound=LEFT, font="Arial 16", bd=1, relief="solid", command=self.tranformarEmOrdem)
        self.btn_AceitarOr.place(x=40, y=180, width=300, height=50)

        self.imagem_ButtonDel = PhotoImage(file="img/remover.png")
        self.imagem_ButtonDelete = self.imagem_ButtonDel.subsample(1,1)
        self.btn_DeletarOr = Button(self.container_EsquerdaAba2, text="   Deletar Orçamento", image=self.imagem_ButtonDelete, compound=LEFT, font="Arial 16", bd=1, relief="solid",command=self.deletarOrcamento)
        self.btn_DeletarOr.place(x=40, y=300, width=300,height=50)

        ############################################# Tree view para a segunda aba #####################################

        def getDataAba2(event):
            selected_row = self.tvAba2.focus()
            data = self.tvAba2.item(selected_row)
            global rowAba2
            rowAba2 = data["values"]
         
        #####################################################################################################################

        self.tvAba2= ttk.Treeview(self.aba2, columns=('id', 'cpfcliente', 'cpfmecanico','valor','descricao'), show='headings', height=24)

        self.tvAba2.column('id', width=60)
        self.tvAba2.column('cpfcliente', width=130)
        self.tvAba2.column('cpfmecanico', width=130)
        self.tvAba2.column('valor', width=140)
        self.tvAba2.column('descricao', width=150)
        

        self.tvAba2.heading('id', text="ID")
        self.tvAba2.heading('cpfcliente', text="CPFCLIENTE")
        self.tvAba2.heading('cpfmecanico', text="CPFMECÂNICO")
        self.tvAba2.heading('valor', text="VALOR")
        self.tvAba2.heading('descricao', text="DESCRIÇÃO")
    
        self.tvAba2.bind("<ButtonRelease-1>", getDataAba2)
        self.tvAba2.place(x=380,y=0)
        self.mostrarOrcamento()

        mainloop()

    #########################################################################################################################

    def limparCliente(self):
        self.entrada_NomeAba1.delete(0,END)
        self.entrada_CpfAba1.delete(0,END)
        self.entrada_FoneAba1.delete(0,END)
        self.entrada_EmailAba1.delete(0,END)
        self.entrada_PlacaAba1.delete(0,END)
        self.entrada_EnderecoAba1.delete(0,END)

    def mostrarCliente(self):
        self.tvAba1.delete(*self.tvAba1.get_children())
        sql = "SELECT * FROM cliente"
        linhas = banco.mostrarDados(sql)
        for i in linhas:
            self.tvAba1.insert("", "end", values=i)

    def cadastrarCliente(self):
        if self.entrada_NomeAba1.get() == "" or self.entrada_CpfAba1.get() == "" or self.entrada_FoneAba1.get() == "" or self.entrada_EmailAba1.get() == "" or self.entrada_PlacaAba1.get() == "" or self.entrada_EnderecoAba1.get() == "":
            messagebox.showinfo(title="ERRO", message="Digite todos os dados")
        try:
            sql = "INSERT INTO cliente (nome,cpf,telefone,email, placa,endereco) VALUES ('{}','{}','{}','{}','{}','{}')".format(self.entrada_NomeAba1.get(), self.entrada_CpfAba1.get(), self.entrada_FoneAba1.get(), self.entrada_EmailAba1.get(),self.entrada_PlacaAba1.get(), self.entrada_EnderecoAba1.get())
            banco.Dados(sql)
        except:
            messagebox.showinfo(title="ERRO", message="Erro ao cadastrar novo cliente")
        self.mostrarCliente()
        self.limparCliente()
    
    def editarCliente(self):
        if self.entrada_NomeAba1.get() == "" or self.entrada_CpfAba1.get() == "" or self.entrada_FoneAba1.get() == "" or self.entrada_EmailAba1.get() == ""   or self.entrada_PlacaAba1.get() == "" or self.entrada_EnderecoAba1.get() == "":
            messagebox.showinfo(title="ERRO", message="Digite todos os dados")
        try:
            sql = "UPDATE cliente SET nome = '{}', cpf = '{}', telefone = '{}', email = '{}' , placa = '{}', endereco = '{}' WHERE idcliente = {}".format(self.entrada_NomeAba1.get(),self.entrada_CpfAba1.get(),self.entrada_FoneAba1.get(),self.entrada_EmailAba1.get(),self.entrada_PlacaAba1.get(),self.entrada_EnderecoAba1.get(), rowAba1[0])
            banco.Dados(sql)
        except:
            messagebox.showinfo(title="ERRO", message="Erro ao editar dados")
        self.mostrarCliente()
        self.limparCliente()

    def deletarCliente(self):
        sql = "DELETE FROM cliente WHERE idcliente = '{}'".format(rowAba1[0])
        banco.Dados(sql)
        self.limparCliente()
        self.mostrarCliente()

    ########################################################################################################################

    def mostrarOrcamento(self):
        self.tvAba2.delete(*self.tvAba2.get_children())
        sql = "SELECT * FROM orcamento"
        linhas = banco.mostrarDados(sql)
        for i in linhas:
            self.tvAba2.insert("", "end", values=i)

    def tranformarEmOrdem(self):
        sql = "INSERT INTO ordem SELECT * FROM orcamento WHERE idorcamento = {}".format(rowAba2[0])
        banco.Dados(sql)
        self.mostrarOrcamento()
        self.deletarOrcamento()

    def deletarOrcamento(self):
        sql = "DELETE FROM orcamento WHERE idorcamento = '{}'".format(rowAba2[0])
        banco.Dados(sql)
        self.mostrarOrcamento()

    ########################################################################################################################

    def pesquisarAba1(self):
        self.tvAba1.delete(*self.tvAba1.get_children())
        sql = "SELECT * FROM cliente WHERE nome LIKE '%{}%'".format(self.entrada_pesquisarAba1.get())
        linhas = banco.mostrarDados(sql)
        for i in linhas:
            self.tvAba1.insert("", "end", values=i)

    def pesquisarAba2(self):
        self.tvAba2.delete(*self.tvAba2.get_children())
        sql = "SELECT * FROM orcamento WHERE cpfcliente LIKE '%{}%'".format(self.entrada_pesquisarAba2.get())
        linhas = banco.mostrarDados(sql)
        for i in linhas:
            self.tvAba2.insert("", "end", values=i)

    #########################################################################################################################

    def limparAba1(self):
        self.entrada_pesquisarAba1.delete(0,END)
        self.mostrarCliente()

    def limparAba2(self):
        self.entrada_pesquisarAba2.delete(0,END)
        self.mostrarOrcamento()