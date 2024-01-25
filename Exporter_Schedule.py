class Exporter_Schedule:
  def export_schedule(self, schedule):
    if not isinstance(schedule, dict):
      raise ValueError("Esperado que 'schedule' seja um dicionário.")
    
    f = open('my-contacts.txt', 'a')
    count = 1
    for contact in schedule.values():
      f.write(f'[{count}] {contact.name} - {contact.number}\n')
      count = count + 1
    f.close()
