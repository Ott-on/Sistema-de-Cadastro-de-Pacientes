import pandas as pd
import os.path


class SistemaDoenca:
    def __init__(self):
        self.arquivo_csv = "dados/doencas.csv"

        # Verificar se o arquivo existe
        if not os.path.isfile(self.arquivo_csv):
            # Criar o arquivo e adicionar os cabeçalhos das colunas
            df_cabecalho = pd.DataFrame(columns=["Nome", "CID"])
            df_cabecalho.to_csv(self.arquivo_csv, index=False, sep=';')

    # Metodo para cadastrar doença
    def cadastrar(self, nome, cid):
        dados = {
            "nome": [nome],
            "cid": [cid],
        }

        df = pd.DataFrame(dados)
        df.to_csv("dados/otton.csv", index=False, sep=',', mode='a')

        lido = pd.read_csv("dados/doencas.csv")
        print(lido)

    def remover(self, doenca_selecionada):

        # lê o arquivo csv das doenças
        tabela_doencas = pd.read_csv("dados/doencas.csv")

        # procura a linha da doença no arquivo
        doença_procurada = tabela_doenças .loc[tabela_doenças ['Nome'] == doenca_selecionada | tabela_doenças ['CID'] == doenca_selecionada]

        # retira a linha do arquivo
        tabela_doencas = df.drop(doenca_procurada.index)

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

    def consultar(self, doenca_selecionada):
        # lê o arquivo csv das doenças
        tabela_doencas = pd.read_csv("dados/doencas.csv")

        # procura a linha do paciente no arquivo
        doenca_procurada = tabela_doencas.loc[tabela_doencas['Nome'] ==
                                              doenca_selecionada | tabela_pacientes['CPF'] == doenca_selecionada]

        print(doenca_procurada)
