import sys, argparse, marshal, zlib, base64, codecs, binascii

try:
    file = input("Input File : ")
    total = int(input("Limit : "))
    
    if total < 101:
        out = input("Output File : ")
        xos = open(file).read()
        
        # Metode Marshal
        encoded_marshal = repr(marshal.dumps(xos))
        
        with open(out, 'w') as w:
            w.write(f"import marshal\n")
            w.write(f"exec((lambda _ : (marshal.loads(_) if _ else None))({encoded_marshal}))")
            
        komter = 0
        while total >= komter:
            encoded_marshal = repr(marshal.dumps(open(out).read()))
            with open(out, 'w') as w:
                w.write(f"import marshal\n")
                w.write(f"exec((lambda _ : (marshal.loads(_) if _ else None))({encoded_marshal}))")
            komter += 1
            print(f"\nSuccess Obfuscate File, File saved to : {out}")
            
        exit(f"Limit Max > {total} 101")
except Exception as e:
    print(f"Error: {str(e)}")
