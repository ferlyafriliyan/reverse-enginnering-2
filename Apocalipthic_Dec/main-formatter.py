#!/usr/bin/python3
_V="<class 'function'>"
_U=b'locals()['
_T='>> permission denied!'
_S='>> file not found!'
_R='>> this file to large!'
_Q=b'\r\r\n'
_P='<< Input full file Hyperion: '
_O='>> reading file....'
_N='shutil'
_M='subprocess'
_L='>> at line {} in code <<'
_K='builtins'
_J='{}('
_I=None
_H='nt'
_G='utf8'
_F='\\'
_E=False
_D=True
_C='rb'
_B=b'\n'
_A='sys'
import os
if __name__!='__main__':exit()
os.system('cls')
print('>>> Hyperion Deobf by __builtins__.KhanhNguyen__bot')
print('>>> FB: https://fb.me/freya.xyz')
print('!! ĐÂY LÀ CÔNG CỤ CÓ THỂ GIẢI MÃ MÃ OBF TỪ BILLY !!')
print('!! NẾU BẠN MUA TOOL NÀY TỪ MỘT AI ĐÓ, HỌ LÀ LỪA ĐẢO !!')
print()
__builtins__.bbllaacckk_deobfuscate_tokenize=__import__('tokenize')
__builtins__.bbllaacckk_sieu_nhan_gao_den=__import__('os')
__builtins__.bbllaacckk_thanks_to_nguyen=__import__(_M)
__builtins__.bbllaacckk_khong_co_gi_la_kho=__import__(_A)
__builtins__.bbllaacckk_sieu_nhan_gao_trang=__import__('marshal')
__builtins__.bbllaacckk_khanh_dep_trai_dang_test_thu_unhexlify=__import__('binascii').unhexlify
__builtins__.bbllaacckk_MinhNguyen_x_NgocUyen_bot=__import__('io').BytesIO
__builtins__.bbllaacckk_stdout__=__import__(_A).stdout
__builtins__.bbllaacckk_nhung_modules_bi_khoa=['os','threading',_M,_A]
__builtins__.bbllaacckk___devnull__=open('nul'if __builtins__.bbllaacckk_sieu_nhan_gao_den.name==_H else'/dev/null','wb')
try:__cpy_syspath__=__cpy_syspath__+'\\python.exe'
except NameError:__cpy_syspath__=__builtins__.bbllaacckk_khong_co_gi_la_kho.executable
class bbllaacckk_KhanhNguyen__bot:
	def rm_pycache():
		try:__import__(_N).rmtree('__pycache__')
		except:pass
	def get_py_ver():return'.'.join(__builtins__.bbllaacckk_khong_co_gi_la_kho.version.split(' ')[0].split('.')[:-1])
	def get_f_d(bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum):
		A='/';file_name=A.join(bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum.split('.')[0].split(_F)).split(A)[-1];folder=A.join(bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum.split(_F)).split(A)[:-1]
		if __builtins__.bbllaacckk_sieu_nhan_gao_den.name==_H:
			folder=_F.join(folder)+_F
			if folder==_F:folder='.'+folder
		else:
			folder=A.join(folder)+A
			if folder==A:folder='.'+folder
		return file_name,folder
	def get_license(file_name,bbllaacckk_day_la_binary):return f"# Hyperion deobf by __.KhanhNguyen__bot\n# FB: https://fb.me/freya.xyz\n# File name: [{file_name}.py] (".encode(_G)+str('pyc'if bbllaacckk_day_la_binary else'py').encode(_G)+' - '.encode(_G)+__builtins__.bbllaacckk_KhanhNguyen__bot.get_py_ver().encode(_G)+')\n\n'.encode(_G)
	def get_code(self):return __builtins__.bbllaacckk_deobfuscate_tokenize.untokenize(self.ntokens)
	def replace_var(self,target,var):
		self.ntokens=[]
		for token in self.content:
			string=token.string
			if int(token.type)==1:
				if str(string)==str(target):string=str(var)
			self.ntokens.append(__builtins__.bbllaacckk_deobfuscate_tokenize.TokenInfo(token.type,string,token.start,token.end,token.line))
		self.put_code(self.get_code())
	def put_code(self,content):self.content=list(__builtins__.bbllaacckk_deobfuscate_tokenize.tokenize(__builtins__.bbllaacckk_MinhNguyen_x_NgocUyen_bot(content).readline))
	def replace_by_khanh_dep_trai(tai_sao_em_khong_dua_cho_anh_code,bbllaacckk_thang_nao_bao_em_khong_dep_trai,bbllaacckk_tao_dep_trai_nhat_vu_tru):
		A='mot_dong_string_rat_dai';tai_sao_em_khong_dua_cho_anh_code=tai_sao_em_khong_dua_cho_anh_code.split(_B)
		for __builtins__.bbllaacckk_khanh_dep_trai_qua in range(0,len(tai_sao_em_khong_dua_cho_anh_code),1):
			if bbllaacckk_thang_nao_bao_em_khong_dep_trai in tai_sao_em_khong_dua_cho_anh_code[__builtins__.bbllaacckk_khanh_dep_trai_qua]:
				__builtins__.bbllaacckk_sieu_nhan_gao_do=tai_sao_em_khong_dua_cho_anh_code[__builtins__.bbllaacckk_khanh_dep_trai_qua]
				for __builtins__.bbllaacckk_sieu_nhan_gao_xanh in range(0,len(__builtins__.bbllaacckk_sieu_nhan_gao_do),1):
					try:
						if __builtins__.bbllaacckk_sieu_nhan_gao_do[__builtins__.bbllaacckk_sieu_nhan_gao_xanh:__builtins__.bbllaacckk_sieu_nhan_gao_xanh+len(bbllaacckk_thang_nao_bao_em_khong_dep_trai)]==bbllaacckk_thang_nao_bao_em_khong_dep_trai:
							if __builtins__.bbllaacckk_sieu_nhan_gao_do[__builtins__.bbllaacckk_sieu_nhan_gao_xanh+len(bbllaacckk_thang_nao_bao_em_khong_dep_trai):__builtins__.bbllaacckk_sieu_nhan_gao_xanh+len(bbllaacckk_thang_nao_bao_em_khong_dep_trai)+1]in globals()[A]or __builtins__.bbllaacckk_sieu_nhan_gao_do[__builtins__.bbllaacckk_sieu_nhan_gao_xanh-1:__builtins__.bbllaacckk_sieu_nhan_gao_xanh]in globals()[A]:break
							else:__builtins__.bbllaacckk_sieu_nhan_gao_do=__builtins__.bbllaacckk_sieu_nhan_gao_do[:__builtins__.bbllaacckk_sieu_nhan_gao_xanh]+bbllaacckk_tao_dep_trai_nhat_vu_tru+__builtins__.bbllaacckk_sieu_nhan_gao_do[__builtins__.bbllaacckk_sieu_nhan_gao_xanh+len(bbllaacckk_thang_nao_bao_em_khong_dep_trai):]
					except IndexError:break
				tai_sao_em_khong_dua_cho_anh_code[__builtins__.bbllaacckk_khanh_dep_trai_qua]=__builtins__.bbllaacckk_sieu_nhan_gao_do
		tai_sao_em_khong_dua_cho_anh_code=_B.join(tai_sao_em_khong_dua_cho_anh_code);return tai_sao_em_khong_dua_cho_anh_code
	def read(bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum,bbllaacckk_day_la_binary,is_dump=_E):
		L='!! failed when deobfuscate!';K='!! cannot auto detect real code! please manually input code+vars if you can!';J='[::-1]))),globals())';I='exec(__import__("marshal").loads(__import__("zlib").decompress(__import__("base64").b64decode(';H='base64';G='_py';F='temp_run.py';E='zlib';D='exec';C='<KhanhNguyen9872>';B='khanh_dep_trai_tmp.py';A='temp_code.py';print(_O)
		if bbllaacckk_day_la_binary:
			for __builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao in range(1,101,1):
				try:
					__builtins__.bbllaacckk_sieu_nhan_gao_do=''
					if'<code object <module>'in str(__builtins__.bbllaacckk_sieu_nhan_gao_trang.loads(open(bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum,_C).read()[__builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao:])):__builtins__.bbllaacckk_sieu_nhan_gao_do=open(bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum,_C).read()[__builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao:];print('>> found pyc at {}!'.format(__builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao));break
				except ValueError:pass
			if not __builtins__.bbllaacckk_sieu_nhan_gao_do:print('!! cannot deobfuscate this file !!');input();__import__(_A).exit()
			__builtins__.bbllaacckk_sieu_nhan_gao_do=__builtins__.bbllaacckk_sieu_nhan_gao_trang.dumps(compile('\n__import__(\'khanh_dep_trai_tmp\').__spec__ = __import__(\'zlib\').__spec__\n__import__(\'sys\').modules[\'zlib\']=__import__(\'sys\').modules[\'khanh_dep_trai_tmp\']\n__import__(\'zlib\').decompress.__module__ = \'zlib\'\n__file__ = """{0}"""\n\nexec(__import__(\'marshal\').loads('.format(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum)+str(__builtins__.bbllaacckk_sieu_nhan_gao_do)+'),globals())',C,D))
		else:__builtins__.bbllaacckk_sieu_nhan_gao_do=__builtins__.bbllaacckk_sieu_nhan_gao_trang.dumps(compile('\n__import__(\'khanh_dep_trai_tmp\').__spec__ = __import__(\'zlib\').__spec__\n__import__(\'sys\').modules[\'zlib\']=__import__(\'sys\').modules[\'khanh_dep_trai_tmp\']\n__import__(\'zlib\').decompress.__module__ = \'zlib\'\n__file__ = """{0}"""\n\n'.format(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum).encode(_G)+open(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum,_C).read(),C,D))
		try:
			if is_dump:
				file_name,folder=__builtins__.bbllaacckk_KhanhNguyen__bot.get_f_d(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum)
				try:__import__(_N).rmtree(folder+file_name+G)
				except:pass
				try:__builtins__.bbllaacckk_sieu_nhan_gao_den.mkdir(folder+file_name+G)
				except:pass
				folder=folder+file_name+G+folder[-1:];folder=folder.replace(_F,'\\\\');__builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao=__builtins__.bbllaacckk_sieu_nhan_gao_trang.dumps(compile('\nimport zlib\nfrom zlib import *\nglobal khanhcount\nkhanhcount=0\n__file__ = """{0}"""\ntxxt = {3}\ndef decompress(code):\n    global khanhcount\n    try:\n        open({2}.decode(\'utf8\') + \'deobf_layer_{{}}_{1}.txt\'.format(khanhcount),"wb").write(txxt + zlib.decompress(code))\n    except:\n        open({2}.decode(\'utf8\') + \'deobf_layer_{{}}_{1}.txt\'.format(khanhcount),"w").write(str(txxt.decode(\'utf8\')) + str(zlib.decompress(code)))\n    khanhcount+=1\n    return zlib.decompress(code)\n\n'.format(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum,file_name,str(folder.encode(_G)),str(__builtins__.bbllaacckk_KhanhNguyen__bot.get_license(file_name,__builtins__.bbllaacckk_day_la_binary))),C,D));print('>> Obf code will start now! please wait.....')
			else:__builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao=__builtins__.bbllaacckk_sieu_nhan_gao_trang.dumps(compile('\nfrom zlib import *\n__file__ = """{0}"""\ndef decompress(code):\n    open("temp_run.py","wb").write(code)\n    __import__("sys").exit(0)\n'.format(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum),C,D))
			open(B,'w').write(I+str(__import__(H).b64encode(__import__(E).compress(__builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao))[::-1])+J);del __builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao
		except KeyboardInterrupt:print('!! cannot write file !!');input()
		try:open(A,'w').write(I+str(__import__(H).b64encode(__import__(E).compress(__builtins__.bbllaacckk_sieu_nhan_gao_trang.dumps(compile('\n__file__ = """{0}"""\nwhile 1:\n    try:\n        exec(__import__(\'marshal\').loads(__import__("zlib").decompress(__import__("base64").b64decode('+str(__import__(H).b64encode(__import__(E).compress(__builtins__.bbllaacckk_sieu_nhan_gao_do)))+"))),globals())\n        break\n    except ModuleNotFoundError as e:\n        __import__('sys').modules[str(e).split()[-1][1:-1]] = __import__('sys').modules['sys']\n".format(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum),C,D))))[::-1])+J)
		except SyntaxError:__builtins__.bbllaacckk_sieu_nhan_gao_den.unlink(B);print('!! obf code is error !!');__import__(_A).exit()
		try:
			cmd=f"{__cpy_syspath__} temp_code.py"if __builtins__.bbllaacckk_sieu_nhan_gao_den.name==_H else'{} temp_code.py'.format(__builtins__.bbllaacckk_khong_co_gi_la_kho.executable)
			if __builtins__.bbllaacckk_sieu_nhan_gao_den.name==_H:__builtins__.bbllaacckk_thanks_to_nguyen.check_output(cmd,timeout=15,stderr=__builtins__.bbllaacckk___devnull__)
			else:__builtins__.bbllaacckk_thanks_to_nguyen.run(cmd,stderr=__builtins__.bbllaacckk___devnull__,shell=_D)
			__builtins__.bbllaacckk_KhanhNguyen__bot.rm_pycache();__builtins__.bbllaacckk_sieu_nhan_gao_den.unlink(B);del cmd
			if is_dump:return''
			__builtins__.bbllaacckk_sieu_nhan_gao_do=open(F,_C).read()
			if not __builtins__.bbllaacckk_sieu_nhan_gao_do:__builtins__.bbllaacckk_sieu_nhan_gao_den.unlink(A);print(K);input();__import__(_A).exit()
			else:open(F,'wb').write(__import__(E).decompress(__builtins__.bbllaacckk_sieu_nhan_gao_do))
		except __builtins__.bbllaacckk_thanks_to_nguyen.TimeoutExpired:
			__builtins__.bbllaacckk_sieu_nhan_gao_den.unlink(A);__builtins__.bbllaacckk_sieu_nhan_gao_den.unlink(B)
			if is_dump:return''
			print(L);input();__import__(_A).exit()
		except __builtins__.bbllaacckk_thanks_to_nguyen.CalledProcessError:
			__builtins__.bbllaacckk_sieu_nhan_gao_den.unlink(A);__builtins__.bbllaacckk_sieu_nhan_gao_den.unlink(B)
			if __builtins__.bbllaacckk_day_la_binary:print('!! only support pyc python3.11 !!')
			else:print(K)
			print(L);input();__import__(_A).exit()
		except PermissionError as e:__builtins__.bbllaacckk_sieu_nhan_gao_den.unlink(A);__builtins__.bbllaacckk_sieu_nhan_gao_den.unlink(B);print('>> permission error: {}'.format(e));input();__import__(_A).exit()
		except FileNotFoundError:__builtins__.bbllaacckk_sieu_nhan_gao_den.unlink(A);print('!! cannot get code, this code is hyperion??? !!');input();__import__(_A).exit()
		__builtins__.bbllaacckk_sieu_nhan_gao_den.unlink(A);__builtins__.bbllaacckk_sieu_nhan_gao_do=open(F,_C).read().split(_B);__builtins__.bbllaacckk_sieu_nhan_gao_den.unlink(F);return __builtins__.bbllaacckk_sieu_nhan_gao_do
