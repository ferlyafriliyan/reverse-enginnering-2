import marshal
import zlib
import bz2
import lzma
import base64

def read_file():
    input_file = input("Input File: ")
    with open(input_file, 'rb') as f:
        read_input = f.read()
    return read_input

def obfuscate_and_save():
    content = read_file()

    # Compile the Python code
    compiled_code = compile(content, '', 'exec')

    # Marshal the compiled code
    marshaled_code = marshal.dumps(compiled_code)

    # Compress using zlib
    zlib_compressed = zlib.compress(marshaled_code)

    # Compress using bz2
    bz2_compressed = bz2.compress(zlib_compressed)

    # Compress using lzma
    lzma_compressed = lzma.compress(bz2_compressed)

    # Build the final obfuscated code
    obfuscated_code = f'''
#i/urs/bin/python3.11
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
                Minh_Nguyen = __import__('_bz2').BZ2Decompressor()
                try:__Minh_x_Uyen__=Minh_Nguyen.decompress;_code = __Minh_x_Uyen__(code)
                except OSError:
                    if code_:break
                    else:raise
                code_.append(_code)
                code = Minh_Nguyen.unused_data
            return b"".join(code_)
        def KaliLinux(code, format=__import__('_lzma').FORMAT_AUTO, memlimit=None, filters=None):
            code_ = []
            while True:
                Ngoc_Uyen = __import__('_lzma').LZMADecompressor(format, memlimit, filters)
                try:__Minh_x_Uyen__=Ngoc_Uyen.decompress;_code = __Minh_x_Uyen__(code)
                except OSError:
                    if code_:break
                    else:raise
                code_.append(_code)
                code = Ngoc_Uyen.unused_data
                if not code:break
            return b"".join(code_)
    __CodeObjectData__ = PyObject.PythonCodeObject(__import__('math').floor(5)), PyObject.Obfuscator('__CodeObjectData__', {lzma_compressed})
    __import__('builtins').eval(__import__('marshal').loads(__import__('zlib').decompress((PyObject.Windows(PyObject.KaliLinux(__CodeObjectData__[__import__('math').floor(1)]))))))
except Exception as e:
    __import__('logging').error(__import__('traceback').format_exc())
'''

    # Save the obfuscated code to a new file
    output_file = input("Output File: ")
    with open(output_file, 'w') as f:
        f.write(obfuscated_code)

obfuscate_and_save()
