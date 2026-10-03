import re,sys,collections
words=['goal','goals','identity','focus','luck','distribution','attention','value','mind','game','habit','skill','problem','purpose','leverage','alignment','character','culture','expectation','force','frame','intention','lenses','perspective','polarity','rules','dissonance','generalist','builder','elements','channels','nodes','residue','toolbox','gravity','filtration','conformity','conditioning','autopilot','assignment','awareness','mindset','self','growth','mission','vision','feedback','output','input']
for f in sys.argv[1:]:
    c=collections.Counter(); ex={}
    for line in open(f):
        if line.startswith('**Fuente') or line.startswith('<!--'): continue
        l=re.sub(r'`[^`]*`','',line)
        for w in words:
            for m in re.finditer(r'(?<![\w-])'+w+r'(?![\w-])',l,flags=re.I):
                c[w]+=1; ex.setdefault(w,l[max(0,m.start()-60):m.end()+60].strip())
    print('==',f, sum(c.values()))
    for w,n in c.most_common(25): print(f'  {w:14}{n:5}  | {ex[w][:150]}')
