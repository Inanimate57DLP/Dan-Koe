# Auditoría de cobertura — Lote 13 (capítulos 25 y 26)

Auditor independiente. Fase 5. Alcance: puntos 2–8 del prompt del auditor para `05_capitulos_en/cap-25.md` y `05_capitulos_en/cap-26.md`, contrastados con `04b_material/cap-25.md` y `04b_material/cap-26.md`. El punto 1 (IDs no cubiertos) lo verificó un script y queda fuera de este reporte. No se corrigió nada.

## Resumen

| Capítulo | PÉRDIDAS | MENORES |
|---|---|---|
| 25 — Por qué una audiencia: atención, distribución y leverage | 0 | 7 |
| 26 — Crecer: contenido validado, tráfico y networking | 0 | 6 |

**Método y muestra.**

- Leí completos los dos capítulos: 1.377 líneas el 25 y 1.272 el 26.
- Del material leí el 100 % de las unidades: 204 del capítulo 25 y 210 del 26. En cada una contrasté desarrollo, ejemplos, cifras, cita, origen y tensión con el texto del capítulo, sección por sección.
- Anexo A (evolución): revisé todas las entradas, 28 en el 25 y 22 en el 26.
- Anexo B (léxico): leí todas las entradas, 92 en el 25 y 88 en el 26. Además comprobé con grep la presencia en el capítulo de unos 45 términos por capítulo, priorizando términos acuñados y palabras comunes con sentido propio.
- Anexo C (fuentes): leí todas las entradas, 31 en el 25 y 17 en el 26.
- Para la progresión consulté `04_arquitectura.md` y, con grep, los capítulos anteriores (01–24). Verifiqué las remisiones internas a secciones (24.4, 24.5, 25.x, 26.x) y a capítulos previos.

**Juicio global.** Los dos capítulos tienen una fidelidad muy alta. Conservan prácticamente todos los mecanismos, cadenas numeradas, cifras (incluidas las que no cuadran, señaladas como tales), ejemplos, metáforas y guiones de DM del material. Separan con cuidado lo que es de los invitados (Eriksen, Hugh, Vitali, Welsh, Bloom, Bush) de lo que es de Koe. Presentan casi todas las tensiones del Anexo A con fecha y razón, a menudo en tablas: taxonomías de distribución, formas de leverage, juicio sobre las redes, plataformas, benchmarks, paid growth, engagement groups y non-needy networking 2023/2026. Cuando proponen una reconciliación, la marcan como interpretación. No encontré ninguna unidad reducida a una frase cuando el material traía mecanismo, condiciones y ejemplos, así que no registro ninguna PÉRDIDA. Los hallazgos son matices:

- una cita alterada;
- dos términos usados sin definir o con la atribución incompleta;
- tres evoluciones presentadas con huecos;
- una discrepancia entre capítulos que ninguno de los dos registra;
- dos inferencias presentadas como hechos;
- dos remisiones erróneas o imprecisas.

---

## Capítulo 25 — Por qué una audiencia: atención, distribución y leverage

### 2. Unidades declaradas como cubiertas pero solo mencionadas

Sin hallazgos de PÉRDIDA. Todas las unidades de tipo framework, proceso, método, historia, caso, metáfora, dato, término acuñado, fuente de tercero y argumento están explicadas con su mecanismo y sus ejemplos. Algunos ejemplos:

- la cadena de cinco pasos de la atención como poder (U-023-055/U-003-127);
- el método de IA con prompts blueprint/coach (U-016-281);
- los tres tipos de distribución en sus dos versiones y las dos taxonomías alternativas, con una tabla que muestra dónde caen los patrocinios (U-001-134, U-016-138, U-013-095, U-009-045);
- el digital leverage en tres partes, con la discrepancia $139.000/$130.000 (U-001-128/U-007-126);
- las cuatro versiones de las formas de leverage, en tabla (U-011-037, U-019-059, U-019-139, U-010-332, U-014-173);
- el plan de software "education first" y su contraste con Kortex (U-009-040, EV-302);
- los seis beneficios de la audiencia (U-009-231);
- el caso Eriksen completo: buffer, midlist, cadena de seis pasos, el editor del "dead spider", Kickstarter de $43.000 (U-006-064 a U-006-070);
- las tres capas de Matt Mike (U-011-201);
- el protocolo de uso de menos de 30 minutos (U-027-019);
- las razones de Twitter como "idea platform" (U-011-105/U-001-066);
- concentration of force en sus tres sentidos (U-022-139, U-016-236 a U-016-243).

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