__builtins__.bbllaacckk_KhanhNguyen__bot=bbllaacckk_KhanhNguyen__bot
del bbllaacckk_KhanhNguyen__bot
__builtins__.bbllaacckk_KhanhNguyen__bot.rm_pycache()
print('>> Python: {}'.format(__builtins__.bbllaacckk_KhanhNguyen__bot.get_py_ver()))
while 1:
	inp=input('!! Auto Detect Code + Vars? [Y/n]: ').lower()
	if inp=='y':
		while 1:
			try:
				__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum=input(_P).replace('"','');__builtins__.bbllaacckk_sieu_nhan_gao_xanh=open(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum,_C).read(4)
				if _Q in __builtins__.bbllaacckk_sieu_nhan_gao_xanh:__builtins__.bbllaacckk_day_la_binary=_D
				else:__builtins__.bbllaacckk_day_la_binary=_E
				if int(__builtins__.bbllaacckk_sieu_nhan_gao_den.stat(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum).st_size)>524288000:print('>> This file becomes Large!');continue
				break
			except FileNotFoundError:print('>> File not Found!')
			except PermissionError:print('>> Permission Denied!')
			except OSError:continue
		__builtins__.bbllaacckk_sieu_nhan_gao_do=__builtins__.bbllaacckk_KhanhNguyen__bot.read(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum,__builtins__.bbllaacckk_day_la_binary,_E);break
	elif inp=='n':
		while 1:
			inp=str(input('!! Do you want to deobf all first layer? [Y/n]: '))
			if inp=='y':
				while 1:
					try:
						__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum=input(_P).replace('"','');__builtins__.bbllaacckk_sieu_nhan_gao_xanh=open(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum,_C).read(4)
						if _Q in __builtins__.bbllaacckk_sieu_nhan_gao_xanh:__builtins__.bbllaacckk_day_la_binary=_D
						else:__builtins__.bbllaacckk_day_la_binary=_E
						if int(__builtins__.bbllaacckk_sieu_nhan_gao_den.stat(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum).st_size)>524288000:print(_R);continue
						break
					except FileNotFoundError:print(_S)
					except PermissionError:print(_T)
					except OSError:continue
				__builtins__.bbllaacckk_sieu_nhan_gao_do=__builtins__.bbllaacckk_KhanhNguyen__bot.read(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum,__builtins__.bbllaacckk_day_la_binary,_D);print('>> Done all first layer!');__import__(_A).exit(0)
			elif inp=='n':
				__builtins__.bbllaacckk_day_la_binary=_E;print('!! you must deobfuscate the first layer Hyperion into a file first!')
				while 1:
					try:
						__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum=input('<< Input file code+vars (one file): ').replace('"','');__builtins__.bbllaacckk_sieu_nhan_gao_do=open(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum,_C).read(1)
						if int(__builtins__.bbllaacckk_sieu_nhan_gao_den.stat(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum).st_size)>524288000:print(_R);continue
						break
					except FileNotFoundError:print(_S)
					except PermissionError:print(_T)
					except OSError:continue
				print(_O);__builtins__.bbllaacckk_sieu_nhan_gao_do=open(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum,_C).read().split(_B);break
		if inp=='y'or inp=='n':break
