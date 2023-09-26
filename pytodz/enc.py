import os, sys, re, time
import binascii
import base64
import marshal
import zlib
from py_compile import compile as _compile

_0o0oO_ = '\x4b\x6f\x6e\x74\x6f\x6c\x69\x76\x6f\n'

tod = []


def save_file(outfile, value):
    with open(outfile, 'w') as file:
        file.write(value[0])
    del value[::]
    main_menu('[√] File Saved ' + outfile)


class Compile:
    def __init__(self, file):
        try:
            self.code = open(file).read()
            self.outfile = file + '_'
            self.filename = file
        except Exception as exception:
            main_menu(exception)

    def marshal(self):
        code = repr(marshal.dumps(compile(self.code, self.filename, 'exec')))
        tod.append(f'import marshal\nexec(marshal.loads({code}))')
        save_file(self.outfile, tod)

    def pyc(self):
        _compile(self.filename)
        main_menu('[√] File Saved ' + self.filename + 'c')

    def zlib(self):
        code = repr(zlib.compress(self.code.encode()))
        tod.append(f'import zlib\nexec(zlib.decompress({code}).decode())')
        save_file(self.outfile, tod)

    def base16(self):
        code = repr(base64.b16encode(self.code.encode()).decode())
        tod.append(f'import base64\nexec(base64.b16decode({code}).decode())')
        save_file(self.outfile, tod)

    def base32(self):
        code = repr(base64.b32encode(self.code.encode()).decode())
        tod.append(f'import base64\nexec(base64.b32decode({code}).decode())')
        save_file(self.outfile, tod)

    def base64(self):
        code = repr(base64.b64encode(self.code.encode()).decode())
        tod.append(f'import base64\nexec(base64.b64decode({code}).decode())')
        save_file(self.outfile, tod)

    def hex(self):
        code = repr(binascii.hexlify(self.code.encode()).decode())
        tod.append(f'import binascii\nexec(binascii.unhexlify({code}).decode())')
        save_file(this.outfile, tod)

    def bin(self):
        code = repr(binascii.hexlify(self.code.encode()).decode())
        tod.append(f'import binascii\nexec(binascii.unhexlify({code}).decode())')
        save_file(self.outfile, tod)


def main_menu(text=None):
    if text is not None:
        print(text)
        time.sleep(1.5)
    else:
        pass

    os.system('clear')
    print(_0o0oO_)
    print('—' * 48)
    print('[1] Compile {0}\n[2] Exit'.format('Menu'))
    print('—' * 48)

    try:
        choose = input('[•] Choose: ')
    except (EOFError, KeyboardInterrupt):
        sys.exit('exit')
        time.sleep(0.01)

    if choose in ('1', '2'):
        choose = int(choose)
        if choose == 1:
            compile_menu()
        elif choose == 2:
            sys.exit('[!] Exit')
    else:
        sys.exit('[!] Wrong Input')
        time.sleep(0.01)


def compile_menu():
    os.system('clear')
    print(_0o0oO_)
    print('—' * 48)
    print('[1] {0} marshal\n[2] {0} pyc\n[3] {0} zlib\n[4] {0} base16\n[5] {0} base32\n[6] {0} base64\n[7] {0} hex\n[8] {0} bin\n[B] Back'.format('Compile'))
    print('—' * 48)

    try:
        choose = input('[•] Choose: ')
    except (EOFError, KeyboardInterrupt):
        os.system('clear')

    if choose in ('1', '2', '3', '4', '5', '6', '7', '8'):
        try:
            file = input('[•] Input File: ')
        except Exception as exception:
            main_menu(exception)
        choose = int(choose)
        if choose == 1:
            Compile(file).marshal()
        elif choose == 2:
            Compile(file).pyc()
        elif choose == 3:
            Compile(file).zlib()
        elif choose == 4:
            Compile(file).base16()
        elif choose == 5:
            Compile(file).base32()
        elif choose == 6:
            Compile(file).base64()
        elif choose == 7:
            Compile(file).hex()
        elif choose == 8:
            Compile(file).bin()
    elif choose in ['b', 'B']:
        main_menu()
    else:
        sys.exit('[!] Wrong Input')
        time.sleep(0.01)


if __name__ == '__main__':
    main_menu()
