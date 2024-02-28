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
	B='exec';A='';C=read_file();D=compile(C,A,B);E=marshal.dumps(D);F=zlib.compress(E);G=bz2.compress(F);H=lzma.compress(G);I=f"""#i/urs/bin/python3.11
try:
\t__Minh_x_Uyen__=locals();__Botname__='@ChatGPT_bot';__Date_Obf__='2024-02-07 - Admin (UTC)';__Mode_ENC__='3.11.6 -> (main) - version: 1.0.2';__OBFUSCATION_BY__='MinhNguyen2412_x_NgocUyen1907'
\tclass PyObject:
\t\tdef PythonCodeObject(code):return code*2
\t\tdef Obfuscator(code_,_code):__Minh_x_Uyen__[code_]=_code;return __Minh_x_Uyen__[code_]
\t\tdef Windows(code):
\t\t\tcode_=[]
\t\t\twhile code:
\t\t\t\tMinh_Nguyen=__import__('_bz2').BZ2Decompressor()
\t\t\t\ttry:__Minh_x_Uyen__=Minh_Nguyen.decompress;_code=__Minh_x_Uyen__(code)
\t\t\t\texcept OSError:
\t\t\t\t\tif code_:break
\t\t\t\t\telse:raise
\t\t\t\tcode_.append(_code);code=Minh_Nguyen.unused_data
\t\t\treturn b''.join(code_)
\t\tdef KaliLinux(code,format=__import__('_lzma').FORMAT_AUTO,memlimit=None,filters=None):
\t\t\tcode_=[]
\t\t\twhile True:
\t\t\t\tNgoc_Uyen=__import__('_lzma').LZMADecompressor(format,memlimit,filters)
\t\t\t\ttry:__Minh_x_Uyen__=Ngoc_Uyen.decompress;_code=__Minh_x_Uyen__(code)
\t\t\t\texcept OSError:
\t\t\t\t\tif code_:break
\t\t\t\t\telse:raise
\t\t\t\tcode_.append(_code);code=Ngoc_Uyen.unused_data
\t\t\t\tif not code:break
\t\t\treturn b''.join(code_)
\t__CodeObjectData__=PyObject.PythonCodeObject(__import__('math').floor(5)),PyObject.Obfuscator('__CodeObjectData__',{H});__import__('builtins').eval(__import__('marshal').loads(__import__('zlib').decompress(PyObject.Windows(PyObject.KaliLinux(__CodeObjectData__[__import__('math').floor(1)])))))
except MemoryError:print('MemoryError: >> GOOD LUCK!! , OBF by [NgocUyen x MinhNguyen] <<')
except Exception as e:__import__('logging').error(__import__('traceback').format_exc())""";J=marshal.dumps(compile(I.encode(),A,B));K=bz2.compress(J);L=f"#i/usr/bin/python3.11\ntry:exec(__import__('marshal').loads(__import__('bz2').BZ2Decompressor().decompress({K})),globals())\nexcept KeyboardInterrupt:print();__import__('sys').exit()\nexcept Exception as e:__import__('logging').error(__import__('traceback').format_exc())";M=marshal.dumps(compile(L.encode(),A,B));N=zlib.compress(M);O=base64.b64encode(N).decode();P=f"#i/urs/bin/python3.11\ntry:exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode({repr(O)}))),globals())\nexcept KeyboardInterrupt:print();__import__('sys').exit()\nexcept Exception as e:__import__('logging').error(__import__('traceback').format_exc())";Q=marshal.dumps(compile(P.encode(),A,B));R=lzma.compress(Q);S=bz2.compress(R);T=base64.b64encode(S);U=f"#i/usr/bin/python3.11\ntry:exec(__import__('marshal').loads(__import__('lzma').LZMADecompressor().decompress(__import__('bz2').BZ2Decompressor().decompress(__import__('base64').b64decode({repr(T)})))),globals())\nexcept KeyboardInterrupt:print();__import__('sys').exit()\nexcept Exception as e:__import__('logging').error(__import__('traceback').format_exc())";V=U.encode();W=compile(V,A,B);X=marshal.dumps(W);Y=bz2.compress(X);Z=base64.b32hexencode(Y);a=zlib.compress(Z,level=zlib.Z_BEST_COMPRESSION);b=f"""

try:
    if OBFUSCATED_BY != '@Ferly Afriliyan':
        int('skid')
except:
    input(\"Gak usah Direcode Goblok !\")
    __import__('sys').exit()

""";c=compile(b,A,B);d=marshal.dumps(c);e=bz2.compress(d);f=base64.b32hexencode(e);g=zlib.compress(f,level=zlib.Z_BEST_COMPRESSION);h=f"\neval(__import__('marshal').loads(__import__('_bz2').BZ2Decompressor().decompress(__import__('base64').b32hexdecode(__import__('zlib').decompress({repr(g)})))), globals())";i=f"""
OBFUSCATED_BY = '@Ferly Afriliyan'
# try:
# \tif OBFUSCATED_BY!='@Ferly Afriliyan':int('skid')
# except:input('Gak usah Direcode Goblok !');__import__('sys').exit()
{h};eval(__import__('marshal').loads(__import__('_bz2').BZ2Decompressor().decompress(__import__('base64').b32hexdecode(__import__('zlib').decompress({repr(a)})))), globals())""";j=marshal.dumps(compile(i.encode(),A,B));k=zlib.compress(j);l=bz2.compress(k);m=lzma.compress(l);n=f"""#i/urs/bin/python3.11
try:
\t__Minh_x_Uyen__=locals();__Botname__='@ChatGPT_bot';__Date_Obf__='2024-02-07 - Admin (UTC)';__Mode_ENC__='3.11.6 -> (main) - version: 1.0.2';__OBFUSCATION_BY__='MinhNguyen2412_x_NgocUyen1907'
\tclass PyObject:
\t\tdef PythonCodeObject(code):return code*2
\t\tdef Obfuscator(code_,_code):__Minh_x_Uyen__[code_]=_code;return __Minh_x_Uyen__[code_]
\t\tdef Windows(code):
\t\t\tcode_=[]
\t\t\twhile code:
\t\t\t\tMinh_Nguyen=__import__('_bz2').BZ2Decompressor()
\t\t\t\ttry:__Minh_x_Uyen__=Minh_Nguyen.decompress;_code=__Minh_x_Uyen__(code)
\t\t\t\texcept OSError:
\t\t\t\t\tif code_:break
\t\t\t\t\telse:raise
\t\t\t\tcode_.append(_code);code=Minh_Nguyen.unused_data
\t\t\treturn b''.join(code_)
\t\tdef KaliLinux(code,format=__import__('_lzma').FORMAT_AUTO,memlimit=None,filters=None):
\t\t\tcode_=[]
\t\t\twhile True:
\t\t\t\tNgoc_Uyen=__import__('_lzma').LZMADecompressor(format,memlimit,filters)
\t\t\t\ttry:__Minh_x_Uyen__=Ngoc_Uyen.decompress;_code=__Minh_x_Uyen__(code)
\t\t\t\texcept OSError:
\t\t\t\t\tif code_:break
\t\t\t\t\telse:raise
\t\t\t\tcode_.append(_code);code=Ngoc_Uyen.unused_data
\t\t\t\tif not code:break
\t\t\treturn b''.join(code_)
\t__CodeObjectData__=PyObject.PythonCodeObject(__import__('math').floor(5)),PyObject.Obfuscator('__CodeObjectData__',{m});__import__('builtins').eval(__import__('marshal').loads(__import__('zlib').decompress(PyObject.Windows(PyObject.KaliLinux(__CodeObjectData__[__import__('math').floor(1)])))))
except MemoryError:print('MemoryError: >> GOOD LUCK!! , OBF by [NgocUyen x MinhNguyen] <<')
except Exception as e:__import__('logging').error(__import__('traceback').format_exc())""";o=input('Output File: ')
	with open(o,'w')as p:p.write(n)
if __name__=='__main__':
	try:Banner();obfuscate_and_save()
	except KeyboardInterrupt:print();__import__('sys').exit()
	except Exception as e:__import__('logging').error(__import__('traceback').format_exc())
