from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import marshal
import zlib
import bz2
import lzma
import base64
import os
import sys
import platform
import random


def read_file():
    input_file = input("Input File: ")
    with open(input_file, "rb") as f:
        read_input = f.read()
    return read_input

def Banner():
    os.system("cls" if "win" in sys.platform.lower() else "clear")
    print(
        """
  ___ ___                  .___ ________ _____________________
 /   |   \_____ _______  __| _/ \_____  \\\______   \_   _____/
/    ~    \__  \\\_  __ \/ __ |   /   |   \|    |  _/|    __)  
\    Y    // __ \|  | \/ /_/ |  /    |    \    |   \|     \   
 \___|_  /(____  /__|  \____ |  \_______  /______  /\___  /   
       \/      \/           \/          \/       \/     \/    
"""
    )

def obfuscate_and_save():
    content = read_file()
    compiled_code = compile(content, "", "exec")
    marshaled_code = marshal.dumps(compiled_code)
    zlib_compressed = zlib.compress(marshaled_code)
    bz2_compressed = bz2.compress(zlib_compressed)
    lzma_compressed = lzma.compress(bz2_compressed)

    aes_key = get_random_bytes(32)
    iv = get_random_bytes(16)
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(lzma_compressed, AES.block_size))
    hex_aes_key = aes_key.hex()
    hex_iv = iv.hex()
    obfuscated_code = f"""#i/usr/bin/python3.11
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
    __CodeObjectData__ = PyObject.PythonCodeObject(__import__('math').floor(5)),PyObject.Obfuscator('__CodeObjectData__', {lzma_compressed})
    __import__("builtins").eval(__import__("marshal").loads(__import__("zlib").decompress(PyObject.Windows(PyObject.KaliLinux(__CodeObjectData__[__import__("math").floor(1)])))))
except MemoryError:print("MemoryError: >> GOOD LUCK!! , OBF by [NgocUyen x MinhNguyen] <<")
except Exception as e:__import__("logging").error(__import__("traceback").format_exc())"""

    marshal_code_2 = marshal.dumps(compile(obfuscated_code.encode(), "", "exec"))
    bz2_code_2 = bz2.compress(marshal_code_2)
    obfuscate_code_2 = f"""#i/usr/bin/python3.11
try:exec(__import__('marshal').loads(__import__('bz2').BZ2Decompressor().decompress({bz2_code_2})),globals())
except KeyboardInterrupt:print();__import__('sys').exit()
except Exception as e:__import__('logging').error(__import__('traceback').format_exc())"""

    marshal_code_3 = marshal.dumps(compile(obfuscate_code_2.encode(), "", "exec"))
    zlib_code_3 = zlib.compress(marshal_code_3)
    base64_code_3 = base64.b64encode(zlib_code_3).decode()
    obfuscate_code_3 = f"""#i/urs/bin/python3.11
try:exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode({repr(base64_code_3)}))),globals())
except KeyboardInterrupt:print();__import__('sys').exit()
except Exception as e:__import__('logging').error(__import__('traceback').format_exc())"""

    marshal_code_4 = marshal.dumps(compile(obfuscate_code_3.encode(), "", "exec"))
    lzma_code_4 = lzma.compress(marshal_code_4)
    bz2_code_4 = bz2.compress(lzma_code_4)
    base64_code_4 = base64.b64encode(bz2_code_4)
    obfuscate_code_4 = f"""#i/usr/bin/python3.11
try:exec(__import__('marshal').loads(__import__('lzma').LZMADecompressor().decompress(__import__('bz2').BZ2Decompressor().decompress(__import__('base64').b64decode({repr(base64_code_4)})))),globals())
except KeyboardInterrupt:print();__import__('sys').exit()
except Exception as e:__import__('logging').error(__import__('traceback').format_exc())"""

    marshall_code = marshal.dumps(compile(obfuscate_code_4.encode(), "", "exec"))
    code_base64 = base64.b64encode(base64.b32encode(zlib.compress(marshall_code)))[::-1]
    base64_encoded = base64.b64encode(code_base64)
    base64x2_encoded = base64.b64encode(base64_encoded)
    base32_encoded = base64.b32encode(base64x2_encoded)
    base64x3_encoded = base64.b64encode(base32_encoded)
    aes_key = get_random_bytes(32)
    iv = get_random_bytes(16)
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(base64x3_encoded, AES.block_size))
    hex_aes_key = aes_key.hex()
    hex_iv = iv.hex()
    obfuscate_code_5 = f"""__author__ = 'Ferly Afriliyan'
__madeBy__ = 'CyberPandemonium '
__git__ = 'https://github.com/ferlyafriliyan'

# Obfuscated with CyberPandemonium

try:
    import base64 as _________;import marshal as _______;import zlib as __________;from Crypto.Cipher import AES;from Crypto.Util.Padding import pad, unpad;from Crypto.Random import get_random_bytes;import base64;__vare__ = lambda x: _______.loads(__________.decompress(_________.b32decode(_________.b64decode(x[::-1]))));__mycip__= AES.new(bytes.fromhex("{hex_aes_key}"), AES.MODE_CBC, bytes.fromhex("{hex_iv}"));__step1__=bytes.fromhex("{encrypted_data.hex()}");__step2__=__mycip__.decrypt(__step1__);__decr__=base64.b64decode(__step2__);__decrdata__=__decr__;__gotnew__=base64.b32decode(__decr__);__newdecr__={random.randint(99999999,999999999999)};__getnew__=__newdecr__;__myb64code__=base64.b64decode(__gotnew__);__myb64codee__=base64.b64decode(__myb64code__);___ = __myb64codee__;exec(__vare__(___))
except (KeyboardInterrupt, Exception) as e:
    from os import system
    __import__('os').system('xdg-open https://facebook.com/freya.xyz')
    exit(f"[Error] {{str(e).capitalize()}}!")"""

    # marshal_code_5 = marshal.dumps(obfuscate_code_5.encode())
    marshal_code_5 = marshal.dumps(compile(obfuscate_code_5.encode(), "", "exec"))
    zlib_code_6 = zlib.compress(marshal_code_5)
    bz2_code_6 = bz2.compress(zlib_code_6)
    lzma_code_6 = lzma.compress(bz2_code_6)
    hard_obfuscate = f"""#i/urs/bin/python3.11
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
    __CodeObjectData__ = PyObject.PythonCodeObject(__import__('math').floor(5)),PyObject.Obfuscator('__CodeObjectData__', {lzma_code_6})
    __import__("builtins").eval(__import__("marshal").loads(__import__("zlib").decompress(PyObject.Windows(PyObject.KaliLinux(__CodeObjectData__[__import__("math").floor(1)])))))
except MemoryError:print("MemoryError: >> GOOD LUCK!! , OBF by [NgocUyen x MinhNguyen] <<")
except Exception as e:__import__("logging").error(__import__("traceback").format_exc())"""
    
    output_file = input("Output File: ")
    with open(output_file, 'w') as f:
        f.write(hard_obfuscate)

if __name__ == "__main__":
    try:
        Banner()
        obfuscate_and_save()
    except KeyboardInterrupt:
        print()
        __import__("sys").exit()
    except Exception as e:
        __import__("logging").error(__import__("traceback").format_exc())
