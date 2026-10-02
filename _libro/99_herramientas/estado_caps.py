import re,glob,os,subprocess
os.chdir('/home/user/Dan-Koe')
p='_libro/00_ESTADO.md'; s=open(p).read()
lines=[]
for f in sorted(glob.glob('_libro/05_capitulos_en/cap-*.md')):
    t=open(f).read()
    if '<!-- COBERTURA' not in t: continue
    w=len(re.sub(r'<!--.*?-->','',t,flags=re.S).split())
    n=len(set(re.findall(r'U-\d{3}-\d+',t.split('<!-- COBERTURA')[-1])))
    lines.append(f'- {os.path.basename(f)}: {w} palabras, {n} IDs en COBERTURA ✔')
blk='## Fase 4 — capítulos escritos\n'+'\n'.join(lines)+f'\n- **Total:** {len(lines)}/40 capítulos\n'
s=re.sub(r'## Fase 4 — capítulos escritos\n.*?(?=\n## )',blk,s,flags=re.S)
s=re.sub(r'- \*\*Fase actual:\*\*.*',f'- **Fase actual:** Fase 4 en curso — redacción de capítulos en inglés ({len(lines)}/40), 3 subagentes en paralelo; instrucciones en /tmp (regenerables con los scripts descritos en Notas).',s)
h=subprocess.run(['git','log','-1','--format=%h %s'],capture_output=True,text=True).stdout.strip()
s=re.sub(r'- \*\*Último commit:\*\*.*',f'- **Último commit:** {h}',s)
open(p,'w').write(s)
