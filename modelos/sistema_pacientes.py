import pandas as pd
import os.path

rom paciente import *f

from modelos.paciente import Paciente


class SistemaPacientes:
    def __init__(self):
        self.arquivo_csv = "dados/pacientes.csv"

        # Verificar se o arquivo existe
        if not os.path.isfile(self.arquivo_csv):
            # Criar o arquivo e adicionar os cabeçalhos das colunas
            df_cabecalho = pd.DataFrame(columns=["Nome", "CPF", "Email", "Telefone", "Celular", "Data de Nascimento", "Sexo", "Estado Civil"])
            df_cabecalho.to_csv(self.arquivo_csv, index=False, sep=';')

    # Metodo para cadastrar paciente
    def cadastrar(self, paciente: Paciente):
        dados = {
            "nome": [paciente.nome],
            "cpf": [paciente.cpf],
            "email": [paciente.email], 
            "telefone": [paciente.telefone], 
            "celular": [paciente.celular], 
            "data_nascimento": [paciente.data_nascimento], 
            "sexo": [paciente.sexo], 
            "estado_civil": [paciente.estado_civil],
        }

        df = pd.DataFrame(dados)
        df.to_csv("dados/pacientes.csv", index=False, sep=',', mode='a')

        lido = pd.read_csv("dados/pacientes.csv")
        print(lido)


    def remover(self, paciente_selecionado):

        # lê o arquivo csv dos pacientes
        tabela_pacientes = pd.read_csv("dados/pacientes.csv")

        # procura a linha do paciente no arquivo
        paciente_procurado = tabela_pacientes.loc[tabela_pacientes['Nome'] == paciente_selecionado | tabela_pacientes['CPF'] == paciente_selecionado]

        # retira a linha do arquivo
        tabela_pacientes = df.drop(paciente_procurado.index)

        # substitui o arquivo antigo pelo arquivo sem o paciente
        tabela_pacientes.to_csv('dados/pacientes.csv', index=False, sep=';')


    def alterar_cadastro(self, paciente_selecionado, dado_para_alterar, novo_dado):

        # lê o arquivo csv dos pacientes
        tabela_pacientes = pd.read_csv("dados/pacientes.csv")

        # procura a linha do paciente no arquivo
        paciente_procurado = tabela_pacientes.loc[tabela_pacientes['Nome'] == paciente_selecionado | tabela_pacientes['CPF'] == paciente_selecionado]

        # altera o dado especifico da linha
        paciente_procurado.loc[paciente_procurado.index, dado_para_alterar] = novo_dado

        # coloca o novo dado no arquivo principal de pacientes
        tabela_pacientes.loc[paciente_procurado.index] = paciente_procurado

        # substitui a o arquivo antigo pelo arquivo alterado
        tabela_pacientes.to_csv('dados/pacientes.csv', index=False, sep=';')


    def consultar_paciente(self, paciente_selecionado):
        # lê o arquivo csv dos pacientes
        tabela_pacientes = pd.read_csv("dados/pacientes.csv")

        # procura a linha do paciente no arquivo
        paciente_procurado = tabela_pacientes.loc[tabela_pacientes['Nome'] == paciente_selecionado | tabela_pacientes['CPF'] == paciente_selecionado]

        print(paciente_procurado)
