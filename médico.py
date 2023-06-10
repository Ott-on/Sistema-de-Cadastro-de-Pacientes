class SistemaMedico:
    def __init__(self):
        self.medicos = []
        self.junta_senhas = []

    def CadastroMédico(self):
        medico = []

        medico.append(input("Nome: "))
        medico.append(input("Email: "))
        medico.append(input("Senha: "))
        medico.append(input("CPF: "))
        medico.append(input("Celular do Médico: "))
        medico.append(input("Telefone do Médico: "))
        medico.append(input("Data de Nascimento: "))
        medico.append(input("Especialidade: "))
        medico.append(input("Sexo: "))
        medico.append(input("CRM: "))
        medico.append(input("UF: "))
        medico.append(input("CEP: "))

        CRM = medico[9]
        UF = medico[10]
        CEP = medico[11]
        
        while len(CRM) > 6:
            CRM = input("Número maior que 6 dígitos: ")
        
        while len(CRM) < 6:
            CRM = input("Número menor que 6 dígitos: ")
        
        while not CRM.isdigit():
            CRM = input("Não digitou números: ")
        
        while len(UF) > 2:
            UF = input("Número maior que 2 dígitos: ")
        
        while len(UF) < 2:
            UF = input("Número menor que 2 dígitos: ")

        while not UF.isalpha():
            UF = input("Não digitou palavras: ")

        while len(CEP) > 8:
            CEP = input("Número maior que 8 dígitos: ")
        
        while len(CEP) < 8:
            CEP = input("Número menor que 8 dígitos: ")
        
        while not CEP.isdigit():
            CEP = input("Não é dígito: ")
        
        # Fim das delimitações
        self.medicos.append(medico)
        self.junta_senhas.append([medico[3], medico[2]])  # [cpf, senha]

    def LoginMédico(self):
        cpflogin = input("Seu CPF: ")
        senhalogin = input("Sua senha: ")

        while [cpflogin, senhalogin] not in self.junta_senhas:
            print("Seu CPF ou senha estão incorretos.")
            cpflogin = input("Seu CPF: ")
            senhalogin = input("Sua senha: ")