del inp
__builtins__.bbllaacckk_KhanhNguyen__bot.rm_pycache()
__builtins__.bbllaacckk_sieu_nhan_gao_xanh=0
__builtins__.bbllaacckk_sieu_nhan_gao_vang=0
__builtins__.bbllaacckk_ignore_var_by_khanh=_E
print('>> split code....')
for __builtins__.bbllaacckk_khanh_dep_trai_nhi in range(0,len(__builtins__.bbllaacckk_sieu_nhan_gao_do),1):
	if b'from builtins import 'in __builtins__.bbllaacckk_sieu_nhan_gao_do[__builtins__.bbllaacckk_khanh_dep_trai_nhi]:__builtins__.bbllaacckk_sieu_nhan_gao_xanh=__builtins__.bbllaacckk_khanh_dep_trai_nhi;__builtins__.bbllaacckk_ignore_var_by_khanh=_D;break
__builtins__.bbllaacckk_dep_trai_thi_khong_co_gi_la_sai=0
__builtins__.bbllaacckk_line_removed=0
if _U not in __builtins__.bbllaacckk_sieu_nhan_gao_do[0]:
	print('>> remove license....')
	for __builtins__.bbllaacckk_khanh_dep_trai_nhi in range(0,len(__builtins__.bbllaacckk_sieu_nhan_gao_do),1):
		if _U in __builtins__.bbllaacckk_sieu_nhan_gao_do[__builtins__.bbllaacckk_khanh_dep_trai_nhi]:__builtins__.bbllaacckk_sieu_nhan_gao_do=__builtins__.bbllaacckk_sieu_nhan_gao_do[__builtins__.bbllaacckk_khanh_dep_trai_nhi:];__builtins__.bbllaacckk_dep_trai_thi_khong_co_gi_la_sai=__builtins__.bbllaacckk_khanh_dep_trai_nhi;__builtins__.bbllaacckk_line_removed=__builtins__.bbllaacckk_khanh_dep_trai_nhi;break
