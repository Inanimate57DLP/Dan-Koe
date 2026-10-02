import pickle,json,collections,math,os
os.chdir('/home/user/Dan-Koe')
th,blocks=pickle.load(open('/tmp/claude-0/th.pkl','rb'))
tags=json.load(open('/tmp/claude-0/tags.json'))['tags']
names={l.split('|')[1].strip():l.split('|')[2].strip() for l in open('_libro/02b_indice/taxonomia-trabajo.md') if l.startswith('| T')}
plan=[]
for t in sorted(th):
    ids=sorted(th[t],key=lambda i:(tags[i][2],i))
    w=sum(len(blocks[i].split()) for i in ids)
    n=max(1,math.ceil(w/55000))
    # split at subtema boundaries near equal word counts
    groups=collections.OrderedDict()
    for i in ids: groups.setdefault(tags[i][2],[]).append(i)
    parts=[[]];acc=0;target=w/n
    for s,g in groups.items():
        gw=sum(len(blocks[i].split()) for i in g)
        if acc>=target*len(parts) and len(parts)<n: parts.append([])
        parts[-1].append((s,g)); acc+=gw
    for k,p in enumerate(parts):
        suf='' if n==1 else f'-{chr(97+k)}'
        fn=f'{t}{suf}.md'
        cnt=sum(len(g) for s,g in p)
        with open(f'_libro/02c_por_tema/{fn}','w') as f:
            f.write(f'# {t}{suf} — {names[t]}\n\n{cnt} unidades.\n\n')
            for s,g in p:
                f.write(f'### subtema: {s}\n\n')
                for i in g: f.write(blocks[i]+'\n')
        plan.append((t,suf,fn,cnt,sum(len(blocks[i].split()) for s,g in p for i in g)))
for p in plan: print(p)
json.dump(plan,open('/tmp/claude-0/plan.json','w'))
