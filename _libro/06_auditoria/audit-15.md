# Auditoría de cobertura — Lote 15 (capítulos 29 y 30)

Auditor independiente, fase 5. El reporte cubre los puntos 2 a 8 del prompt del auditor para `05_capitulos_en/cap-29.md` y `05_capitulos_en/cap-30.md`, contrastados con `04b_material/cap-29.md` y `04b_material/cap-30.md`. El punto 1 (IDs no cubiertos) ya lo verificó un script y queda fuera de este reporte.

## Resumen

| Capítulo | PÉRDIDAS | MENORES |
|---|---|---|
| 29 — Cómo empezar: rutas, lo mínimo viable y el primer cliente | 0 | 5 |
| 30 — De servicio a producto: el roadmap por etapas | 0 | 6 |

**Método y muestra.**

- Leí completos los dos capítulos: 999 líneas el 29 y 982 el 30.
- Del material leí `desarrollo`, `ejemplos`, `cita` y `tension` de todas las unidades: 148 en el capítulo 29 y 149 en el 30. Es decir, el 100 % de cada sección, más allá del 40 % exigido. Las comparé con el texto sección por sección.
- Pasé además un control automático. Para cada unidad busqué en el capítulo sus citas textuales (las del campo `cita` y las entrecomilladas de `desarrollo`) en ventanas de cinco palabras.
  - En el capítulo 29 solo tres unidades no superaron el umbral: U-007-012, U-007-063 y U-009-001. Las revisé a mano y están desarrolladas con otras palabras: la cifra de 2.000–3.000 USD, la progresión del freelancer y las razones por las que el autor empezó como freelance.
  - En el capítulo 30 todas las unidades superaron el umbral.
- Revisé todas las entradas del Anexo A: 15 en el capítulo 29 y 23 en el 30.
- Del Anexo B leí todas las entradas: unas 85 en el capítulo 29 y unas 95 en el 30.
- Del Anexo C leí todas las entradas: 8 en el capítulo 29 y 21 en el 30.
- Para la progresión consulté `04_arquitectura.md` y busqué en los capítulos 1–28 la primera aparición de los términos que el 29 y el 30 usan sin glosa: lead magnet, Build Teach Earn, PPP, Cortex, Koe's Law, topic tree, gatekeeper mindset, offer stack y monetization lever.

**Juicio global.** Los dos capítulos tienen una fidelidad excepcional.

- Conservan prácticamente todas las cadenas numeradas, con sus pasos completos:
  - los siete caminos de carrera;
  - las cuatro partes de la micro offer;
  - el plan de 60 días;
  - las secuencias servicio → producto;
  - los seis pasos de Justin Welsh;
  - el roadmap por etapas;
  - la smart progression;
  - los nueve y los seis pasos del negocio de escritura.
- Mantienen todas las cifras y todos los casos: el sitio web de 300 USD, el analista de sistemas, el jabón para el eczema, Jose Rosado, Ari y Matt.
- Marcan las fuentes de terceros (Eriksen, Welsh, John Hugh, Vitali, Bezos, Altman, MVP, labor theory of value) como contexto complementario o como ideas del invitado.
- Presentan casi todas las tensiones del Anexo A como no resueltas, con lecturas por etapa que se ofrecen como lectura del capítulo y no del autor.
- Señalan los errores de las fuentes: 30 × 8 = 240, la cifra "$752,000", el "$11,000" y la numeración "five" dicha dos veces.
- El capítulo 30 advierte con honestidad que el material solo conserva un paso de cada etapa del roadmap, y lo verifiqué: es exacto.

No encontré ninguna unidad con mecanismo y ejemplos reducida a una sola frase, de modo que no registro PÉRDIDAS. Los hallazgos son matices:

- una datación que inventa una "nueva versión";
- un término acuñado que choca con su sentido registrado;
- algunas tablas de evolución que omiten escalones sin remitir al capítulo donde están;
- dos tensiones que el capítulo concilia sin avisar que el corpus las deja abiertas.

---

## Capítulo 29 — Cómo empezar: rutas, lo mínimo viable y el primer cliente

### 2. Unidades declaradas como cubiertas pero solo mencionadas

Sin hallazgos. Están explicadas con su mecanismo, sus ejemplos y sus cifras, entre otras:

- las rutas skill-based, development-based y "both" en sus cinco versiones (U-007-010, U-001-017, U-007-203, U-006-120 a U-006-126 y U-010-300 a U-010-302), con tabla de evolución;
- los siete caminos (U-008-090 a U-008-099), con todos los ejemplos: Tweet Hunter, MrBeast, el planner y "desaturate the market";
- la minimum viable vision en sus nueve formulaciones (U-017-020, U-023-180, U-024-187, U-016-068, U-025-073, U-026-162, U-026-161, U-024-086, U-025-027 y U-025-161);
- la estructura del tutoring offer, con el ejemplo de edición de YouTube llamada por llamada (U-008-070);
- los cuatro pasos de la micro offer (U-009-253 a U-009-259);
- el caso del analista de sistemas (U-008-156);
- los seis pasos de Justin Welsh y la comunidad de 99 USD por trimestre (U-005-056, U-005-057 y U-005-040);
- la adquisición manual de clientes, incluidos los teléfonos anotados de los vehículos (U-002-115);
- la tabla de síntomas y diagnósticos de "launch for data" (U-015-125);
- el plan de 60 días con sus cifras y el error aritmético señalado (U-009-266 a U-009-270).

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

- **MENOR — U-012-233 (publicar la primera idea).** El capítulo reproduce todo el bucle: hook, cuerpo, "embrace that the first iteration will suck", el diagnóstico escritura/crecimiento y la consulta a YouTube, Google o Claude. Omite un detalle de proceso: el autor ofrece en ese mismo paso un prompt o skill que convierte la respuesta en 12 ángulos y variantes de borrador. Es la única mención en la sección 29.4 del uso de IA dentro del ciclo de publicación. Debería ir en §29.4, "You can't improve what doesn't exist", tras "make the hook attention-grabbing".

### 4. Términos acuñados no definidos u homogeneizados

Sin hallazgos. Los términos propios llevan glosa en su primera aparición y con el sentido que registra el léxico. Entre ellos:

- human progression pattern, new 9-to-5 y sus variantes, business of you, underdeveloped person, notes disguised as ideas;
- forced to be a generalist, CEO-level traits, irreplaceable asset, digital resume y public resume;
- figments of consciousness, mechanical living, life project, magnetic goal, mental currency, true goals y cheap desires;
- minimum viable offer, micro offer, micro service, digital tutoring offers, manual work up front, unique process;
- client route, strategized messaging, multi-directional approach, loser's game, unemployable, tool belt, full stack business, tangible product;
- gatekeeper mindset (ya definido en el capítulo 28), faucet, ordered information, unvalidated, fail soon, fail in public, flow of feedback, stress testing;
- active tutorial, ideas beget ideas, swipe file.

Las palabras comunes con sentido propio reciben el sentido del autor, no el de diccionario: commodity, starving artist, unconscious competence, flavor of the day, prototype y relationship with money.

### 5. Cambios de posición (Anexo A) no presentados o resueltos indebidamente

Las 15 entradas están presentadas. Se explicita "Koe does not reconcile them himself" en EV-042, EV-200, EV-293, EV-197 y EV-299. Los hallazgos son de matiz.

- **MENOR — EV-035 (¿se puede no saber lo que uno quiere?).** §29.2 ("The minimum viable vision", último párrafo) presenta bien las tres posiciones: 2022–2023, 2024 y 2025. Pero cierra con "The minimum viable vision fits all three versions" sin advertir que el corpus registra el caso como **contradicción no resuelta**. En las demás tensiones del capítulo sí se dice que la conciliación es del capítulo y no del autor. Aquí la lectura conciliadora puede confundirse con una resolución del autor.
- **MENOR — EV-201 (MVO → micro offer → micro service; precios).** La tabla "One offer under three names" (§29.2) omite dos escalones que registra la entrada, sin remitir a donde se tratan:
  - la oferta de 500 USD por dos llamadas (U-007-218, 2023-06), que se desarrolla en el capítulo 17;
  - la precisión de 2026 de que un cliente freelance de 5.000 USD es "a pretty high price point for just starting out" (U-016-261), recogida en §30.6.

  Hacen falta para sostener la afirmación de la tabla de que "the prices apply to different stages, topics and audiences". Bastaría una nota con remisión.
