import readline
agenda = {}


def mostrar_disciplinas():
   if agenda:
      for disciplina in agenda:
            buscar_disciplina(disciplina)
   else:
      print('====> Não há disciplinas no banco de dados :(')
      print('')


def buscar_disciplina(disciplina):
   try:        
      print('Nome:', disciplina)
      print('Código:', agenda[disciplina]['codigo'])
      print('Professor:', agenda[disciplina]['professor'])
      print('Email:', agenda[disciplina]['email'])
      print('Sala de aula:', agenda[disciplina]['saladeaula'])
      print('Horário/Dia das aulas:', agenda[disciplina]['horariodia'])
      print('Avaliações:', agenda[disciplina]['avaliacoes'])
      print('Horário da avaliação:', agenda[disciplina]['horarioav'])
      print('========================================================')
   except KeyError:
      print('====> Disciplina não cadastrada D:')
      print('')
   except Exception as error:
      print('====> Erro')
      print('')
      print(error)


def ler_detalhes_disciplina():
   codigo = input('Código da disciplina: ')
   professor = input('Nome do professor(a): ')
   email = input('Email do professor(a): ')
   saladeaula = input('Código da sala: ')
   horariodia = input('Horário e dia das aulas: ')
   avaliacoes = input('Data das avaliações: ')
   horarioav = input('Horário das avaliações: ')
   return codigo, professor, email, saladeaula, horariodia, avaliacoes, horarioav


def incluir_editar_disciplina(disciplina, codigo, professor, email, saladeaula, horariodia, avaliacoes, horarioav):
   agenda[disciplina] = {
      'codigo': codigo,
      'professor': professor,
      'email': email,
      'saladeaula': saladeaula,
      'horariodia': horariodia,
      'avaliacoes': avaliacoes,
      'horarioav': horarioav,
   }
   salvar()
   print()
   print('====> Disciplina {} adicionada/editada com sucesso :)'.format(disciplina))
   print()


def excluir_disciplina(disciplina):
   try:
      agenda.pop(disciplina)
      salvar()
      print()
      print('====> Disciplina {} excluída com sucesso :)'.format(disciplina))
      print()
   except KeyError:
      print('====> Disciplina inexistente D:')
   except Exception as error:
      print('====> Error')
      print(error)


def exportar_disciplinas(nome_do_arquivo):
   try:
      with open(nome_do_arquivo, 'w') as arquivo:
            for disciplina in agenda:
               codigo = agenda[disciplina]['codigo']
               professor = agenda[disciplina]['professor']
               email = agenda[disciplina]['email']
               saladeaula = agenda[disciplina]['saladeaula']
               horariodia = agenda[disciplina]['horariodia']
               avaliacoes = agenda[disciplina]['avaliacoes']
               horarioav = agenda[disciplina]['horarioav']
               arquivo.write("{} | {} | {} | {} | {} | {} | {} | {}\n".format(disciplina , codigo , professor , email , saladeaula , horariodia , avaliacoes , horarioav))
               
      print('====> Disciplinas exportadas')
   except Exception as error:
      print('====> Ocorreu um erro ao exportar as disciplinas')
      print('')
      print(error)


def importar_disciplinas(nome_do_arquivo):
   try:
      with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
               detalhes = linha.strip().split(',')

               nome = detalhes[0]
               codigo = detalhes[1]
               professor = detalhes[2]
               email = detalhes[3]
               saladeaula = detalhes[4]
               horariodia = detalhes[5]
               avaliacoes = detalhes[6]
               horarioav = detalhes[7]

               incluir_editar_disciplina(nome, codigo, professor, email, saladeaula, horariodia, avaliacoes, horarioav)
   except FileNotFoundError:
      print('====> Arquivo não encontrado')
   except Exception as error:
      print('====> Erro inesperado')
      print(error)

# Pré-definição da extensão e nome do arquivo de banco de dados
def salvar():
   exportar_disciplinas('databasedisc.csv')


def carregar():
   try:
      with open('databasedisc.csv', 'r') as arquivo:
            linhas = arquivo.redlines()
            for linha in linhas:
               detalhes = linha.strip().split(',')

               nome = detalhes[0]
               codigo = detalhes[1]
               professor = detalhes[2]
               email = detalhes[3]
               saladeaula = detalhes[4]
               horariodia = detalhes[5]
               avaliacoes = detalhes[6]
               horarioav = detalhes[7]

               agenda[nome] = {
                        'codigo': codigo,
                        'professor': professor,
                        'email': email,
                        'saladeaula': saladeaula,
                        'horariodia': horariodia,
                        'avaliacoes': avaliacoes,
                        'horarioav': horarioav,
                  }
      print('====> Database carregado')
      print('====> {} disciplinas carregadas'.format(len(agenda)))
   except FileNotFoundError:
      print('====> Arquivo não encontrado')
   except Exception as error:
      print('====> Erro inesperado')
      print(error)


def imprimir_menu():
   print('==================================================')
   print('')
   print('1 - Mostrar todas as disciplinas')
   print('2 - Buscar disciplina')
   print('3 - Incluir disciplina')
   print('4 - Editar disciplina')
   print('5 - Excluir disciplina')
   print('6 - Exportar disciplina para CSV')
   print('7 - Importar disciplina CSV')
   print('0 - Fechar agenda')
   print('')
   print('===================================================')


# START
# As instruções de sequência e entrada para o menu do programa
carregar()
while True:
   imprimir_menu()

   opcao = input('Escolha uma opção: ')
   if opcao == '1':
      mostrar_disciplinas()
   elif opcao == '2':
      disciplina = input('Nome da disciplina: ')
      buscar_disciplina(disciplina)
   elif opcao == '3':
      disciplina = input('Nome da disciplina: ')

      try:
            agenda[disciplina]
            print('====> Disciplina já cadastrada')
      except KeyError:
            codigo, professor, email, saladeaula, horariodia, avaliacoes, horarioav = ler_detalhes_disciplina()
            incluir_editar_disciplina(disciplina, codigo, professor, email, saladeaula, horariodia, avaliacoes, horarioav)
   elif opcao == '4':
      disciplina = input('Nome da disciplina: ')

      try:
            agenda[disciplina]
            print('====> Editando disciplina: ', disciplina)
            codigo, professor, email, saladeaula, horariodia, avaliacoes, horarioav = ler_detalhes_disciplina()
            incluir_editar_disciplina(disciplina, codigo, professor, email, saladeaula, horariodia, avaliacoes, horarioav)
      except KeyError:
            print('====> Disciplina não cadastrada')

   elif opcao == '5':
      disciplina = input('Nome da disciplina: ')
      excluir_disciplina(disciplina)
   elif opcao == '6':
      nome_do_arquivo = input('Digite o nome do arquivo a ser exportado: ')
      exportar_disciplinas(nome_do_arquivo)
   elif opcao == '7':
      nome_do_arquivo = input('Digite o nome do arquivo a ser importado: ')
      importar_disciplinas(nome_do_arquivo)
   elif opcao == '0':
      print('====> Fechando programa')
      break
   else:
      print('====> Opção inválida')
      print('')