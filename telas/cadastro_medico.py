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
        self.configure(bg='white')

        #escritos e imagens:
        img2 = PhotoImage(file='imagens/tela_cadastro_medico.png')
        label_image = Label(self, image=img2, relief='solid',borderwidth=0,highlightthickness=0)
        label_image.image = img2 
        label_image.place(x=0, y=90)

        label_retangulo = Label(self, width=1000, height=5, bg='#02bae8')
        label_retangulo.place(x=0, y=0) 

        label_retangulocinza = Label(
            self, width=45, height=30, background='#242323', relief=RAISED)
        label_retangulocinza.place(x=638, y=110)

        label_cadastrar =Label(self, width=15, height=2, text='CADASTRE-SE', font=(
            "Arial", 25), bg='#242323', fg='#02bae8')
        label_cadastrar.place(x=650, y=130) 

        label_usuario = Label(self, width=10, height=2, text='Usuário:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_usuario.place(x=640, y=310) 
        
        label_crm = Label(self, width=10, height=2, text='CRM:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_crm.place(x=640, y=210)

        label_senha = Label(self, width=10, height=2, text='Senha:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_senha.place(x=640, y=410)

        #botão voltar
        img = PhotoImage(file='imagens/voltar_label.png')
        button_image = Button(self, image=img, bg='#02bae8', fg='#02bae8', command=lambda: self.voltar_login(controller), relief='solid', overrelief='solid',borderwidth=0, highlightthickness=0)
        button_image.image = img
        button_image.place(x=10, y=20)  

        #Entradas:
        entrada_usuario2 = Entry(self,width=14, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_usuario2.place(x=660, y=350)

        self.entrada_usuario2 = entrada_usuario2
        
        entrada_crm2 = Entry(self,width=14, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_crm2.place(x=660, y=250)

        self.entrada_crm2 = entrada_crm2

        entrada_senha2 = Entry(self,width=14, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_senha2.place(x=660, y=450)

        self.entrada_senha2 = entrada_senha2

    def voltar_login(self, controller):
        usuario = self.entrada_usuario2.get()
        crm = self.entrada_crm2.get()
        senha = self.entrada_senha2.get()

        controller.show_frame(LoginMedico)



