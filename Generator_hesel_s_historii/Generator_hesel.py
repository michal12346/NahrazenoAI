# Generator hesel - 1 VERZE

import secrets
import string

# 2) Generátor hesla

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*_-+"
    return "".join(secrets.choice(chars) for _ in range(length))

# 5) Hlavní program
# vygeneruje heslo
heslo = generate_password(16)
print("Vygenerované heslo:", heslo)