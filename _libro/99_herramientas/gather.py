import re,glob,os,json,collections
os.chdir('/home/user/Dan-Koe')
files=sorted(glob.glob('_libro/02d_consolidacion/T*.md'))
def section(t,name):
    m=re.search(r'^## '+name+r'.*?$(.*?)(?=^## |\Z)',t,re.M|re.S)
    return m.group(1).strip() if m else ''
cat=[];evo=[];lex=[];src=[];res=[];puen=[];clmap={};fus=[]
for f in files:
    k=os.path.basename(f)[:-3]; t=open(f,encoding='utf-8').read()
    res.append(f'### {k}\n'+section(t,'Resumen'))
    puen.append(f'### {k}\n'+section(t,'Puentes'))
    evo.append(f'## Bloque {k}\n'+section(t,'Evoluci'))
    for l in section(t,'L[ée]xico').splitlines():
        if l.startswith('|') and not re.match(r'\|\s*-',l) and 'Término (tal cual)' not in l: lex.append(l.rstrip()+f' {k} |')
    for l in section(t,'Fuentes de terceros').splitlines():
        if l.startswith('|') and not re.match(r'\|\s*-',l) and 'Fuente (persona' not in l: src.append(l.rstrip()+f' {k} |')
    for l in section(t,'Fusiones').splitlines():
        if l.startswith('FUSION'): fus.append(l)
    for b in re.split(r'^### (?=C-)',section(t,'Cl[uú]steres'),flags=re.M)[1:]:
        head=b.split('\n',1)[0].strip()
        cid=head.split(':')[0].strip(); name=head.split(':',1)[1].strip() if ':' in head else ''
        g=lambda key:(re.search(r'^- \*\*'+key+r':\*\*\s*(.*)$',b,re.M) or [None,''])[1].strip()
        ids=re.findall(r'U-\d{3}-\d+',g('ids'))
        clmap[cid]=dict(name=name,bloque=k,nivel=g('nivel'),idea=g('idea'),depende=g('depende_de'),ids=ids,evol=g('evolucion'))
json.dump(clmap,open('_libro/02e_sintesis/clusters.json','w'),ensure_ascii=False,indent=0)
with open('_libro/02e_sintesis/catalogo-clusters.md','w') as o:
    o.write('# Catálogo compacto de clústeres (de 02d_consolidacion)\n\nFormato: ID | nombre | nivel | nº unidades | idea | depende de\n\n')
    for cid,c in clmap.items(): o.write(f"- **{cid}** | {c['name']} | {c['nivel']} | {len(c['ids'])} u. | {c['idea']} | dep: {c['depende']}\n")
open('_libro/02e_sintesis/resumenes-y-puentes.md','w').write('# Resúmenes de bloque\n\n'+'\n\n'.join(res)+'\n\n# Puentes\n\n'+'\n\n'.join(puen))
open('_libro/02e_sintesis/evolucion-todo.md','w').write('# Evolución y tensiones (todos los bloques)\n\n'+'\n\n'.join(evo))
lex.sort(key=lambda l:l.split('|')[1].strip().strip('*"“').lower())
open('_libro/02e_sintesis/lexico-todo.md','w').write('| Término | Definición | Acuñado por | IDs | Fechas | Relación | Bloque |\n|---|---|---|---|---|---|---|\n'+'\n'.join(lex))
src.sort(key=lambda l:l.split('|')[1].strip().lower())
open('_libro/02e_sintesis/fuentes-todo.md','w').write('| Fuente | Idea | Uso/adaptación | IDs | Bloque |\n|---|---|---|---|---|\n'+'\n'.join(src))
open('_libro/02e_sintesis/fusiones-todo.txt','w').write('\n'.join(fus))
allids=[i for c in clmap.values() for i in c['ids']]
u=json.load(open('/tmp/claude-0/units.json'))
print('files',len(files),'clusters',len(clmap),'ids',len(allids),'unique',len(set(allids)),'missing',len(set(x['id'] for x in u)-set(allids)),'lex',len(lex),'src',len(src),'fus',len(fus))
