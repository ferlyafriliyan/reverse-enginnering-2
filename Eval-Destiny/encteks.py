import random

def generate_random_encryption(target_text):
    encryption = ''.join([f'\\x{ord(c):02x}' for c in target_text])
    return encryption

target_text = "# Obfuscated with PyObfuscate\n# https://ferlyafriliyan.vercel.app\n# import Kontolivo\n# Decrypt keterangan Author By : Ferly Afriliyan\n"

encryption = generate_random_encryption(target_text)
print(encryption)