- **MENOR — cita alterada (U-007-110, EV-173).** En §25.3, "Built, borrowed and bought (2024), and the case of Cortex", el capítulo resume la postura temprana sobre los anuncios como "a way of 'throwing money into an oven'". La expresión va entre comillas como si fuera literal. El corpus dice "shoveling money into a furnace", y el propio capítulo la cita correctamente en §25.4 ("Testing with content instead of a furnace"). Debería decir "shoveling money into a furnace", o quitar las comillas.

### 4. Términos acuñados no definidos u homogeneizados

- **MENOR — "socialization chamber" (U-027-016, EV-006).** La introducción del capítulo anuncia que §25.5 presenta los juicios de Koe sobre si la sociedad de las redes es "a socialization chamber or a vessel". Pero el cuerpo de §25.5 ("Devil or vessel") nunca usa ni define la expresión, ni la variante de 2022 "socialization makes you stupid" (EV-006). El lector se encuentra con un término de Koe que se anuncia y no se explica. Debería introducirse en el subapartado de la posición crítica de noviembre de 2022.
- **MENOR — "intellectual athlete" sin su origen (U-016-243; léxico: dos acepciones, la primera de Naval).** En §25.6, "Concentration of force beyond platforms", el capítulo dice: "**Intellectual athlete** is Koe's name, in this passage, for the entrepreneur dedicated to performance in business…". El léxico registra que el término es primero de Naval (2025-05: entrenar, esprintar, descansar). El capítulo 6 ya lo presentó como "Naval's phrase". El 25 no remite al 6 ni menciona a Naval, de modo que la atribución queda incompleta y el lector puede tomar como acuñación de Koe lo que es una reutilización con otro sentido. Debería añadirse algo como "a phrase Koe takes from Naval (Chapter 6) and applies here to…".

Por lo demás, sin hallazgos. Están definidos, casi siempre con fecha:

- investing attention, conceptual survival, external/internal power, attention is the root of existence, knowledge is king;
- attention economy/engagement game (como uso propio de términos comunes), attention as the ultimate leverage, attention is the only differentiator, epistemic commons, lore, blueprint/coach prompt, attention as moat;
- distribution (en sus dos sentidos, incluido el inbound de Hugh), distribution equals freedom, audience equals distribution, number one lever, one-person media company, personal distribution center, owned distribution, prove your value in public;
- backbone, foundational traffic source, business agnostic, sink or swim phase, create a Creator/avatar as the face of the brand;
- built/borrowed/bought, deplatform (como palabra común con sentido propio), low/high leverage, renting others' audiences, manual/bot/borrowed/owned, digital leverage, network effect (distinguido del sentido económico);
- permissionless leverage, full stack creator, philosopher builder, skill gatekeepers, skill cap, permissionless launchpad, old/new leverage, broke in more areas than finances;
- span and depth, data failures/growth successes, warm outreach, warm DMs, final kicker;
- audience (en el sentido de Eriksen), readers/followers, likes ain't cash, glorified search engine, your product is you, money is a measure of trust;
- virtual society, Digital Society, collective consciousness, online avatar, new town square, new party, tribe, digital storefront, character in virtual reality, atomization, you are the media, midlist, cycle of centralization and decentralization, global decentralized economy, path of high agency, luck surface area, vessel for your potential, way of water/way of fire, pockets of the internet (con su doble signo);
- idea platform, top of funnel, networkable/algorítmica, tribe/syndicate, Social Capital, suction system/momentum trick, branch into speaking, concentration of force (tres sentidos).

