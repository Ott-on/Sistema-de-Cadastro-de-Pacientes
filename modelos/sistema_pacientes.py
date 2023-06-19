import pandas as pd
import os.path
from modelos.paciente import Paciente


class SistemaPacientes:
    def __init__(self):
        self.arquivo_csv = "dados/pacientes.csv"

        # Verificar se o arquivo existe
        if not os.path.isfile(self.arquivo_csv):
            # Criar o arquivo e adicionar os cabeçalhos das colunas
            df_cabecalho = pd.DataFrame(columns=[
                                        "nome", "cpf", "email", "telefone", "celular", "data_nascimento", "sexo", "estado_civil"])
            df_cabecalho.to_csv(self.arquivo_csv, index=False, sep=';')

    def obter_pacientes(self):
        tabela_pacientes = pd.read_csv(self.arquivo_csv, sep=";")
        pacientes = []

        # adiciona cada linha do arquivo na lista pacientes
        for _, row in tabela_pacientes.iterrows():
            paciente = (
                row['cpf'],
                row['nome'],
                row['email'],
                row['telefone'],
                row['celular'],
                row['data_nascimento'],
                row['sexo'],
                row['estado_civil']
            )
            pacientes.append(paciente)
        return pacientes

    # Metodo para cadastrar paciente
    def cadastrar(self, paciente: Paciente):
        
        # cria um dicionario com todas os dados do paciente
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

        df.to_csv(self.arquivo_csv, index=False,
                  sep=';', mode='a', header=False)

    def remover(self, cpf, nome):
        # Lê o arquivo CSV dos pacientes
        tabela_pacientes = pd.read_csv(self.arquivo_csv, sep=';')

        # Procura as linhas dos pacientes com base no CPF e no nome
        pacientes_procurados = tabela_pacientes.loc[
            (tabela_pacientes['cpf'] == cpf) & (
                tabela_pacientes['nome'] == nome)
        ]

        # Remove as linhas dos pacientes encontrados
        tabela_pacientes = tabela_pacientes.drop(pacientes_procurados.index)

        # Substitui o arquivo antigo pelo arquivo sem os pacientes
        tabela_pacientes.to_csv(self.arquivo_csv, index=False, sep=';')

    def alterar(self, cpf, nome, paciente: Paciente):

        self.remover(cpf, nome)
        self.cadastrar(paciente)

    def consultar(self, buscador):
        # Converter o buscador para string
        buscador = str(buscador)

        # lê o arquivo csv dos pacientes
        tabela_pacientes = pd.read_csv(self.arquivo_csv, sep=";")

        # Verificar se o buscador é um CPF válido
        if buscador.isdigit():
            # Buscar pelo CPF
            pacientes_procurados = tabela_pacientes.loc[tabela_pacientes['cpf'].astype(
                str).str.contains(buscador)]
        else:
            # Buscar pelo nome ou parte do nome
            pacientes_procurados = tabela_pacientes.loc[tabela_pacientes['nome'].astype(
                str).str.contains(buscador, case=False)]

        # Se houver pacientes encontrados, retorna as informações como uma lista de tuplas
        if not pacientes_procurados.empty:
            pacientes_info = []
            for _, paciente in pacientes_procurados.iterrows():
                paciente_info = (
                    paciente['cpf'],
                    paciente['nome'],
                    paciente['email'],
                    paciente['telefone'],
                    paciente['celular'],
                    paciente['data_nascimento'],
                    paciente['sexo'],
                    paciente['estado_civil'],
                )
                pacientes_info.append(paciente_info)

            return pacientes_info

        # Retorna None se não houver pacientes encontrados
        return None
