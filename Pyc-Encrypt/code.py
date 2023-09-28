import os, sys, zlib, base64, marshal, binascii, time, py_compile;from time import sleep as waktu;from random import randint;import time
cout = 0
p, m, i, b, k, cg, ba, pu, gr, pb = '\x1b[0m', '\x1b[31m', '\x1b[32m', '\x1b[34m', '\x1b[33;1m', '\x1b[36m', '\x1b[96;1m', '\x1b[35m', '\x1b[37m', '\x1b[47m'
def ArielSandyPermana(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1.0 / 10)

os.system('clear')
def main():
    global bin
    global cout
    p, m, i, b, k, cg, ba, pu, gr, pb = '\x1b[0m', '\x1b[31m', '\x1b[32m', '\x1b[34m', '\x1b[33;1m', '\x1b[36m', '\x1b[96;1m', '\x1b[35m', '\x1b[37m', '\x1b[47m'
    try:
        lis = 'KONTOLIVO'
        print lis + '\n\x1b[31m[ \x1b[32m01 \x1b[31m]\x1b[0m Compile Marshal\n\x1b[31m[ \x1b[32m02 \x1b[31m]\x1b[0m Compile Marshal > base64\x1b[0m\n\x1b[31m[ \x1b[32m03 \x1b[31m]\x1b[0m Compile Marshal > base64 > pycom\n\x1b[31m\x1b[31m[ \x1b[32m04 \x1b[31m]\x1b[0m Compile By Tegar 2\n\x1b[31m[ \x1b[32m05 \x1b[31m]\x1b[0m Compile By Tegar 3\n\x1b[31m[ \x1b[32m06 \x1b[31m]\x1b[0m Compile By Tegar 4\n\x1b[31m[ \x1b[32m07 \x1b[31m]\x1b[0m Compile Zlib\n\x1b[31m[ \x1b[32m08 \x1b[31m]\x1b[0m Compile Base64\n\x1b[31m[ \x1b[32m09 \x1b[31m]\x1b[0m Compile Base16\n\x1b[31m[ \x1b[32m10 \x1b[31m]\x1b[0m Compile Base32\n\x1b[31m[ \x1b[32m11 \x1b[31m]\x1b[0m Compile Base64&marshal\n\x1b[31m[ \x1b[32m12 \x1b[31m]\x1b[0m Compile By Tegar 5\n\x1b[31m[ \x1b[32m12 \x1b[31m]\x1b[0m Pyc EDIT PESAN\n\x1b[31m[ \x1b[33m00 \x1b[31m]\x1b[0m \x1b[32mExit \x1b[0m\x1b[31m\x1b[0m\x1b[31m\x1b[0m\n'
        chos = raw_input('[!] Pilih >> %s' % i)
        if chos == '1' or chos == '01':
            file = raw_input('%s[%s\xe2\x9b\xa5%s] %sFile >> %s' % (b, i, b, gr, i))
            cot = int(raw_input('%s[%s\xe2\x9b\xa5%s] %sMau Berapa Lapis >> %s' % (b, m, b, gr, i)))
            if cot < 500000:
                out = file.replace('.py', '') + '_.py'
                oa = open(file).read()
                ni = compile(oa, '<Kontolivo>', 'exec')
                bo = marshal.dumps(ni)
                ab = repr(bo)
                s = open(out, 'w')
                s.write('#Decrypt by : Ferly Afriliyan\nimport marshal\nexec(marshal.loads(' + str(ab) + '))')
                s.close()
                while True:
                    if cot >= cout:
                        nz = open(out).read()
                        dn = compile(nz, '<Kontolivo>', 'exec')
                        bx = marshal.dumps(dn)
                        nl = repr(bx)
                        ns = open(out, 'w')
                        ns.write('#Decrypt by : Ferly Afriliyan\nimport marshal\nexec(marshal.loads(' + str(nl) + '))')
                        ns.close()
                        cout += 1
                        continue
                    break

                print '\x1b[34m[\x1b[31m!\x1b[34m] \x1b[37mDone Di Simpan \x1b[32m[ \x1b[37m%s \x1b[32m] \x1b[37m!' % out
                exit();time.sleep(0.1)
            else:
                print '%s[%s+%s] %sCout Terlalu Besar \xe2\x9d\x97' % (b, m, b, gr)
                waktu(0.8)
                main()
        elif chos == '2' or chos == '02':
            file = raw_input('%s[%s\xe2\x9b\xa5%s] %sFile >> %s' % (b, i, b, gr, i))
            cot = int(raw_input('%s[%s\xe2\x9b\xa5%s] %sMau Berapa Lapis >> %s' % (b, m, b, gr, i)))
            if cot < 500000:
                out = file.replace('.py', '') + '_.py'
                oa = open(file).read()
                ni = compile(oa, '<Kontolivo>', 'exec')
                bo = marshal.dumps(ni)
                ab = repr(bo)
                s = open(out, 'w')
                s.write('#Decrypt by : Ferly Afriliyan\nimport marshal\nexec(marshal.loads(' + str(ab) + '))')
                s.close()
                while True:
                    if cot >= cout:
                        nz = open(out).read()
                        dn = compile(nz, '<Kontolivo>', 'exec')
                        bx = marshal.dumps(dn)
                        nl = repr(bx)
                        ns = open(out, 'w')
                        ns.write('#Decrypt by : Ferly Afriliyan\nimport marshal\nexec(marshal.loads(' + str(nl) + '))')
                        ns.close()
                        cout += 1
                        continue
                    break

                mx = open(out).read()
                nl = base64.b32encode(mx)
                xn = open(out, 'w')
                xn.write("#Decrypt by : Ferly Afriliyan\nimport base64\nexec(base64.b32decode('%s'))\n" % nl)
                xn.close()
                print '\x1b[34m[\x1b[31m!\x1b[34m] \x1b[37mDone Di Simpan \x1b[32m[ \x1b[37m%s \x1b[32m] \x1b[37m!' % out
                exit();time.sleep(0.1)
            else:
                print '%s[%s+%s] %sCout Terlalu Besar \xe2\x9d\x97' % (b, m, b, gr)
                waktu(0.8)
                main()
        elif chos == '3' or chos == '03':
            file = raw_input('%s[%s\xe2\x9b\xa5%s] %sFile >> %s' % (b, i, b, gr, i))
            cot = int(10)
            if cot < 40000:
                out = file.replace('.py', '') + '_.py'
                oa = open(file).read()
                ni = compile(oa, '<Kontolivo>', 'exec')
                bo = marshal.dumps(ni)
                ab = repr(bo)
                s = open(out, 'w')
                s.write('#Decrypt by : Ferly Afriliyan\nimport marshal\nexec(marshal.loads(' + str(ab) + '))')
                s.close()
                while True:
                    if cot >= cout:
                        nz = open(out).read()
                        dn = compile(nz, '<Kontolivo>', 'exec')
                        bx = marshal.dumps(dn)
                        nl = repr(bx)
                        ns = open(out, 'w')
                        ns.write('#Decrypt by : Ferly Afriliyan\nimport marshal\nexec(marshal.loads(' + str(nl) + '))')
                        ns.close()
                        cout += 1
                        continue
                    break

                mx = open(out).read()
                nl = base64.b32encode(mx)
                xn = open(out, 'w')
                xn.write("#Coded By Ferly Afriliyan\nimport base64\nexec(base64.b32decode('%s'))\n" % nl)
                xn.close()
                print '\x1b[34m[\x1b[31m!\x1b[34m] \x1b[37mDone Di Simpan \x1b[32m[ \x1b[37m%s \x1b[32m] \x1b[37m!' % out
                exit();time.sleep(0.1)
        elif chos == '4' or chos == '04':
            ia = raw_input('%s[%s\xe2\x9b\xa5%s] %sFile >> %s' % (b, i, b, gr, i))
            a = open(ia).read()
            z = []
            u = []
            for x in a:
                z.append(ord(x))

            for c in z:
                u.append(zlib.compress(str(c)))

            o = []
            for p in u:
                o.append(marshal.dumps(p))

            fip = ('import marshal;import zlib\nd={}\nexec("".join([chr(int(zlib.decompress(marshal.loads(i)))) for i in d]))').format(o)
            js = ia.replace('.py', '_.py')
            ox = open(js, 'w')
            ox.write(fip)
            ox.close()
            bx = open(js).read()
            xs = binascii.hexlify(bx)
            fc = ('exec ("{}").decode("hex")').format(xs)
            nk = open(js, 'w')
            nk.write(fc)
            nk.close()
            py_compile.compile(js)
            os.system('rm ' + js)
            print '\x1b[34m[\x1b[31m!\x1b[34m] \x1b[37mDone Di Simpan \x1b[32m[ \x1b[37m%s \x1b[32m] \x1b[37m!' % js
            exit();time.sleep(0.1)
        elif chos == '5' or chos == '05':
            ia = raw_input('%s[%s\xe2\x9b\xa5%s] %sFile >> %s' % (b, i, b, gr, i))
            bc = open(ia).read()
            xs = binascii.hexlify(bc)
            js = ia.replace('.py', '_.py')
            fc = ('exec ("{}").decode("hex")').format(xs)
            nk = open(js, 'w')
            nk.write(fc)
            nk.close()
            p = []
            n = []
            gn = open(js).read()
            for l in gn:
                p.append(ord(l))

            for b in p:
                n.append('x' * b)

            fin = ('d={}\nexec("".join([chr(len(i)) for i in d]))').format(n)
            bp = open(js, 'w')
            bp.write(fin)
            bp.close()
            py_compile.compile(js)
            os.system('rm ' + js)
            print '\x1b[34m[\x1b[31m!\x1b[34m] \x1b[37mDone Di Simpan \x1b[32m[ \x1b[37m%sc \x1b[32m] \x1b[37m!' % js
            exit();time.sleep(0.1)
        elif chos == '6' or chos == '06':
            file = raw_input('%s[%s\xe2\x9b\xa5%s] %sFile >> %s' % (b, i, b, gr, i))
            cot = int(raw_input('%s[%s\xe2\x9b\xa5%s] %sMau Berapa Lapis >> %s' % (b, m, b, gr, i)))
            if cot < 500000:
                out = file.replace('.py', '') + '_.py'
                oa = open(file).read()
                xs = zlib.compress(oa)
                s = open(out, 'w')
                s.write('#Decrypt by : Ferly Afriliyan\nimport zlib\nexec(zlib.decompress(' + repr(xs) + '))')
                s.close()
                while True:
                    if cot >= cout:
                        nz = open(out).read()
                        ci = zlib.compress(nz)
                        ns = open(out, 'w')
                        ns.write('#Decrypt by : Ferly Afriliyan\nimport zlib\nexec(zlib.decompress(' + repr(ci) + '))')
                        ns.close()
                        cout += 1
                        continue
                    break

                print '\x1b[34m[\x1b[31m!\x1b[34m] \x1b[37mDone Di Simpan \x1b[32m[ \x1b[37m%s \x1b[32m] \x1b[37m!' % out
                raw_input('%s[%s\xe2\x9d\x97%s] %sBack %s\xe2\x9e\xa4 %s' % (b, m, b, gr, i, cg))
                exit();time.sleep(0.1)
            else:
                print '%s[%s+%s] %sCout Terlalu Besar \xe2\x9d\x97' % (b, m, b, gr)
                waktu(0.8)
                main()
        elif chos == '7' or chos == '07':
            file = raw_input('%s[%s\xe2\x9b\xa5%s] %sFile >> %s' % (b, i, b, gr, i))
            cot = int(raw_input('%s[%s\xe2\x9b\xa5%s] %sMau Berapa Lapis >> %s' % (b, m, b, gr, i)))
            if cot < 500000:
                out = file.replace('.py', '') + '_.py'
                oa = open(file).read()
                xs = base64.b64encode(oa)
                s = open(out, 'w')
                s.write('#Decrypt by : Ferly Afriliyan\nimport base64\nexec(base64.b64decode("' + xs + '"))')
                s.close()
                while True:
                    if cot >= cout:
                        nz = open(out).read()
                        ci = base64.b64encode(nz)
                        ns = open(out, 'w')
                        ns.write('#Decrypt by : Ferly Afriliyan\nimport base64\nexec(base64.b64decode("' + ci + '"))')
                        ns.close()
                        cout += 1
                        continue
                    break

                print '\x1b[34m[\x1b[31m!\x1b[34m] \x1b[37mDone Di Simpan \x1b[32m[ \x1b[37m%s \x1b[32m] \x1b[37m!' % out
                exit();time.sleep(0.1)
        elif chos == '8' or chos == '08':
            file = raw_input('%s[%s\xe2\x9b\xa5%s] %sFile >> %s' % (b, i, b, gr, i))
            cot = int(raw_input('%s[%s\xe2\x9b\xa5%s] %sMau Berapa Lapis >> %s' % (b, m, b, gr, i)))
            if cot < 500000:
                out = file.replace('.py', '') + '_.py'
                oa = open(file).read()
                xs = base64.b16encode(oa)
                s = open(out, 'w')
                s.write('#Decrypt by : Ferly Afriliyan\nimport base64\nexec(base64.b16decode("' + xs + '"))')
                s.close()
                while True:
                    if cot >= cout:
                        nz = open(out).read()
                        ci = base64.b16encode(nz)
                        ns = open(out, 'w')
                        ns.write('#Decrypt by : Ferly Afriliyan\nimport base64\nexec(base64.b16decode("' + ci + '"))')
                        ns.close()
                        cout += 1
                        continue
                    break

                print '\x1b[34m[\x1b[31m!\x1b[34m] \x1b[37mDone Di Simpan \x1b[32m[ \x1b[37m%s \x1b[32m] \x1b[37m!' % out
                exit();time.sleep(0.1)
        elif chos == '9' or chos == '09':
            file = raw_input('%s[%s\xe2\x9b\xa5%s] %sFile >> %s' % (b, i, b, gr, i))
            cot = int(raw_input('%s[%s\xe2\x9b\xa5%s] %sMau Berapa Lapis >> %s' % (b, m, b, gr, i)))
            if cot < 500000:
                out = file.replace('.py', '') + '_.py'
                oa = open(file).read()
                xs = base64.b32encode(oa)
                s = open(out, 'w')
                s.write('#Decrypt by : Ferly Afriliyan\nimport base64\nexec(base64.b32decode("' + xs + '"))')
                s.close()
                while True:
                    if cot >= cout:
                        nz = open(out).read()
                        ci = base64.b32encode(nz)
                        ns = open(out, 'w')
                        ns.write('#Decrypt by : Ferly Afriliyan\nimport base64\nexec(base64.b32decode("' + ci + '"))')
                        ns.close()
                        cout += 1
                        continue
                    break

                print '\x1b[34m[\x1b[31m!\x1b[34m] \x1b[37mDone Di Simpan \x1b[32m[ \x1b[37m%s \x1b[32m] \x1b[37m!' % out
                exit();time.sleep(0.1)
        elif chos == '10':
            file = raw_input('%s[%s\xe2\x9b\xa5%s] %sFile >> %s' % (b, i, b, gr, i))
            cot = int(raw_input('%s[%s\xe2\x9b\xa5%s] %sMau Berapa Lapis >> %s' % (b, m, b, gr, i)))
            if cot < 500000:
                out = file.replace('.py', '') + '_.py'
                oa = open(file).read()
                cpa = compile(oa, '<Kontolivo>', 'exec')
                cotn = marshal.dumps(cpa)
                xs = base64.b64encode(cotn)
                s = open(out, 'w')
                s.write('#Decrypt by : Ferly Afriliyan\nimport base64\nimport marshal\nexec marshal.loads(base64.b64decode("' + xs + '"))')
                s.close()
                while True:
                    if cot >= cout:
                        nz = open(out).read()
                        ci = base64.b32encode(nz)
                        ns = open(out, 'w')
                        ns.write('#Decrypt by : Ferly Afriliyan\nimport base64\nimport marshal\nexec marshal.loads(base64.b64decode("' + ci + '"))')
                        ns.close()
                        cout += 1
                        continue
                    break

                print '\x1b[34m[\x1b[31m!\x1b[34m] \x1b[37mDone Di Simpan \x1b[32m[ \x1b[37m%s \x1b[32m] \x1b[37m!' % out
                exit();time.sleep(0.1)
        elif chos == '11':
            file = raw_input('%s[%s\xe2\x9b\xa5%s] %sFile >> %s' % (b, i, b, gr, i))
            notes = raw_input('%s[%s\xe2\x9b\xa5%s] %sMasukan Pesan nya >> %s' % (b, i, b, gr, i))
            js = file.replace('.py', '_.py')
            py_compile.compile(file)
            gb = open(file + 'c').read()
            bi = open(js, 'w')
            bi.write(gb + '\n\n\n\t' + notes)
            bi.close()
            os.system('rm ' + file + 'c')
            print '\x1b[34m[\x1b[31m!\x1b[34m] \x1b[37mDone Di Simpan \x1b[32m[ \x1b[37m%s \x1b[32m] \x1b[37m!' % js
            exit()
        elif chos == '0' or chos == '00' or chos == '0' or chos == '00' or chos == '0' or chos == '00':
            sys.exit()
        else:
            print '%s[%s!%s] %sWrong Input !' % (b, m, b, gr)
            waktu(0.5)
            main()
    except KeyboardInterrupt:
        print '%s[%s!%s] %sCtrl+C not Working Pliss ctr+d !' % (b, m, b, gr)
        waktu(0.5)
        main()
    except EOFError:
        sys.exit()
    except IOError:
        print '%s[%s\xe2\x9d\x97%s] %sFile Tidak Di Temukan !' % (b, m, b, gr)
        waktu(0.5)
        main()
    except ValueError:
        print '%s[%s!%s] %sCout Berupa Angka ! ' % (b, m, b, gr)
main()