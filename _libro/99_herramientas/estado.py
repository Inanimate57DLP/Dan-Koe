import re,glob,subprocess,sys
s=open('_libro/00_ESTADO.md').read()
done=sys.argv[1].split(',') if len(sys.argv)>1 else []
lines=[]
tot=0
for n in done:
    f=f'_libro/02_unidades/lote-{int(n):03d}.md'
    c=len(re.findall(r'^## U-',open(f).read(),re.M)); tot+=c
    lines.append(f'- lote-{int(n):03d}: {c} unidades ✔')
blk="## Fase 1 — lotes extraídos\n"+"\n".join(lines)+f"\n- **Total parcial:** {tot} unidades en {len(done)}/27 lotes\n"
s=re.sub(r'## Fase 1 — lotes extraídos\n.*?(?=\n## )',blk,s,flags=re.S)
h=subprocess.run(['git','log','-1','--format=%h %s'],capture_output=True,text=True).stdout.strip()
s=re.sub(r'- \*\*Último commit:\*\*.*',f'- **Último commit:** {h}',s)
s=re.sub(r'- \*\*Fase actual:\*\*.*',f'- **Fase actual:** Fase 1 en curso (extracción con subagentes, 4 en paralelo)',s)
open('_libro/00_ESTADO.md','w').write(s)
