import pandas

#  listas  com os dados dos pacientes

informacoes_pacientes = []

informacoes_doencas = []

informacoes_registros = []
informacoes_datas_atendimentos = []

informacoes_relatorios = []

# Classe para cadastro de pacientes

class CadastroPaciente():
  def __init__(self):

    pass


  #função cadastrar paciente

  def cadastrar_paciente(self):
    global informacoes_pacientes
    
    cadastro_paciente = []

    cadastro_paciente.append(input('\nNome do paciente: '))
    cadastro_paciente.append(input('CPF do paciente: '))
    cadastro_paciente.append(input('Email do paciente: '))
    cadastro_paciente.append(input('Telefone do paciente: '))
    cadastro_paciente.append(input('Celular do paciente: '))
    cadastro_paciente.append(input('Data de Nascimento do paciente: '))
    cadastro_paciente.append(input('Sexo do paciente: '))
    cadastro_paciente.append(input('Estado Civil do paciente: '))

    informacoes_pacientes.append(cadastro_paciente)


  # função remover paciente

  def remover_cadastro(self):
    global informacoes_pacientes

    paciente = 0

    remover = input('digite o CPF do paciente: ')

    for i in informacoes_pacientes:
      if i[1] == remover:
        informacoes_pacientes.pop(paciente)
        
      paciente += 1


  # função alterar cadatro

  def alterar_cadastro(self):
    global informacoes_pacientes

    alterar = input('digite o cpf do paciente que deseja alterar informações: ')
    
    paciente = 0
    
    for i in informacoes_pacientes:
      if i[1] == alterar:
        o_que = int(input('o que você deseja alterar: nome (1), cpf (2), Email(3), Telefone(4), Celular(5), Data de nascimento(6), Sexo do paciente(7), Estado Civil(8): '))
        informacoes_pacientes[paciente][o_que - 1] = input('Digite o novo dado: ')
      paciente += 1

        
  # função consultar informações de pacientes

  def consultar_cadastro(self):
    global informacoes_pacientes

    pedaco_nome = ''
    nome_em_lista = []

    nome_exato = False

    pedaco_consulta = ''
    consulta_em_lista = []

    cadastrado = False

    consulta = input('Digite o cpf, nome ou parte do nome do paciente que deseja consultar informações: ')

    for i in informacoes_pacientes:

      if i[1] == consulta or i[0] == consulta:
        print(i)
        cadastrado = True
        nome_exato = True
        
      
    if nome_exato == False:


      # separar o nome digitado em partes

      for x in consulta:
        if x != ' ':
          pedaco_consulta += x
                  
        else:
          consulta_em_lista.append(pedaco_consulta)
          pedaco_consulta = ''
                  
      consulta_em_lista.append(pedaco_consulta)
      pedaco_consulta = ''


      # separar nome de determinado paciente em partes

      for o in informacoes_pacientes:

        for j in o[0]:

          if j != ' ':
            pedaco_nome += j

          else:
            nome_em_lista.append(pedaco_nome)
            pedaco_nome = ''
        
        nome_em_lista.append(pedaco_nome)
        pedaco_nome = ''


        # conferir se alguma das partes do nome digitado é igual a alguma parte do nome do determinado paciente

        igual = 0

        for f in consulta_em_lista:
          for p in nome_em_lista:

            if f == p:

              igual += 1
              pass

            if len(consulta_em_lista) == igual:
              print(o)
              cadastrado = True
              break
        nome_em_lista = []

    if cadastrado == False:
      print('\nEste paciente ainda não foi cadastrado, cadastre-o: ')
      funcionalidade_1.cadastrar_paciente()



    

# Classe para cadastro de doenças

