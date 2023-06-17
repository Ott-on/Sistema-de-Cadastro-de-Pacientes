import pandas as pd
import os.path
from modelos.paciente import Paciente


class SistemaPacientes:
    def __init__(self):
        self.arquivo_csv = "dados/pacientes.csv"

        # Verificar se o arquivo existe
        if not os.path.isfile(self.arquivo_csv):
            print('não existe')
            # Criar o arquivo e adicionar os cabeçalhos das colunas
            df_cabecalho = pd.DataFrame(columns=[
                                        "Nome", "CPF", "Email", "Telefone", "Celular", "Data de Nascimento", "Sexo", "Estado Civil"])
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

        df.to_csv("dados/pacientes.csv", index=False, sep=';', mode='a')

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

    def alterar(self, paciente_selecionado, dado_para_alterar, novo_dado):

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

    def consultar(self, paciente_selecionado):
        # lê o arquivo csv dos pacientes
        tabela_pacientes = pd.read_csv("dados/pacientes.csv", sep=";")
        # procura a linha do paciente no arquivo

        # Se paciente_procurado não estiver vazio, retorna as informações como um dicionário
        if not paciente_procurado.empty:
            paciente_info = {
                'nome': paciente_procurado['nome'].values[0],
                'cpf': paciente_procurado['cpf'].values[0],
                'email': paciente_procurado['email'].values[0],
                'telefone': paciente_procurado['telefone'].values[0],
                'celular': paciente_procurado['celular'].values[0],
                'data_nascimento': paciente_procurado['data_nascimento'].values[0],
                'sexo': paciente_procurado['sexo'].values[0],
                'estado_civil': paciente_procurado['estado_civil'].values[0],
            }
            return paciente_info

        # retorna None se estiver vazio
        return None
