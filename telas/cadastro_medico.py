#class SistemaMedico:
    #def __init__(self):
        #self.medicos = []          # Lista de médicos cadastrados
        #self.junta_senhas = []     # Lista de pares CPF-Senha para verificação de login

    #def CadastroMédico(self):
        # Comentários explicando o que cada linha faz
        # medico = []

        # medico.append(input("Nome: "))
        # medico.append(input("Email: "))
        # medico.append(input("Senha: "))
        # medico.append(input("CPF: "))
        # medico.append(input("Celular do Médico: "))
        # medico.append(input("Telefone do Médico: "))
        # medico.append(input("Data de Nascimento: "))
        # medico.append(input("Especialidade: "))
        # medico.append(input("Sexo: "))
        # medico.append(input("CRM: "))
        # medico.append(input("UF: "))
        # medico.append(input("CEP: "))

        # CRM = medico[9]
        # UF = medico[10]
        # CEP = medico[11]

        # while len(CRM) > 6:
        #     CRM = input("Número maior que 6 dígitos: ")
        #
        # while len(CRM) < 6:
        #     CRM = input("Número menor que 6 dígitos: ")
        #
        # while not CRM.isdigit():
        #     CRM = input("Não digitou números: ")
        #
        # while len(UF) > 2:
        #     UF = input("Número maior que 2 dígitos: ")
        #
        # while len(UF) < 2:
        #     UF = input("Número menor que 2 dígitos: ")
        #
        # while not UF.isalpha():
        #     UF = input("Não digitou palavras: ")
        #
        # while len(CEP) > 8:
        #     CEP = input("Número maior que 8 dígitos: ")
        #
        # while len(CEP) < 8:
        #     CEP = input("Número menor que 8 dígitos: ")
        #
        # while not CEP.isdigit():
        #     CEP = input("Não é dígito: ")
        
        # Fim das delimitações
        # self.medicos.append(medico)
        # self.junta_senhas.append([medico[3], medico[2]])  # [cpf, senha]

    #def LoginMédico(self):
        # Comentários explicando o que cada linha faz
        # cpflogin = input("Seu CPF: ")
        # senhalogin = input("Sua senha: ")

        # while [cpflogin, senhalogin] not in self.junta_senhas:
        #     print("Seu CPF ou senha estão incorretos.")
        #     cpflogin = input("Seu CPF: ")
        #     senhalogin = input("Sua senha: ")

import tkinter as tk
from tkinter import RAISED, RIDGE, Button, Entry, Label, PhotoImage, messagebox


class CadastroMedico(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#02bae8')

        # Usuário:
        label_usuario = Label(self, width=10, height=2, text='', font=(
            "Arial", 10), bg='white', fg='#888a89')
        label_usuario.place(x=650, y=50)
        entrada_usuario = Entry(self, width=14, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_usuario.place(x=670, y=190)

        self.entrada_usuario = entrada_usuario

        # Senha:
        label_senha = Label(self, width=10, height=2, text='Senha:', font=(
            "Arial", 10), bg='white', fg='#888a89')
        label_senha.place(x=650, y=240)
        entrada_senha = Entry(self, width=14, font=(
            "Arial", 25), show="*", bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_senha.place(x=670, y=270)

        self.entrada_senha = entrada_senha

    def fazer_login(self):
        usuario = self.entrada_usuario.get()
        senha = self.entrada_senha.get()

        # Aqui verificamos se os campos foram preenchidos caso não deve mostrar um erro pedindo para preencher os campos
        if len(usuario) != 0:
            # Se ocorrer tudo bem iremos fazer o login
            print(f"usuário:", usuario)
            print(f"senha:", senha)
        else:
            # Aqui exibimos um popup de aviso pedindo para os campos serem preenchidos
            messagebox.showinfo(
                "Aviso!", "Preencha os campos para continuar", icon="warning")



