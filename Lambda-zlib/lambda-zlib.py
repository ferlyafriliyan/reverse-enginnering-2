import zlib


try:
  code='exec((lambda _____, ______ : ______(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))(\'\',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(_____),"<Ryougaa-Hideki","exec"))(%s,compile))'
  computer=0
  file=input('File : ')
  count=int(input('Count : '))
  if(count<300):
    out=input('Output : ')
    read1=open(file).read()
    repr1=repr(zlib.compress(read1.encode('utf-8')))
    new1=open(out, 'w')
    new1.write(code % repr1)
    new1.close()
    while(count>=computer):
      read2=open(out).read()
      repr2=repr(zlib.compress(read2.encode('utf-8')))
      new2=open(out, 'w')
      new2.write(code % repr2)
      new2.close()
      print('obfuscating file at {computer}')
      computer+=1
    print(f'encrypt success | file save as {out}')
except ValueError:
  print('Masukan angka di count')
except KeyboardInterrupt:
  print('\nDihentikan')
