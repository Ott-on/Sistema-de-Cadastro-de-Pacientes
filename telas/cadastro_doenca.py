import tkinter as tk
from tkinter import END, RAISED, RIDGE, Button, Entry, Label, PhotoImage, messagebox
from modelos.sistema_doencas import SistemaDoenca


class cadastrarDoencas(tk.Frame):
    def __init__(self, parent, controller, *args):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#242323')

        sistema_doenca = SistemaDoenca()

        self.modo = "cadastrar"
        # verificando o modo do cadastro de doenças
        self.doenca_alterar = {}

        # Verificando se o modo é cadastro ou alterar
        if args:
            print("=======> ENTRANDO NO MODO ALTERAR DOENÇA!")
            self.modo = args[0]["modo"]
            self.doenca_alterar = args[0]["doenca_alterar"]

        # retangulo azul da tela
        label_retangulo = Label(self, width=1000, height=4, bg='#02bae8')
        label_retangulo.place(x=0, y=0)

        # Nome
        entrada_nome = Entry(self, width=20, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_nome.place(x=160, y=190)
        label_nome = Label(self, width=10, height=2, text='Nome:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_nome.place(x=145, y=150)

        self.entrada_nome = entrada_nome

        # cid
        entrada_cid = Entry(self, width=10, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_cid.place(x=160, y=340)
        label_cid = Label(self, width=10, height=2, text='CID:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_cid.place(x=140, y=300)

        self.entrada_cid = entrada_cid

        # botão voltar
        img = PhotoImage(file='imagens/voltar_label.png')
        button_image = Button(self, image=img, bg='#02bae8', fg='#02bae8', activebackground='#02bae8', command=lambda: self.voltar(
            controller), relief='solid', overrelief='solid', borderwidth=0, highlightthickness=0)
        button_image.image = img
        button_image.place(x=10, y=10)

        # botão cadastrar
        button_cadastrar_text = "Alterar" if self.modo == "alterar" else "Cadastrar"
        button_cadastrar = Button(self, text=button_cadastrar_text, font=("Arial", 16), activebackground='#02bae8', bg='#02bae8', fg='white', command=lambda: self.fazer_cadastro(sistema_doenca,
                                                                                                                                                                                  controller), relief='solid', overrelief='solid', width=10, height=2, borderwidth=0, highlightthickness=0)
        button_cadastrar.place(x=180, y=450)

        if self.modo == "alterar":
            self.entrada_nome.insert(0, self.doenca_alterar[1])
            self.entrada_cid.insert(0, self.doenca_alterar[0])

    def limpar_campos(self):
        self.entrada_nome.delete(0, END)
        self.entrada_cid.delete(0, END)

    def voltar(self, controller):
        from telas.tela_doencas import DoencasListagem
        controller.carregar_tela(DoencasListagem)

    def fazer_cadastro(self, sistema_doencas: SistemaDoenca,  controller):

        nome = self.entrada_nome.get()
        cid = self.entrada_cid.get()

        if nome and cid:
            if self.modo == 'alterar':
                sistema_doencas.alterar(cid=cid, nome_doenca=nome)
                messagebox.showinfo(
                    "Sucesso!", "Doença alterada com sucesso!")
                self.voltar(controller)
            else:
                messagebox.showinfo(
                    "Sucesso!", "Doença cadastrada com sucesso!")
                sistema_doencas.cadastrar(cid=cid, nome_doenca=nome)
            self.limpar_campos()
        else:
            messagebox.showinfo(
                "Aviso!", "Preencha todos os campos para continuar", icon="warning")