### 5. Cambios de posición (Anexo A) no presentados o resueltos indebidamente

Las 28 entradas están presentes y bien tratadas. Destacan EV-006, EV-153, EV-162, EV-163, EV-164, EV-166, EV-173, EV-176, EV-177, EV-179, EV-185, EV-242, EV-252, EV-257, EV-258, EV-259, EV-293, EV-298, EV-300 y EV-302. Las reconciliaciones que propone el capítulo van marcadas como lectura propia. Hay dos presentaciones incompletas:

- **MENOR — EV-239 (code y media), oscilación recortada.** En §25.3, "Media and code", el párrafo de cierre resume la línea así: 2022 "entender ambos"; 2023 "empieza por uno" o "you don't need to learn to code"; 2025 fusionar los polos; 2026 media por encima de code. Faltan los hitos intermedios que la entrada registra:
  - diciembre de 2023: a partir de Balaji, aprender código y contenido "is not optional" (U-012-013);
  - junio de 2024: Koe se aparta explícitamente del énfasis que percibe en Naval por el código, "media primero" (U-019-069);
  - julio de 2024: "I would be telling my grandchild not to go study coding" (U-006-103).

  Esas unidades están cubiertas en otros capítulos (30 y 36). Pero sin ellas la "oscilación" que el capítulo anuncia parece casi lineal, y se pierde que la divergencia con Naval es explícita y de Koe (ver también el punto 6).
- **MENOR — EV-006 (juicio sobre las redes), tabla con huecos.** La tabla de §25.5 empieza en "Late 2022 | Critical". La entrada registra que antes, en 2022, Koe presentaba internet con entusiasmo, como "a giant mind" cuyos creadores serían "the greatest evolvers of humanity" (U-011-019). Así, el punto de partida no fue crítico. Faltan además dos formulaciones marcadas de la entrada:
  - noviembre de 2023: "While most see social media as a net negative to humanity, I couldn't disagree more" (U-016-174);
  - 2025: "a mimetic desire amplification machine" y la expansión del "level one thinking" (U-023-210, U-015-165).

  El texto resume 2025–2026 como "amplifying unconsciousness", lo cual es correcto pero menos preciso. La trayectoria no lineal sí está bien descrita.

### 6. Fuentes de terceros cuya atribución se perdió o se alteró

Sin hallazgos graves. Las atribuciones son cuidadosas:

- Jocko Willink, incluida la nota sobre "Draco willing";
- Jack Butcher, y el paso de la cita a la adaptación;
- Naval, con el Arquímedes como contexto complementario;
- Kevin Kelly, con la observación de que Koe no lo nombra y solo lo nombra Welsh;
- Priestley, con la grafía "Presley";
- Balaji, con la grafía "Bala G";
- Schmachtenberger, con "the application is his";
- Matt Mike, aclarando que las proyecciones son del hilo;
- JK Molina, Jason Roberts, Ali Abdaal ("the idea is Abdaal's"), Eriksen ("This argument is Eriksen's, not Koe's"), John Hugh, Vitali, Welsh, Sahil Bloom, Dickie Bush, Jose Rosado y Kevin Dorsey;
- Dead Internet Theory vía Wikipedia.

Hay dos matices:

- **MENOR — "people follow people" (léxico: "término de invitado", acuñado por Vitali, U-004-029).** El capítulo usa la frase como principio de Koe:
  - en la introducción ("why 'people follow people' and not glorified search engines");
  - en §25.2 ("the principle of Section 25.4 that 'people follow people'");
  - como título de subapartado en §25.4.

  Solo al final de "Not a glorified search engine" aparece la frase en boca de Vitali. Koe tiene formulaciones propias cercanas: "people follow humans, they don't follow company accounts" (2023) y "they follow people who share ideas" (2025). El capítulo no se equivoca de fondo, pero convendría señalar que la fórmula exacta es de Vitali y que Koe la sostiene con palabras propias.