if __builtins__.bbllaacckk_ignore_var_by_khanh:print('>> code detected! try deobfuscate completely....');__builtins__.bbllaacckk_khanh_dep_trai_nhi=_B.join(__builtins__.bbllaacckk_sieu_nhan_gao_do[:__builtins__.bbllaacckk_sieu_nhan_gao_xanh-__builtins__.bbllaacckk_dep_trai_thi_khong_co_gi_la_sai]);__builtins__.bbllaacckk_khanh_nguyen_9872=_B.join(__builtins__.bbllaacckk_sieu_nhan_gao_do[__builtins__.bbllaacckk_sieu_nhan_gao_xanh-__builtins__.bbllaacckk_dep_trai_thi_khong_co_gi_la_sai:]);__builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao=_E
else:
	print('>> code undetected! only deobfuscate vars....');__builtins__.bbllaacckk_khanh_dep_trai_nhi=_B.join(__builtins__.bbllaacckk_sieu_nhan_gao_do);__builtins__.bbllaacckk_khanh_nguyen_9872=_B.join(__builtins__.bbllaacckk_sieu_nhan_gao_do);__builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao=_D;print('!! only deobfuscate vars is NOT recommend to reading vars !!')
	while 1:
		bbllaacckk_khanh_dep_trai_nhat=input('>> do you want to reading vars? [Y/n]: ').lower()
		if bbllaacckk_khanh_dep_trai_nhat=='y':__builtins__.bbllaacckk_ignore_var_by_khanh=_D;break
		elif bbllaacckk_khanh_dep_trai_nhat=='n':break
