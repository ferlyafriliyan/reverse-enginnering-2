import marshal
import base64
import zlib
import time;import datetime
import platform;from random import randint as rr
from os import system as autoclear

variable_value = '=(:__:-_= __, lambda c; _ = ,__ .' * rr(14, 44)

current_time = datetime.datetime.now()
current_time_str = current_time.strftime("%A, %B %d, %Y %H:%M:%S")
            
try:
    file = input("Input File : ")
    total = int(input("Limit : "))

    if total < 101:
        out = input("Output File : ")
        xos = open(file, 'rb').read()

        # Metode Enkripsi
        encoded_data = base64.b64encode(zlib.compress(marshal.dumps(compile(xos, '', 'exec')))).decode()
            
        with open(out, 'wb') as w:
            w.write(b"import marshal\n")
            w.write(b"import base64\n")
            w.write(b"import zlib\n")
            w.write(b"\n")
            w.write(f"# Time : {current_time_str}\n".encode())
            w.write(f"# Platform : {platform.system()}-{platform.machine()}\n".encode())
            w.write("# Obfuscated by : Ferly Afriliyan (Ryougaa Hideki)\n".encode())
            w.write(b"\n")
            w.write(f"# Variable Value : {len(encoded_data)}\n".encode())
            w.write(b"\n")
            w.write(f"'{variable_value}';exec((lambda _ : (marshal.loads(zlib.decompress(base64.b64decode(_))) if _ else None))('{encoded_data}'))\n".encode())

        komter = 0
        while total >= komter:
            encoded_data = base64.b64encode(zlib.compress(marshal.dumps(compile(open(out, 'rb').read(), '', 'exec')))).decode()

            with open(out, 'wb') as w:
                w.write(b"import marshal\n")
                w.write(b"import base64\n")
                w.write(b"import zlib\n")
                w.write(b"\n")
                w.write(f"# Time : {current_time_str}\n".encode())
                w.write(f"# Platform : {platform.system()}-{platform.machine()}\n".encode())
                w.write("# Obfuscated by : Ferly Afriliyan (Ryougaa Hideki)\n".encode())
                w.write(b"\n")
                w.write(f"# Variable Value : {len(encoded_data)}\n".encode())
                w.write(b"\n")
                w.write(f"'{variable_value}';exec((lambda _ : (marshal.loads(zlib.decompress(base64.b64decode(_))) if _ else None))('{encoded_data}'))\n".encode())

            current_iteration = komter
            total_iterations = total
            loading_percentage = (current_iteration / total_iterations) * 100
            print(f"Encrypting: [{loading_percentage:.2f}%]", end='\r')
            time.sleep(0.00)
            komter += 1

        compiled_file = file.replace('.py', '_.py')
        with open(compiled_file, 'wb') as compiled:
            compiled.write(marshal.dumps(compile(open(out, 'rb').read(), '', 'exec')))
        print(f"\nCompiled file saved to: {compiled_file}")

        # Evaluasi kode yang telah di-compile
        eval(compile(open(compiled_file, 'rb').read(), '', 'exec'))

        exit(f"Limit Max > {total} 101")
except Exception as e:
    print(f"Error: {str(e)}")