- **MENOR — EV-196 (client work).** La tabla "Koe's evaluation of client work moved more than any other judgment" (§29.3, "The limit of client work") pasa de "2024: a new 9-to-5" a "Feb 2025: very good option". Omite el escalón de 2024-02 en que el autor aconseja saltarse el freelance e ir directo a coaching o consultoría (U-008-126, en el capítulo 12). Omite también, en el mismo febrero de 2025, que los marketplaces de freelance son "known paths… no different from a job" (U-010-243, en §30.1). Sin ese dato, la fila de 2025 parece un giro uniforme hacia la aceptación, cuando en el mismo mes coexisten las dos valoraciones. Debería ir en esa tabla o en una nota con remisión a §30.1.
- **MENOR — EV-200 (tráfico, servicio, autoridad y producto).** La conciliación de §29.4 ("The advice to launch immediately coexists…") solo enumera el lado "antes": traffic before offer, data-driven product y become an authority. Omite el elemento posterior más directamente opuesto a "launch a product ASAP": en 2024-12 el autor dice "I would build the service first so you can make money faster" y relega el micro product (U-008-154, desarrollado en el capítulo 32). Ese dato toca el núcleo de la sección, servicio primero frente a producto inmediato. Debería ir en el mismo párrafo, con remisión al capítulo 32.

### 6. Fuentes de terceros con atribución perdida, confundida o alterada

Sin hallazgos. Revisé las ocho entradas del Anexo C:

- **MVP:** marcado como contexto complementario (lean startup, Eric Ries), con la aclaración de que el autor no cita esa literatura.
- **Justin Welsh:** "The material below is Welsh's own system", separado de la adopción del autor.
- **Devon Eriksen:** "The idea is Eriksen's; Koe takes it up", con la distinción entre el mecanismo emocional y el epistémico.
- **John Hugh:** "The point is Hugh's, not Koe's".
- **MrBeast:** presentado como ejemplo.
- **"Buyers buy again":** "states it as a known marketing principle without attributing it".
- **Tweet Hunter:** presentado como ejemplo.
- **"Learn a skill, sell a skill, teach a skill":** "This formula is not his".

### 7. Argumentos construidos por capas reducidos a su conclusión

Sin hallazgos. Conservan la cadena lógica:

- el argumento de los dos cuellos de botella del servicio frente al producto (U-016-262);
- el de por qué enseñar supera a hacer, porque el currículo es un subproducto (U-006-140);
- la secuencia "goals don't start out magnetic" → mental currency → sunk cost (U-026-165, U-007-205 y U-020-062), con contexto complementario sobre la falacia del costo hundido;
- la cadena problema → meta → proceso del jabón para el eczema (U-013-184);
- el argumento del 0,4 % de conversión del plan de 60 días.

### 8. Conceptos usados antes de introducirse

Sin hallazgos. Los términos que el capítulo usa sin glosa ya aparecen en capítulos anteriores:

- lead magnet, en los capítulos 2, 12 y 15;
- Build Teach Earn, en el capítulo 14;
- Cortex y 2 Hour Writer, desde el capítulo 4;
- gatekeeper mindset, en el capítulo 28;
- offer stack, en el capítulo 28.

Las nociones que pertenecen a capítulos posteriores llevan glosa breve y remisión explícita:

- value equation, al capítulo 31;
- done for you, done with you y DIY, al capítulo 33;
- irreplaceable individual, al capítulo 35;
- money programming, al capítulo 34.

---

## Capítulo 30 — De servicio a producto: el roadmap por etapas

### 2. Unidades declaradas como cubiertas pero solo mencionadas

Sin hallazgos. Están explicadas con mecanismo, condiciones y ejemplos, entre otras:

- la ruta de la oferta en cuatro movimientos y la versión de siete pasos con "spaceships" (U-002-128 y U-016-210);
- los tres movimientos evolutivos del autor, en tabla, con la restricción que elimina cada uno (U-009-085);
- el especialista como "specialized robot" frente al solution-builder, con el ejemplo del coach (U-011-082, U-001-047 y U-001-049);
- las agencias de short-form y la pregunta "are you the reason behind their success?" (U-008-049);
- "productize before the traffic spike", con la advertencia sobre el 62 % y el 60 % sin fuente (U-007-138 y U-001-137);
- los guest methods de John Hugh y Justin Welsh (U-004-032 y U-005-055);
- el Gap, con sus tres capas (U-001-028, U-007-002 y U-007-027);
- las tres etapas, sus trampas y el paso de etapa 3 con el intercambio Twitter↔Instagram (U-001-141 a U-001-152);
- la smart progression (U-010-139 a U-010-149);
- la escalera de contenido (U-016-134);
- los cuatro puntos de iteración, en tabla (U-016-144);
- la cadencia trimestral y los micro products (U-009-218, U-009-222 y U-012-113);
- la matemática del millón y los tres juegos incoherentes de ratios por seguidor, con su explicación (U-016-261, U-016-265, U-001-146, U-002-122 y U-012-039);
- los wrappers (U-008-189) y el "externalized clone of a creative process" (U-019-145).

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

- **MENOR — U-008-135 (no preocuparse por la web, la LLC ni los impuestos).** §30.6 ("What not to worry about yet") dice "the claim about audits is his opinion", pero el texto nunca enuncia ese reclamo. Omite la afirmación de la unidad de que el IRS "won't audit you over it" con ingresos de 10.000–50.000 USD. El lector recibe la advertencia sin el contenido advertido. Debería ir tras "minuscule to the IRS".

### 4. Términos acuñados no definidos u homogeneizados

- **MENOR — "monetization lever" (léxico: *monetization lever / promotion schedule*).**
  - En §30.4 ("The quickest fix is the longest path", cierre), el capítulo escribe en cursiva "That is the sense in which Koe calls them a *monetization lever*". Lo presenta como término propio con el sentido de "palanca que el fundador controla y que compone" (inteligencia, creatividad, carácter).
  - El léxico registra *monetization lever* como término acuñado con otro sentido: la promoción sistematizada dentro de la creación de contenido. Con ese sentido lo define el capítulo 32 ("The monetization lever: promotion built into content creation").
  - En U-021-038 la expresión es descriptiva ("intelligence is a more sustainable monetization lever"), no el término acuñado.
  - El capítulo crea así un segundo significado para un término que el libro define después de otra forma. Debería ir sin cursiva y sin "Koe calls", como uso descriptivo, o con remisión que distinga los dos usos.

Fuera de este caso, los términos propios llevan glosa:

- new 9-to-5 y sus variantes, skill for someone else compared to art for you, builder, known path (con sus dos sentidos), feast-or-famine cycle, intention of evolution, freelancer mindset;
- the Gap, clarity, lever-moving actions, plumber for a business, high-ticket client cycle, de-niche, brand actualization pyramid;
- startup idea junkie, content ladder, beginner/big boy business model, positive behavior change at scale, right angle;
- metapath, director of your life, business paradigm, stepping stone, launchpad, pigeonholed, compounded knowledge;
- quickest fix is the longest path, myopic, focus is a currency, gray area, kernels of truth, iterative products, base income y micro products;
- your standard, framing device, traffic mechanism, monetize your intelligence, perpetual cycle of content, catalyst, wrapper, externalized clone of a creative process.

Psychic entropy, intrinsic drivers y labor theory of value llevan su atribución.

### 5. Cambios de posición (Anexo A) no presentados o resueltos indebidamente

Están presentadas con su tipo, casi siempre con la fórmula "Koe does not resolve it", las entradas:

- EV-052, EV-067, EV-160, EV-186, EV-196, EV-197, EV-200, EV-202, EV-203;
- EV-205, EV-206, EV-207, EV-209, EV-215, EV-227, EV-228;
- EV-240, EV-253, EV-262 y EV-304.

- **MENOR — U-003-055 / U-017-004 (datación que fabrica una "nueva versión").**
  - §30.1 ("'A new 9-to-5': the diagnosis") dice: "In March 2024 he tells the same passage as autobiography", y atribuye a 2024 el relato de que tomó menos clientes, productizó y vendió a su audiencia.
  - U-003-055 procede de una compilación de 2024-03-21 que reedita el video "The 4-Hour Workday" de 2023-01. El material lo fusiona con U-017-004 ("mismo pasaje").
  - El ejemplo autobiográfico ya estaba en la versión de 2023 (U-017-003, ejemplos). Así lo data el propio capítulo 29 en §29.3 ("From service to product: the sequences").
  - El texto sugiere una evolución, de la advertencia de 2023 a la autobiografía de 2024, que no existe, y queda en contradicción con el capítulo 29. Debería decir que el pasaje de 2023 ya incluía su propio caso y que la compilación de 2024 lo repite.