if __builtins__.bbllaacckk_ignore_var_by_khanh:
	__builtins__.bbllaacckk_ignore_var_by_khanh=['__cpy_syspath__','__name__','exit','__doc__','__file__','__cached__','__package__','__loader__','__spec__','__annotations__','__builtins__','__warningregistry__'];print('>> prevent import....');__builtins__.bbllaacckk_chan_quyen_thoat_code=vars(__import__(_A)).copy();__import__(_A).exit=_I;__import__(_K).exit=_I;exit=_I;__builtins__.bbllaacckk_backup_modules_vip_pro={}
	for __builtins__.bbllaacckk_khanh_dep_trai_qua in __builtins__.bbllaacckk_nhung_modules_bi_khoa:
		try:__builtins__.bbllaacckk_backup_modules_vip_pro[__builtins__.bbllaacckk_khanh_dep_trai_qua]=__builtins__.bbllaacckk_khong_co_gi_la_kho.modules[__builtins__.bbllaacckk_khanh_dep_trai_qua];__builtins__.bbllaacckk_khong_co_gi_la_kho.modules[__builtins__.bbllaacckk_khanh_dep_trai_qua]=_I
		except KeyError:pass
	print('>> reading vars....');print('================ [Use: <Ctrl + C> if code started!]\n');__builtins__.bbllaacckk_khanh_dep_trai_nhi=__builtins__.bbllaacckk_khanh_dep_trai_nhi.split(_B);__builtins__.bbllaacckk_max__=len(__builtins__.bbllaacckk_khanh_dep_trai_nhi);__builtins__.bbllaacckk_min__=0
	for __builtins__.bbllaacckk_khanh_dep_trai_qua in __builtins__.bbllaacckk_khanh_dep_trai_nhi:
		try:exec(__builtins__.bbllaacckk_khanh_dep_trai_qua,globals());__builtins__.index=int(__builtins__.bbllaacckk_khanh_dep_trai_nhi.index(__builtins__.bbllaacckk_khanh_dep_trai_qua))+1;__builtins__.i=int(100/(__builtins__.bbllaacckk_max__-__builtins__.bbllaacckk_min__)*(__builtins__.index-__builtins__.bbllaacckk_min__));__builtins__.bbllaacckk_stdout__.write(f"\r[%-25s] %d%% ({__builtins__.index}/{__builtins__.bbllaacckk_max__})"%('='*int(__builtins__.i/4),__builtins__.i));__builtins__.bbllaacckk_stdout__.flush()
		except KeyboardInterrupt:print('\n!! break read vars [KeyboardInterrupt] !!');print(_L.format(int(__builtins__.bbllaacckk_khanh_dep_trai_nhi.index(__builtins__.bbllaacckk_khanh_dep_trai_qua))+__builtins__.bbllaacckk_line_removed+1),end='');break
		except Exception as e:print('\n!! stop read vars due to [{}] !!'.format(str(e)));print(_L.format(int(__builtins__.bbllaacckk_khanh_dep_trai_nhi.index(__builtins__.bbllaacckk_khanh_dep_trai_qua))+__builtins__.bbllaacckk_line_removed+1),end='');break
		except:print('\n!! stop read vars due to [unknown error] !!');print(_L.format(int(__builtins__.bbllaacckk_khanh_dep_trai_nhi.index(__builtins__.bbllaacckk_khanh_dep_trai_qua))+__builtins__.bbllaacckk_line_removed+1),end='');break
	print('\n\n================ [read vars completed]');print('>> restore import....')
	for __builtins__.bbllaacckk_khanh_dep_trai_qua in __builtins__.bbllaacckk_backup_modules_vip_pro:
		try:__builtins__.bbllaacckk_khong_co_gi_la_kho.modules[__builtins__.bbllaacckk_khanh_dep_trai_qua]=__builtins__.bbllaacckk_backup_modules_vip_pro[__builtins__.bbllaacckk_khanh_dep_trai_qua]
		except KeyError:pass
	exit=__builtins__.bbllaacckk_chan_quyen_thoat_code['exit'];__import__(_A).exit=exit;__import__(_K).exit=exit;__builtins__.bbllaacckk_khanh_dep_trai_nhi={};__builtins__.bbllaacckk_dep_trai_thi_khong_co_gi_la_sai=1
	for __builtins__.bbllaacckk_dep_trai_thi_khong_co_gi_la_sai in globals():
		if __builtins__.bbllaacckk_dep_trai_thi_khong_co_gi_la_sai in __builtins__.bbllaacckk_ignore_var_by_khanh:continue
		elif __builtins__.bbllaacckk_dep_trai_thi_khong_co_gi_la_sai in __import__(_K).__dict__:continue
		__builtins__.bbllaacckk_khanh_dep_trai_nhi[__builtins__.bbllaacckk_dep_trai_thi_khong_co_gi_la_sai]=globals()[__builtins__.bbllaacckk_dep_trai_thi_khong_co_gi_la_sai]
	__builtins__.bbllaacckk_khanh_dep_trai_nhi=dict(sorted(__builtins__.bbllaacckk_khanh_dep_trai_nhi.items(),key=lambda x:(len(x[0]),len(x[0])),reverse=_D));unhexlify_name='__builtins__.bbllaacckk_khanh_dep_trai_dang_test_thu_unhexlify';eval_name='eval';mot_dong_string_rat_dai=[str(char).encode()for char in'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890']
	if __builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao:
		__builtins__.bbllaacckk_replace_type=0;print('!! only deobfuscate vars is NOT recommend to replace vars string !!')
		while 1:
			bbllaacckk_khanh_dep_trai_nhat=input('>> do you want to replace vars string? [Y/n]: ').lower()
			if bbllaacckk_khanh_dep_trai_nhat=='y':__builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao=_E;break
			elif bbllaacckk_khanh_dep_trai_nhat=='n':break
	else:
		while 1:
			choose=str(input('>> replace vars [1 - Fast (Low accuracy), 2 - Very Slow (Extreme accuracy), 3 - Skip]: '))
			if choose=='1':__builtins__.bbllaacckk_replace_type=0;break
			elif choose=='2':__builtins__.bbllaacckk_replace_type=1;break
			elif choose=='3':__builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao=_D;break
		del choose
	if not __builtins__.bbllaacckk_cuoc_doi_that_dep_lam_sao:
		print('>> replace vars string [{} mode]....'.format('Fast'if __builtins__.bbllaacckk_replace_type==0 else'Very Slow'))
		if __builtins__.bbllaacckk_replace_type==1:Khanh=__builtins__.bbllaacckk_KhanhNguyen__bot();Khanh.put_code(__builtins__.bbllaacckk_khanh_nguyen_9872)
		__tmp_list__=list(__builtins__.bbllaacckk_khanh_dep_trai_nhi);__builtins__.bbllaacckk_max__=len(__tmp_list__);__builtins__.bbllaacckk_min__=0
		for bbllaacckk_khanh_dep_trai_nhat in __builtins__.bbllaacckk_khanh_dep_trai_nhi:
			if len(bbllaacckk_khanh_dep_trai_nhat)>=1:
				if bbllaacckk_khanh_dep_trai_nhat.encode()in __builtins__.bbllaacckk_khanh_nguyen_9872:
					__builtins__.bbllaacckk___tmp_var__=str(type(__builtins__.bbllaacckk_khanh_dep_trai_nhi[bbllaacckk_khanh_dep_trai_nhat]))
					if __builtins__.bbllaacckk___tmp_var__=="<class 'bool'>"or __builtins__.bbllaacckk___tmp_var__=="<class 'int'>"or __builtins__.bbllaacckk___tmp_var__=="<class 'float'>":__builtins__.bbllaacckk_khanh_number_one=str(__builtins__.bbllaacckk_khanh_dep_trai_nhi[bbllaacckk_khanh_dep_trai_nhat])
					elif __builtins__.bbllaacckk___tmp_var__==_V:__builtins__.bbllaacckk_khanh_number_one=str(__builtins__.bbllaacckk_khanh_dep_trai_nhi[bbllaacckk_khanh_dep_trai_nhat]).split(' ')[1]
					elif __builtins__.bbllaacckk___tmp_var__=="<class 'builtin_function_or_method'>":
						__builtins__.bbllaacckk___tmp_var__=str(__builtins__.bbllaacckk_khanh_dep_trai_nhi[bbllaacckk_khanh_dep_trai_nhat]).split(' ')[-1][:-1]
						if __builtins__.bbllaacckk___tmp_var__=='unhexlify':__builtins__.bbllaacckk___tmp_var__=unhexlify_name
						__builtins__.bbllaacckk_khanh_number_one=__builtins__.bbllaacckk___tmp_var__
					elif __builtins__.bbllaacckk___tmp_var__==_V:
						__builtins__.bbllaacckk_khanh_number_one=str(__builtins__.bbllaacckk_khanh_dep_trai_nhi[bbllaacckk_khanh_dep_trai_nhat])
						if'<function <lambda> at 'in __builtins__.bbllaacckk_khanh_number_one:continue
						else:__builtins__.bbllaacckk_khanh_number_one=' '.join(str(__builtins__.bbllaacckk_khanh_number_one).split(' ')[:-2][-1:])+"() '''args: {}'''".format(str(__builtins__.bbllaacckk_khanh_dep_trai_nhi[bbllaacckk_khanh_dep_trai_nhat].__code__.co_varnames))
					elif __builtins__.bbllaacckk___tmp_var__=="<class 'type'>":__builtins__.bbllaacckk_khanh_number_one=str(__builtins__.bbllaacckk_khanh_dep_trai_nhi[bbllaacckk_khanh_dep_trai_nhat]).split(' ')[1].split('.')[-1][:-2]
					elif __builtins__.bbllaacckk___tmp_var__=="<class 'bytes'>":__builtins__.bbllaacckk_khanh_number_one=str(__builtins__.bbllaacckk_khanh_dep_trai_nhi[bbllaacckk_khanh_dep_trai_nhat]).replace('\r','\\r').replace('\n','\\n').replace('\t','\\t')
					else:__builtins__.bbllaacckk_khanh_number_one=str('"'+str(__builtins__.bbllaacckk_khanh_dep_trai_nhi[bbllaacckk_khanh_dep_trai_nhat]).replace(_F,'\\\\').replace('"','\\"')+'"').replace('\n','\\n').replace('\t','\\t').replace('\r','\\r').replace('\x08','\\b').replace('\x0c','\\f')
					if __builtins__.bbllaacckk_replace_type==1:Khanh.replace_var(bbllaacckk_khanh_dep_trai_nhat,__builtins__.bbllaacckk_khanh_number_one)
					elif __builtins__.bbllaacckk_replace_type==0:__builtins__.bbllaacckk_khanh_nguyen_9872=__builtins__.bbllaacckk_KhanhNguyen__bot.replace_by_khanh_dep_trai(__builtins__.bbllaacckk_khanh_nguyen_9872,bbllaacckk_khanh_dep_trai_nhat.encode(),__builtins__.bbllaacckk_khanh_number_one.encode())
			__builtins__.index=int(__tmp_list__.index(bbllaacckk_khanh_dep_trai_nhat))+1;__builtins__.i=int(100/(__builtins__.bbllaacckk_max__-__builtins__.bbllaacckk_min__)*(__builtins__.index-__builtins__.bbllaacckk_min__));__builtins__.bbllaacckk_stdout__.write(f"\r[%-25s] %d%% ({__builtins__.index}/{__builtins__.bbllaacckk_max__} var)"%('='*int(__builtins__.i/4),__builtins__.i));__builtins__.bbllaacckk_stdout__.flush()
		__builtins__.bbllaacckk_stdout__.write(f"\r[=========================] 100% ({__builtins__.bbllaacckk_max__}/{__builtins__.bbllaacckk_max__} var)");__builtins__.bbllaacckk_stdout__.flush();print('')
		if __builtins__.bbllaacckk_replace_type==1:__builtins__.bbllaacckk_khanh_nguyen_9872=Khanh.get_code()
	if _J.format(unhexlify_name).encode()in __builtins__.bbllaacckk_khanh_nguyen_9872:
		if input('!! found unhexlify! do you want to decode it? [Y/n]: ').lower()=='y':
			print('>> fixing unhexlify [this may take too long]....');song_chet_co_so='{}({}('.format(eval_name,unhexlify_name).encode();__builtins__.bbllaacckk_khanh_nguyen_9872=__builtins__.bbllaacckk_khanh_nguyen_9872.split(_B);__builtins__.bbllaacckk_khanh_number_one=b'';__builtins__.bbllaacckk_max__=len(__builtins__.bbllaacckk_khanh_nguyen_9872);__builtins__.bbllaacckk_min__=0
			for bbllaacckk_khanh_dep_trai_nhat in range(0,len(__builtins__.bbllaacckk_khanh_nguyen_9872),1):
				if _J.format(unhexlify_name).encode()in __builtins__.bbllaacckk_khanh_nguyen_9872[bbllaacckk_khanh_dep_trai_nhat]:
					ghe_vay_sao=__builtins__.bbllaacckk_khanh_nguyen_9872[bbllaacckk_khanh_dep_trai_nhat].split(b'=')
					for __builtins__.bbllaacckk_khanh_dep_trai_nhi in range(0,len(ghe_vay_sao),1):
						if _J.format(unhexlify_name).encode()in ghe_vay_sao[__builtins__.bbllaacckk_khanh_dep_trai_nhi]:
							__builtins__.bbllaacckk___tmp_var__=ghe_vay_sao[__builtins__.bbllaacckk_khanh_dep_trai_nhi]
							while 1:
								while __builtins__.bbllaacckk___tmp_var__:
									if __builtins__.bbllaacckk___tmp_var__[:len(eval_name)+len(unhexlify_name)+2]==song_chet_co_so:
										while len(__builtins__.bbllaacckk___tmp_var__)>len(eval_name)+len(unhexlify_name)+2:
											try:
												if song_chet_co_so in __builtins__.bbllaacckk___tmp_var__:__builtins__.bbllaacckk_khanh_number_one=eval(__builtins__.bbllaacckk___tmp_var__[5:-1]).encode()
												else:__builtins__.bbllaacckk_khanh_number_one=eval(__builtins__.bbllaacckk___tmp_var__).encode()
												__builtins__.bbllaacckk_khanh_number_one=ghe_vay_sao[__builtins__.bbllaacckk_khanh_dep_trai_nhi].replace(__builtins__.bbllaacckk___tmp_var__,__builtins__.bbllaacckk_khanh_number_one);break
											except Exception:__builtins__.bbllaacckk___tmp_var__=__builtins__.bbllaacckk___tmp_var__[:-1]
										break
									elif __builtins__.bbllaacckk___tmp_var__[:len(unhexlify_name)+1]==song_chet_co_so:
										while len(__builtins__.bbllaacckk___tmp_var__)>len(unhexlify_name)+1:
											try:__builtins__.bbllaacckk_khanh_number_one=eval(__builtins__.bbllaacckk___tmp_var__).encode();__builtins__.bbllaacckk_khanh_number_one=ghe_vay_sao[__builtins__.bbllaacckk_khanh_dep_trai_nhi].replace(__builtins__.bbllaacckk___tmp_var__,__builtins__.bbllaacckk_khanh_number_one);break
											except Exception:__builtins__.bbllaacckk___tmp_var__=__builtins__.bbllaacckk___tmp_var__[:-1]
										break
									else:__builtins__.bbllaacckk___tmp_var__=__builtins__.bbllaacckk___tmp_var__[1:]
								if _J.format(unhexlify_name).encode()in __builtins__.bbllaacckk_khanh_number_one:ghe_vay_sao[__builtins__.bbllaacckk_khanh_dep_trai_nhi]=__builtins__.bbllaacckk_khanh_number_one;__builtins__.bbllaacckk___tmp_var__=__builtins__.bbllaacckk_khanh_number_one;continue
								if not __builtins__.bbllaacckk___tmp_var__:__builtins__.bbllaacckk_khanh_number_one=ghe_vay_sao[__builtins__.bbllaacckk_khanh_dep_trai_nhi]
								break
							ghe_vay_sao[__builtins__.bbllaacckk_khanh_dep_trai_nhi]=__builtins__.bbllaacckk_khanh_number_one
					__builtins__.bbllaacckk_khanh_nguyen_9872[bbllaacckk_khanh_dep_trai_nhat]=b'='.join(ghe_vay_sao)
				__builtins__.i=int(100/(__builtins__.bbllaacckk_max__-__builtins__.bbllaacckk_min__)*(bbllaacckk_khanh_dep_trai_nhat-__builtins__.bbllaacckk_min__))+1;__builtins__.bbllaacckk_stdout__.write(f"\r[%-25s] %d%% ({bbllaacckk_khanh_dep_trai_nhat+1}/{__builtins__.bbllaacckk_max__} unhexlify)"%('='*int(__builtins__.i/4),__builtins__.i));__builtins__.bbllaacckk_stdout__.flush()
			__builtins__.bbllaacckk_stdout__.write(f"\r[=========================] 100% ({__builtins__.bbllaacckk_max__}/{__builtins__.bbllaacckk_max__} unhexlify)");__builtins__.bbllaacckk_stdout__.flush();print('');__builtins__.bbllaacckk_khanh_nguyen_9872=_B.join(__builtins__.bbllaacckk_khanh_nguyen_9872)
		else:__builtins__.bbllaacckk_khanh_nguyen_9872=b'from binascii import unhexlify\n'+__builtins__.bbllaacckk_khanh_nguyen_9872
	__builtins__.bbllaacckk_khanh_nguyen_9872=__builtins__.bbllaacckk_khanh_nguyen_9872.replace(unhexlify_name.encode(),b'unhexlify')
file_name,folder=__builtins__.bbllaacckk_KhanhNguyen__bot.get_f_d(__builtins__.bbllaacckk_ten_cua_file_code_bi_ma_hoa_tum_lum)
print(f">> saving.... [ket_qua_cua_viec_dep_trai_{file_name}.py]")
open(f"{folder}ket_qua_cua_viec_dep_trai_{file_name}.py",'wb').write(__builtins__.bbllaacckk_KhanhNguyen__bot.get_license(file_name,__builtins__.bbllaacckk_day_la_binary)+__builtins__.bbllaacckk_khanh_nguyen_9872)
print('>> done!')