class CadastroDoenca():
  def __init__(self):

    pass
  
  # função  cadastrar doenças

  
  def cadastrar_doenca(self):
    global informacoes_doencas

    cadastro_doenca = []

    cadastro_doenca.append(input('Digite o código da doença: '))
    cadastro_doenca.append(input('Digite o nome da doenca: '))

    informacoes_doencas.append(cadastro_doenca)
  
  
  # função remover cadastro de doenças

  def remover_cadastro(self):
    global informacoes_doencas

    doenca = 0

    remover = input('digite o código da doença que deseja remover: ')

    for i in informacoes_doencas:
      if i[0] == remover:
        informacoes_doencas.pop(doenca)
        
      doenca += 1


  # função alterar dados de uma doença

  def alterar_doenca(self):
    global informacoes_doencas

    alterar = input('digite o código da doença que deseja alterar informações: ')
    
    doenca = 0
    
    for i in informacoes_doencas:
      if i[0] == alterar:
        o_que = int(input('o que você deseja alterar: código (1), nome (2): '))
        informacoes_doencas[doenca][o_que - 1] = input('Digite o novo dado: ')
    doenca += 1


  # funcao consultar informações de doenças

  def consultar_doencas(self):
    global informacoes_doencas

    pedaco_nome = ''
    nome_em_lista = []

    nome_exato = False

    pedaco_consulta = ''
    consulta_em_lista = []

    consulta = input('Digite o código,nome ou parte do nome da doença que deseja consultar informações: ')

    for i in informacoes_doencas:
      if i[0] == consulta or i[1] == consulta:
        print(i)
        nome_exato = True
        
      
    if nome_exato == False:


      # separar o nome digitado em partes

      for x in consulta:
        if x != ' ':
          pedaco_consulta += x
                  
        else:
          consulta_em_lista.append(pedaco_consulta)
          pedaco_consulta = ''
                  
      consulta_em_lista.append(pedaco_consulta)
      pedaco_consulta = ''


      # separar nome de determinado paciente em partes

      for o in informacoes_doencas:

        for j in o[1]:

          if j != ' ':
            pedaco_nome += j

          else:
            nome_em_lista.append(pedaco_nome)
            pedaco_nome = ''
        
        nome_em_lista.append(pedaco_nome)
        pedaco_nome = ''


        # conferir se alguma das partes do nome digitado é igual a alguma parte do nome do determinado paciente

        igual = 0

        for f in consulta_em_lista:
          for p in nome_em_lista:

            if f == p:

              igual += 1
              pass

            if len(consulta_em_lista) == igual:
              print(o)
              break
        nome_em_lista = []
    


# Classe para registro de atendimento

class RegistroAtendimento():
  def __init__(self):

    pass

  # função registrar o atendimento de um novo paciente

  def novo_atendimento(self):

    registro_paciente = []

    registro_paciente.append(input('Peso do paciente: '))
    registro_paciente.append(input('Altura do paciente: '))
    registro_paciente.append(input('Relato do paciente: '))
    registro_paciente.append(input('Anotações do médico: '))
    registro_paciente.append(input('Relação de exames passados: '))
    registro_paciente.append(input('Diagnostico médico: '))
    registro_paciente.append(input('Código CID do diagnostico: '))
    registro_paciente.append(input('Tratamento e/ou medicamentos prescistros: '))

    registro_paciente.append(informacoes_pacientes[-1][1])

    informacoes_registros.append(registro_paciente)


    # função consultar o registro de atendimentos do paciente consultado

  def previamente_atendido(self): 

    print(informacoes_datas_atendimentos)

    detalhes = input('visualizar detalhes do atendimento (nº do atendimento): ')


# criando objetos

funcionalidade_1 = CadastroPaciente()
funcionalidade_2 = CadastroDoenca()
funcionalidade_3 = RegistroAtendimento()


while True:

  funcionalidade = input('\nCadastrar paciente (1), cadastrar código de doença (2), relatório (3), encerrar (s): ')

  # menu de cadastramento do paciente

  if funcionalidade == '1':

    opcoes_cadastro_paciente = input('Cadastrar (1), Remover (2), Alterar (3), Consultar nome/CPF (4): ')

    if opcoes_cadastro_paciente == '1':
      funcionalidade_1.cadastrar_paciente()

      registro = input('registrar atendimento (s): ')

      if registro == 's':
        funcionalidade_3.novo_atendimento()

    elif opcoes_cadastro_paciente == '2':
      funcionalidade_1.remover_cadastro()
      
    elif opcoes_cadastro_paciente == '3':
      funcionalidade_1.alterar_cadastro()

    else:
      funcionalidade_1.consultar_cadastro()
    
      registro = input('Consultar atendimentos (s): ')

      if registro == 's':
        funcionalidade_3.previamente_atendido()


  # menu de cadastramento de doença

  if funcionalidade == '2':

    opcoes_cadastro_doenca = input('Cadastrar (1), Remover (2), Alterar (3), Consultar (4): ')

    if opcoes_cadastro_doenca == '1':
      funcionalidade_2.cadastrar_doenca()

    elif opcoes_cadastro_doenca == '2':
      funcionalidade_2.remover_cadastro()

    elif opcoes_cadastro_doenca == '3':
      funcionalidade_2.alterar_doenca()
    
    else:
      funcionalidade_2.consultar_doencas()
  
  if funcionalidade == 's':
    break


































