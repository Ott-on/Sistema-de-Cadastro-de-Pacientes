import tkinter as tk
from tkcalendar import DateEntry
from tkinter import END, RAISED, RIDGE, Button, Entry, Label, PhotoImage, messagebox
from modelos.paciente import *
from tkinter import ttk


class cadastrarPacientes(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#242323')

        # retangulo azul da tela
        label_retangulo = Label(self, width=1000, height=4, bg='#02bae8')
        label_retangulo.place(x=0, y=0)

        # Nome
        entrada_nome = Entry(self, width=10, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_nome.place(x=160, y=190)
        label_nome = Label(self, width=10, height=2, text='Nome:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_nome.place(x=145, y=150)

        self.entrada_nome = entrada_nome

        # CPF
        entrada_cpf = Entry(self, width=10, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_cpf.place(x=160, y=340)
        label_cpf = Label(self, width=10, height=2, text='CPF:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_cpf.place(x=140, y=300)

        self.entrada_cpf = entrada_cpf

        # Email
        entrada_email = Entry(self, width=10, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_email.place(x=160, y=490)
        label_cpf = Label(self, width=10, height=2, text='Email:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_cpf.place(x=140, y=450)

        self.entrada_email = entrada_email

        # Celular
        entrada_celular = Entry(self, width=10, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_celular.place(x=430, y=190)
        label_celular = Label(self, width=10, height=2, text='Celular:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_celular.place(x=420, y=150)

        self.entrada_celular = entrada_celular

        # Telefone
        entrada_telefone = Entry(self, width=10, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_telefone.place(x=430, y=340)
        label_telefone = Label(self, width=10, height=2, text='Telefone:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_telefone.place(x=420, y=300)

        self.entrada_telefone = entrada_telefone

        # Data de Nascimento
        entrada_nascimento = DateEntry(self, width=12, background='#02bae8',
                                       foreground='white', borderwidth=2, locale='pt_BR')
        entrada_nascimento.place(x=430, y=500)
        label_nascimento = Label(self, width=15, height=2, text='Data de Nascimento:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_nascimento.place(x=420, y=450)

        self.entrada_nascimento = entrada_nascimento

        # Sexo
        entrada_sexo = ttk.Combobox(
            self, values=['Masculino', 'Feminino', 'Prefiro não dizer'])
        entrada_sexo.place(x=700, y=190)
        entrada_sexo.current(0)
        label_sexo = Label(self, width=10, height=2, text='Sexo:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_sexo.place(x=680, y=150)

        self.entrada_sexo = entrada_sexo

        # Estado Civil
        entrada_civil = ttk.Combobox(
            self, values=['Solteiro', 'Casado', 'Divorciado', 'Viúvo'])
        entrada_civil.place(x=700, y=340)
        entrada_civil.current(0)
        label_civil = Label(self, width=10, height=2, text='Estado Civil:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_civil.place(x=700, y=300)

        self.entrada_civil = entrada_civil

        img = PhotoImage(file='imagens/voltar_label.png')
        button_image = Button(self, image=img, bg='#02bae8', fg='#02bae8', activebackground='#02bae8', command=lambda: self.voltar_menu(
            controller), relief='solid', overrelief='solid', borderwidth=0, highlightthickness=0)
        button_image.image = img
        button_image.place(x=10, y=10)

        # botão confirmar cadastro
        button_cadastrar = Button(self, text='Confirmar', font=("Arial", 16), activebackground='#02bae8', bg='#02bae8', fg='white', command=lambda: self.fazer_cadastro(
            controller), relief='solid', overrelief='solid', width=10, height=2, borderwidth=0, highlightthickness=0)

        button_cadastrar.place(x=700, y=450)

    def voltar_menu(self, controller):
        from telas.menu_opcoes import MenuOpcoes
        controller.show_frame(MenuOpcoes)

    # Metodo para limpar os campos
    def limpar_campos(self):
        self.entrada_nome.delete(0, END)
        self.entrada_nome.delete(0, END)
        self.entrada_cpf.delete(0, END)
        self.entrada_email.delete(0, END)
        self.entrada_telefone.delete(0, END)
        self.entrada_celular.delete(0, END)
        self.entrada_sexo.delete(0, END)
        self.entrada_civil.delete(0, END)

    def fazer_cadastro(self, controller):
        from modelos.sistema_pacientes import SistemaPacientes
        from modelos.paciente import Paciente

        nome = self.entrada_nome.get()
        cpf = self.entrada_cpf.get()
        email = self.entrada_email.get()
        telefone = self.entrada_telefone.get()
        celular = self.entrada_celular.get()
        nascimento = str(self.entrada_nascimento.get_date()).split("-")
        sexo = self.entrada_sexo.get()
        civil = self.entrada_civil.get()

        # formatando a data de nascimento para o formato dd/mm/aaaa
        nascimento_formatado = f"{nascimento[2]}/{nascimento[1]}/{nascimento[0]}"

        # fazendo validação dos campos
        if nome and cpf and email and telefone and celular and nascimento and sexo and civil:
            if len(cpf) == 11:
                if "@" in email:
                    if len(telefone) == 11:
                        if len(telefone) == 11:
                            print('Tudo ok!')
                            Paciente = Paciente(nome, cpf, email, telefone,
                                                celular, nascimento_formatado, sexo, civil)
                            SistemaPacientes.cadastrar(self, Paciente)
                            # self.limpar_campos()
                        else:
                            messagebox.showinfo(
                                "Aviso!", "Informe um telefone valido ex: DD912345678", icon="warning")
                    else:
                        messagebox.showinfo(
                            "Aviso!", "Informe um telefone valido ex: DD912345678", icon="warning")
                else:
                    messagebox.showinfo(
                        "Aviso!", "Informe um endereço de email válido", icon="warning")
            else:
                messagebox.showinfo(
                    "Aviso!", "Informe um cpf válido!", icon="warning")
        else:
            messagebox.showinfo(
                "Aviso!", "Preencha todos os campos para continuar", icon="warning")
