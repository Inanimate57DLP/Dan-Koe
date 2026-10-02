import re,json,os,pickle
os.chdir('/home/user/Dan-Koe')
cl=json.load(open('_libro/02e_sintesis/clusters.json'))
chapters=json.load(open('/tmp/claude-0/chapters.json'))
th,blocks=pickle.load(open('/tmp/claude-0/th.pkl','rb'))
fus=open('_libro/02e_sintesis/fusiones-todo.txt').read().splitlines()
def entries(path,hdr):
    t=open(path,encoding='utf-8').read()
    parts=re.split(hdr,t,flags=re.M)
    return [p for p in parts[1:]]
lex=re.split(r'^(?=### )',open('_libro/03c_lexico.md').read(),flags=re.M)[1:]
src=re.split(r'^(?=#{3,4} )',open('_libro/03d_fuentes-citadas.md').read(),flags=re.M)[1:]
evo=re.split(r'^(?=#{2,4} .*EV-\d+|\*\*EV-\d+|#{2,4} EV-)',open('_libro/03b_evolucion.md').read(),flags=re.M)[1:]
os.makedirs('_libro/04b_material',exist_ok=True)
stats=[]
for ch in chapters:
    ids=set();out=[]
    out.append(f"# Material del Capítulo {ch['n']} — {ch['title']}\n\nEste archivo reúne TODO el material obligatorio del capítulo, ordenado por sección y clúster según `_libro/04_arquitectura.md`. Las unidades aparecen completas (copiadas de `_libro/02_unidades/`).\n")
    for s in ch['sections']:
        out.append(f"\n# SECCIÓN {s['num']} — {s['title']}\n")
        for c in s['cids']:
            if c not in cl: continue
            d=cl[c]; ids|=set(d['ids'])
            fl=[l for l in fus if any(i in l for i in d['ids'])]
            out.append(f"\n## CLÚSTER {c}: {d['name']}\n- idea: {d['idea']}\n- nivel: {d['nivel']}\n- evolución: {d['evol']}\n- fusiones (unidades sustancialmente idénticas; usa la unión de su contenido): {' ; '.join(fl) if fl else 'ninguna'}\n")
            for u in d['ids']: out.append(blocks[u].replace('## U-','### U-',1)+'\n')
    rx=lambda e: set(re.findall(r'U-\d{3}-\d+',e))&ids
    le=[e for e in lex if rx(e)]; se=[' '.join(e.split()[:160])+(' […]' if len(e.split())>160 else '')+'\n' for e in src if rx(e)]; ee=[e for e in evo if rx(e)]
    out.append("\n# ANEXO A — Entradas de evolución relevantes (extracto de `_libro/03b_evolucion.md`)\n\n"+('\n'.join(ee) if ee else 'ninguna\n'))
    out.append("\n# ANEXO B — Entradas del léxico relevantes (extracto de `_libro/03c_lexico.md`)\n\n"+'\n'.join(le))
    out.append("\n# ANEXO C — Fuentes de terceros relevantes (extracto de `_libro/03d_fuentes-citadas.md`)\n\n"+'\n'.join(se))
    fn=f"_libro/04b_material/cap-{ch['n']:02d}.md"
    txt='\n'.join(out); open(fn,'w').write(txt)
    stats.append((ch['n'],len(ids),len(txt.split()),len(ee),len(le),len(se)))
    ch['ids']=sorted(ids)
json.dump(chapters,open('/tmp/claude-0/chapters.json','w'),ensure_ascii=False)
for s in stats: print(s)
