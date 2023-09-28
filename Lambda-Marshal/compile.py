import marshal
import base64
import zlib
from os import system as autoclear
autoclear('clear')

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
            w.write(f"exec((lambda _ : (marshal.loads(zlib.decompress(base64.b64decode(_))) if _ else None))('{encoded_data}'))\n".encode())

        komter = 0
        while total >= komter:
            encoded_data = base64.b64encode(zlib.compress(marshal.dumps(compile(open(out, 'rb').read(), '', 'exec')))).decode()

            with open(out, 'wb') as w:
                w.write(b"import marshal\n")
                w.write(b"import base64\n")
                w.write(b"import zlib\n")
                w.write(f"exec((lambda _ : (marshal.loads(zlib.decompress(base64.b64decode(_))) if _ else None))('{encoded_data}'))\n".encode())

            print(f"\nSuccess Obfuscate File, File saved to : {out}")

        compiled_file = file.replace('.py', '_.py')
        with open(compiled_file, 'wb') as compiled:
            compiled.write(marshal.dumps(compile(open(out, 'rb').read(), '', 'exec')))
        print(f"Compiled file saved to: {compiled_file}")

        # Evaluasi kode yang telah di-compile
        eval(compile(open(compiled_file, 'rb').read(), '', 'exec'))

        exit(f"Limit Max > {total} 101")
except Exception as e:
    print(f"Error: {str(e)}")