- **MENOR — relación con Naval.** El capítulo afirma que Koe adaptó a Naval "more than any other source" y presenta la línea code/media como una adaptación continua. Omite la toma de distancia explícita de 2024 respecto del énfasis de Naval en el código (U-019-069, EV-239; ver punto 5). Lo cuento dentro del hallazgo de EV-239; no suma al conteo.

### 7. Argumentos construidos por capas reducidos a su conclusión

Sin hallazgos. Las cadenas se conservan paso a paso:

- la pirámide de la atención (cinco pasos);
- "attention is the root of existence", con la objeción y las contrapreguntas;
- la secuencia de siete pasos de Butcher con el umbral 10.000/1.000/100;
- "three things you need for success", con la tabla y la condición del tercer componente;
- el experimento mental de los 100.000 seguidores y el CPM;
- la cadena de seis pasos de Eriksen sobre la ruptura del modelo editorial, separando la parte estructural de la política;
- el argumento del voto;
- las cuatro "realizations" de la salida del outreach (U-002-117).

### 8. Conceptos usados antes de introducirse

- **MENOR — remisión errónea.** En §25.6, "From short form to long form", el capítulo dice: "Later, as noted in Section 25.1, Koe describes long form as 'a moat... because AI can't really replicate it'". La §25.1 no menciona el long form como moat. Solo trata "attention is one of the last moats" (U-010-288), que es otra idea. El dato procede de EV-148 (U-022-215, 2026-03). Debería quitarse la remisión o introducir el dato allí mismo con su fecha.

Las demás remisiones son correctas:

- hacia atrás: Parte I (pirámides, capítulo 2), Parte II (conceptual survival), Parte III, capítulo 12, capítulo 19, capítulos 22–23, §24.4 "Newsletter as the Hub" y §24.5 "A tweet is the new MVP";
- hacia adelante, anunciadas como tales: capítulos 26, 27, Partes X–XIII.

Los términos internos (lore, network effect, Cortex/Kortex, value creator) se definen en su primer uso.

---

## Capítulo 26 — Crecer: contenido validado, tráfico y networking

### 2. Unidades declaradas como cubiertas pero solo mencionadas

Sin hallazgos de PÉRDIDA. Todas las unidades principales están desarrolladas con su mecanismo, condiciones y ejemplos. Algunos ejemplos:

- las cuatro versiones del sistema de crecimiento (U-004-144, U-008-088, U-014-159, U-004-097), con sus dependencias y la nota sobre la numeración inestable;
- beginner hell en sus dos definiciones (U-004-093, U-015-083) y los siete pasos, en tabla, con la advertencia sobre la numeración (U-015-091);
- los tests de "qualified" (U-007-054, U-001-016, U-006-117, U-010-298);
- el fat personal trainer (U-008-109) y la tabla de distancias (EV-189);
- el validated content con el recommendation mechanism, el caso Craig Perry, el reset period y la línea de lo que se puede tomar, en tabla (U-004-098 a U-004-112, U-022-147, U-021-217);
- el in wedge frente a make noise, con seis enfoques en tabla (U-004-026 a U-004-031, U-002-005, U-015-129);
- los cuatro traffic mechanisms, en tabla y con detalle (U-004-149 a U-004-156);
- los tres idea catalysts (U-014-162 a U-014-165);
- paid growth en sus cuatro fechas (U-004-160 a U-004-166, U-004-115);
- el mastermind y los engagement groups, en tabla (U-004-163, U-015-046, U-009-268, U-008-013);
- los dos procesos de non-needy networking, paso a paso y comparados (U-015-019 a U-015-031, U-004-120 a U-004-130);
- el caso del autor completo: fotógrafo, cuenta de arte, Twitter, descubrimiento, digital real estate, volumen de iteración, video desde Core Notes y bache de YouTube (U-004-132 a U-004-140, U-011-152/153, U-004-091, U-002-119, U-019-140, U-014-048, U-009-086, U-010-133, U-010-136, U-015-067, U-015-077, U-015-099).

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

