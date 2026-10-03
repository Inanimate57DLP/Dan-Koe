# Lista ocurrencias de palabras inglesas comunes fuera de citas originales, títulos y líneas Fuente.
import re,sys
W={'conditioning':'condicionamiento','conformity':'conformidad','autopilot':'piloto automático','assignment':'asignación','assignments':'asignaciones',
'awareness':'toma de consciencia / consciencia','mindset':'mentalidad','self':'yo','programming':'programación','goal':'meta','goals':'metas',
'identity':'identidad','focus':'foco','luck':'suerte','distribution':'distribución','attention':'atención','value':'valor','mind':'mente',
'game':'juego','habit':'hábito','habits':'hábitos','skill':'habilidad','skills':'habilidades','problem':'problema','problems':'problemas','purpose':'propósito',
'leverage':'apalancamiento','alignment':'alineación','character':'personaje','culture':'cultura','perspective':'perspectiva','frame':'marco',
'intention':'intención','generalist':'generalista','residue':'residuo','gravity':'gravedad','dissonance':'disonancia','growth':'crecimiento','vision':'visión','force':'fuerza','rules':'reglas','personal brand':'marca personal','personal branding':'construcción de marca personal','survival mode':'modo supervivencia','self-awareness':'autoconsciencia','outline':'esquema','outlines':'esquemas'}
f=sys.argv[1]; n=0
for i,line in enumerate(open(f),1):
    if line.startswith('#') : pass
    l=re.sub(r'\*\*Fuente:\*\*[^.]*?\.md[^)]*\)?','',line)
    l=re.sub(r'\*\*Fuente:\*\*.*?\.md','',l)
    l=re.sub(r'\("[^"]*"\)','',l)            # citas originales entre paréntesis
    l=re.sub(r'"[A-Za-z][^"]*?[a-z][^"]*"',lambda m: '' if len(re.findall(r'\b(the|and|you|your|is|of|to|that|it)\b',m.group(0)))>=2 else m.group(0),l)  # citas en inglés
    l=re.sub(r'\*[^*]+\*(?!\*)','',l) if False else l
    l=re.sub(r'(?<!\*)\*(?!\*)[^*]+\*(?!\*)','',l)   # títulos en cursiva
    l=re.sub(r'`[^`]*`','',l)
    for w,tr in W.items():
        for m in re.finditer(r'(?<![\w-])'+w+r'(?![\w-])',l,flags=re.I):
            after=l[m.end():m.end()+3]
            if after.startswith(' ('): continue   # primera aparición glosada
            # dentro de término compuesto en inglés (palabra inglesa contigua)
            ctx=l[max(0,m.start()-25):m.end()+25]
            print(f"{i}: [{w}→{tr}] …{ctx.strip()}…"); n+=1
import unicodedata
for i,line in enumerate(open(f),1):
    for ch in line:
        if ord(ch)>0x2FF and unicodedata.category(ch).startswith('L'):
            print(f"{i}: [CARÁCTER NO LATINO {ch!r}] …{line.strip()[:80]}…"); n+=1; break
    if line.startswith('#') and re.search(r'\b(the|and|of|your|to|is)\b',line) and not re.search(r'[áéíóúñ¿¡]|\b(el|la|los|las|de|del|y|tu|en|un|una|que)\b',line):
        print(f"{i}: [ENCABEZADO EN INGLÉS: añadir glosa española entre paréntesis] {line.strip()}"); n+=1
print('TOTAL',n,file=sys.stderr)
