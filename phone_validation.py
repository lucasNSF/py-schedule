import re

def phone_validation(phone):
  regex = r'^(\+55\s?)?(\(\d{2}\)\s?|\d{2}\s?)(9\d{4}|\d{4})-\d{4}$'
  if re.match(regex, phone):
    return True
  return False
