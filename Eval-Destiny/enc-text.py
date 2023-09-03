import random

def generate_random_encryption(target_text):
    encryption = ''.join([f'\\x{ord(c):02x}' for c in target_text])
    return encryption

target_text = "text yang pengen di enc make simbol\\"
encryption = generate_random_encryption(target_text)
print(encryption)
