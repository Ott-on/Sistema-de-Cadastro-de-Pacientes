import datetime
import tkinter as tk
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from tkinter import END, RAISED, RIDGE, Button, Entry, Label, PhotoImage, messagebox
from modelos.atendimento import Atendimento

from modelos.sistema_registro_atendimento import SistemaAtendimento


class RegistrarAtendimento(tk.Frame):
    def __init__(self, parent, controller, *args):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#242323')

        self.paciente_dados = {}

        # Criando uma instancia do sistema atendimento
        sistema_atendimento = SistemaAtendimento()

        if args:
            self.paciente_dados = args[0]["paciente"]

        # retangulo azul da tela
        label_retangulo = Label(self, width=1000, height=4, bg='#02bae8')
        label_retangulo.place(x=0, y=0)

        # Nome do paciente
        label_nome = Label(self, width=15, height=2, text='Nome do paciente:', font=(
            "Arial", 12), bg='#02bae8', fg='#242323')
        label_nome.place(x=100, y=12)

        nome_paciente = self.paciente_dados[1] if self.paciente_dados else "Não setado"
        label_nome_escrito = Label(
            self, width=35, height=2, text=nome_paciente, bg='white')
        label_nome_escrito.place(x=240, y=13)

        # Cpf do paciente
        label_cpf = Label(self, width=5, height=2, text='CPF:', font=(
            "Arial", 12), bg='#02bae8', fg='#242323')
        label_cpf.place(x=505, y=12)

        cpf_paciente = self.paciente_dados[0] if self.paciente_dados else "Não setado"
        label_cpf_escrito = Label(
            self, width=35, height=2, text=cpf_paciente, bg='white')
        label_cpf_escrito.place(x=555, y=13)

        # Peso
        entrada_peso = Entry(self, width=10, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_peso.place(x=160, y=190)
        label_peso = Label(self, width=10, height=2, text='Peso:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_peso.place(x=140, y=150)

        self.entrada_peso = entrada_peso

        # Altura
        entrada_altura = Entry(self, width=10, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_altura.place(x=160, y=340)
        label_altura = Label(self, width=10, height=2, text='Altura:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_altura.place(x=140, y=300)

        self.entrada_altura = entrada_altura

        # Relato do paciente
        entrada_relato_paciente = Entry(self, width=10, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_relato_paciente.place(x=160, y=490)
        label_relato_paciente = Label(self, width=18, height=2, text='Relato do Paciente:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_relato_paciente.place(x=140, y=450)

        self.entrada_relato_paciente = entrada_relato_paciente

        # Anotações do médico
        entrada_anotacoes_medico = Entry(self, width=10, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_anotacoes_medico.place(x=430, y=190)
        label_anotacoes_medico = Label(self, width=18, height=2, text='Anotações do Médico:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_anotacoes_medico.place(x=425, y=150)

        self.entrada_anotacoes_medico = entrada_anotacoes_medico

        # Diagnóstico Médico
        entrada_diagnostico = Entry(self, width=10, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_diagnostico.place(x=430, y=340)
        label_diagnostico = Label(self, width=10, height=2, text='Diagnóstico:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_diagnostico.place(x=425, y=300)

        self.entrada_diagnostico = entrada_diagnostico

        # Codigo CID
        entrada_codigo_cid = Entry(self, width=10, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_codigo_cid.place(x=430, y=490)

        label_codigo_cid = Label(self, width=15, height=2, text='Código CID:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_codigo_cid.place(x=405, y=450)

        self.entrada_codigo_cid = entrada_codigo_cid

        # Tratamento
        entrada_tratamento = Entry(self, width=10, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_tratamento.place(x=680, y=190)
        label_tratamento = Label(self, width=10, height=2, text='Tratamento:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_tratamento.place(x=680, y=150)

        self.entrada_tratamento = entrada_tratamento

        # Exames
        entrada_exames = Entry(self, width=10, font=(
            "Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_exames.place(x=680, y=340)
        label_exames = Label(self, width=10, height=2, text='Tratamento:', font=(
            "Arial", 10), bg='#242323', fg='#888a89')
        label_exames.place(x=680, y=300)

        self.entrada_exames = entrada_exames

        img = PhotoImage(file='imagens/voltar_label.png')
        button_image = Button(self, image=img, bg='#02bae8', fg='#02bae8', activebackground='#02bae8', command=lambda: self.voltar_para_pacientes(
            controller), relief='solid', overrelief='solid', borderwidth=0, highlightthickness=0)
        button_image.image = img
        button_image.place(x=10, y=10)

        # botão Registrar Atendimento
        button_registrar = Button(self, text='Registrar Atendimento', font=("Arial", 16), activebackground='#02bae8', bg='#02bae8', fg='white', command=lambda: self.registrar_atendimento(sistema_atendimento,
                                                                                                                                                                                           controller), relief='solid', overrelief='solid', width=18, height=2, borderwidth=0, highlightthickness=0)
        button_registrar.place(x=680, y=490)

        # botão Consultar
        button_sair = Button(self, text='Consultar', command=lambda: self.consultar_paciente(
            controller), font=("Arial", 20))
        button_sair.place(x=850, y=5)

    def voltar_para_pacientes(self, controller):
        from telas.tela_paciente import Pacientes
        controller.carregar_tela(Pacientes)

    def consultar_paciente(self, controller):
        from telas.consultar_paciente import ConsultarPaciente
        controller.carregar_tela(ConsultarPaciente, {
                                 "paciente": self.paciente_dados, "acessado_pela_tela": "atendimento", })

    def registrar_atendimento(self, sistema_registro_atendimento: SistemaAtendimento, controller):
        data_atendimento = datetime.datetime.now()

        data = data_atendimento.strftime('%d/%m/%Y')
        hora = data_atendimento.strftime('%H:%M:%S')

        cpf_paciente = self.paciente_dados[0]
        peso_paciente = self.entrada_peso.get()
        altura_paciente = self.entrada_altura.get()
        relato_paciente = self.entrada_relato_paciente.get()
        anotacoes_medico = self.entrada_anotacoes_medico.get()
        exames_passados = self.entrada_exames.get()
        diagnostico_medico = self.entrada_diagnostico.get()
        codigo_cid = self.entrada_codigo_cid.get()
        tratamento_ou_medicamentos_prescritos = self.entrada_tratamento.get()

        atendimento = Atendimento(cpf_paciente=cpf_paciente,
                                  data_atendimento=data,
                                  hora_atendimento=hora,
                                  peso_paciente=peso_paciente,
                                  altura_paciente=altura_paciente,
                                  relato_paciente=relato_paciente,
                                  anotacoes_medico=anotacoes_medico,
                                  exames_passados=exames_passados,
                                  diagnostico_medico=diagnostico_medico,
                                  codigo_cid=codigo_cid,
                                  tratamento_ou_medicamentos_prescritos=tratamento_ou_medicamentos_prescritos,)

        sistema_registro_atendimento.registrar(atendimento=atendimento)

        messagebox.showinfo(
            "Sucesso!", "Atendimento registrado com sucesso!")
