# Expande 04_arquitectura.md: clústeres -> IDs de unidades; control de huérfanos; genera material por capítulo
import re,json,os,collections
os.chdir('/home/user/Dan-Koe')
cl=json.load(open('_libro/02e_sintesis/clusters.json'))
arch=open('_libro/04_arquitectura.md',encoding='utf-8').read()
chapters=[];cur=None
for line in arch.splitlines():
    m=re.match(r'^####\s+Cap[ií]tulo\s+(\d+)\s*[—–-]\s*(.*)',line)
    if m: cur=dict(n=int(m.group(1)),title=m.group(2).strip(),sections=[]); chapters.append(cur); continue
    m=re.match(r'^-\s+\*\*(\d+\.\d+)\s+(.*?)\*\*\s*(.*)$',line)
    if m and cur:
        cids=re.findall(r'C-T\d+[ab]?-\d+',line)
        cur['sections'].append(dict(num=m.group(1),title=m.group(2).strip(),cids=cids))
seen=collections.Counter(c for ch in chapters for s in ch['sections'] for c in s['cids'])
missing=[c for c in cl if c not in seen]; dup=[c for c,v in seen.items() if v>1]; unknown=[c for c in seen if c not in cl]
units=collections.Counter(u for ch in chapters for s in ch['sections'] for c in s['cids'] if c in cl for u in cl[c]['ids'])
print('capitulos',len(chapters),'secciones',sum(len(c['sections']) for c in chapters))
print('clusters asignados',len(seen),'/',len(cl),'faltan',missing[:20],len(missing),'dup',dup[:10],'desconocidos',unknown[:10])
print('unidades asignadas',len(units))
for ch in chapters:
    n=sum(len(cl[c]['ids']) for s in ch['sections'] for c in s['cids'] if c in cl)
    w=0
    ch['nunits']=n
    print(ch['n'],n,ch['title'][:70])
json.dump(chapters,open('/tmp/claude-0/chapters.json','w'),ensure_ascii=False)
