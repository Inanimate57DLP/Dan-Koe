import re,os
E='_libro/05_capitulos_en/'; S='_libro/09_capitulos_es/'
def secs(t):
    t=re.sub(r'<!--.*?-->','',t,flags=re.S)
    parts=re.split(r'^(#{1,6} .*)$',t,flags=re.M)
    out=[]; cur=('(intro)',parts[0])
    out.append(cur)
    for i in range(1,len(parts),2): out.append((parts[i],parts[i+1]))
    return out
def paras(s): return len([p for p in re.split(r'\n\s*\n',s) if p.strip()])
flag=0
for f in sorted(os.listdir(S)):
    if not os.path.exists(E+f): continue
    a=secs(open(E+f).read()); b=secs(open(S+f).read())
    if len(a)!=len(b): print(f,'SECCIONES',len(a),len(b)); flag+=1; continue
    for (ha,ta),(hb,tb) in zip(a,b):
        wa=len(ta.split()); wb=len(tb.split())
        pa,pb=paras(ta),paras(tb)
        if wa>=60 and (wb/wa<0.85 or wb/wa>1.45) or pa!=pb:
            print(f"{f} | {ha[:50]!r} -> {hb[:50]!r} | palabras {wa}/{wb} ({wb/max(wa,1):.2f}) | párrafos {pa}/{pb}"); flag+=1
print('secciones señaladas',flag)
