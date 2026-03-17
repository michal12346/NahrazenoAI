# Generator hesel -  1 VERZE

import secrets
import string

# Generátor hesla
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*_-+"
    return "".join(secrets.choice(chars) for _ in range(length))

# Hlavní program
# Vygeneruje heslo
heslo = generate_password(16)
print("Vygenerované heslo:", heslo)
