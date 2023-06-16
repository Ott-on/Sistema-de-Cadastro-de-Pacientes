import pandas as pd
import os.path
from modelos.paciente import Paciente


class SistemaPacientes:
    def __init__(self):
        print('Chamandoooooo')
        self.arquivo_csv = "dados/pacientes.csv"

        # Verificar se o arquivo existe
        if not os.path.isfile(self.arquivo_csv):
            print('nâo existe')
            # Criar o arquivo e adicionar os cabeçalhos das colunas
            df_cabecalho = pd.DataFrame(columns=[
                                        "Nome", "CPF", "Email", "Telefone", "Celular", "Data_nascimento", "Sexo", "Estado_civil"])
            df_cabecalho.to_csv(self.arquivo_csv, index=False, sep=';')

    # Metodo para cadastrar paciente
    def cadastrar(self, paciente: Paciente):
        dados = {
            "Nome": [paciente.nome],
            "Cpf": [paciente.cpf],
            "Email": [paciente.email],
            "Telefone": [paciente.telefone],
            "Celular": [paciente.celular],
            "Data_nascimento": [paciente.data_nascimento],
            "Sexo": [paciente.sexo],
            "Estado_civil": [paciente.estado_civil],
        }

        df = pd.DataFrame(dados)

        df.to_csv("dados/pacientes.csv", index=False,
                  sep=';', mode='a', header=False)

        lido = pd.read_csv("dados/pacientes.csv")
        print(lido)

    def remover(self, paciente_selecionado):

        # lê o arquivo csv dos pacientes
        tabela_pacientes = pd.read_csv("dados/pacientes.csv")

        # procura a linha do paciente no arquivo
        paciente_procurado = tabela_pacientes.loc[tabela_pacientes['Nome'] ==
                                                  paciente_selecionado | tabela_pacientes['CPF'] == paciente_selecionado]

        # retira a linha do arquivo
        tabela_pacientes = tabela_pacientes.drop(paciente_procurado.index)

        # substitui o arquivo antigo pelo arquivo sem o paciente
        tabela_pacientes.to_csv('dados/pacientes.csv', index=False, sep=';')

    def alterar_cadastro(self, paciente_selecionado, dado_para_alterar, novo_dado):

        # lê o arquivo csv dos pacientes
        tabela_pacientes = pd.read_csv("dados/pacientes.csv")

        # procura a linha do paciente no arquivo
        paciente_procurado = tabela_pacientes.loc[tabela_pacientes['Nome'] ==
                                                  paciente_selecionado | tabela_pacientes['CPF'] == paciente_selecionado]

        # altera o dado especifico da linha
        paciente_procurado.loc[paciente_procurado.index,
                               dado_para_alterar] = novo_dado

        # coloca o novo dado no arquivo principal de pacientes
        tabela_pacientes.loc[paciente_procurado.index] = paciente_procurado

        # substitui a o arquivo antigo pelo arquivo alterado
        tabela_pacientes.to_csv('dados/pacientes.csv', index=False, sep=';')

    def consultar_paciente(self, paciente_selecionado):
        # lê o arquivo csv dos pacientes
        tabela_pacientes = pd.read_csv("dados/pacientes.csv", sep=";")

        # procura a linha do paciente no arquivo
        paciente_procurado = tabela_pacientes.loc[(tabela_pacientes['nome'] == paciente_selecionado) | (
            tabela_pacientes['cpf'] == paciente_selecionado)]

        # retona as informações como string
        print(paciente_procurado)
