from builtins import *
# •
builtglob = list(globals().keys())

from tokenize import tokenize, untokenize, TokenInfo
from random import choice, shuffle, randint
from io import BytesIO;import os, sys
from binascii import hexlify
from zlib import compress

from rich import print
from re import findall

# Definisi warna teks ANSI
Hitam = "\x1b[0;90m"     # Hitam
Merah = "\x1b[38;5;196m" # Merah
Hijau = "\x1b[38;5;46m"  # Hijau
Kuning = "\x1b[38;5;226m" # Kuning
Biru = "\x1b[38;5;44m"  # Biru
Ungu = "\x1b[0;95m"     # Ungu
Putih = "\x1b[38;5;231m" # Putih
Jingga = "\x1b[38;5;208m" # Jingga
Abu = "\x1b[38;5;248m" # Abu-Abu

# Definisi warna teks Rich
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu
V2 = "[#8B00FF]"  # Violet

# Clear Terminal
def clear():
    if 'linux' in sys.platform.lower():os.system('clear')
    elif 'win' in sys.platform.lower():os.system('cls') # clear()


class Apocalipthic:
    def __init__(self, content: str, clean = True, obfcontent = True, renlibs = True, renvars = True, addbuiltins = True, randlines = True, shell = True, camouflate = True, safemode = True, ultrasafemode = False) -> None:
        clear()
        p("Starting Hyperization.")

        self.content = "exec('')\n\n" + content

        self.camouflate = camouflate

        self.add_imports = []
        self.impcontent2 = []

        self.safemode = safemode

        if addbuiltins:
            p("Adding the builtins...")
            self.AddBuiltins()

        p("Creating default vars...")
        self.CreateVars()


        if renlibs:
            p("Renaming imported libraries...")
            valid = self.RenameImports()

        if renvars and valid:
            p("Renaming variables...")
            self.RenameVars()

        self.strings = {}

        if obfcontent:
            p("Obfuscating the content of each variable...")
            self.ObfContent()

        if clean:
            p("Cleaning the basic script!")
            self.CleanCode()

        if not self._verify_lin(content):
            p("Multi-lines brackets detected! Skipping the layers protecting the chunks.")
            randlines, shell = False, False

        if randlines:
            p("Adding random lines between each chunk...")
            self.RandLines()

        if shell:
            p("Adding a shell to each chunk...")
            self.Shell()

        p("Organising everything...")
        self.Organise()

        # p("Adding anti skid layer...") ;)
        self.AntiSkid()

        if clean:
            p("Cleaning the final script!")
            self.CleanCode()

        p("Compressing the final script...")
        self.Compress()

        if camouflate:
            p("Camouflating the final script to make it less suspicious...")
            self.Camouflate()
        else:
            self.content = ';'.join(self.content)

    # Layers

    def AntiSkid(self):
        if self.camouflate:
            self.content = fr"""
# GG! You just deobfuscated a file obfuscated with Apocalipthic

# Congratulations!

# https://github.com/ferlyafriliyan/Apocalipthic

# coded By : billythegoat356 and BlueRed


try:
    if (
        __obfuscator__ != "Apocalipthic" or
        __authors__ != ('billy', 'BlueRed') or
        __github__ != "https://github.com/ferlyafriliyan/Apocalipthic" or
        __website__ != "https://ferlyafriliyan.vercel.app" or
        __license__ != "EPL-2.0" or
        __code__ != 'print("Hello world!")'
    ):
        int('skid')
except:
    input("Roses are red\nViolets are blue\nYou are a skid\nNobody likes you")
    __import__('sys').exit()


{self.content}""".strip()

    def AddBuiltins(self):
        imp = "from builtins import " + ','.join(f'{var}' for var in builtglob if not var.startswith('__') and var not in ('None', 'True', 'False') and f'{var}(' in self.content) + '\n'
        if imp == "from builtins import \n":
            imp = ""
        self.content = imp + self.content

    def CreateVars(self):

        self.globals = self._randvar()
        self.locals = self._randvar()
        self.vars = self._randvar()

        self.__import__ = self._randvar()

        imports = self._to_import

        impcontent = """
{0}()['{1}']=locals
{1}()['{2}']=__import__
{0}()['{3}']={2}('builtins').vars"""[1:].format(self.globals, self.locals, self.__import__, self.vars, self.unhexlify).splitlines()

        nimpcontent = [f"{self._randglob()}()['{imports[imp]}']={imp}" for imp in imports]
        shuffle(nimpcontent)

        impcontent.extend(iter(nimpcontent))

        self.local_import = f"locals()['{self.globals}']=globals"
        self.impcontent = impcontent
        
    def RenameImports(self):
        _imports = self._gather_imports()
        if _imports == False:
            print(f"Star import detected! Skipping the renaming of imported libraries and variables.")
            # raise self.StarImport()
            return False
        imports = []
        for imp in _imports:
            imports.extend(iter(imp))
        self.imports = {}
        for imp in imports:
            self.imports[imp] = self._randvar()
        impcontent = [f"{self._randglob()}()['{self.imports[imp]}']={self._randglob()}()[{self._protect(imp)}]" for imp in self.imports]
        shuffle(impcontent)

        self.add_imports = [lin for lin in self.content.splitlines() if self._is_valid(lin)]
        self.content = '\n'.join(lin for lin in self.content.splitlines() if lin not in self.add_imports)

        self.impcontent2 = iter(impcontent)
        return True

    def RenameVars(self):
        f = BytesIO(self.content.encode('utf-8'))
        self.tokens = list(tokenize(f.readline))

        # input('\n'.join(str(tok) for tok in self.tokens))

        strings = {}

        ntokens = []

        passed = []

        for token in self.tokens:
            string, type = token.string, token.type

            
            if type == 1:
                if (
                    ((self.tokens[self.tokens.index(token)+1].string == '=' and self._is_not_arg(string)) or
                    self.tokens[self.tokens.index(token)-1].string in ('def', 'class')) and
                    self._check_fstring(string) and
                    self._is_not_library(token=token) and
                    string not in passed and
                    string not in self.imports and
                    (not string.startswith('__') and not string.endswith('__'))
                    ):
                    string = self._randvar()
                    strings[token.string] = string
                elif string in strings and self._is_not_library(token=token) and self.tokens[self.tokens.index(token)+1].string != '=':
                    string = strings[string]
                elif string in self.imports and self._is_exact_library(token=token):
                    if ((self.tokens[self.tokens.index(token)+1].string != '=') and
                        self.tokens[self.tokens.index(token)-1].string not in ('def', 'class')):
                        string = self.imports[string]
                else:
                    passed.append(string)
            
            ntokens.append(TokenInfo(type, string, token.start, token.end, token.line))
            


        self.content = untokenize(ntokens).decode('utf-8')
 
    def ObfContent(self):
        f = BytesIO(self.content.encode('utf-8'))
        self.tokens = list(tokenize(f.readline))

        # input('\n'.join(str(tok) for tok in self.tokens))

        ntokens = []

        for token in self.tokens:
            string, type = token.string, token.type

            if type == 1:
                if string in ('True', 'False'):
                    string = self._obf_bool(string)

            elif type == 2:
                string = self._obf_int(string)

            elif type == 3:
                string = self._obf_str(string)

            ntokens.append(TokenInfo(type, string, token.start, token.end, token.line))

        self.ostrings = self.strings

        self.lambdas = []
        self._add_lambdas()

        strings = [f"{self.vars}()[{self._protect(var)}]={value}" for var, value in self.strings.items()]
        shuffle(strings)

        self.strings = strings

        self.content = untokenize(ntokens).decode('utf-8')

    def CleanCode(self):
            
            self.RemoveComments()
            self.CompressCode()

    def RandLines(self):
        content = []
        lines = self.content.splitlines()
    
        for lin, nextlin in zip(lines, range(len(lines))):
            content.append(lin)
            if (
                    nextlin == len(lines)-1 or
                    self._get_first_statement(lines[nextlin+1]) in ('elif', 'else', 'except', 'finally') or
                    lin.strip()[-1] == ','
                ):
                continue
            fakelin = self._fake_lin(self._get_indentations(lines[nextlin+1]))
            content.append(fakelin)

        self.content = '\n'.join(content)

    def Shell(self):
        chunks = self._get_chunks()

        chunks = [f"{self._protect_var(self.exec)}({self._protect(chunk, r=1)})" for chunk in chunks]
        chunks = [f"""{self._protect_var(self.eval)}({self._protect_var(self.compile)}({self._protect(chunk, char=2)},filename={self._protect(self._randvar())},mode={self._protect('eval')}))""" for chunk in chunks]

        self.content = '\n'.join(chunks)
        
    def Organise(self):
        gd_vars = [f"{self.globals}()[{self._protect(self.getattr, basic=True, )}]=getattr", f"{self.globals}()[{self._protect(self.dir, basic=True)}]=dir"]
        shuffle(gd_vars)
        exec_var = f"{self.globals}()[{self._protect(self.exec)}]={self._protect_built('exec')}"
        add_imports = [f"{self.globals}()[{self._protect(self.exec)}]({self._protect(imp.strip())})" for imp in self.add_imports]

        self.content = self.local_import + '\n' + '\n'.join(gd_vars) + '\n' + '\n'.join(self.impcontent) + '\n' + exec_var + '\n' + '\n'.join(add_imports) + '\n' + '\n'.join(self.impcontent2) + '\n' + '\n'.join(self.strings) + '\n' + self.content

    def Compress(self):

        eval_var = f"globals()['{self._hex('eval')}']"
        str_var = f"globals()['{self._hex('str')}']"
        compile_var = f"globals()['{self._hex('compile')}']"
        
        arg1, arg2 = self._randvar(), self._randvar()
        lambda1 = f"""(lambda {arg1}:{eval_var}({compile_var}({str_var}("{self._hex(eval_var)}({arg1})"),filename='{self._hex(self._randvar())}',mode='{self._hex('eval')}')))"""
        lambda2 = f"(lambda {arg1}:{arg1}(__import__('{self._hex('zlib')}')))"
        lambda3 = f"(lambda {arg1}:{arg1}['{self._hex('decompress')}'])"

        lambdas = [lambda1, lambda2, lambda3]

        lambda4 = f"""(lambda {arg2},{arg1}:{arg2}({arg1}))"""
        lambda5 = f"""(lambda:{lambda1}('{self._hex("__import__('builtins').exec")}'))"""

        lambdas2 = [lambda4, lambda5]

        shuffle(lambdas)
        shuffle(lambdas2)

        keys = {lamb: self._randvar() for lamb in lambdas}

        keys2 = {lamb: self._randvar() for lamb in lambdas2}

        compressed = self._compress(self.content)
        if self.camouflate:
            self.compressed = compressed
            compressed = "RANDOMVARS"

        decompress = f"{keys[lambda3]}({keys[lambda2]}({keys[lambda1]}('{self._hex('vars')}')))"
        exec_content = f"{keys2[lambda5]}()({keys2[lambda4]}({decompress},{compressed}))"

        all_keys = keys

        all_keys.update(keys2)
    
        self.content = ['from builtins import *', ','.join(all_keys.values()) + '=' + ','.join(all_keys.keys()), exec_content]


    def Camouflate(self):
        self.gen = gen = []
        content = self.content

        for _ in range(25):
            self._gen_var()

        compressed = self._split_content(self.compressed, n = 2500)

        bvars = {self._randvar(): var for var in compressed}
        vars = [f"{self._rand_pass()}{' ' * 250};{gen[0]}.{gen[19]}({gen[21]}='{a}',{gen[22]}={b})" for a, b in bvars.items()]
        vars = '\n\n'.join(' ' * 8 + var for var in vars)

        actions = ('!=', 'is', '==', '<', '>', '>=', '<=')
        keys = ('',)
        ext = ('((var1, var2) for var2 in var3)', 'var1 if action else action2', '((var2, var1) for var2 in var3 if action)', '(var1 or var2 if var1 and var2 else ... or (var2, var1))')
        generate = lambda: [
            '{%s: %s}' % (tuple(
                choice(
                    [repr(self._randvar2()), *gen[11:17]]
                ) for _ in range(2)
            )),
            ('(' + ', '.join(f'var{num + 1}' for num in range(randint(2, 3))) + ')').replace(
                'var1', choice(gen[11:17])
            ).replace(
                'var2', choice(gen[11:17])
            ).replace(
                'var3', choice(gen[11:17])
            ).replace(
                'var4', choice(gen[11:17])
            )
        ]

        gen2 = generate()

        for _ in range(int((20 / 2) - 1)):
            gen2.extend(generate())


        rands = [
            '\n' + (' ' * (4 * 2)) + 'try:\n' +  '    ' * 3 + self._rand_gen(ext, keys, gen, gen2, actions) + '\n\n' + (' ' * (4 * 2)) + f'except {self._rand_error()}:\n' + '    ' * 3 + self._rand_gen(ext, keys, gen, gen2, actions) + '\n\n' + (' ' * (4 * 2)) + f'except:\n' + '    ' * 3 + f"{gen[24]}({self._rand_int()} {self._rand_op()} {self._rand_int()}) == {self._rand_type()}"
            for _ in range(4)
        ]

        randomvars = '+'.join(f"{gen[0]}.{gen[18]}({gen[20]}='{var}')" for var in bvars)
        sourcery = "# sourcery skip: collection-to-bool, remove-redundant-boolean, remove-redundant-except-handler"


        self.content = f"""
{content[0]}
from math import prod as {gen[5]}

\x23\x20\x63\x6f\x64\x65\x64\x20\x42\x79\x20\x3a\x20\x62\x69\x6c\x6c\x79\x74\x68\x65\x67\x6f\x61\x74\x33\x35\x36\x20\x61\x6e\x64\x20\x42\x6c\x75\x65\x52\x65\x64

\x5f\x5f\x6f\x62\x66\x75\x73\x63\x61\x74\x6f\x72\x5f\x5f\x20\x3d\x20\x27\x41\x70\x6f\x63\x61\x6c\x69\x70\x74\x68\x69\x63\x27
__authors__ = ('\x62\x69\x6c\x6c\x79', '\x42\x6c\x75\x65\x52\x65\x64')
__github__ = 'https://github.com/ferlyafriliyan/Apocalipthic'
__website__ = 'https://ferlyafriliyan.vercel.app'
__license__ = 'EPL-2.0'

__code__ = '\x70\x72\x69\x6e\x74\x28\x22\x48\x65\x6c\x6c\x6f\x20\x77\x6f\x72\x6c\x64\x21\x22\x29'


{gen[11]}, {gen[12]}, {gen[13]}, {gen[14]}, {gen[15]}, {gen[17]}, {gen[24]} = exec, str, tuple, map, ord, globals, type

class {gen[0]}:
    def __init__(self, {gen[4]}):
        self.{gen[3]} = {gen[5]}(({gen[4]}, {self._rand_int()}))
        self.{gen[1]}({gen[6]}={self._rand_int()})

    def {gen[1]}(self, {gen[6]} = {self._rand_type()}):
        {sourcery}
        self.{gen[3]} {self._rand_op()}= {self._rand_int()} {self._rand_op()} {gen[6]}
        {rands[0]}

    def {gen[2]}(self, {gen[7]} = {self._rand_int()}):
        {sourcery}
        {gen[7]} {self._rand_op()}= {self._rand_int()} {self._rand_op()} {self._rand_int()}
        self.{gen[8]} != {self._rand_type()}
        {rands[1]}

    def {gen[18]}({gen[20]} = {self._rand_type()}):
        return {gen[17]}()[{gen[20]}]

    def {gen[19]}({gen[21]} = {self._rand_int()} {self._rand_op()} {self._rand_int()}, {gen[22]} = {self._rand_type()}, {gen[23]} = {gen[17]}):
        {sourcery}
        {gen[23]}()[{gen[21]}] = {gen[22]}
        {rands[2]}

    def execute(code = str):
        return {gen[11]}({gen[12]}({gen[13]}({gen[14]}({gen[15]}, code))))

    @property
    def {gen[8]}(self):
        self.{gen[9]} = '<__main__.{choice(gen)} object at 0x00000{randint(1000, 9999)}BE{randint(10000, 99999)}>'
        return (self.{gen[9]}, {gen[0]}.{gen[8]})

if __name__ == '__main__':
    try:
        {gen[0]}.execute(code = __code__)
        {gen[10]} = {gen[0]}({gen[4]} = {self._rand_int()} {self._rand_op()} {self._rand_int()})

{vars}

        {self._rand_pass()}{' ' * 250};{content[1]}
        {self._rand_pass()}{' ' * 250};{content[2].replace("RANDOMVARS", randomvars)}

    except Exception as {gen[16]}:
        if {self._rand_bool(False)}:
            {gen[0]}.execute(code = {gen[12]}({gen[16]}))

        elif {self._rand_bool(False)}:
            {self._rand_pass(line = False)}
""".strip()
        



    # Exceptions

    class StarImport(Exception):
        def __init__(self):
            super().__init__("Star Import is forbidden, please update your script")



    # All

    
    def _verify_lin(self, content):
        return all(lin.strip() not in ['(','[','{','}',']',')'] for lin in content.splitlines())

    def _hex(self, var):
        return ''.join(f"\\x{hexlify(char.encode('utf-8')).decode('utf-8')}" for char in var)

    def _randvar(self):
        return choice((
            ''.join(choice(('l','I')) for _ in range(randint(17, 25))),
            'O' + ''.join(choice(('O','0','o')) for _ in range(randint(17, 25))),
            ''.join(choice(('D','O','o')) for _ in range(randint(17, 25))),
            'S' + ''.join(choice(('S','2')) for _ in range(randint(17, 25))),
            ''.join(choice(('M','N')) for _ in range(randint(17, 25))),
            ''.join(choice(('m','n')) for _ in range(randint(17, 25))),
            ''.join(choice(('X','W')) for _ in range(randint(17, 25))),
            ''.join(choice(('x','w')) for _ in range(randint(17, 25))),
            ''.join(choice(('J','I','L')) for _ in range(randint(17, 25))),
            ''.join(choice(('j','i','l')) for _ in range(randint(17, 25)))
        ))
    
    def _randvar2(self):
        return ''.join(choice('ferlyafriliyan, Apocalipthic') for _ in range(randint(5, 20)))

    def _randglob(self):
        return choice((
            self.globals,
            self.locals,
            self.vars
        ))

    
    def _protect(self, var, basic=False, r=0, char=1):
        char = "'" if char == 1 else '"'
        if basic:
            return f"{char}{''.join(reversed(var))}{char}[::+-+-(-(+1))]"
        if type(var) == int:
            return self._adv_int(var)
        if r == 0:
            r = randint(1, 2)
        if r == 1:
            return f"{self.unhexlify}({hexlify(var.encode('utf-8'))}).decode({self.utf8})"
        else:
            return f"{char}{''.join(reversed(var))}{char}[::+-+-(-(+{self._protect(1, basic=basic)}))]"

    def _protect_built(self, var, lib='builtins'):
        protected = self._protect(lib, r=2, basic=True)
        return f"{self.getattr}({self.__import__}({protected}),{self.dir}({self.__import__}({protected}))[{self.dir}({self.__import__}({protected})).index({self._protect(var, r=2, basic=True)})])"

    
    # CreateVars

    @property
    def _to_import(self):

        self.dir = self._randvar()
        self.getattr = self._randvar()

        self.exec = self._randvar()
        
        self.eval = self._randvar()
        self.compile = self._randvar()
        self.join = self._randvar()
        self.true = self._randvar()
        self.false = self._randvar()
        self.bool = self._randvar()
        self.str = self._randvar()
        self.float = self._randvar()
        self.unhexlify = self._randvar()
        

        imports = {
            self._protect_built('eval'): self.eval,
            self._protect_built('compile'): self.compile,
            "''.join": self.join,
            self._protect_built('True'): self.true,
            self._protect_built('False'): self.false,
            self._protect_built('bool'): self.bool,
            self._protect_built('str'): self.str,
            self._protect_built('float'): self.float,
            self._protect_built('unhexlify', lib='binascii'): self.unhexlify,
        }

        return imports

    @property
    def utf8(self):
        return self._protect('utf8', basic=True, r=2)


    # RenameImports

    def _gather_imports(self):
        imports = [lin for lin in self.content.splitlines() if self._is_valid(lin)]
        for imp in imports:
            if '*' in imp:
                return False
        return [imp.replace('import ',',').replace('from ', '').replace(' ','').split(',')[1:] if 'from' in imp else imp.replace('import ', '').replace(' ','').split(',') for imp in imports]

    def _is_valid(self, lin: str):
        return ('import' in lin and '"' not in lin and "'" not in lin and ';' not in lin and '.' not in lin and '#' not in lin)

    # RenameVars

    def _is_not_arg(self, string):
        if not self.safemode:
            return True
        funcs = self._gather_funcs
        for lin in self.content.splitlines():
            if string in lin:
                for imp in self.imports.keys():
                    if imp in lin and '=' in lin and lin.index(imp) < lin.index('='):
                        return False
        return all(string.lower() not in func for func in funcs)

    def _check_fstring(self, string):
        
        fstrings = findall(r'{[' + self._fstring_legal_chars + r']*}', self.content.lower())
        return all(string.lower() not in fstring for fstring in fstrings)


    def _is_not_library(self, token: str):

        while True:
            if self.tokens[self.tokens.index(token)-1].string == '.':
                token = self.tokens[self.tokens.index(token)-2]
            else:
                break
            
        return token.string not in self.imports
    
    def _is_exact_library(self, token: str):
        ntoken = token
        while True:
            if self.tokens[self.tokens.index(token)-1].string == '.':
                token = self.tokens[self.tokens.index(token)-2]
            else:
                break
            
        return ntoken == token
    
    @property
    def _gather_funcs(self):
        lins = [lin.strip().split('(')[1] for lin in self.content.splitlines() if lin.strip().split(' ')[0]=='def']
        return lins

    @property
    def _fstring_legal_chars(self):
        return """abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUV_WXYZ0123456789/*-+. ,/():"'"""


    # ObfContent

    def _obf_bool(self, string):
        if string == 'False':
            obf = f'not({self.bool}({self.str}({self.false})))'
        elif string == 'True':
            obf = f'{self.bool}((~{self.false})or(({self.true})and({self.false})))'
        string = self._randvar()
        while string in self.strings:
            string = self._randvar()
        self.strings[string] = obf
        return string

    def _obf_int(self, string):
        if string.isdigit():
            obf = self._adv_int(int(string))
        elif string.replace('.','').isdigit():
            obf = f"{self.float}({self._protect(string)})"
        else:
            return string
        string = self._randvar()
        while string in self.strings:
            string = self._randvar()
        self.strings[string] = obf
        return string
    
    def _obf_str(self, string):
        obf, do = self._adv_str(string)
        if do:
            string = self._randvar()
            while string in self.strings:
                string = self._randvar()
            self.strings[string] = obf
        else:
            string = obf
        return string

    def _adv_int(self, string):
        n = choice((1, 2))
        if n == 1:
            rnum = randint(1000000,9999999999)
            x = rnum - string
            return f"{self.eval}({self._protect(f'{self._underscore_int(rnum)}+(-{self._underscore_int(x)})')})"
        elif n == 2:
            rnum = randint(0, string)
            x = string - rnum
            return f"{self.eval}({self._protect(f'{self._underscore_int(x)}-(-{self._underscore_int(rnum)})')})"
    
    def _adv_str(self, string):
    
        var = f"""{self.eval}({self._protect(string, r=1)})"""
        if (string.replace('b','').replace('u','').replace('r','').replace('f','')[0] == '"' and string.split('"')[0].count('f') != 0) or (string.replace('b','').replace('u','').replace('r','').replace('f','')[0] == "'" and string.split("'")[0].count('f') != 0):
            return var, False
        return var, True

    def _underscore_int(self, string):
        # return string
        return '_'.join(str(string)).replace('-_','-').replace('+_','+')

    def RemoveComments(self):
        self.content = "".join(lin + '\n' for lin in self.content.splitlines() if lin.strip() and not lin.strip().startswith('#'))

    def CompressCode(self):
        content = self.content
        while True:
            for x in ('=','(',')','[',']','{','}','*','+','-','/',':','<','>',','):
                content = content.replace(f' {x}', x).replace(f'{x} ', x)
            if content == self.content:
                break
            self.content = content
    
    def CompressIndentations(self):
        ...

    def _get_indentations(self, lin):
        i = 0
        for x in lin:
            if x == ' ':
                i += 1
            else:
                break
        return i

    def _get_first_statement(self, lin):
        s = ''
        for x in lin.strip():
            if x.lower() in 'abcdefghijklmnopqrstuvwxyz':
                s += x
            else:
                break
        return s
    
    def _add_lambdas(self):
        for _ in range(10):
            lamb = self._randvar()
            arg = self._randvar()
            self.strings[lamb] = f'lambda {arg}:{self._randglob()}()'
            self.lambdas.append(lamb)

    def _fake_lin(self, indent):
        return f"{' ' * indent}if {choice(list(self.ostrings.keys()))}:\n{' ' * indent * 2 if indent else ' '}{choice(self.lambdas)}({choice(list(self.ostrings.keys()))})"
        
    def _get_chunks(self):
        chunks = []
        lines = self.content.splitlines()
        chunk = []
        for lin, nextlin in zip(lines, range(len(lines))):
            chunk.append(lin)
            if nextlin+1 == len(lines):
                break
            if (
                self._get_indentations(lines[nextlin+1]) == 0 and
                self._get_first_statement(lines[nextlin+1]) not in ('elif', 'else', 'except', 'finally') and
                lin.strip()[-1] != ','
            ):
                chunks.append('\n'.join(chunk))
                chunk = []
        if chunk:
            chunks.append('\n'.join(chunk))

        return chunks
    def _protect_var(self, var):
        return f"{self._randglob()}()[{self._protect(var)}]"

    def _compress(self, content):
        # content = "".join(chr(ord(char)+1) for char in content)
        return compress(content.encode('utf-8'))

    def _gen_var(self):
        var = choice(self._gen_vars)
        while var in self.gen:
            var = choice(self._gen_vars)
        self.gen.append(var)
        return var

    def _rand_type(self):
        return choice(('type', 'None', 'Ellipsis', 'True', 'False', 'str', 'int', 'float', 'bool'))
    
    def _rand_int(self):
        return randint(-100000, 100000)
    
    def _rand_op(self):
        return choice(('+', '-', '*', '/'))

    def _rand_pass(self, line = True):
        gen = self.gen
        a1 = f"{gen[0]}({gen[4]} = {self._rand_int()} {self._rand_op()} {self._rand_int()})"
        c1 = f"{gen[2]}({gen[7]} = {self._rand_int()} {self._rand_op()} {gen[10]}.{gen[3]})"
        c2 = f"{gen[1]}({gen[6]} = {gen[10]}.{gen[3]} {self._rand_op()} {self._rand_int()})"
        chosen = choice((
            f"{gen[10]}.{c1}",
            f"{gen[10]}.{c2}",
            f"{a1}.{c1}",
            f"{a1}.{c2}"
        ))
        return self._rand_line(chosen) if line else chosen

    def _rand_line(self, chosen):
        if randint(1, 2) == 1:
            return chosen
        c2 = self._rand_pass(line = False)
        final = f"""
if {self._rand_bool(False)}:
            {chosen}
        elif {self._rand_bool(True)}:
            {c2}
        """.strip()
        return final

    def _rand_bool(self, op):
        op = '<' if op == True else '>'
        return f"{randint(100000, 499999)} {op} {randint(500000, 9999999)}"


    def _split_content(self, content, n = 500):
        ncontent = []
        while content:
            if len(content) > n:
                ncontent.append(content[:n])
            else:
                ncontent.append(content)
                break
            content = content[n:]
        return ncontent

    def _rand_gen(self, ext, keys, gen, gen2, actions):
        return ' '.join([
                choice(keys),
                choice(
                ext
                ).replace('action2', ' '.join([gen2[randint(11, 17)], choice(actions), gen[randint(11, 17)]])).replace(
                    'var1', gen2[randint(11, 17)]
                ).replace(
                    'var2', choice(gen[11:17])
                ).replace(
                    'var3', gen2[randint(11, 17)]
                ).replace('action', ' '.join([gen[randint(11, 17)], choice(actions), gen[randint(11, 17)]])).replace(
                    'var1', gen2[randint(11, 17)]
                ).replace(
                    'var2', gen2[randint(11, 17)]
                ).replace(
                    'var3', gen2[randint(11, 17)]
                )
            ]).strip()
    
    def _rand_error(self):
        return choice((
            'OSError',
            'TypeError',
            'ArithmeticError',
            'AssertionError',
            'AttributeError'
        ))

    @property
    def _gen_vars(self):
        gen = [
            'MemoryAccess', 'StackOverflow', 'System',
            'Divide', 'Product', 'CallFunction',
            'Math', 'Calculate', 'Hypothesis',
            'Frame', 'DetectVar', 'Substract',
            'Theory', 'Statistics', 'Random',
            'Round', 'Absolute', 'Negative',
            'Algorithm', 'Run', 'Builtins',
            'Positive', 'Invert', 'Square',
            'Add', 'Multiply', 'Modulo',
            'Power', 'Floor', 'Ceil',
            'Cube', 'Walk', 'While',
        ]
        _gen = list(gen)
        gen.extend(f'_{g.lower()}' for g in _gen)
        return gen



    
