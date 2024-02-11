import marshal,zlib,bz2,lzma,base64,os,sys,platform
def read_file():
	A=input('Input File: ')
	with open(A,'rb')as B:C=B.read()
	return C
def Banner():os.system('cls'if'win'in sys.platform.lower()else'clear');print(f"""
  ___ ___                  .___ ________ _____________________
 /   |   \\_____ _______  __| _/ \\_____  \\\\______   \\_   _____/
/    ~    \\__  \\\\_  __ \\/ __ |   /   |   \\|    |  _/|    __)  
\\    Y    // __ \\|  | \\/ /_/ |  /    |    \\    |   \\|     \\   
 \\___|_  /(____  /__|  \\____ |  \\_______  /______  /\\___  /   
       \\/      \\/           \\/          \\/       \\/     \\/    
""")
def obfuscate_and_save():
	B='exec';A='<M_i_n_h_x_U_y_e_n>';C=read_file();D=compile(C,A,B);E=marshal.dumps(D);F=zlib.compress(E);G=bz2.compress(F);H=lzma.compress(G);I=f"""#i/urs/bin/python3.11
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
            return b\"\".join(code_)
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
            return b\"\".join(code_)
            print('>> Fucking You ! <<'),
    __CodeObjectData__ = PyObject.PythonCodeObject(__import__('math').floor(5)),PyObject.Obfuscator('__CodeObjectData__', {H})
    __import__('builtins').eval(__import__('marshal').loads(__import__('zlib').decompress(PyObject.Windows(PyObject.KaliLinux(__CodeObjectData__[__import__('math').floor(1)])))))
except MemoryError:print(\"MemoryError: >> GOOD LUCK!! , OBF by [NgocUyen x MinhNguyen] <<\")
except Exception as e:__import__('logging').error(__import__('traceback').format_exc())""";J=marshal.dumps(compile(I.encode(),A,B));K=bz2.compress(J);L=f"""#i/usr/bin/python3.11
try:
    exec(__import__('marshal').loads(__import__('bz2').BZ2Decompressor().decompress({K})), globals())
except KeyboardInterrupt:
    print()
    __import__('sys').exit()
except Exception as e:
    __import__('logging').error(__import__('traceback').format_exc())""";M=marshal.dumps(compile(L.encode(),A,B));N=zlib.compress(M);O=base64.b64encode(N).decode();P=f"""#i/urs/bin/python3.11
try:
    exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode({repr(O)}))), globals())
except KeyboardInterrupt:
    print()
    __import__('sys').exit()
except Exception as e:
    __import__('logging').error(__import__('traceback').format_exc())""";Q=marshal.dumps(compile(P.encode(),A,B));R=lzma.compress(Q);S=bz2.compress(R);T=base64.b64encode(S);U=f"""#i/usr/bin/python3.11
try:
    exec(__import__('marshal').loads(__import__('lzma').LZMADecompressor().decompress(__import__('bz2').BZ2Decompressor().decompress(__import__('base64').b64decode({repr(T)})))), globals())
except KeyboardInterrupt:
    print()
    __import__('sys').exit()
except Exception as e:
    __import__('logging').error(__import__('traceback').format_exc())""";V=marshal.dumps(compile(U.encode(),A,B));W=zlib.compress(V);X=bz2.compress(W);Y=lzma.compress(X);Z=f"""#i/urs/bin/python3.11
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
            return b\"\".join(code_)
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
            return b\"\".join(code_)
            print('>> Fucking You ! <<'),
    __CodeObjectData__ = PyObject.PythonCodeObject(__import__('math').floor(5)),PyObject.Obfuscator('__CodeObjectData__', {Y})
    __import__('builtins').eval(__import__('marshal').loads(__import__('zlib').decompress(PyObject.Windows(PyObject.KaliLinux(__CodeObjectData__[__import__('math').floor(1)])))))
except MemoryError:print(\"MemoryError: >> GOOD LUCK!! , OBF by [NgocUyen x MinhNguyen] <<\")
except Exception as e:__import__('logging').error(__import__('traceback').format_exc())""";a=input('Output File: ')
	with open(a,'w')as b:b.write(Z)
if __name__=='__main__':
	try:Banner();obfuscate_and_save()
	except KeyboardInterrupt:print();__import__('sys').exit()
	except Exception as e:__import__('logging').error(__import__('traceback').format_exc())