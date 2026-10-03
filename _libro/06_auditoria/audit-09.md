# Auditoría de cobertura — Lote 09 (capítulos 17 y 18)

Auditor independiente. Fase 5. Alcance: puntos 2–8 del prompt del auditor para `05_capitulos_en/cap-17.md` y `05_capitulos_en/cap-18.md`, contrastados con `04b_material/cap-17.md` y `04b_material/cap-18.md`. El punto 1 (IDs no cubiertos) lo verificó un script y queda fuera de este reporte.

## Resumen

| Capítulo | PÉRDIDAS | MENORES |
|---|---|---|
| 17 — Cómo pensar | 0 | 4 |
| 18 — Creatividad, originalidad y gusto | 0 | 3 |

**Método y muestra.**

- Leí completos los dos capítulos.
- Comprobé que el bloque `<!-- COBERTURA: -->` de cada capítulo coincide exactamente con las unidades del material: 156 en el 17 y 114 en el 18, sin sobrantes ni faltantes.
- Del material revisé el 100 % de las unidades. En cada una leí `tipo`, `desarrollo`, `ejemplos`, `origen` y `tension`, y las comparé con el texto del capítulo, sección por sección.
- Pasé además dos controles automáticos:
  - **Citas.** Busqué la cita clave de cada unidad en el capítulo, en ventanas de cinco palabras. Las unidades sin coincidencia literal (siete en el 17 y siete en el 18, casi todas con citas de una sola palabra o con "ninguna") las revisé a mano. Todas están desarrolladas con otras palabras.
  - **Fuentes.** Comprobé que el archivo fuente de cada unidad aparece citado en el capítulo. Los pocos casos que el script no encontró se debían a diferencias tipográficas (apóstrofos) y están citados.
- Revisé el 100 % de las entradas del Anexo A: 17 en el capítulo 17 y 20 en el 18.
- En el Anexo B comprobé de forma automática todos los términos (106 en el 17 y 64 en el 18). Además leí completas unas 35 entradas por capítulo. Prioricé las palabras comunes con sentido propio, los términos con varias acepciones y los de terceros.
- En el Anexo C leí todas las entradas: 30 en el 17 y 23 en el 18. En el 18 son menos de 30 porque el anexo no tiene más.
- Para la progresión consulté `04_arquitectura.md`. Busqué en los capítulos anteriores los términos que el texto usa o remite a otro capítulo, por ejemplo Focus Matrix, conscious conditioning, pain and gain story, mastery over misery, narrowers of the mind, perspective vessel y Build Teach Earn.

**Juicio global.** Los dos capítulos tienen una fidelidad muy alta.

- Conservan casi literalmente los mecanismos, las cadenas argumentales, los ejemplos y las cifras, con su fuente y su fecha. Por ejemplo:
  - en el 17, la partida de ajedrez con el *fork*, Francia en 1940, la cadena "I don't like how I look" → "I don't want to end up alone", las seis preguntas de "study the opposite" y los siete pasos de la secuencia de promoción de Justin Welsh;
  - en el 18, el gráfico de los puntos, el "acre of fog", el herrero mental (armadura y armas), las cuatro etapas del gráfico del value creator, los siete rasgos del strategist y los nueve preceptos de Musashi.
- Presentan casi todas las tensiones del Anexo A sin resolverlas indebidamente, y cuando proponen una lectura conciliadora la marcan como propia ("a reading that the corpus allows", "neither reading is stated in the corpus").
- Separan con cuidado las ideas de terceros de las del autor, con contexto complementario correcto. En el 17: Bruce Lee, Wittgenstein, Sexto Empírico, Freedman, Porter, Fischer, McKeown, Welsh/Vassallo, Bloom, Bernstein y Klein. En el 18: Krishnamurti, Ira Glass, el invitado de Senra, Borges/Borel, Kleon, Schwartz/De Mello y Spiral Dynamics.
- Señalan los datos sin fuente: el 99 % de negocios que fracasan, el 60 % de empleos futuros, la encuesta infantil, los 15 minutos de meditación atribuidos a Wilber y el 90 % de personas que no saben qué quieren.

No encontré ninguna unidad reducida a una mención cuando el material traía mecanismo, condiciones y ejemplos, así que no registro ninguna PÉRDIDA. Los hallazgos son matices:

- dos remisiones internas equivocadas en el capítulo 17;
- un término acuñado sin nombrar;
- un ejemplo menor omitido;
- una acepción de "articulation" sin presentar ni remitir;
- un cambio de posición sin remisión;
- una ambigüedad de identidad ("Devon") en el capítulo 18.

---

