import re

def phone_validation(phone):
  regex = r'^(\d{2})?[-. ]?(\d{8})$'
  if re.match(regex, phone):
    return True
  return False
