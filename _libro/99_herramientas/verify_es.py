import re,os,sys
E='_libro/05_capitulos_en/'; S='_libro/09_capitulos_es/'
vos=re.compile(r'\b(vos|tenés|podés|sabés|querés|hacé|escribí|registrá|mirá|fijate|che|sos|decís|hacés|sentís|vení|andá|pensá|elegí)\b',re.I)
def st(t):
    t=re.sub(r'<!--.*?-->','',t,flags=re.S)
    return dict(w=len(t.split()),h=[len(m) for m in re.findall(r'^(#+) ',t,re.M)],src=len(re.findall(r'\*\*(?:Source|Fuente):\*\*',t)),
      cc=len(re.findall(r'\*\*(?:Complementary context|Contexto complementario):\*\*',t)),tab=len(re.findall(r'^\|',t,re.M)))
for f in sorted(os.listdir(S)):
    if not os.path.exists(E+f): continue
    a=st(open(E+f).read()); bt=open(S+f).read(); b=st(bt)
    v=len(vos.findall(re.sub(r'\([^)]*\)|"[^"]*"','',bt)))
    probs=[]
    if a['h']!=b['h']: probs.append(f"enc {len(a['h'])}/{len(b['h'])}")
    if a['src']!=b['src']: probs.append(f"fuente {a['src']}/{b['src']}")
    if a['cc']!=b['cc']: probs.append(f"cc {a['cc']}/{b['cc']}")
    if a['tab']!=b['tab']: probs.append(f"tabla {a['tab']}/{b['tab']}")
    r=b['w']/a['w']
    if not .95<=r<=1.25: probs.append(f"razón {r:.2f}")
    if v: probs.append(f"voseo {v}")
    print(f"{f:12} {a['w']:7} {b['w']:7} {r:.2f} {'OK' if not probs else ' | '.join(probs)}")