## Capítulo 17 — Cómo pensar

### 2. Unidades declaradas como cubiertas pero solo mencionadas

Sin hallazgos. Todas las unidades de tipo framework, proceso, método, historia, ejemplo, metáfora, dato, término acuñado, fuente de tercero y argumento están explicadas con su mecanismo, sus condiciones y sus ejemplos. Algunos ejemplos:

- **Stupid thinking en sus tres versiones** (U-023-002, U-023-004, U-022-051, U-022-070, U-022-071), con la tabla de rasgos y la distinción entre síntoma y mecanismo de EV-129.
- **Smart but dumb** (U-022-073, U-022-076, U-024-103, U-020-086), con los tres retratos (el empresario de 100 millones, el creativo sin ingresos y el "meathead") y la frase sobre el dinero y el sentido.
- **Deep thinking → Critical Thinking 101 → genius thinking** (U-023-006, U-017-085, U-022-053, U-022-072, U-022-085, U-022-102), con tabla de evolución.
- **Pre-rational, rational, post-rational** (U-010-118 a U-010-123, U-021-090, U-020-190, U-024-129, U-022-097), cronológico y con la atribución a Wilber graduada año por año.
- **El true skeptic** (U-022-162 a U-022-167, U-017-093), con Sexto Empírico, la adaptación "firm beliefs held loosely" y las seis preguntas numeradas.
- **El proceso de aprendizaje en seis pasos** (U-027-125), con la nota sobre la segunda lista del mismo video (U-027-141).
- **El sistema de escritura propio** (U-013-031, U-001-096, U-002-105), con PAS, AIDA y PASTOR y el paso de 4 horas a 1–2 horas.
- **Los prompts de IA que preguntan** (U-018-112, U-018-061, U-024-223, U-024-137, U-016-282, U-003-213, U-024-177), en una tabla con su función.
- **Pain and process y sus variantes** (U-022-179, U-014-094, U-008-164, U-015-093, U-015-094, U-015-152, U-004-015, U-010-260), con el tweet "if you're tired all the time" y su conclusión.
- **Persuasion 101, PAS, el selling framework y la secuencia de Welsh** (U-010-188, U-002-134, U-007-218, U-005-037, U-013-242).
- **El big problem y el desired outcome** (U-009-167 a U-009-172), con el ejemplo de la halterofilia en los tres dominios y "vanity → therapy".
- **Los siete pilares (2025) y los siete principios (2026)** (U-022-027 a U-022-036, U-022-123, U-022-130 a U-022-146), cada uno desarrollado y comparados en tabla.
- **El premortem** (U-022-039, U-022-040, U-022-042), con los siete modos de fallo y los cuatro pasos.

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

- **MENOR — Liver King** (U-007-163). El material registra que el autor menciona a Liver King como referencia de "snake oil salesman", aclarando que no vende cursos y que evita el drama. El capítulo conserva la tipología de los tres grupos y la frase "an epoch of existence", pero omite este ejemplo concreto. Debería ir en 17.1, "Selective skepticism and other signs of a closed mind". Es un detalle ilustrativo, no un mecanismo.

No encontré otras omisiones. Los ejemplos y cifras del material están todos, con sus reservas: el 0,001 % del consejo aplicable, el "10 times more", el 80 % del contenido de principiante, los 500 dólares por dos llamadas, los 150 y 50 dólares con descuento del 25–30 %, las "10 $50,000 businesses", la ecuación 4 + 6 × (5 + 3 − 2) y los 15 minutos de meditación.

### 4. Términos acuñados no definidos u homogeneizados

- **MENOR — "partial thinking"** (U-024-103; Anexo B: término acuñado, única aparición, 2025-10). El capítulo desarrolla bien el contenido de la unidad: la cita "an internal mental problem may not be best solved by vocational means…" y "money often doesn't solve for meaning…". Pero no nombra el término, que es el campo `terminos` de la unidad. El contenido queda absorbido bajo "smart but dumb", que el léxico registra como término vecino y distinto. Debería ir en 17.1, "The 'smart but dumb' phenomenon", en el párrafo que cita el video de octubre de 2025.

Sin otros hallazgos. Las palabras comunes con sentido propio del Anexo B están tratadas con su sentido propio y en general glosadas explícitamente: "fluff", "direct experience", "awareness", "project" (como "vessel for making mistakes"), "high value" (señalado como término popular que el autor critica) y "light in the dark". Los términos con varias acepciones aparecen con la que corresponde al capítulo. Ejemplos: "firm beliefs held loosely", con la nota de sus otros usos; "pockets of the internet", con la advertencia de su uso positivo en 2024; y "complexity of self", con la adaptación de Csikszentmihalyi.