- **MENOR — dato sin su fuente (U-009-094).** En §26.1, "Realistic timelines and benchmarks", el párrafo dice: "Two months later he calls 100,000 followers in a year an 'extremely good,' nearly perfect result". La línea **Source** que lo cierra solo cita *Micro Education Businesses Are The Future…* (2023-09). El dato es de *Turn Your Knowledge Into A Business (How To Productize Your Mind).md* (2023-11-26), que falta en la línea. Hay que añadir esa fuente.
- **MENOR — discrepancia entre capítulos no registrada (U-002-004 frente a U-015-120).** Los dos capítulos dan dos versiones del primer contacto entre Dickie Bush y Koe, y ninguno señala la diferencia:
  - el capítulo 25 (§25.5, "The internet as the great attractor") dice que Bush escribió a Koe "in mid-2020 after hearing him on Danny Miranda's podcast";
  - el 26 (§26.5, "A smart social game: the Dickie Bush case") cuenta que "in 2021 Dickie Bush… reached out after Koe posted about his fitness progress" (el tuit sobre los carbohidratos).

  Pueden ser dos momentos distintos, pero tal como están parecen dos relatos del mismo primer DM. El capítulo 26 debería anotarlo, como hace con otras cifras que no cuadran.

### 4. Términos acuñados no definidos u homogeneizados

Sin hallazgos. Están definidos:

- interest graph (con contexto complementario), beginner hell, the click (en su acepción de 2025, "intermediate heaven"), make your interest interesting, market of extremes, stepping into the arena, time to feedback, public market, the Gap (con sus otros sentidos), misery doesn't scale (de Welsh), uncertainty is signal;
- validated content y sus variantes, do what works from your own perspective, consumer behavior, recommendation mechanism, green streak, reset period, lens of specificity, data points, baseline/angle, digital asset, scarcity (como palabra común con sentido propio, distinta de la escasez de precio);
- exponential event, anomaly (con la cifra del doble de engagement), sell what's already selling, buyers buy again, Mother Nature, blue oceans;
- our Lord and savior the algorithm, get eyes on your content, slave to the algorithm (en sus dos sentidos), other people's audiences, generate traffic manually, network effect, traffic mechanisms, corporate speak/robot, reply like a madman, idea catalyst, pay to play, inject yourself in a tribe, social capital, strategic post, remixing, clippable moment, paid growth, churn and burn;
- making friends, vote of approval (de Vitali), seeding connections, engagement groups/pod/farm, mastermind, Lone Wolf mentality, big internet group chat, neediness (como palabra común con sentido propio), a post is an offer, smart social game, the digital world has no barriers, value exchange, perception goes two ways, mindset and awareness gap (de Hugh), non-needy networking, inspired compliment/simple praise, lead with value/show you're useful, faint connection, brutal honesty;
- shiny object syndrome (como palabra común con sentido propio), digital real estate (en el sentido de las audiencias de nicho, con aviso de sus otros sentidos).

### 5. Cambios de posición (Anexo A) no presentados o resueltos indebidamente

Las 22 entradas están presentes y la mayoría con tabla o párrafo propio: EV-151, EV-155, EV-159, EV-163, EV-166, EV-167, EV-168, EV-169, EV-170, EV-172, EV-176, EV-178, EV-179, EV-186, EV-189, EV-221, EV-263, EV-293 y EV-300. Ninguna se resuelve indebidamente: el capítulo marca como "inference" o "reading" sus reconciliaciones, por ejemplo entre recommendation mechanism y networking, o entre escasez y volumen. Matices:

- **MENOR — EV-186 (¿empezar estrecho o amplio?), voz omitida.** La tabla de enfoques de §26.3 ("The counterpoint: the 'in wedge'") incluye a Koe, Hugh, Bush y Vitali. Deja fuera la posición de Sahil Bloom que registra la entrada: no nichar "es más lento" y "you get defined by your niche" (U-005-108, U-005-109). Esas unidades están cubiertas en el capítulo 19, pero aquí falta una voz que matiza justamente la tensión que la sección deja abierta.
- **MENOR — EV-157 y EV-151, pasos intermedios omitidos.** En §26.3 ("From 'write what interests you' to 'research what works'" y el párrafo "This position has evolved") faltan dos hitos de 2024 que suavizan el salto entre 2023 y 2026:
  - "offer-driven content" si la meta es solo ganar dinero, sin anular lo anterior (U-008-161, 2024-12);
  - "take the ideas that already work and post them under your brand" (U-010-193, 2024).

  Sin ellos, la evolución parece pasar directamente de "escribe lo que te interese" (2022–2023) a "investiga lo que funciona" (2026).

