from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import banco


class Mecanico:
    def __init__(self):

        self.cor1 = "#DEDEDE"

        self.janela = Toplevel()
        self.janela.title("Mecânico")
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

        self.nb.add(self.aba1, text="Cadastrar Orçamento")
        self.nb.add(self.aba2, text="Ver Ordems de serviço")

        ##################################### Primeira aba ########################################

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

        #####################################################################################################################

        cpfcliente = StringVar()
        cpfmecanico = StringVar()
        valor = StringVar()
        
        self.label_cpfClienteAba1 = Label(self.container_EsquerdaAba1, text="CpfCliente", font="Arial 16", bg=self.cor1)
        self.label_cpfClienteAba1.place(x=10,y=110)
        self.entrada_cpfClienteAba1 = Entry(self.container_EsquerdaAba1, font="Arial 14", bd=1,relief="solid", textvariable=cpfcliente)
        self.entrada_cpfClienteAba1.place(x=140,y=112, width=230)
    
        self.label_cpfMecAba1 = Label(self.container_EsquerdaAba1, text="CpfMecânico", font="Arial 16", bg=self.cor1)
        self.label_cpfMecAba1.place(x=10,y=160)
        self.entrada_cpfMecAba1 = Entry(self.container_EsquerdaAba1, font="Arial 14", bd=1,relief="solid", textvariable=cpfmecanico)
        self.entrada_cpfMecAba1.place(x=140,y=162, width=230)

        self.label_valorAba1 = Label(self.container_EsquerdaAba1, text="Valor", font="Arial 16", bg=self.cor1)
        self.label_valorAba1.place(x=10,y=210)
        self.entrada_valorAba1 = Entry(self.container_EsquerdaAba1, font="Arial 14", bd=1, relief="solid", textvariable=valor)
        self.entrada_valorAba1.place(x=140, y=212, width=230)

        self.label_descricaoAba1 = Label(self.container_EsquerdaAba1, text="Descrição", font="Arial 16", bg=self.cor1)
        self.label_descricaoAba1.place(x=10,y=260)
        self.text_descricaoAba1 = Text(self.container_EsquerdaAba1, font="Arial 10", bd=1, relief="solid")
        self.text_descricaoAba1.place(x=140, y=262, height=100, width=230)

        ####################################################################################################################

        self.btn_CadastrarAba1 = Button(self.container_EsquerdaAba1, text="Cadastrar", font="Arial 16", bd=1, relief="solid", command=self.cadastrarOrcamento)
        self.btn_CadastrarAba1.place(x=20, y=380, width=150)

        self.btn_DeletarAba1 = Button(self.container_EsquerdaAba1, text="Deletar", font="Arial 16", bd=1, relief="solid", command=self.deletarOrcamento)
        self.btn_DeletarAba1.place(x=190, y=380, width=150)

        self.btn_EditarAba1 = Button(self.container_EsquerdaAba1, text="Editar", font="Arial 16", bd=1, relief="solid", command=self.editarOrcamento)
        self.btn_EditarAba1.place(x=20, y=450, width=150)

        self.btn_LimparAba1 = Button(self.container_EsquerdaAba1, text="Limpar", font="Arial 16", bd=1, relief="solid", command=self.limparOrcamento)
        self.btn_LimparAba1.place(x=190, y=450, width=150)

        ########################################## Tree view primeira aba ########################

        def getData(event):
            selected_row = self.tvAba1.focus()
            data = self.tvAba1.item(selected_row)
            global row 
            row = data["values"]
            cpfcliente.set(row[1])
            cpfmecanico.set(row[2])
            valor.set(row[3])
            self.text_descricaoAba1.delete(1.0, END)
            self.text_descricaoAba1.insert(END, row[4])

        #####################################################################################################################

        self.tvAba1= ttk.Treeview(self.aba1, columns=('id', 'cpfcliente', 'cpfmecanico','valor','descricao'), show='headings', height=24)

        self.tvAba1.column('id', width=60)
        self.tvAba1.column('cpfcliente', width=130)
        self.tvAba1.column('cpfmecanico', width=130)
        self.tvAba1.column('valor', width=140)
        self.tvAba1.column('descricao', width=150)
        

        self.tvAba1.heading('id', text="ID")
        self.tvAba1.heading('cpfcliente', text="CPFCLIENTE")
        self.tvAba1.heading('cpfmecanico', text="CPFMECÂNICO")
        self.tvAba1.heading('valor', text="VALOR")
        self.tvAba1.heading('descricao', text="DESCRIÇÃO")
        
        self.tvAba1.bind("<ButtonRelease-1>", getData)
        self.tvAba1.place(x=380,y=0)
        self.mostrarOrcamento()

        ########################################## Segunda ABA #########################################

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

        self.btn_MostrarOrAti= Button(self.container_EsquerdaAba2, text="Mostrar Ordems Ativas", font="Arial 16", bd=1, relief="solid", command=self.mostrarAtivas)
        self.btn_MostrarOrAti.place(x=40, y=180, width=300,height=50)

        self.btn_MostrarOrCon = Button(self.container_EsquerdaAba2, text="Mostrar Ordems Concluidas", font="Arial 16", bd=1, relief="solid", command=self.mostrarConcluidas)
        self.btn_MostrarOrCon.place(x=40, y=280, width=300,height=50)

        self.btn_Sair = Button(self.container_EsquerdaAba2, text="Sair", font="Arial 16", bd=1, relief="solid", command=self.sair)
        self.btn_Sair.place(x=40, y=380, width=300,height=50)

        ######################################### Tree  view da segunda aba #########################

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
    
        self.tvAba2.place(x=380,y=0)
        self.mostrarAtivas()

        mainloop()

        #####################################################################################################################
    def limparOrcamento(self):
        self.entrada_cpfClienteAba1.delete(0,END)
        self.entrada_cpfMecAba1.delete(0,END)
        self.entrada_valorAba1.delete(0,END)
        self.text_descricaoAba1.delete(1.0,END)

    def mostrarOrcamento(self):
        self.tvAba1.delete(*self.tvAba1.get_children())
        sql = "SELECT * FROM orcamento"
        linhas = banco.mostrarDados(sql)
        for i in linhas:
            self.tvAba1.insert("", "end", values=i)
        
    def cadastrarOrcamento(self):
        if self.entrada_cpfClienteAba1.get() == "" or self.entrada_cpfMecAba1.get() == "" or self.entrada_valorAba1.get() == "" or self.text_descricaoAba1.get(1.0,END) == "":
                messagebox.showinfo(title="ERRO", message="Digite todos os dados")
        try:
            sql = "INSERT INTO orcamento (cpfcliente,cpfmecanico,valor,descricao) VALUES ('{}','{}','{}','{}')".format(self.entrada_cpfClienteAba1.get(), self.entrada_cpfMecAba1.get(), self.entrada_valorAba1.get(), self.text_descricaoAba1.get(1.0,END))
            banco.Dados(sql)
        except:
            messagebox.showinfo(title="ERRO", message="Erro ao cadastrar novos dados")
        self.mostrarOrcamento()
        self.limparOrcamento()

    def editarOrcamento(self):
        if self.entrada_cpfClienteAba1.get() == "" or self.entrada_cpfMecAba1.get() == "" or self.entrada_valorAba1.get() == "" or self.text_descricaoAba1.get(1.0,END) == "":
         messagebox.showinfo(title="ERRO", message="Digite todos os dados")
        try:
           sql = "UPDATE orcamento SET cpfcliente = '{}',cpfmecanico = '{}', valor = '{}', descricao = '{}' WHERE idorcamento = '{}'".format(self.entrada_cpfClienteAba1.get(), self.entrada_cpfMecAba1.get(), self.entrada_valorAba1.get(), self.text_descricaoAba1.get(1.0,END), row[0])
           banco.Dados(sql)
        except:
                messagebox.showinfo(title="ERRO", message="Erro ao editar dados")
        self.mostrarOrcamento()
        self.limparOrcamento()

    def deletarOrcamento(self):
        sql = "DELETE FROM orcamento WHERE idorcamento = '{}'".format(row[0])
        banco.Dados(sql)
        self.limparOrcamento()
        self.mostrarOrcamento()

    #########################################################################################################################

    def mostrarAtivas(self):
        sql = "SELECT cpffun FROM funcionarios WHERE status = 'Logado'"
        cpflog = banco.mostrarDados(sql)
        sql2 = "SELECT * FROM ordem WHERE cpfmecanico = {} AND status = 'Ativa' ".format(cpflog[0][0])
        linha = banco.mostrarDados(sql2)
        self.tvAba2.delete(*self.tvAba2.get_children())
        for i in linha:
            self.tvAba2.insert("", "end",values=i )

    def mostrarConcluidas(self):
        sql = "SELECT cpffun FROM funcionarios WHERE status = 'Logado'"
        cpflog = banco.mostrarDados(sql)
        sql2 = "SELECT * FROM ordem WHERE cpfmecanico = {} AND status = 'concluida'".format(cpflog[0][0])
        linha = banco.mostrarDados(sql2)
        self.tvAba2.delete(*self.tvAba2.get_children())
        for i in linha:
            self.tvAba2.insert("", "end",values=i )

    def sair(self):
        sql = "SELECT cpffun FROM funcionarios WHERE status = 'Logado'"
        cpflog = banco.mostrarDados(sql)
        desconet = "UPDATE funcionarios SET status = 'desconectado' WHERE cpffun = {}".format(cpflog[0][0])
        banco.Dados(desconet)
        self.janela.destroy()
        
    ########################################################################################################################

    def limparAba1(self):
        self.entrada_pesquisarAba1.delete(0,END)
        self.mostrarOrcamento()

    def limparAba2(self):
        self.entrada_pesquisarAba2.delete(0,END)
        self.mostrarAtivas()

    ########################################################################################################################

    def pesquisarAba1(self):
        self.tvAba1.delete(*self.tvAba1.get_children())
        sql = "SELECT * FROM orcamento WHERE cpfcliente LIKE '%{}%'".format(self.entrada_pesquisarAba1.get())
        linhas = banco.mostrarDados(sql)
        for i in linhas:
            self.tvAba1.insert("", "end", values=i)

    def pesquisarAba2(self):
        self.tvAba2.delete(*self.tvAba2.get_children())
        sql = "SELECT * FROM ordem WHERE cpfcliente LIKE '%{}%'".format(self.entrada_pesquisarAba2.get())
        linhas = banco.mostrarDados(sql)
        for i in linhas:
            self.tvAba2.insert("", "end", values=i)