import json,glob,re,collections,os
os.chdir('/home/user/Dan-Koe')
u={x['id']:x for x in json.load(open('/tmp/claude-0/units.json'))}
tags={}
for f in sorted(glob.glob('_libro/02b_indice/tags-*.tsv')):
    for l in open(f):
        p=l.rstrip('\n').split('\t')
        if len(p)>=4: tags[p[0].strip()]=(p[1].strip(),p[2].strip(),p[3].strip().lower())
print('tagged',len(tags),'units',len(u),'missing',[k for k in u if k not in tags][:5])
# block text
blocks={}
for f in sorted(glob.glob('_libro/02_unidades/lote-*.md')):
    t=open(f,encoding='utf-8').read()
    for b in re.split(r'^## (?=U-\d{3}-\d+)',t,flags=re.M)[1:]:
        uid=b.split('\n',1)[0].strip()
        b=re.split(r'^# ',b,flags=re.M)[0]  # drop trailing source headers
        blocks[uid]='## '+b.rstrip()+'\n'
th=collections.defaultdict(list)
for k,(t,t2,s) in tags.items(): th[t].append(k)
stats={t:(len(v),sum(u[i]['words'] for i in v)) for t,v in sorted(th.items())}
for t,s in stats.items(): print(t,s)
json.dump({'tags':tags},open('/tmp/claude-0/tags.json','w'))
import pickle; pickle.dump((th,blocks),open('/tmp/claude-0/th.pkl','wb'))
