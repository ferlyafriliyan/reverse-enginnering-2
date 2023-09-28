import marshal
from os import system as autoclear
autoclear('clear')

try:
    file = input("Input File : ")
    total = int(input("Limit : "))

    if total < 101:
        out = input("Output File : ")
        xos = open(file).read()
        
        # Metode Marshal
        encoded_marshal = repr(marshal.dumps(compile(xos, '', 'exec')))
        
        with open(out, 'w') as w:
            w.write(f"import marshal\n")
            w.write(f"exec((lambda _ : (marshal.loads(_) if _ else None))({encoded_marshal}))")
            
        komter = 0
        while total >= komter:
            encoded_marshal = repr(marshal.dumps(compile(open(out).read(), '', 'exec')))
            with open(out, 'w') as w:
                w.write(f"import marshal\n")
                w.write(f"exec((lambda _ : (marshal.loads(_) if _ else None))({encoded_marshal}))")
            komter += 1
            print(f"\nSuccess Obfuscate File, File saved to : {out}")
            
        compiled_file = file.replace('.py', '_.py')
        with open(compiled_file, 'wb') as compiled:
            compiled.write(marshal.dumps(compile(open(out).read(), '', 'exec')))
        print(f"Compiled file saved to: {compiled_file}")
        
        # Evaluasi kode yang telah di-compile
        eval(compile(open(compiled_file).read(), '', 'exec'))
            
        exit(f"Limit Max > {total} 101")
except Exception as e:
    print(f"Error: {str(e)}")