from pystyle import *
from time import sleep, time
from getpass import getpass

text = f"""
██   █ ▄▄  ████▄ ▄█▄    ██   █    ▄█ █ ▄▄     ▄▄▄▄▀ ▄  █ ▄█ ▄█▄    
█ █  █   █ █   █ █▀ ▀▄  █ █  █    ██ █   █ ▀▀▀ █   █   █ ██ █▀ ▀▄  
█▄▄█ █▀▀▀  █   █ █   ▀  █▄▄█ █    ██ █▀▀▀      █   ██▀▀█ ██ █   ▀  
█  █ █     ▀████ █▄  ▄▀ █  █ ███▄ ▐█ █        █    █   █ ▐█ █▄  ▄▀ 
   █  █          ▀███▀     █     ▀ ▐  █      ▀        █   ▐ ▀███▀  
  █    ▀                  █            ▀             ▀             
 ▀                       ▀                                         """[:-1]

_banner = (text)

dark = Col.dark_gray
light = Col.light_gray
purple = Colors.StaticMIX((Col.purple, Col.blue))
bpurple = Colors.StaticMIX((Col.purple, Col.blue, Col.blue))

def p(text):
    # sleep(0.05)
    return print(text)

def stage(text: str, symbol: str = '...', col1=light, col2=None) -> str:
    if col2 is None:
        col2 = light if symbol == '...' else purple
    if symbol in {'...', '!!!'}:
        return f"""     {Col.Symbol(symbol, col1, dark)} {col2}{text}{Col.reset}"""
    else:
        return f""" {Col.Symbol(symbol, col1, dark)} {col2}{text}{Col.reset}"""