### 5. Cambios de posición (Anexo A) no presentados o resueltos indebidamente

Sin hallazgos. Las 17 entradas están presentadas y ninguna se resuelve indebidamente:

- **EV-014.** La ambigüedad "in no specific order" está explícita.
- **EV-027.** Tabla 2022–2026 con la atribución graduada.
- **EV-041.** "Post-mortem" como probable lapsus, coherente con el capítulo 7.
- **EV-092.** Presión frente a preparación en el mismo video, con remisión a 10.6.
- **EV-108.** Las listas de aprendizaje con remisión al capítulo 14.
- **EV-109.** Andamio, no ley, con las citas de 2022, 2023 y 2024.
- **EV-129, EV-130 y EV-131.** Con tablas.
- **EV-135.** El "esoteric crap" frente a *The Kybalion*.
- **EV-139.** La tribe of mentors frente a estudiar lo opuesto.
- **EV-140.** La interpretación frente al problem-first.
- **EV-156 y EV-158.** La pirámide y la historia del esqueleto de 1.000 palabras.
- **EV-201.** Micro offer, con remisión al capítulo 29.
- **EV-217.** 90 % frente a 95 % y "up the ladder".
- **EV-258.** Small bets frente a concentration of force. Se declara expresamente "unresolved" y se ofrecen dos lecturas marcadas como no presentes en el corpus.

### 6. Fuentes de terceros cuya atribución se perdió, se confundió o se alteró

Sin hallazgos. Todas las atribuciones del Anexo C se conservan con su grado de certeza:

- Wittgenstein ("if I said that correctly").
- Wilber: "I believe" en 2023, firme en 2024 e inferido en 2026.
- Einstein ("or supposedly said"), con nota sobre la falta de fuente.
- "Devon", con la reserva de que probablemente es Devon Eriksen sin confirmación.
- Vassallo vía Welsh.
- Eddie Shlainer vía Welsh.
- Max Bernstein, con el método declarado suyo y sin detalles.
- Sahil Bloom, con la formulación marcada como suya.
- El mapa y el territorio, sin atribuir en la fuente y con Korzybski como contexto.
- El premortem, con Gary Klein como contexto y la aclaración de que Koe no lo atribuye.
- El pyramid principle, con Minto como contexto y la aclaración de que Koe no la nombra.

*The Power of Now* aparece sin el nombre de Tolle, pero el autor y el libro ya se introdujeron en los capítulos 1–2 y 16, así que no es una pérdida de atribución.

### 7. Argumentos construidos por capas reducidos a su conclusión

Sin hallazgos. Las cadenas se conservan paso a paso y a menudo se numeran:

- selective skepticism: decisiones → futuro → la mente no ve un buen futuro → vida mediocre;
- error → problema → límite de la mente → mente cambiada (U-026-127), con lista de cuatro eslabones;
- el silogismo de la adaptabilidad: los errores son la única fuente de verdad → la experimentación produce errores → la experimentación es la única vía;
- "advice is not starting", con el orden de los seis pasos y el lugar del consejo;
- el argumento teoría frente a práctica, con la escalada de ejemplos;
- la lectura del ajedrez como construcción de posición jugada a jugada.

### 8. Conceptos usados antes de introducirse

No hay violaciones de progresión: los conceptos que pertenecen a capítulos posteriores (AQAL, strategist stage, Human 3.0, metatypes, micro offer, training wheels, specific knowledge, "you are the niche") llevan glosa o contexto complementario y remisión. Hay dos remisiones internas equivocadas:

- **MENOR — "pain and gain story … developed in Chapter 7"** (17.3, "Personal context"; U-018-061). El término se desarrolla en el capítulo 4 (4.2, "Pain is the signal: limbo, strategic dissonance and the pain-and-gain story") y en el capítulo 11 (protocolo de detox). El capítulo 7 no lo usa. El capítulo 9 lo relaciona con la anti-visión y la visión del capítulo 7, así que la remisión es aproximada pero no exacta. Debería remitir a 4.2 y al capítulo 11.
- **MENOR — "conscious conditioning … from Chapters 4 and 11"** (17.5, "What it takes to reach a new stage"; U-021-085). El término solo aparece introducido en el capítulo 1: el personaje principal que "creates themselves through years of conscious conditioning". No aparece en los capítulos 4 ni 11. Debería remitir al capítulo 1.

---

## Capítulo 18 — Creatividad, originalidad y gusto

### 2. Unidades declaradas como cubiertas pero solo mencionadas

