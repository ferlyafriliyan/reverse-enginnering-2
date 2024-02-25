import marshal, zlib, base64, bz2, lzma
import os, sys

def reading_file():
    input_file = input(f'Input file path: ')
    with open(input_file, 'r', encoding='utf-8') as f:
        contents = f.read()
        return contents

def clear():
    os.system('cls' if 'win' in sys.platform.lower() else 'clear')

def obfuscate():
    clear()
    code = reading_file()
    compile_code = compile(code, '', 'exec')
    marshal_code = marshal.dumps(compile_code)
    bz2_code = bz2.compress(marshal_code)
    base64_code = base64.b32hexencode(bz2_code)
    zlib_code = zlib.compress(base64_code, level=zlib.Z_BEST_COMPRESSION)
    
    anti_skid = f'''

try:
    if OBFUSCATED_BY != '@Ferly Afriliyan':
        int('skid')
except:
    input("Gak usah Direcode Goblok !")
    __import__('sys').exit()

'''
    skid_ = compile(anti_skid, '', 'exec')
    marshal_ = marshal.dumps(skid_)
    bz2_ = bz2.compress(marshal_)
    base64_ = base64.b32hexencode(bz2_)
    zlib_ = zlib.compress(base64_, level=zlib.Z_BEST_COMPRESSION)

    obfuscate_skid = f'''
eval(__import__('marshal').loads(__import__('_bz2').BZ2Decompressor().decompress(__import__('base64').b32hexdecode(__import__('zlib').decompress({repr(zlib_)})))), globals())
'''
    obfuscate_code = f'''
OBFUSCATED_BY = '@Ferly Afriliyan'
{obfuscate_skid}
# try:
# 	if OBFUSCATED_BY!='@Ferly Afriliyan':int('skid')
# except:input('Gak usah Direcode Goblok !');__import__('sys').exit()
eval(__import__('marshal').loads(__import__('_bz2').BZ2Decompressor().decompress(__import__('base64').b32hexdecode(__import__('zlib').decompress({repr(zlib_code)})))), globals())'''

    output_file = input(f'Output file: ')
    with open(output_file, 'w') as f:
        f.write(obfuscate_code)

if __name__ == '__main__':
    try:
        obfuscate()
    except (Exception, KeyboardInterrupt) as e:
        print(e)
