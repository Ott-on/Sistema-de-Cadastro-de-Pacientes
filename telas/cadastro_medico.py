import tkinter as tk
from tkinter import RAISED, RIDGE, Button, Entry, Label, PhotoImage, messagebox
from modelos.sistema_medico import SistemaMedico


class CadastroMedico(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')

        # Criando a instancia do Sistema medico
        sistema_medico = SistemaMedico()

        # escritos e imagens:
        img2 = PhotoImage(file='imagens/tela_cadastro_medico.png')
        label_image = Label(self, image=img2, relief='solid',
                            borderwidth=0, highlightthickness=0)
        label_image.image = img2
        label_image.place(x=0, y=90)

        label_retangulo = Label(self, width=1000, height=4, bg='#02bae8')
        label_retangulo.place(x=0, y=0)

        label_retangulocinza = Label(
            self, width=51, height=40, background='#242323', relief=RAISED)
        label_retangulocinza.place(x=638, y=65)

        label_cadastrar = Label(self, width=15, height=2, text='CADASTRE-SE', font=(
            "Arial", 25), bg='#242323', fg='#02bae8')
        label_cadastrar.place(x=680, y=70)

        # Nome do medico
        label_nome_medico = Label(self, width=20, height=2, text='Nome Completo do Médico:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_nome_medico.place(x=690, y=150)

        entrada_nome_medico = Entry(self, width=14, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_nome_medico.place(x=690, y=190)
        # fim Nome do medico

        self.entrada_nome_medico = entrada_nome_medico

        label_usuario = Label(self, width=20, height=2, text='Usuário (para acesso):', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_usuario.place(x=670, y=325)

        label_crm = Label(self, width=20, height=1, text='CRM do Médico:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_crm.place(x=653, y=250)

        label_senha = Label(self, width=20, height=2, text='Senha (para acesso):', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_senha.place(x=670, y=410)

        # botão voltar
        img = PhotoImage(file='imagens/voltar_label.png')
        button_image = Button(self, image=img, bg='#02bae8', fg='#02bae8', activebackground='#02bae8', command=lambda: self.voltar_login(
            controller), relief='solid', overrelief='solid', borderwidth=0, highlightthickness=0)
        button_image.image = img
        button_image.place(x=10, y=10)

        # Entradas:
        entrada_usuario2 = Entry(self, width=14, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_usuario2.place(x=690, y=360)

        self.entrada_usuario2 = entrada_usuario2

        entrada_crm2 = Entry(self, width=14, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_crm2.place(x=690, y=280)

        self.entrada_crm2 = entrada_crm2

        entrada_senha2 = Entry(self, width=14, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_senha2.place(x=690, y=450)

        self.entrada_senha2 = entrada_senha2

        botao_cadastrar = Button(self, text='Cadastrar', width=23, command=lambda: self.cadastrar_medico(sistema_medico, controller), height=2, font=(
            "Arial", 15), bg='#02bae8', fg='white', relief=RAISED, overrelief=RAISED)
        botao_cadastrar.place(x=690, y=518)

    def voltar_login(self, controller):
        from telas.login_medico import LoginMedico
        controller.show_frame(LoginMedico)

    def cadastrar_medico(self, sistema_medico: SistemaMedico, controller):
        from telas.login_medico import LoginMedico

        entrada_nome_medico = self.entrada_nome_medico.get()
        usuario = self.entrada_usuario2.get()
        crm = self.entrada_crm2.get()
        senha = self.entrada_senha2.get()

        # Verifica se algum dos campos estão vazios
        if entrada_nome_medico or usuario or crm or senha:
            if len(crm) == 7:
                if len(senha) >= 8:
                    # Se todas as verificações darem certo.
                    sistema_medico.cadastrar(
                        crm, entrada_nome_medico, usuario, senha, lambda: controller.show_frame(LoginMedico))
                else:
                    messagebox.showinfo(
                        "Aviso!", "A senha deve conter no mínimo 8 caracteres!", icon="warning")
            else:
                messagebox.showinfo(
                    "Aviso!", "CRM inválido!", icon="warning")

        else:
            messagebox.showinfo(
                "Aviso!", "Preencha todos os campos para continuar", icon="warning")
