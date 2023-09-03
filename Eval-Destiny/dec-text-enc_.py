def decrypt_random_encryption(encryption):
    hex_values = encryption.split('\\x')[1:]
    decrypted_text = ''.join([chr(int(hex_value, 16)) for hex_value in hex_values])
    return decrypted_text

encrypted_text = "contoh dari : text yang pengen di enc make simbol\\ "  # Ganti dengan nilai enkripsi yang sesuai
decrypted_text = decrypt_random_encryption(encrypted_text)
print(decrypted_text)
