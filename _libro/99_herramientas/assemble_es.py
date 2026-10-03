import re,os,glob,unicodedata
os.chdir('/home/user/Dan-Koe')
parts=[("I","El diagnóstico: la Matrix y el camino por defecto",1,2),("II","La identidad: quién crees ser y cómo cambia",3,4),
("III","La mente como sistema: entropía, atención y metas",5,6),("IV","Dirección: anti-visión, visión, metas, propósito y el juego",7,10),
("V","Autogobierno: dopamina, trabajo enfocado, descanso y rutinas",11,13),("VI","Aprender y pensar",14,18),
("VII","Tú eres el nicho",19,20),("VIII","Escribir: la habilidad base",21,24),("IX","Audiencia, crecimiento y marca",25,27),
("X","El negocio de una persona",28,30),("XI","Valor, persuasión y producto",31,33),("XII","Dinero, agencia y la economía del individuo",34,36),
("XIII","Casos y límites",37,37),("XIV","Niveles de consciencia y sentido",38,40)]
D='_libro/09_capitulos_es/'
strip=lambda t: re.sub(r'<!--.*?-->','',t,flags=re.S).rstrip()+'\n'
front=strip(open(D+'00_title_description.md').read())
mapa=strip(open(D+'01_map_of_the_discipline.md').read())
notes=strip(open(D+'99_notes_on_the_corpus.md').read())
body=[]
for r,t,a,b in parts:
    body.append(f'# Parte {r} — {t}\n')
    for n in range(a,b+1): body.append(strip(open(D+f'cap-{n:02d}.md').read()))
body='\n'.join(body)
gl=open('_libro/10_es/glosario.md').read(); fu=open('_libro/10_es/fuentes-limpio.md').read(); ia=open('_libro/10_es/indice-analitico.md').read()
# map section numbers to headings
sec={}
for l in body.splitlines():
    m=re.match(r'^### (\d+\.\d+)\s+(.*)',l)
    if m: sec[m.group(1)]=f"{m.group(1)} {m.group(2).strip()}"
def fix_links(txt):
    txt=re.sub(r'\[\[#[^\]|]*\|§(\d+\.\d+)\]\]',lambda m:'§'+m.group(1),txt)
    return re.sub(r'(?<![\[#|\w])§(\d+\.\d+)',lambda m: f"[[#{sec[m.group(1)]}|§{m.group(1)}]]" if m.group(1) in sec else '§'+m.group(1),txt)
back='# Material de consulta\n\n'+gl.rstrip()+'\n\n'+fu.rstrip()+'\n\n'+ia.rstrip()+'\n\n'+notes
mapa=fix_links(mapa); body=fix_links(body); back=fix_links(back)
# TOC
toc=['## Índice\n']
def tl(h): return f"[[#{h}]]"
for l in (mapa+'\n'+body+'\n'+back).splitlines():
    m=re.match(r'^(#{1,3}) (.*)',l)
    if not m: continue
    lvl=len(m.group(1)); h=m.group(2).strip()
    if h in ('Ejercicios',) or re.fullmatch(r'[A-Z#]',h): continue
    if lvl==3 and not re.match(r'\d+\.\d+',h) and not h.startswith('('): continue
    toc.append('  '*(lvl-1)+'- '+tl(h))
out=front+'\n'+'\n'.join(toc)+'\n\n'+mapa+'\n'+body+'\n'+back
open('Dan Koe - Libro Maestro.md','w').write(out)
heads=set(re.findall(r'^#{1,6} (.*)$',out,flags=re.M))
links=re.findall(r'\[\[#([^\]|]+)',out)
bad=[x for x in links if x.strip() not in heads]
print('palabras',len(out.split()),'secciones',len(sec),'enlaces',len(links),'rotos',len(bad),bad[:5])
