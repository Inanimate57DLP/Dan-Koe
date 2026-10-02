import re,glob,json,os
os.chdir('/home/user/Dan-Koe')
units=[]
for f in sorted(glob.glob('_libro/02_unidades/lote-*.md')):
    t=open(f,encoding='utf-8').read()
    for b in re.split(r'^## (?=U-\d{3}-\d+)',t,flags=re.M)[1:]:
        uid=b.split('\n',1)[0].strip()
        g=lambda k:(re.search(r'^- \*\*'+k+r':\*\*\s*(.*)$',b,re.M) or [None,''])[1].strip()
        fu=g('fuente'); d=re.search(r'(20\d\d-\d\d-\d\d)',fu)
        units.append(dict(id=uid,tipo=g('tipo'),titulo=g('titulo'),terminos=g('terminos'),origen=g('origen'),nivel=g('nivel'),fecha=d.group(1) if d else '',words=len(b.split()),file=os.path.basename(f)))
json.dump(units,open('/tmp/claude-0/units.json','w'),ensure_ascii=False)
print(len(units))
