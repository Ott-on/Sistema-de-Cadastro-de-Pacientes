import pandas as pd
import os.path


class SistemaDoenca:
    def __init__(self):
        self.arquivo_csv = "dados/doencas.csv"

        # Verificar se o arquivo existe
        if not os.path.isfile(self.arquivo_csv):
            # Criar o arquivo e adicionar os cabeçalhos das colunas
            df_cabecalho = pd.DataFrame(columns=["cid", "nome_doenca"])
            df_cabecalho.to_csv(self.arquivo_csv, index=False, sep=';')

    def obter_doencas(self):
        tabela_doencas = pd.read_csv(self.arquivo_csv, sep=";")
        doencas = []
        for _, row in tabela_doencas.iterrows():
            doenca = (
                row['cid'],
                row['nome'],
            )
            doencas.append(doenca)
        return doencas

    # Metodo para cadastrar doença
    def cadastrar(self, cid, nome_doenca):
        dados = {
            "cid": [cid],
            "nome_doenca": [nome_doenca],
        }

        df = pd.DataFrame(dados)
        df.to_csv("dados/doencas.csv", index=False,
                  sep=';', mode='a', header=False)

        lido = pd.read_csv("dados/doencas.csv")
        print(lido)

    def remover(self, doenca_selecionada):

        # lê o arquivo csv das doenças
        tabela_doencas = pd.read_csv("dados/doencas.csv")

        # procura a linha da doença no arquivo
        doenca_procurada = tabela_doencas.loc[tabela_doencas['Nome'] ==
                                              doenca_selecionada | tabela_doencas['CID'] == doenca_selecionada]

        # retira a linha do arquivo
        tabela_doencas = tabela_doencas.drop(doenca_procurada.index)

        # substitui o arquivo antigo pelo arquivo sem a doença
        tabela_doencas.to_csv('dados/doencas.csv', index=False, sep=';')

    def alterar(self, doenca_selecionada, dado_para_alterar, novo_dado):

        # lê o arquivo csv das doencas
        tabela_doencas = pd.read_csv("dados/doencas.csv")

        # procura a linha da doença no arquivo
        doenca_procurada = tabela_doencas.loc[tabela_doencas['Nome'] ==
                                              doenca_selecionada | tabela_doencas['CID'] == doenca_selecionada]

        # altera o dado especifico da linha
        doenca_procurada.loc[doenca_procurada.index,
                             dado_para_alterar] = novo_dado

        # coloca o novo dado no arquivo principal de doenças
        tabela_doencas.loc[doenca_procurada.index] = doenca_procurada

        # substitui a o arquivo antigo pelo arquivo alterado
        tabela_doencas.to_csv('dados/doencas.csv', index=False, sep=';')

    def consultar(self, buscador):
        # Converter o buscador para string
        buscador = str(buscador)

        # lê o arquivo csv dos doencas
        tabela_doencas = pd.read_csv(self.arquivo_csv, sep=";")

        # Verificar se o buscador é um CPF válido
        if buscador.isalpha():
            # Buscar pelo nome ou parte do nome (ignorando maiúsculas/minúsculas)
            doencas_procuradas = tabela_doencas.loc[tabela_doencas['nome'].astype(
                str).str.contains(buscador, case=False)]
        else:
            # Buscar pelo CID
            doencas_procuradas = tabela_doencas.loc[tabela_doencas['cid'].astype(
                str).str.contains(buscador)]

        # Se houver doencas encontrados, retorna as informações como uma lista de tuplas
        if not doencas_procuradas.empty:
            doencas_info = []
            for _, paciente in doencas_procuradas.iterrows():
                paciente_info = (
                    paciente['cid'],
                    paciente['nome'],
                )
                doencas_info.append(paciente_info)

            return doencas_info

        # Retorna None se não houver doencas encontrados
        return None
