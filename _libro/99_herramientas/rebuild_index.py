import re,glob,collections,unicodedata
gl=set(re.findall(r'^#### (.*)$',open('_libro/10_es/glosario.md').read(),flags=re.M))
idx=collections.defaultdict(set); old=0
for l in open('_libro/10_es/indice-analitico.md'):
    m=re.match(r'^- \*\*(.*)\*\* — (.*)$',l.rstrip())
    if not m: continue
    t=m.group(1); ss=re.findall(r'§(\d+\.\d+)',m.group(2))
    if t in gl: idx[t].update(ss)
    else: old+=1
rows={}
for l in open('_libro/08_lexico-traduccion.md'):
    if l.startswith('| ') and not l.startswith('| Término'):
        c=[x.strip() for x in l.strip().strip('|').split('|')]
        if len(c)>=5: rows[c[0].strip('*` ')]=c
added=0
for t in list(idx):
    r=rows.get(t)
    if r and r[2].startswith('traducir') and r[4] and r[4].lower()!=t.lower():
        idx[f'{r[4]} ({t})'].update(idx[t]); added+=1
for f in sorted(glob.glob('_libro/09_capitulos_es/cap-*.md')):
    for m in re.finditer(r'^### (\d+\.\d+)\s+(.*)$',open(f).read(),flags=re.M):
        idx[m.group(2).strip()].add(m.group(1))
def key(s): return unicodedata.normalize('NFKD',s.strip('"“*`\'¿¡ ').lower()).encode('ascii','ignore').decode()
ia=["## Índice analítico\n","Conceptos, frameworks, metodologías, términos y temas en orden alfabético, con enlaces a las secciones donde se desarrollan. Los términos que en este libro se traducen aparecen dos veces: en su forma española (con el original entre paréntesis) y en su forma original.\n"]
letter=None
for t in sorted(idx,key=key):
    ss=sorted(idx[t],key=lambda x:tuple(map(int,x.split('.'))))
    if not ss: continue
    L=key(t)[:1].upper() or '#'
    if not L.isalpha(): L='#'
    if L!=letter: ia.append(f"\n### {L}\n"); letter=L
    ia.append(f"- **{t}** — "+', '.join('§'+s for s in ss))
open('_libro/10_es/indice-analitico.md','w').write('\n'.join(ia)+'\n')
print('títulos viejos descartados',old,'términos ES añadidos',added,'entradas',len(idx))
