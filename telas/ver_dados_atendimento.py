import tkinter as tk
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from tkinter import END, RAISED, RIDGE, Button, Entry, Label, PhotoImage, messagebox

class VerAtendimento(tk.Frame):
    def __init__(self, parent, controller, *args):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#242323')

        # retangulo azul da tela
        label_retangulo = Label(self, width=1000, height=4, bg='#02bae8')
        label_retangulo.place(x=0, y=0) 

        # Nome do paciente
        label_nome = Label(self, width=15, height=2, text='Nome do paciente:', font=(
            "Arial", 12), bg='#02bae8', fg='#242323')
        label_nome.place(x=100, y=12)

        label_nome_escrito = Label(self, width=35, height=2, text='', bg='white')
        label_nome_escrito.place(x=240, y=13)

        # Cpf do paciente
        label_cpf = Label(self, width=5, height=2, text='CPF:', font=(
            "Arial", 12), bg='#02bae8', fg='#242323')
        label_cpf.place(x=505, y=12)

        label_cpf_escrito = Label(self, width=35, height=2, text='', bg='white')
        label_cpf_escrito.place(x=555, y=13)


        # Peso
        label_peso1 = Label(self, width=10, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        label_peso1.place(x=160, y=190)
        label_peso2 = Label(self, width=10, height=2, text='Peso:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_peso2.place(x=140, y=150)

        self.label_peso1 = label_peso1

        # Altura
        label_altura1 = Label(self, width=10, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        label_altura1.place(x=160, y=340)
        label_altura2 = Label(self, width=10, height=2, text='Altura:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_altura2.place(x=140, y=300)

        self.label_altura1 = label_altura1

        # Relato do paciente
        label_relato_paciente1 = Label(self, width=10, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        label_relato_paciente1.place(x=160, y=490)
        label_relato_paciente2 = Label(self, width=18, height=2, text='Relato do Paciente:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_relato_paciente2.place(x=140, y=450)

        self.label_relato_paciente1 = label_relato_paciente1
        
        # Anotações do médico
        label_anotacoes_medico1 = Label(self, width=10, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        label_anotacoes_medico1.place(x=430, y=190)
        label_anotacoes_medico2 = Label(self, width=18, height=2, text='Anotações do Médico:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_anotacoes_medico2.place(x=425, y=150)

        self.label_anotacoes_medico1 = label_anotacoes_medico1

        # Diagnóstico Médico
        label_diagnostico1 = Label(self, width=10, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        label_diagnostico1.place(x=430, y=340)
        label_diagnostico2 = Label(self, width=10, height=2, text='Diagnóstico:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_diagnostico2.place(x=425, y=300)

        self.label_diagnostico1 = label_diagnostico1

        # Codigo CID
        label_codigo_cid1 = Label(self, width=10, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        label_codigo_cid1.place(x=430, y=490)
        
        label_codigo_cid = Label(self, width=15, height=2, text='Código CID:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_codigo_cid.place(x=405, y=450)

        self.label_codigo_cid1= label_codigo_cid1

        # Tratamento
        label_tratamento1 = Label(self, width=10, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        label_tratamento1.place(x=680, y=190)
        label_tratamento2 = Label(self, width=10, height=2, text='Tratamento:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_tratamento2.place(x=680, y=150)

        self.label_tratamento1 = label_tratamento1

        img = PhotoImage(file='imagens/voltar_label.png')
        button_image = Button(self, image=img, bg='#02bae8', fg='#02bae8', activebackground='#02bae8', command=lambda: self.voltar_para_pacientes(
            controller), relief='solid', overrelief='solid', borderwidth=0, highlightthickness=0)
        button_image.image = img
        button_image.place(x=10, y=10)
        
        # botão Registrar Atendimento
        button_registrar = Button(self, text='Registrar Atendimento', font=("Arial", 16), activebackground='#02bae8', bg='#02bae8', fg='white', command=lambda: self.registrar_atendimento(
        controller), relief='solid', overrelief='solid', width=18, height=2, borderwidth=0, highlightthickness=0)
        button_registrar.place(x=680, y=335)

        # botão Consultar
        button_sair = Button(self, text='Consultar', font=("Arial", 20))
        button_sair.place(x=850, y=5)

    def voltar_para_pacientes(self, controller):
        from telas.tela_paciente import Pacientes
        controller.show_frame(Pacientes)

    def registrar_atendimento(self, controller):
        pass