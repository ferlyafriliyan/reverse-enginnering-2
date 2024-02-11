import marshal
import zlib
import bz2
import lzma
import base64
import os
import sys
import platform

def read_file():
    input_file = input("Input File: ")
    with open(input_file, 'rb') as f:
        read_input = f.read()
    return read_input

def Banner():
    os.system('cls' if 'win' in sys.platform.lower() else 'clear')
    print(f"""
  ___ ___                  .___ ________ _____________________
 /   |   \_____ _______  __| _/ \_____  \\\______   \_   _____/
/    ~    \__  \\\_  __ \/ __ |   /   |   \|    |  _/|    __)  
\    Y    // __ \|  | \/ /_/ |  /    |    \    |   \|     \   
 \___|_  /(____  /__|  \____ |  \_______  /______  /\___  /   
       \/      \/           \/          \/       \/     \/    
""")

def obfuscate_and_save():
    content = read_file()

    # Compile the Python code
    compiled_code = compile(content, '<M_i_n_h_x_U_y_e_n>', 'exec')

    # Marshal the compiled code
    marshaled_code = marshal.dumps(compiled_code)

    # Compress using zlib
    zlib_compressed = zlib.compress(marshaled_code)

    # Compress using bz2
    bz2_compressed = bz2.compress(zlib_compressed)

    # Compress using lzma
    lzma_compressed = lzma.compress(bz2_compressed)

    # Build the final obfuscated code
    _1st_level_of_blurring = f'''#i/urs/bin/python3.11
try:
    __Minh_x_Uyen__=locals()
    __Botname__ = '@MinhNguyen_x_NgocUyen_bot'
    __Date_Obf__ = '2024-02-07 - Admin (UTC)'
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
            print('>> Fucking You ! <<'),
    __CodeObjectData__ = PyObject.PythonCodeObject(__import__('math').floor(5)),PyObject.Obfuscator('__CodeObjectData__', {lzma_compressed})
    __import__('builtins').eval(__import__('marshal').loads(__import__('zlib').decompress(PyObject.Windows(PyObject.KaliLinux(__CodeObjectData__[__import__('math').floor(1)])))))
except MemoryError:print("MemoryError: >> GOOD LUCK!! , OBF by [NgocUyen x MinhNguyen] <<")
except Exception as e:__import__('logging').error(__import__('traceback').format_exc())'''

    _2st_marshal_code = marshal.dumps(compile(_1st_level_of_blurring.encode(), '<M_i_n_h_x_U_y_e_n>', 'exec'))
    _2st_bz2_code = bz2.compress(_2st_marshal_code)

    _2st_level_of_blurring = f'''#i/usr/bin/python3.11
try:
    exec(__import__('marshal').loads(__import__('bz2').BZ2Decompressor().decompress({_2st_bz2_code})), globals())
except KeyboardInterrupt:
    print()
    __import__('sys').exit()
except Exception as e:
    __import__('logging').error(__import__('traceback').format_exc())'''

    _3st_marshal_code = marshal.dumps(compile(_2st_level_of_blurring.encode(), '<M_i_n_h_x_U_y_e_n>', 'exec'))
    _3st_zlib_code = zlib.compress(_3st_marshal_code)
    _3st_base64_code = base64.b64encode(_3st_zlib_code).decode()

    _3st_level_of_blurring = f'''#i/urs/bin/python3.11
try:
    exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode({repr(_3st_base64_code)}))), globals())
except KeyboardInterrupt:
    print()
    __import__('sys').exit()
except Exception as e:
    __import__('logging').error(__import__('traceback').format_exc())'''
    
    _4st_marshal__code = marshal.dumps(compile(_3st_level_of_blurring.encode(), '<M_i_n_h_x_U_y_e_n>', 'exec'))
    _4st_lzma__code = lzma.compress(_4st_marshal__code)
    _4st_bz2_compressed_code = bz2.compress(_4st_lzma__code)
    _4st_base64__code = base64.b64encode(_4st_bz2_compressed_code)

    _4st_level_of_blurring = f'''#i/usr/bin/python3.11
try:
    exec(__import__('marshal').loads(__import__('lzma').LZMADecompressor().decompress(__import__('bz2').BZ2Decompressor().decompress(__import__('base64').b64decode({repr(_4st_base64__code)})))), globals())
except KeyboardInterrupt:
    print()
    __import__('sys').exit()
except Exception as e:
    __import__('logging').error(__import__('traceback').format_exc())'''
    
    _5st_marshal_code = marshal.dumps(compile(_4st_level_of_blurring.encode(), '<M_i_n_h_x_U_y_e_n>', 'exec'))
    _5st_zlib_code = zlib.compress(_5st_marshal_code)
    _5st_bz2_code = bz2.compress(_5st_zlib_code)
    _5st_lzma_code = lzma.compress(_5st_bz2_code)

    _5st_level_of_blurring = f'''#i/urs/bin/python3.11
try:
    __Minh_x_Uyen__=locals()
    __Botname__ = '@MinhNguyen_x_NgocUyen_bot'
    __Date_Obf__ = '2024-02-07 - Admin (UTC)'
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
            print('>> Fucking You ! <<'),
    __CodeObjectData__ = PyObject.PythonCodeObject(__import__('math').floor(5)),PyObject.Obfuscator('__CodeObjectData__', {_5st_lzma_code})
    __import__('builtins').eval(__import__('marshal').loads(__import__('zlib').decompress(PyObject.Windows(PyObject.KaliLinux(__CodeObjectData__[__import__('math').floor(1)])))))
except MemoryError:print("MemoryError: >> GOOD LUCK!! , OBF by [NgocUyen x MinhNguyen] <<")
except Exception as e:__import__('logging').error(__import__('traceback').format_exc())'''

    # Save the obfuscated code to a new file
    output_file = input("Output File: ")
    with open(output_file, 'w') as f:
        f.write(_5st_level_of_blurring)

if __name__ == '__main__':
    try:
        Banner()
        obfuscate_and_save()
    except KeyboardInterrupt:
        print()
        __import__('sys').exit()
    except Exception as e:
        __import__('logging').error(__import__('traceback').format_exc())
