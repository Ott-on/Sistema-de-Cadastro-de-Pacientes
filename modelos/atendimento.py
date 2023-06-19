class Atendimento:
    def __init__(self, cpf_paciente, data_atendimento, hora_atendimento, peso_paciente, altura_paciente, relato_paciente, anotacoes_medico, exames_passados, diagnostico_medico, codigo_cid, tratamento_ou_medicamentos_prescritos, nome_paciente):
        self.cpf_paciente = cpf_paciente
        self.data_atendimento = data_atendimento
        self.hora_atendimento = hora_atendimento
        self.peso_paciente = peso_paciente
        self.altura_paciente = altura_paciente
        self.relato_paciente = relato_paciente
        self.anotacoes_medico = anotacoes_medico
        self.exames_passados = exames_passados
        self.diagnostico_medico = diagnostico_medico
        self.codigo_cid = codigo_cid
        self.tratamento_ou_medicamentos_prescritos = tratamento_ou_medicamentos_prescritos
        self.nome_paciente = nome_paciente
