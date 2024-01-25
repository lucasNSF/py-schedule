from Schedule import Schedule

main_option = None

owner = input("Informe seu nome para prosseguir: ")

schedule = Schedule(owner)

while main_option != 0:
  print('------- MENU PRINCIPAL ------\n')
  print('[1] Adicionar um contato')
  print('[2] Remover um contato')
  print('[3] Atualizar um contato')
  print('[4] Buscar um contato')
  print('[5] Imprimir agenda')
  print('[6] Exportar agenda')
  print('[0] Sair')

  try:
    main_option = int(input('Opção: '))

    if main_option == 1:
      try:
        name = input("Digite o nome do contato: ")
        number = input("Digite o número do contato: ")

        contact_info = dict(name = name, number = number)
        schedule.add_contact(contact_info)
      except ValueError as err:
        print(err)
    elif main_option == 2:
      number = input("Digite o número do contato: ")
      schedule.delete_contact(number)
    elif main_option == 3:
      try:
        print('Informe qual desses campos você deseja atualizar do contato:')
        print('[1] Atualizar nome')
        print('[2] Atualizar número')
        second_option = int(input('Opção: '))
        old_number = input('Digite o número atualmente armazenado do contato que você deseja atualizar: ')
      
        if second_option == 1:
          name = input('Digite o novo nome: ')
          schedule.update_contact_name(old_number, name)
        else:
          new_number = input('Digite o novo número: ')
          schedule.update_contact_number(old_number, new_number)
      except:
        print('Opção inválida!')
    elif main_option == 4:
      try:
        print('Informe o método de busca do contato:')
        print('[1] Buscar por número')
        print('[2] Buscar por nome')

        second_option = int(input('Opção: '))
        if second_option == 1:
          number = input('Informe o número: ')
          try:
            contact = schedule.search_contact_by_number(number)
            print(f'{contact.name} | {contact.number}')
          except ValueError as err:
            print(err)
        else:
          name = input('Digite o nome do contato: ')
          schedule.search_contact_by_name(name)
      except:
        print('Opção inválida!')
    elif main_option == 5:
      print(schedule)
    elif main_option == 6:
      schedule.export_schedule()
      print('Agenda exportada para o arquivo "my-contacts.txt!"')
    elif main_option == 0:
      print('Programa encerrado!')
    else:
      print('Opção inválida. Tente novamente!')
  except:
    print('Opção inválida. Tente novamente!')
  