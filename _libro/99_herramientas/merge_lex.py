import re,glob,os,collections,unicodedata
os.chdir('/home/user/Dan-Koe')
rows=[]
for f in sorted(glob.glob('_libro/08_partes/lexico-traduccion-*.md')):
    for l in open(f,encoding='utf-8'):
        if not l.startswith('| ') or l.startswith('| Término original') or re.match(r'\|\s*-',l): continue
        c=[x.strip() for x in l.strip().strip('|').split('|')]
        if len(c)<6: c+=['']*(6-len(c))
        rows.append(c[:6])
# overrides para palabras comunes
ov={'goal':'meta','identity':'identidad','focus':'foco','luck':'suerte','distribution':'distribución','attention':'atención','value':'valor','mind':'mente','game':'juego','habit':'hábito','skill':'habilidad','problem':'problema','purpose':'propósito','goals':'metas','leverage':'apalancamiento','alignment':'alineación','character':'personaje','culture':'cultura','expectation':'expectativa','force':'fuerza','frame':'marco','intention':'intención','lenses':'lentes','perspective':'perspectiva','polarity':'polaridad','rules':'reglas','dissonance':'disonancia','generalist':'generalista','builder':'constructor','elements':'elementos','channels':'canales','nodes':'nodos','residue':'residuo','toolbox':'caja de herramientas','gravity':'gravedad','filtration':'filtración','commodity':'commodity','influencer':'influencer','copywriting':'copywriting'}
n_ov=0
for r in rows:
    t=r[0].strip('*` ').lower()
    if t in ov:
        r[2]='traducir'; r[3]=ov[t]; r[4]=ov[t]; r[5]=(r[5]+' — Regla general: palabra común; se traduce con forma fija y su sentido propio se explica en el texto.').strip(' —'); n_ov+=1
for r in rows:
    if 'schwartz' in ' '.join(r).lower() or r[0].lower().startswith('levels of awareness'): continue
    for i in (3,4):
        r[i]=r[i].replace('conciencia','consciencia').replace('Conciencia','Consciencia').replace('conscconsciencia','consciencia')
norm=lambda s: unicodedata.normalize('NFKD',s.lower()).encode('ascii','ignore').decode().strip(' *`"')
by=collections.defaultdict(list)
for r in rows:
    if r[4]: by[norm(r[4])].append(r[0])
dups={k:v for k,v in by.items() if len(set(norm(x) for x in v))>1}
hdr="""# 08 — Léxico de traducción (vinculante)

Glosario de traducción bloqueado antes de traducir. Es vinculante para todos los capítulos.

## Reglas generales
1. **Términos acuñados** por el autor o sus invitados, nombres de frameworks, productos y fórmulas de marca: se **conservan en inglés**. Primera aparición en cada capítulo: `término original (traducción)`; después, el término original.
2. **Solo se conservan en inglés los términos que figuran como entrada exacta en esta tabla con decisión conservar.** Las palabras inglesas comunes que NO figuran como entrada propia (conformity, conditioning, autopilot, assignment, etc.) se traducen normalmente (conformidad, condicionamiento, piloto automático, asignación), aunque aparezcan dentro de algún término compuesto de la tabla.\n3. **Palabras comunes muy frecuentes** que el autor usa con sentido propio pero que tienen equivalente natural en español (goal, identity, focus, luck, distribution, attention, value, mind, game, habit, skill, problem, purpose) se **traducen** con forma fija (meta, identidad, foco, suerte, distribución, atención, valor, mente, juego, hábito, habilidad, problema, propósito); su definición propia se explica en el texto. Se conservan en inglés solo dentro de un término acuñado compuesto (p. ej., *goal-oriented*, *Focus Formula*).
4. Otras palabras comunes con sentido fuerte (vessel, leverage, edge, hunting, glitch, NPC, the Matrix…): según la tabla.
5. Términos de terceros con traducción establecida en español: forma estándar (p. ej., entropía, flow, Dinámica Espiral (Spiral Dynamics)).
6. **Nunca** dos términos distintos del autor reciben la misma traducción.
7. Español neutro latinoamericano, sin voseo.\n8. *consciousness* → **consciencia** (sentido filosófico/psicológico); *levels of awareness* de Schwartz → **niveles de conciencia (Schwartz)**, para distinguirlos.

## Tabla

| Término original | Tipo | Decisión | Primera aparición en español | Apariciones siguientes | Nota |
|---|---|---|---|---|---|
"""
rows.sort(key=lambda r: norm(r[0]))
open('_libro/08_lexico-traduccion.md','w').write(hdr+'\n'.join('| '+' | '.join(c.replace('|','/') for c in r)+' |' for r in rows)+'\n')
print('filas',len(rows),'overrides',n_ov,'duplicados de traducción',len(dups))
for k,v in list(dups.items())[:15]: print(' ',k,'<-',v)
import json; json.dump(rows,open('/tmp/claude-0/lexrows.json','w'),ensure_ascii=False)
