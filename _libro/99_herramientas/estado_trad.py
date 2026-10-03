import re,glob,os,subprocess
os.chdir('/home/user/Dan-Koe')
p='_libro/00_ESTADO.md'; s=open(p).read()
lines=[]
for f in sorted(glob.glob('_libro/09_capitulos_es/*.md')):
    w=len(re.sub(r'<!--.*?-->','',open(f).read(),flags=re.S).split())
    lines.append(f'- {os.path.basename(f)}: {w} palabras ✔')
blk='## Fase 7 — capítulos traducidos\n'+'\n'.join(lines)+f'\n- **Total:** {len(lines)}/43 archivos (40 capítulos + portada, mapa y notas)\n'
s=re.sub(r'## Fase 7 — capítulos traducidos\n.*?(?=\n## )',blk,s,flags=re.S)
h=subprocess.run(['git','log','-1','--format=%h %s'],capture_output=True,text=True).stdout.strip()
s=re.sub(r'- \*\*Último commit:\*\*.*',f'- **Último commit:** {h}',s)
open(p,'w').write(s)