Sin hallazgos. Todas las unidades prioritarias están explicadas con su mecanismo, sus condiciones y sus ejemplos. Algunos ejemplos:

- **El true creative** (U-016-053, U-016-054), con el argumento en cuatro pasos sobre el diseñador que odia su trabajo.
- **Las siete definiciones de creatividad, 2022–2026** (U-011-051, U-023-025, U-023-090, U-013-168, U-016-053, U-006-179, U-022-204, U-022-206), en una tabla y con la contradicción literal "something from nothing".
- **El gráfico de los puntos** (U-011-052), con la tabla de elementos y la advertencia sobre la parte que no se puede reconstruir.
- **El missing dot, el candle in a dark room y el idea space** (U-010-040, U-013-069, U-013-216), este último con la "variation" y el vuelo sobre el bosque.
- **Deconstruct/reconstruct y los mental Legos** (U-011-096, U-001-057, U-007-080, U-010-028), con los cuatro pasos.
- **DJs, el herrero mental e idea workers** (U-007-184, U-001-120, U-011-222, U-011-225, U-010-348), con tablas y los subgéneros de EDM.
- **Las cinco vías para pensar originalmente** (U-022-171, U-022-172, U-022-176, U-022-181). Los pasos 2 y 4, cuyas unidades pertenecen a otros capítulos, se resumen y así se declara.
- **El brain dump de 2022 y de 2024** (U-013-019, U-001-089, U-013-144), comparados en una tabla con los "roadblocks" añadidos.
- **El positive mind virus y el one-person business reinterpretado** (U-007-156, U-001-155, U-007-157, U-014-096).
- **Los cuatro rasgos del value creator y el gráfico de cuatro etapas** (U-011-088, U-001-050, U-011-093, U-001-054), más la tabla de formulaciones 2022–2026.
- **La experimentación del sintetizador en entrenamiento y dieta** (U-001-119), con todos sus programas.
- **Second-tier thinking y el strategist** (U-022-064, U-022-065, U-022-120, U-022-121, U-022-116), con los siete rasgos, los nueve preceptos y la ambigüedad de los "nine traits".
- **Taste:** biblioteca infinita, monos infinitos, Ira Glass, Photoshop, el libro *How to Focus* con IA, los cinco ingredientes, el invitado de Senra y las cinco cosas que la IA no puede replicar (U-012-198, U-010-228, U-010-235, U-010-232, U-012-212, U-012-214, U-012-194).
- **El inner album of greatest hits, el body of work y el problema del podcast** (U-022-185, U-022-187, U-022-189, U-022-186).

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

Sin hallazgos de relevancia. Los ejemplos y cifras están todos:

- el perro que ve césped, el "artistic basket weaving", la encuesta infantil y el 60 % de empleos;
- el "I am not that camera", el fog acre y la colonia y el gel;
- la Eisenhower Matrix y los diez posts copiados al día siguiente;
- Claude Sonnet 3.5, los cero a cinco hits por año y los 8–10 big ideas;
- las cifras de tiempo de escritura (EV-160).

Solo faltan alusiones sin contenido propio, como los "seven traits of the irreplaceable individual" que U-013-168 promete para otro video, y no las registro como hallazgo.

### 4. Términos acuñados no definidos u homogeneizados

- **MENOR — "articulation", segunda acepción** (Anexo B: "Ideas are cheap, articulation is expensive", 2026-01, U-010-321 y U-010-322). La sección 18.6 es la sede de la articulación y trata bien la primera acepción: organizar el pensamiento y ponerlo en palabras, y partir de un problema en conversación. No presenta ni remite a la segunda, según la cual la estructura y la articulación de una idea pesan más que la idea misma. Esa segunda acepción solo aparece en el capítulo 22. Habría que añadir, en 18.6, una remisión al capítulo 22 o una línea con la fórmula. Encaja de forma natural en "Articulation requires a body of work".

Sin otros hallazgos. Los términos con sentido propio se usan con ese sentido, por ejemplo "creative", "curator", "vessel" ("you find the vessel"), "value" ("value equals positive behavior change", "value is perception") y "riffing". Los alias están unificados con su variante: "novel/unique perspective", "synthesizer / way of the synthesizer / synthesizer of experience", "earn with the mind, not with time", "the three differentiators" y "name that process".

### 5. Cambios de posición (Anexo A) no presentados o resueltos indebidamente

