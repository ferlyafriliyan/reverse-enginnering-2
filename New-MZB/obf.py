import marshal
import zlib
import base64
import PyInstaller.__main__
import os
import platform
import sys
import time

class ExecuteCode:
    def eval(self, code):
        return eval(code)

    def join(self, char_list):
        return ''.join(char_list)

    def chr(self, code):
        return chr(code)

def clear():
    os.system('clear' if 'linux' in sys.platform.lower() else 'cls')

def obfuscate_and_save(input_file, output_file, iterations):
    # Read the original Python code from the input file
    with open(input_file, 'rb') as f:
        original_code = f.read().decode('utf-8', 'ignore')

    # Perform multiple iterations of encryption
    obfuscated_code = original_code
    for _ in range(iterations):
        obfuscated_code = encrypt_python_code(obfuscated_code)

    # Save the obfuscated code to a new file
    with open(output_file, 'w') as f:
        f.write(obfuscated_code)

    print('Berhasil Obfuscate File : %s' % (input_file))
    print('Sedang membuat executable... ', end='', flush=True)
    animate_loading()
    print('Berhasil')

    # Use PyInstaller to create an executable
    try:
        PyInstaller.__main__.run([
            '--onefile',
            '--noconsole',  # This makes it a GUI application, so the console window doesn't appear
            output_file
        ])
    except Exception as e:
        pass
        # print('\nError:', e)


def animate_loading():
    for _ in range(5):  # Animate loading for 5 iterations
        print('.', end='', flush=True)
        time.sleep(1)
    print('\b\b\b\b\b', end='', flush=True)  # Remove the dots

def encrypt_python_code(code):
    execute_code = ExecuteCode()

    compiled_code = compile(code, 'print("Hello world!")', 'exec')

    # Marshal the compiled code
    marshaled_code = marshal.dumps(compiled_code)

    # Compress the marshaled code using zlib
    compressed_code = zlib.compress(marshaled_code)

    # Encode the compressed code using base64
    encoded_code = base64.b64encode(compressed_code)

    return f'exec(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))(\'\',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))(\'\',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))(\'\',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 98, 97, 115, 101, 54, 52, 34, 41, 46, 98, 54, 52, 100, 101, 99, 111, 100, 101],chr))({repr(encoded_code.decode())}))))'

clear()
# Example usage:
input_file = input('Input File : ')
output_file = 'obfuscated_code.py'
iterations = int(input('Number of iterations: '))

# Obfuscate, save, and create an executable
obfuscate_and_save(input_file, output_file, iterations)