### 6. Fuentes de terceros cuya atribución se perdió o se alteró

Sin hallazgos. Las atribuciones son precisas:

- John Hugh: interest graph y cinco razones, success pipeline, "guarantee", in wedge, Maslow, Emma Chamberlain. El capítulo advierte que son "Hugh's arguments… from the vantage point of a company";
- Vitali: vote of approval, "people follow people", playful, "me me me";
- Justin Welsh: misery doesn't scale, 2–3 años, get there first with value, el post de 3–4 millones de impresiones;
- Sahil Bloom: origen en Twitter y lanzamiento de *The 5 Types of Wealth*;
- Dickie Bush;
- Napoleon Hill, con la atribución tentativa de Koe y la nota de que es correcta;
- Cialdini, sin atribuirle más de lo que Koe dice;
- Séneca, con contexto complementario (Carta 84);
- *Steal Like an Artist* de Kleon, con la observación de que Koe no nombra al autor;
- Tim Ferriss, con la nota de que Koe no leyó el libro;
- Einstein, con la atribución dudosa señalada;
- Kevin Kelly, con la nota de que Koe no lo nombra;
- Alex Hormozi, con el ejemplo presentado como hipotético;
- Blue Ocean Strategy, con la nota de que Koe no discute el libro.

### 7. Argumentos construidos por capas reducidos a su conclusión

Sin pérdidas de cadena. Se conservan:

- la dependencia de los cuatro pasos ("each step is impossible without the one before");
- el silogismo de U-004-114 (seguidores → perfil → audiencias ajenas);
- la cadena de la escalera de Maslow de Hugh;
- la cadena de beneficios del clippable moment;
- el argumento del filtro del paid growth;
- la lógica de reciprocidad del non-needy networking.

Un matiz:

- **MENOR — inferencias del capítulo presentadas como hechos.** En §26.6, "Twitter: consistent growth out of the gate", el capítulo afirma: "The stabilized rate, 1,500 to 2,000 a month, is the source of the benchmark in Section 26.1 ('1,500 to 3,000 followers a month…')". En "The discovery: one reader, one million" añade: "This is the personal origin of the 'main lever' and 'secondary lever' of the magic click". El corpus no conecta esas cifras ni esas fórmulas (U-004-091 frente a U-006-146; U-009-086 frente a U-008-088). Son lecturas plausibles del redactor, pero van redactadas como hechos. Deberían marcarse como interpretación, como el capítulo hace en otros lugares ("A plausible reading is…").

### 8. Conceptos usados antes de introducirse

- **MENOR — remisión imprecisa.** En §26.4, "Leverage people who already have the audience", el capítulo dice: "**Information creates identity** is a concept from Part II applied here to the audience". La fórmula se introdujo en el capítulo 21 (§21.3, Parte VIII). Allí se presenta como la versión de mercado de la tesis de la Parte I/II (§1.2 y capítulos 3–4) de que la identidad se construye con la información absorbida. La remisión debería apuntar al capítulo 21, o a "Part I–II and Chapter 21".

Las demás remisiones son correctas:

- hacia atrás: capítulo 14 (build to learn), capítulo 16 y Core Notes, capítulos 22–23 (Ten Commandments of Engagement, training wheels, time under attention), capítulo 24 ("tweet is the new MVP"), capítulo 25 (built/borrowed/bought, permissionless leverage, network effect), Parte V (365 horas, 4-Hour Workday), Modern Mastery, Digital Economics, Eden y Kortex/Cortex, presentes en capítulos anteriores;
- hacia adelante, anunciadas como tales: capítulos 27, 28, 32, 33 y 37.