- **MENOR — EV-268 (el sentido de la vida).** En 18.1 el capítulo presenta "arguably the meaning of human existence is to create" (U-012-015, 2023-12) como "a position, not a demonstrated fact". No avisa de que en 2026 el autor sistematiza el sentido en otros términos: los "meaning generators" (struggle, status/recognition y curiosity), que el capítulo 39 trata. Remite al capítulo 39 solo por la fórmula de la felicidad, no por este cambio. No es una resolución indebida, pero deja la formulación de 2023 sin su evolución posterior. Una remisión en 18.1, "You are a creator: the human as toolbuilder", bastaría.

Sin otros hallazgos. Las demás entradas están presentadas y ninguna se resuelve indebidamente:

- **EV-134.** "Useless wandering" frente a "do nothing useless". Se muestran las dos y se ofrece una lectura marcada como interpretación.
- **EV-135.** El "esoteric crap".
- **EV-136.** La originalidad, de "nobody has original ideas" al nivel "generative". Se nota que no pueden ser ambas literalmente ciertas.
- **EV-137.** Definiciones de creatividad.
- **EV-142.** La inteligencia, con Eriksen.
- **EV-151.** "Robar" frente a perspectiva propia, con el arco completo 2022–2026.
- **EV-154.** Lo accionable frente a la filosofía, con la deriva Stan / "fortune cookie tweets".
- **EV-159.** Hablar de uno mismo frente a traducir.
- **EV-160.** Cifras de escritura.
- **EV-177.** Qué sigue la gente.
- **EV-232.** Skill stack → cinco ingredientes.
- **EV-233.** La "greatest skill", con la lectura metafórica del propio autor.
- **EV-234.** Agency degradada.
- **EV-244 y EV-245.** Value creator y atención; definición del value creator.
- **EV-299.** ¿Escritor o no?

EV-139 (tribe of mentors) y EV-182 (generalista y especialista) tienen su sede en los capítulos 17 y 20, y el capítulo 18 remite a ellos.

### 6. Fuentes de terceros cuya atribución se perdió, se confundió o se alteró

- **MENOR — identidad de "Devon" en 18.6.** En "When articulation fails: the podcast problem" el capítulo cita "Devon's in control of the editing…" (U-022-186) sin glosa. En 18.1 el mismo capítulo había presentado a "the writer Devon Eriksen" como posible fuente de la definición de creatividad de U-013-168. Un lector puede entender que el novelista Eriksen edita los videos del autor. Ni la unidad ni el Anexo C identifican a este "Devon". Lo prudente es señalar que la transcripción solo da el nombre y que no consta que sea Eriksen, como se hace en 17.6 con el "Devon" del depression apartment.

Sin otros hallazgos. Se conservan:

- Krishnamurti, con su cita completa.
- Arnold, como analogía de tercero.
- Actualized.org (Leo Gura).
- La frontera ambigua Eriksen/Koe en U-013-168.
- El invitado sin nombre del podcast de Senra.
- Ira Glass, idea suya "used as he finds it".
- Schmachtenberger, con la cita marcada como suya.
- Musashi, con la paráfrasis del autor.
- Spiral Dynamics y Cook-Greuter, como base adaptada.
- Kleon y Mizner/Séneca, para "steal like an artist".
- Schwartz y De Mello, por separado.
- La biblioteca y los monos, sin atribuir en la fuente y con Borges y Borel como contexto.
- La posible fuente de Deutsch, señalada solo como parecido.

### 7. Argumentos construidos por capas reducidos a su conclusión

Sin hallazgos. Las cadenas se reconstruyen explícitamente:

- el true creative en cuatro premisas;
- el toolbuilder: naturaleza → herramientas → acumulación → felicidad como progreso más contribución → resolver problemas → creatividad;
- "original thinking is perception → identity → conditioning";
- "most thinking starts with a problem → experimentation → original thinking is the byproduct of experience";
- la greater cascade: información → identidad → conducta → civilización;
- la secuencia caos → claridad en ocho pasos;
- la síntesis de 18.5, de la producción barata a la selección escasa.

### 8. Conceptos usados antes de introducirse

Sin hallazgos. Los conceptos de capítulos anteriores que el texto usa están efectivamente introducidos antes:

- perspective vessel (capítulo 3);
- mastery over misery y mental bodybuilding (capítulo 15);
- narrowers of the mind (capítulo 11);
- commonplace book, Seven Days to Genius Ideas y el software de síntesis (capítulo 16);
- tutorial hell y Build Teach Earn (capítulo 14);
- Eden, Stan y Cortex, nombrados antes.

Los conceptos posteriores llevan glosa y remisión: los niveles de pensamiento y "transcend and include" (capítulo 38), "value equals positive behavior change" (capítulo 31), niche of one (capítulo 19), generalismo (capítulo 20) y agency (capítulo 35).