def main():
    System.Size(150, 47)
    System.Title("Apocalipthic")
    clear()
    print(_banner)
    file = input(stage(f"Drag the file you want to obfuscate {dark}->  {Col.reset}", "?", col2 = bpurple)).replace('"','').replace("'","")
    print('\n')


    try:
        with open(file, mode='rb') as f:
            script = f.read().decode('utf-8')
        filename = file.split('\\')[-1]
    except:
        input(f" {Col.Symbol('!', light, dark)} {Col.light_red}Invalid file!{Col.reset}")
        sys.exit()

    skiprenaming = input(stage(f"Skip the renaming of libraries and variables {dark}[{light}y{dark}/{light}n{dark}] ->  {Col.reset}", "?")).replace('"','').replace("'","") == 'y'
    print()
    skipchunks = input(stage(f"Skip the protection of chunks {dark}[{light}y{dark}/{light}n{dark}] ->  {Col.reset}", "?")).replace('"','').replace("'","") == 'y'

    renvars, renlibs = (False, False) if skiprenaming else (True, True)
    randlines, shell = (False, False) if skipchunks else (True, True)

    print('\n')

    now = time()
    Apoca__ = Apocalipthic(content=script, renvars = renvars, renlibs = renlibs, randlines = randlines, shell = shell)
    script = Apoca__.content
    now = round(time() - now, 2)

    with open(f'obf_{filename}', mode='w') as f:
        f.write(script)
    
    print(f"\n{P2}[{A2}?{P2}] {V2}Obfuscation completed succesfully in {P2}{now}s{V2}.\n{P2}[{A2}+{P2}] {V2}Obfuscation files are saved in {P2} obf_{filename}")
    sys.exit()
    # dire aussi l ancienne et nouvelle taille du fichier

if __name__ == '__main__':
    main()