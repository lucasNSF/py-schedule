from phone_validation import phone_validation
from Exporter_Schedule import Exporter_Schedule

class Schedule:
  _schedule = {}
  _exporter_schedule = Exporter_Schedule()

  def __init__(self, owner):
    self.owner = owner

  def __str__(self):
    count = 0
    print('Name | Number')
    for contact in self._schedule.values():
      count = count + 1
      print(f'[{count}] {contact.name} | {contact.number}')

  def export_schedule(self):
    self._exporter_schedule.export_schedule(self._schedule)

  def add_contact(self, contactInfo):
    if not self._is_dict(contactInfo):
      raise ValueError('Argumento esperado deve ser um dicionário.')
    if not phone_validation(contactInfo.number):
      raise ValueError('Formato de número incorreto. Tente: (DD) XXXX-XXXX')
    
    self._schedule[contactInfo.number] = contactInfo
    print('Contato adicionado à sua agenda!')

  def delete_contact(self, number):
    if not phone_validation(number):
      raise ValueError('Formato de número incorreto. Tente: (DD) XXXX-XXXX')
    if not self._has_contact(number):
      print('Contato inexistente!')
      return
    self._schedule.pop(number)
    print('Contato removido!')

  def update_contact_name(self, number, name):
    if not phone_validation(number):
      raise ValueError('Formato de número incorreto. Tente: (DD) XXXX-XXXX')
    if not self._has_contact(number):
      print('Contato inexistente!')
      return
    
    self._schedule[number].name = name
    print(f'Nome do contato {number} atualizado para {name}')

  def update_contact_number(self, old_number, new_number):
    if not phone_validation(old_number) or not phone_validation(new_number):
      raise ValueError('Formato de número incorreto. Tente: (DD) XXXX-XXXX')
    if not self._has_contact(old_number):
      print('Contato inexistente!')
      return

    contact_info = self._schedule.get(old_number)
    contact_info.number = new_number
    self._schedule.pop(old_number)
    self._schedule[contact_info.number] = contact_info
    print(f'Número do antigo contato {old_number} atualizado para {new_number}')

  def search_contact_by_number(self, number):
    if not phone_validation(number):
      raise ValueError('Formato de número incorreto. Tente: (DD) XXXX-XXXX')
    
    return self._schedule.get(number)

  def search_contact_by_name(self, name):
    count = 0

    print('Name | Number')
    for contact in self._schedule.values():
      if contact[name] == name:
        count = count + 1
        print(f'[{count}] {contact.name} | {contact.number}')

  def _is_dict(self, value):
    return isinstance(value, dict)
  
  def _has_contact(self, number):
    return self._schedule.get(number) is not None
  