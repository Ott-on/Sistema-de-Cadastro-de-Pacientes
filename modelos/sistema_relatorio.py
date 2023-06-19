import pandas as pd


class SistemaRelatorios:
    def __init__(self):
        self.arquivo_csv_pacientes = "dados/pacientes.csv"
        self.registros_atendimentos = "dados/registros_atendimentos.csv"

    def obter_todos_atendimentos(self):
        """
        Obtém todos os registros de atendimentos do arquivo CSV.
        Retorna uma lista com os registros de atendimento.
        """
        tabela_pacientes = pd.read_csv(self.registros_atendimentos, sep=";")
        atendimentos = []
        for _, row in tabela_pacientes.iterrows():
            paciente = (
                row["cpf_paciente"],
                row["data_atendimento"],
                row["codigo_cid"],
                row["nome_paciente"],
            )
            atendimentos.append(paciente)
        return atendimentos

    def listar_atendimentos_pelo_codigo_cid(self, codigo_cid):
        """
        Lista os atendimentos correspondentes ao código CID fornecido.
        Retorna uma lista com os registros de atendimento.
        """
        codigo_cid = str(codigo_cid)

        tabela_atendimentos = pd.read_csv(self.registros_atendimentos, sep=";")

        atendimentos_procurados = tabela_atendimentos.loc[tabela_atendimentos['codigo_cid'].astype(
            str).str.contains(codigo_cid)]

        if not atendimentos_procurados.empty:
            registros_atendimentos_info = []
            for _, registro in atendimentos_procurados.iterrows():
                registro_atendimento_info = (
                    registro["cpf_paciente"],
                    registro["data_atendimento"],
                    registro["codigo_cid"],
                    registro["nome_paciente"],
                )
                registros_atendimentos_info.append(registro_atendimento_info)

            return registros_atendimentos_info

        # Retorna None se não houver registros encontrados
        return None

    def listar_atendimentos_pelo_nome_ou_cpf(self, nome_ou_cpf):
        """
        Lista os atendimentos correspondentes ao nome ou CPF fornecido.
        Retorna uma lista com os registros de atendimento.
        """
        nome_ou_cpf = str(nome_ou_cpf)

        tabela_atendimentos = pd.read_csv(self.registros_atendimentos, sep=";")

        procurado_pelo_nome = tabela_atendimentos.loc[tabela_atendimentos['nome_paciente'].astype(
            str).str.contains(nome_ou_cpf, case=False)]

        procurado_pelo_cpf = tabela_atendimentos.loc[tabela_atendimentos['cpf_paciente'].astype(
            str).str.contains(nome_ou_cpf)]

        if not procurado_pelo_nome.empty:
            atendimentos_procurados = procurado_pelo_nome
        else:
            atendimentos_procurados = procurado_pelo_cpf

        if not atendimentos_procurados.empty:
            registros_atendimentos_info = []
            for _, registro in atendimentos_procurados.iterrows():
                registro_atendimento_info = (
                    registro["cpf_paciente"],
                    registro["data_atendimento"],
                    registro["codigo_cid"],
                    registro["nome_paciente"],
                )
                registros_atendimentos_info.append(registro_atendimento_info)

            return registros_atendimentos_info

        # Retorna None se não houver registros encontrados
        return None

    def listar_atendimentos_pelo_calendario(self, dia_mes_ano):
        """
        Retorna uma lista com os registros de atendimento correspondentes à data fornecida.
        Retorna uma lista com os registros de atendimento.
        """
        dia_mes_ano = str(dia_mes_ano)

        tabela_atendimentos = pd.read_csv(self.registros_atendimentos, sep=";")

        atendimentos_procurados = tabela_atendimentos.loc[tabela_atendimentos['data_atendimento'].astype(
            str).str.contains(dia_mes_ano)]

        # CPF | Data de Atendimento | codigo CID | Nome

        if not atendimentos_procurados.empty:
            registros_atendimentos_info = []
            for _, registro in atendimentos_procurados.iterrows():
                registro_atendimento_info = (
                    registro["cpf_paciente"],
                    registro["data_atendimento"],
                    registro["codigo_cid"],
                    registro["nome_paciente"],
                )
                registros_atendimentos_info.append(registro_atendimento_info)

            return registros_atendimentos_info

        # Retorna None se não houver registros encontrados
        return None
