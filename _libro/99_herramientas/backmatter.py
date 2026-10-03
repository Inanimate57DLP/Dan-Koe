import re,json,os,glob,collections,unicodedata
os.chdir('/home/user/Dan-Koe')
cl=json.load(open('_libro/02e_sintesis/clusters.json'))
chs=json.load(open('/tmp/claude-0/chapters.json'))
u2s={}
for ch in chs:
    for s in ch['sections']:
        for c in s['cids']:
            for u in cl[c]['ids']: u2s.setdefault(u,s['num'])
# headings in Spanish
sec_title={}
for f in sorted(glob.glob('_libro/09_capitulos_es/cap-*.md')):
    for l in open(f):
        m=re.match(r'^### (\d+\.\d+)\s+(.*)',l)
        if m: sec_title[m.group(1)]=f"{m.group(1)} {m.group(2).strip()}"
def link(num):
    t=sec_title.get(num)
    return f"[[#{t}|§{num}]]" if t else f"§{num}"
def secs_for(text):
    ids=re.findall(r'U-\d{3}-\d+',text)
    ss=sorted({u2s[i] for i in ids if i in u2s},key=lambda x:tuple(map(int,x.split('.'))))
    return ss
# ---- Glosario
lex=re.split(r'^(?=### )',open('_libro/03c_lexico.md').read(),flags=re.M)[1:]
gl=["## Glosario maestro\n","Todos los términos acuñados por Dan Koe y sus invitados, las palabras comunes que el autor usa con sentido propio, los términos de terceros que incorpora y los nombres de sus productos y frameworks. Para cada término: tipo, definición según el autor (una línea por versión cuando la definición cambia con el tiempo, con su fecha), quién lo acuñó, fechas de aparición, relación con otros términos y secciones del libro donde se desarrolla.\n"]
index_terms={}
letter=None
for e in lex:
    head=e.split('\n',1)[0][4:].strip()
    body=e.split('\n',1)[1] if '\n' in e else ''
    body=re.sub(r'^- \*\*IDs:\*\*.*\n?','',body,flags=re.M)
    body=re.sub(r'\s*\(?U-\d{3}-\d+(?:\s*[,;–-]\s*U-\d{3}-\d+)*\)?','',body)
    ss=secs_for(e)
    L=unicodedata.normalize('NFKD',head.strip('"“*`\'¿¡ ')[:1].upper()).encode('ascii','ignore').decode() or '#'
    if not L.isalpha(): L='#'
    if L!=letter: gl.append(f"\n### {L}\n"); letter=L
    gl.append(f"#### {head}\n"+body.rstrip()+("\n- **Se desarrolla en:** "+', '.join(link(s) for s in ss) if ss else '')+"\n")
    index_terms[head]=ss
open('_libro/10_es/glosario.md','w').write('\n'.join(gl))
# ---- Fuentes
src=open('_libro/03d_fuentes-citadas.md').read()
def repl_ids(m):
    ss=secs_for(m.group(0))
    return ('secciones '+', '.join(link(s) for s in ss)) if ss else ''
src2=re.sub(r'U-\d{3}-\d+(?:\s*(?:[,;y]|–|-)\s*U-\d{3}-\d+)*',repl_ids,src)
src2=re.sub(r'^#\s+03d.*\n','',src2,flags=re.M)
src2=re.sub(r'^# (.*)$',r'## \1',src2,count=1,flags=re.M)
src2=re.sub(r'\bbloques?\s+T\d+[ab]?(?:-[ab])?(?:\s*,\s*T\d+[ab]?(?:-[ab])?)*','',src2)
src2=re.sub(r'\*\*Bloques?:\*\*[^\n]*\n','',src2)
src2=re.sub(r'\*\*IDs?:\*\*\s*','**Secciones:** ',src2)
# demote headings so the appendix sits under level-2 heading
src2=re.sub(r'^(#{2,5}) ',lambda m:'#'*min(len(m.group(1))+1,6)+' ',src2,flags=re.M)
open('_libro/10_es/fuentes.md','w').write("## Fuentes y referentes del autor\n\n"+src2)
# ---- Índice analítico: términos del glosario + títulos de sección
idx=collections.defaultdict(set)
for t,ss in index_terms.items():
    for s in ss: idx[t].add(s)
for num,t in sec_title.items():
    title=t.split(' ',1)[1]
    idx[title].add(num)
def key(s): return unicodedata.normalize('NFKD',s.strip('"“*`\'¿¡ ').lower()).encode('ascii','ignore').decode()
ia=["## Índice analítico\n","Conceptos, frameworks, metodologías, términos y temas en orden alfabético, con enlaces a las secciones donde se desarrollan.\n"]
letter=None
for t in sorted(idx,key=key):
    ss=sorted(idx[t],key=lambda x:tuple(map(int,x.split('.'))))
    if not ss: continue
    L=key(t)[:1].upper() or '#'
    if not L.isalpha(): L='#'
    if L!=letter: ia.append(f"\n### {L}\n"); letter=L
    ia.append(f"- **{t}** — "+', '.join(link(s) for s in ss))
open('_libro/10_es/indice-analitico.md','w').write('\n'.join(ia)+'\n')
print('glosario',len(lex),'secciones con título ES',len(sec_title),'entradas índice',len(idx))
