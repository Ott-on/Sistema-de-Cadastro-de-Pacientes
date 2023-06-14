import tkinter as tk
from tkinter import RAISED, RIDGE, Button, Entry, Label, PhotoImage, messagebox
from modelos.sistema_medico import SistemaMedico
from telas.cadastro_medico import CadastroMedico
from telas.menu_opcoes import MenuOpcoes


class LoginMedico(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Instância do sistema do medico
        sistema_medico = SistemaMedico()

        self.configure(bg='white')
        img = PhotoImage(file='imagens/tela_abertura.png')
        label_image = Label(self, image=img)
        label_image.image = img
        label_image.place(x=-60, y=-2)

        label_fundobranco = Label(
            self, width=45, height=30, background='#242323', relief=RAISED)
        label_fundobranco.place(x=638, y=50)

        label_escrita = Label(
            self, width=20, height=1, fg='#888a89', text='Ainda não tem sua conta?', background='#242323', font=(
                "Arial", 10))
        label_escrita.place(x=685, y=400)

        # LOGIN:
        label_LOGIN = Label(self, width=10, height=2, text='LOGIN', font=(
            "Arial", 25), bg='#242323', fg='#02bae8')
        label_LOGIN.place(x=700, y=70)

        # Usuário:
        label_usuario = Label(self, width=10, height=2, text='Usuário:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_usuario.place(x=650, y=160)
        entrada_usuario = Entry(self, width=14, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_usuario.place(x=670, y=190)

        self.entrada_usuario = entrada_usuario

        # Senha:
        label_senha = Label(self, width=10, height=2, text='Senha:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_senha.place(x=650, y=240)
        entrada_senha = Entry(self, width=14, font=(
            "Arial", 25), show="*", bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_senha.place(x=670, y=270)

        self.entrada_senha = entrada_senha

        # botões:
        botao_login = Button(self, text='Entrar', width=23, command=lambda: self.fazer_login(sistema_medico, controller), height=2, font=(
            "Arial", 15), bg='#02bae8', fg='white', relief=RAISED, overrelief=RAISED)
        botao_login.place(x=670, y=330)

        botao_cadastro = Button(self, text='Cadastra-se', width=10, command=lambda: self.fazer_cadastro(sistema_medico, controller), height=1, font=(
            "Arial", 10, "underline"), bg='#242323', fg='#02bae8', relief='solid', overrelief='solid', borderwidth=0, highlightthickness=0)
        botao_cadastro.place(x=845, y=400)

    def fazer_login(self, sistema_medico: SistemaMedico, controller):
        usuario = self.entrada_usuario.get()
        senha = self.entrada_senha.get()

        # Aqui verificamos se os campos foram preenchidos caso não deve mostrar um erro pedindo para preencher os campos
        if len(usuario) != 0:
            # Se ocorrer tudo bem iremos fazer o login
            # print("médico:", usuario)
            # print("senha:", senha)
            sistema_medico.login(
                usuario, senha, transacao_tela=lambda: controller.show_frame(MenuOpcoes))

        else:
            # Aqui exibimos um popup de aviso pedindo para os campos serem preenchidos
            messagebox.showinfo(
                "Aviso!", "Preencha os campos para continuar", icon="warning")

    def fazer_cadastro(self, sistema_medico: SistemaMedico, controller):
        # Função para realizar o cadastro
        controller.show_frame(CadastroMedico)
        print("Cadastro realizado!")
