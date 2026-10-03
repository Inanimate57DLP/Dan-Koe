import re,os
os.chdir('/home/user/Dan-Koe')
parts=[("I","The Diagnosis: The Matrix and the Default Path",1,2),("II","Identity: Who You Think You Are and How It Changes",3,4),
("III","The Mind as a System: Entropy, Attention and Goals",5,6),("IV","Direction: Anti-Vision, Vision, Goals, Purpose and the Game",7,10),
("V","Self-Governance: Dopamine, Focused Work, Rest and Routines",11,13),("VI","Learning and Thinking",14,18),
("VII","You Are the Niche",19,20),("VIII","Writing: The Foundational Skill",21,24),("IX","Audience, Growth and Brand",25,27),
("X","The One-Person Business",28,30),("XI","Value, Persuasion and Product",31,33),("XII","Money, Agency and the Economy of the Individual",34,36),
("XIII","Cases and Limits",37,37),("XIV","Levels of Consciousness and Meaning",38,40)]
strip=lambda t: re.sub(r'<!--\s*COBERTURA:.*?-->','',t,flags=re.S).rstrip()+'\n'
front=open('_libro/06b_front/00_title_description.md').read().rstrip()+'\n'
mapa=open('_libro/06b_front/01_map_of_the_discipline.md').read().rstrip()+'\n'
notes=open('_libro/06b_front/99_notes_on_the_corpus.md').read().rstrip()+'\n'
body=[]
for r,t,a,b in parts:
    body.append(f'# Part {r} — {t}\n')
    for n in range(a,b+1): body.append(strip(open(f'_libro/05_capitulos_en/cap-{n:02d}.md').read()))
backmatter=["## Master Glossary\n\n*(Built in the final Spanish edition from `03c_lexico.md`: every coined term with the author's definitions by date, related terms and links to the sections where it is developed.)*\n",
"## The Author's Sources and References\n\n*(Built in the final Spanish edition from `03d_fuentes-citadas.md`.)*\n",
"## Analytical Index\n\n*(Generated in the final Spanish edition from the real headings, with Obsidian internal links.)*\n", notes]
allbody='\n'.join(body)
# TOC from headings
toc=['## Table of Contents\n','- [[#Map of the Discipline]]']
for line in allbody.splitlines():
    m=re.match(r'^(#{1,3}) (.*)',line)
    if not m: continue
    lvl=len(m.group(1)); h=m.group(2).strip()
    if h=='Exercises': continue
    toc.append('  '*(lvl-1)+f'- [[#{h}]]')
toc+= ['- [[#Master Glossary]]','- [[#The Author\'s Sources and References]]','- [[#Analytical Index]]','- [[#Notes on the Corpus]]']
out=front+'\n'+'\n'.join(toc)+'\n\n'+mapa+'\n'+allbody+'\n# Back Matter\n\n'+'\n'.join(backmatter)
open('_libro/07_libro_en.md','w').write(out)
print(len(out.split()), len(toc))
