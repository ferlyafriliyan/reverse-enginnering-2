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
	B='<M_i_n_h_x_U_y_e_n>';A='exec';C=read_file();D=compile(C,'',A);E=marshal.dumps(D);F=zlib.compress(E);G=bz2.compress(F);H=lzma.compress(G);I=f"""#i/urs/bin/python3.11
try:
\t__Minh_x_Uyen__=locals();__Botname__='@MinhNguyen_x_NgocUyen_bot';__Date_Obf__='2024-02-07 - Admin (UTC)';__Mode_ENC__='3.11.6 -> (main) - version: 1.0.1';__OBFUSCATION_BY__='MinhNguyen2412_x_NgocUyen1907'
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
except Exception as e:__import__('logging').error(__import__('traceback').format_exc())""";J=marshal.dumps(compile(I.encode(),B,A));K=bz2.compress(J);L=f"#i/usr/bin/python3.11\ntry:exec(__import__('marshal').loads(__import__('bz2').BZ2Decompressor().decompress({K})),globals())\nexcept KeyboardInterrupt:print();__import__('sys').exit()\nexcept Exception as e:__import__('logging').error(__import__('traceback').format_exc())";M=marshal.dumps(compile(L.encode(),B,A));N=zlib.compress(M);O=base64.b64encode(N).decode();P=f"#i/urs/bin/python3.11\ntry:exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode({repr(O)}))),globals())\nexcept KeyboardInterrupt:print();__import__('sys').exit()\nexcept Exception as e:__import__('logging').error(__import__('traceback').format_exc())";Q=marshal.dumps(compile(P.encode(),B,A));R=lzma.compress(Q);S=bz2.compress(R);T=base64.b64encode(S);U=f"#i/usr/bin/python3.11\ntry:exec(__import__('marshal').loads(__import__('lzma').LZMADecompressor().decompress(__import__('bz2').BZ2Decompressor().decompress(__import__('base64').b64decode({repr(T)})))),globals())\nexcept KeyboardInterrupt:print();__import__('sys').exit()\nexcept Exception as e:__import__('logging').error(__import__('traceback').format_exc())";V=marshal.dumps(compile(U.encode(),B,A));W=zlib.compress(V);X=bz2.compress(W);Y=lzma.compress(X);Z=f"""#i/urs/bin/python3.11
try:
\t__Minh_x_Uyen__=locals();__Botname__='@MinhNguyen_x_NgocUyen_bot';__Date_Obf__='2024-02-07 - Admin (UTC)';__Mode_ENC__='3.11.6 -> (main) - version: 1.0.1';__OBFUSCATION_BY__='MinhNguyen2412_x_NgocUyen1907'
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
\t__CodeObjectData__=PyObject.PythonCodeObject(__import__('math').floor(5)),PyObject.Obfuscator('__CodeObjectData__',{Y});__import__('builtins').eval(__import__('marshal').loads(__import__('zlib').decompress(PyObject.Windows(PyObject.KaliLinux(__CodeObjectData__[__import__('math').floor(1)])))))
except MemoryError:print('MemoryError: >> GOOD LUCK!! , OBF by [NgocUyen x MinhNguyen] <<')
except Exception as e:__import__('logging').error(__import__('traceback').format_exc())""";a=input('Output File: ')
	with open(a,'w')as b:b.write(Z)
if __name__=='__main__':
	try:Banner();obfuscate_and_save()
	except KeyboardInterrupt:print();__import__('sys').exit()
	except Exception as e:__import__('logging').error(__import__('traceback').format_exc())