- **MENOR — EV-239 (code y media).** §30.3 ("Media matters more than code for beginners") afirma que "His own position on code moves over the years… but this ordering survives the changes".
  - El orden media primero, software después es estable desde 2023-09. Sin embargo, la entrada registra una **contradicción no resuelta** que el capítulo no presenta: en 2023-12, a partir de Balaji, aprender código y contenido "is not optional" (U-012-013), y "content route, code route, or both" (U-012-027).
  - Esa fase está desarrollada en los capítulos 28 y 36, pero aquí no hay remisión. La frase "survives the changes" cierra una oscilación que el corpus deja abierta.
  - Debería ir una línea con remisión al capítulo 36.
- **MENOR — EV-144 (pilares de contenido y topic tree).** El paso 1 de la smart progression (§30.2, "two to three topics that lead to your vision", U-010-140) se presenta como método vigente.
  - La entrada registra que en 2026 el autor afloja ese criterio: "just focus on the ideas that are important to you and share those. That's your entire content strategy" (U-010-319, cuya tensión remite justamente a U-010-140), y "ignore niche and content pillars" (U-012-230).
  - Lo desarrolla el capítulo 22, pero falta la remisión. El párrafo de tensión sobre el nicho que cierra §30.2 cubre EV-186, no esta entrada.
- **MENOR — EV-019 (gradual frente a extremo).** §30.5 ("Small wins as the test of the right path") presenta la sobrecarga progresiva de 5.000 en 5.000 USD (U-017-130) como el modelo de avance, y la apoya en "the stages of Section 30.2 are not shortcuts".
  - La entrada registra que el autor sostiene en paralelo el registro opuesto, como contradicción no resuelta: "rip the band-aid off", "give yourself permission to be extreme", "flip the switch overnight".
  - No hace falta desarrollarlo aquí, porque pertenece al capítulo 4, pero falta una remisión.

### 6. Fuentes de terceros con atribución perdida, confundida o alterada

Sin hallazgos. Revisé todas las entradas del Anexo C:

- **Ideas de invitados:** John Hugh ("paid in the learning insights" es "Hugh's phrase"), Vitali, Justin Welsh, Ari y Matt figuran como ideas del invitado, con la advertencia de que Koe no las adopta como reglas y con la ambigüedad Ari/Matt señalada.
- **Bezos y Altman:** citados por el autor, y la anécdota de Altman se presenta como "reported secondhand".
- **Naval:** contexto complementario sobre permissionless leverage, con la divergencia de énfasis del autor.
- **Teorías y efectos:** la labor theory of value y el efecto Zeigarnik van como contexto complementario, y en la labor theory se aclara que el uso del autor es libre.
- **Flow drivers:** atribuidos a Kotler ("cites early and later uses without attribution"); psychic entropy, a Csikszentmihalyi.
- **Ratio por seguidor:** se indica que procede de un post anónimo ("adapted from an unnamed post").
- **Ejemplos:** Jose Rosado y Sahil Bloom se presentan como ejemplos.

### 7. Argumentos construidos por capas reducidos a su conclusión

Sin hallazgos. Conservan su cadena:

- el Gap (causal → atencional → epistémico);
- "fulfillment time limits income" (capacidad fija → pico de tráfico → productizar antes);
- "your standard" (estándar → problemas visibles → solución → estándar alcanzado);
- "impossible to fail", con sus tres condiciones explicitadas;
- la matemática del millón (ingreso → ventas diarias → visitas → problema de distribución);
- "productize yourself" en sus dos sentidos.

### 8. Conceptos usados antes de introducirse

Sin hallazgos.

- **Ya introducidos antes:** Koe's Law (capítulo 12), psychic entropy (capítulo 5), lever-moving actions y la jerarquía de metas (capítulo 8), topic tree y PPP (capítulos 22 y 23), Build Teach Earn (capítulo 14), progressive overload (capítulo 15) y social matrix (capítulo 1).
- **Pertenecen a capítulos posteriores, con remisión explícita:** holons y "transcend and include" (capítulo 38), done for you y done with you (capítulo 33), value as perception (capítulo 31), Kortex/Eden (capítulo 37) y agency (capítulo 35).
