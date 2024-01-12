import zlib
import _bz2
import _lzma
import math
import base64

class PyObject:
    @staticmethod
    def PythonCodeObject(code):
        return str(code * 2)  # Convert the result to string

    @staticmethod
    def Obfuscator(code_, _code):
        locals()[code_] = _code
        return locals()[code_]

    @staticmethod
    def Windows(code):
        code_ = []
        while code:
            Minh_Nguyen = zlib.decompress(__import__('_bz2').decompress(code))
            try:
                __Minh_x_Uyen__ = Minh_Nguyen.decode('latin-1')
            except OSError:
                if code_:
                    break
                else:
                    raise
            code_.append(__Minh_x_Uyen__)
            code = Minh_Nguyen[Minh_Nguyen.find(b'\x00')+1:]
        return base64.b64encode(b"".join(code_)).decode('latin-1')

    @staticmethod
    def KaliLinux(code, format=_lzma.FORMAT_XZ, filters=None):
        compressor = _lzma.LZMACompressor(format=format, filters=filters)
        compressed_data = compressor.compress(code.encode())
        compressed_data += compressor.flush()
        return compressed_data

def obfuscate_and_save(input_file, output_file, encrypted_code_filename='encrypted_code.txt'):
    with open(input_file, 'r', encoding='utf-8') as file:
        python_code = file.read()

    # Obfuscate PythonCodeObject to string and compress with ZLIB, BZ2, and LZMA
    encrypted_code = zlib.compress(__import__('_bz2').BZ2Compressor().compress(__import__('_lzma').LZMACompressor().compress(PyObject.PythonCodeObject(int(__import__('math').floor(1))).encode())) + python_code.encode())


    # Save the value of encrypted_code to a file (in base64 format to avoid character issues)
    with open(encrypted_code_filename, 'wb') as encrypted_code_file:
        encrypted_code_file.write(base64.b64encode(encrypted_code))

    obfuscated_code = f"""
#!/usr/bin/python3.11
try:
    __Minh_x_Uyen__=locals()
    __Botname__ = '@MinhNguyen_x_NgocUyen_bot'
    __Date_Obf__ = '2024-01-01 - Admin (UTC)'
    __Mode_ENC__  = '3.11.6 -> (main) - version: 1.0.1'
    __OBFUSCATION_BY__ = 'MinhNguyen2412_x_NgocUyen1907'
    class PyObject:
        def PythonCodeObject(code: int) -> int:return code*2
        def Obfuscator(code_, _code: (...,)) -> (...,):__Minh_x_Uyen__[code_] = _code;return __Minh_x_Uyen__[code_]
        def Windows(code):
            code_ = []
            while code:
                Minh_Nguyen = __import__('zlib').decompress(__import__('_bz2').decompress(code))
                try:__Minh_x_Uyen__=Minh_Nguyen.decode('latin-1');_code = __Minh_x_Uyen__
                except OSError:
                    if code_:break
                    else:raise
                code_.append(_code)
            return __import__('base64').b64decode(b"".join(code_)).decode('latin-1')
        def KaliLinux(code, format=__import__('_lzma').FORMAT_XZ, filters=None):
            compressor = __import__('_lzma').LZMACompressor(format=format, filters=filters)
            compressed_data = compressor.compress(code.encode())
            compressed_data += compressor.flush()
            return compressed_data
    encrypted_code_filename = {encrypted_code}
    __CodeObjectData__ = PyObject.PythonCodeObject(int(__import__('math').floor(1))), PyObject.Obfuscator('__CodeObjectData__', encrypted_code_filename)
    decoded_encrypted_code = __import__('base64').b64decode(__import__('codecs').decode(__CodeObjectData__[int(__import__('math').floor(1))], 'rot_13'))
    __import__('builtins').eval(__import__('marshal').loads(PyObject.Windows(decoded_encrypted_code)))
except Exception as e:
    __import__('logging').error(__import__('traceback').format_exc())
"""

    with open(output_file, 'w') as file:
        file.write(obfuscated_code)

# Change 'input_file.py' and 'output_file.py' with the appropriate file names
obfuscate_and_save('obf.py', 'output_file.py')
