# Auditoría de cobertura — Lote 10 (capítulos 19 y 20)

Auditor independiente. Fase 5. Alcance: puntos 2–8 del prompt del auditor para `05_capitulos_en/cap-19.md` y `05_capitulos_en/cap-20.md`, contrastados con `04b_material/cap-19.md` y `04b_material/cap-20.md`. El punto 1 (IDs no cubiertos) lo verificó un script y queda fuera de este reporte.

## Resumen

| Capítulo | PÉRDIDAS | MENORES |
|---|---|---|
| 19 — You are the niche | 0 | 5 |
| 20 — El generalista y el segundo Renacimiento | 0 | 6 |

**Método y muestra.**

- Leí completos los dos capítulos (1.157 y 939 líneas).
- Del material revisé el 100 % de las unidades: 156 del capítulo 19 y 126 del capítulo 20. En cada una comparé `desarrollo`, `ejemplos`, `cita`, `origen` y `tension` con el texto del capítulo, sección por sección, con atención especial a los tipos framework, proceso, método, historia, caso, metáfora, dato, término acuñado, fuente de tercero y argumento.
- Revisé el 100 % del Anexo A: 23 entradas en el capítulo 19 y 13 en el 20.
- Del Anexo B (léxico) leí todas las entradas: unas 75 en el capítulo 19 y unas 60 en el 20. Prioricé las palabras comunes con sentido propio (niche, niche down, customer avatar, generalist, unconscious competence, hot leads, top of funnel, shiny object syndrome, vessel, specific knowledge, hyper-specialists).
- Del Anexo C leí todas las entradas: 15 en el capítulo 19 y 20 en el capítulo 20. Son menos de 30 porque los anexos no tienen más.
- Para la progresión consulté `04_arquitectura.md` y busqué en los capítulos 1–18 (y en los posteriores, para ubicar las sedes) los términos que los capítulos usan sin glosa.
- Cuando un hallazgo parecía una omisión, busqué en todo `05_capitulos_en/` si el material estaba desarrollado en otro capítulo. Varios cambios de posición del Anexo A que no aparecen en estos capítulos tienen su sede en otro (detalle en cada punto 5). No los cuento como hallazgos.

**Juicio global.** Los dos capítulos son de una fidelidad muy alta. Conservan:

- los mecanismos y las cadenas argumentales (los tres problemas de elegir un nicho de una lista, la cadena valor → identidad → yo pasado, los ocho pasos de los Great Pirates, los cinco pasos del tool builder, el paralelo de la imprenta);
- los ejemplos y las cifras con su estatus (el 95 %, el 80 % de principiantes, el top 25 % "inventado", 30.000 frente a 300.000, 20 frente a 48.000 alfileres);
- las tensiones del corpus, presentadas como tensiones y no resueltas (20/80 frente a 80/20, deep generalist frente a deep specialist, conspiración frente a propiedad del sistema, el renacimiento como afirmación y luego como especulación);
- la separación entre ideas del autor y de terceros (Justin Welsh, John Hugh, Vitali, Dickie Bush, Sahil Bloom, Devon Eriksen, Heinlein, Fuller, Schmachtenberger, Naval, Watts).

No encontré ninguna unidad reducida a una mención cuando el material traía mecanismo, condiciones y ejemplos, así que no registro ninguna PÉRDIDA. Los hallazgos son matices de atribución, de presentación de la evolución y de progresión.

---

## Capítulo 19 — You are the niche

### 2. Unidades declaradas como cubiertas pero solo mencionadas

Sin hallazgos. Todas las unidades revisadas están explicadas con su mecanismo, sus condiciones y sus ejemplos. Algunos casos verificados:

- **Business matrix** (U-010-154, U-010-155): definición, analogía con la social matrix y objeción por motivo ("escape the mechanical... lifestyle").
- **Patrón de los cursos y sus costos** (U-010-095, U-010-096, U-010-039, U-010-158, U-012-097, U-010-161): tabla de los cuatro pasos, la concesión "still works", los tres problemas con la objeción de la "dissonance", la parodia de las soccer moms y el doble sentido del shiny object syndrome.
- **Reality is not niched down** (U-008-010, U-011-228, U-027-147): las tres formulaciones están completas, incluida "Warriors lack brains and intellectuals lack balls".
- **Niche of one y sus fuentes** (U-010-043, U-005-045, U-005-047, U-004-025, U-015-136): también la condición de las hard skills.
- **Unconscious competence** (U-010-212), con glosa del sentido propio.
- **Las tres versiones tardías** (U-012-166, U-014-125, U-021-225), con tabla de evolución.
- **Experience model y cuatro pilares** (U-007-059, U-008-059, U-006-130, U-001-021/U-007-060, U-023-132, U-023-167, U-007-209, U-010-191, U-021-032): incluye la nota textual de que en la segunda pasada de 2022 falta el pilar 4.
- **Build, write and sell to yourself** (U-010-011, U-006-112 con Kinobody, U-010-059, U-010-162, U-009-205 con los 10 tweets, U-016-127, U-016-130, U-007-171/U-001-109, U-015-065).
- **Customer avatar** (U-010-176, U-010-177, U-010-178, U-010-304, U-011-159, U-009-078, U-016-013).
- **Ideal reader en tres tiempos** (U-011-111/U-001-072, U-011-239), Myers-Briggs (U-002-050) y public schools (U-002-049, U-008-018).
- **Guests** (U-004-002, U-004-016, U-004-007, U-002-052 con las dos direcciones del two-year test).
- **Presence of the customer** (U-004-042, U-004-043, U-004-044), con la tensión de Cortex.
- **Eternal markets** (U-012-030, U-012-099, U-015-178, U-010-174, U-001-018, U-001-129/U-007-128, U-007-011, U-007-206, U-008-029, U-023-093, U-012-029, U-016-128, U-009-132, U-010-074, U-010-192, U-010-184, U-010-071, U-011-165, U-008-024, U-010-057, que incluye la nota sobre el lapsus "almost impossible to make money").
- **Broad catch** (U-007-079, U-010-108, U-009-197, U-014-070, U-009-124, U-010-204, U-009-138, U-014-050, U-008-161, U-017-047, U-012-049, U-010-166, U-010-167, U-012-048, U-015-079, U-002-009, U-010-106, U-008-011).
- **Ejercicios y argumentos de 19.6** (U-009-235, U-001-058, U-021-041, U-010-258, U-008-147, U-010-015, U-010-104, U-012-060, U-010-164, U-010-014, U-013-060, U-002-007, U-010-168, U-014-044, U-013-057, U-013-058, U-013-061, U-005-107, U-005-108, U-005-109, U-007-102, U-027-155, U-026-145, U-027-191, U-002-024, U-002-006).
- **Book to Brand** (U-010-024, U-010-022, U-010-025, U-010-031/U-010-044, U-010-032, U-010-038, U-014-051, U-010-194, U-010-195, U-010-196, U-010-197, U-010-213).

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

Sin hallazgos. Están todos los ejemplos y números del material, con su estatus de estimación o ilustración marcado. Algunos ejemplos:

- 5.000 creadores, 50 %+ INFJ, 95 % de problemas de supervivencia, 80 % de principiantes, 80/20 y 20/80;
- 5.000 frente a 20.000 seguidores y 30.000 frente a 300.000, de 900.000 a 1.500.000 por efecto red;
- 3 millones frente a 10.000, 100.000 frente a 10.000;
- $100 al día frente a $5 millones;
- el hilo de las abejas de Sahil, Codie Sanchez, el Rubik de Dickie en unos 18 segundos;
- el videógrafo de la página duplicada (Vitali), United Airlines/Comcast, el planner de 50 habilidades, EDM, Steve Cook y "the modern conqueror".

Los únicos detalles ausentes son triviales y no los cuento: "society is no longer fragmented" no pertenece a este capítulo; la referencia del ejemplo de U-016-013 remite a otra unidad.

### 4. Términos acuñados no definidos u homogeneizados

- **MENOR — "niche" en su sentido propio (léxico: U-010-172, U-010-189, U-010-175).**
  - **Lo que registra el léxico:** tres definiciones del autor: "a perspective or worldview", "the frame of big goals and burning problems that compose your worldview" y "what you are interested in and why it's important to your life".
  - **Lo que deja el capítulo:** solo la tercera (19.2, "Nicheless") y la definición del customer avatar como worldview (19.3, 19.4). No define el nicho mismo como cosmovisión, aunque es el capítulo sede del término.
  - **Dónde está:** esa definición aparece en el capítulo 22 (línea 80, "Your niche is the frame of big goals and burning problems...").
  - **No es pérdida:** el material de esas unidades no pertenece al lote del capítulo 19. Lo que falta es una remisión en 19.2 o 19.4 al capítulo 22.

El resto de los términos del Anexo B están definidos con su sentido propio y no se diluyen en un genérico. Entre ellos: business matrix, niche of one, nicheless, experience model, four pillars of the one-person business, four pillars of you (distinguido de los pilares del negocio), Eternal markets, experience vessel, broad catch / specific sale, a landing page is content, specificity for impact, base audience, glorified search engine, ideal reader, promotion schedule, offer-driven content, enemy of your brand y brand is the depth behind everything.

Las palabras comunes con sentido propio (unconscious competence, hot leads, network effect, customer avatar, niche down) se glosan expresamente en su uso del autor.

### 5. Cambios de posición (Anexo A) no presentados o resueltos indebidamente

- **MENOR — EV-193 (pilares: de cuatro a tres y sus metáforas).**
  - **Lo que dice el capítulo (19.2):** "the metaphors migrate: 'map' is applied to the product in one 2023 version and to content in the 2.0 version".
  - **El problema:** la tabla de versiones del capítulo no incluye esa versión de 2023 (U-008-025, 2023-03: brand = story, content = school, product = map). Tampoco incluye las de 2022-12 (what/how/why), 2023-11 (macronutrients), 2024-01 ("your philosophy is your brand") ni las cuatro de 2026. El lector no puede comprobar la afirmación sobre "map" con lo que tiene delante.
  - **Dónde está:** el capítulo 28 desarrolla la secuencia completa (líneas 943–996).
  - **Qué falta:** una remisión al capítulo 28 junto a la tabla, o bien no afirmar el desplazamiento de "map" sin mostrar la versión.

**Presentadas correctamente y sin resolución indebida:**

- EV-082, EV-157, EV-159, EV-166, EV-171, EV-174, EV-185, EV-188, EV-189, EV-190, EV-194, EV-222, EV-240, EV-275 y EV-305. Las tensiones se registran como tales y las lecturas conciliadoras se marcan como no dichas por Koe.
- EV-180, EV-181 y EV-186 tienen aquí su parte central. Sus extremos tardíos tienen sede en otros capítulos:
  - "you are the infinite niche": capítulos 22 y 27;
  - "experiment with ideas until people tell you": capítulo 26;
  - "your mission is your niche": capítulos 22 y 32;
  - lead magnet como "first niche": capítulo 30.
- EV-187: el capítulo 19 presenta la parte que le toca; el capítulo 4 tiene la tabla completa.
- EV-146: no aparece aquí, pero está en los capítulos 21 y 23.

### 6. Fuentes de terceros cuya atribución se perdió, se confundió o se alteró

- **MENOR — Origen de "niche of one" (U-005-045; léxico "niche of one").**
  - **Lo que registra el léxico:** "acuñado por: Dan Koe (Justin Welsh lo usa en 2021)".
  - **Lo que dice el capítulo:** abre la subsección con el título "Where the term comes from: Justin Welsh" y afirma: "The phrase 'niche of one' did not originate with Koe".
  - **El problema:** el corpus solo muestra que la primera aparición registrada está en boca de Welsh. Que el término no se originara en Koe es una inferencia que el capítulo presenta como hecho. Además choca con la introducción del propio capítulo ("Koe's name for this market is the **niche of one**").
  - **Formulación recomendada:** "la primera aparición en el corpus es de Justin Welsh (2021)", sin afirmar la autoría.
- **MENOR — Dirección de la influencia en "escape competition through authenticity" (U-004-025, U-015-136).**
  - **Lo que dice el capítulo (19.2):** "The idea that authenticity removes competition reaches Koe through two later sources, both of which go back to Naval Ravikant."
  - **El problema:** la frase sugiere que Koe recibe la idea de esas fuentes. Pero Koe ya la formula en 2021 ("your conditioning... makes it so nobody can compete with you", U-005-047). De las dos "fuentes", una es John Hugh (2025) y la otra es el propio Koe citando a Naval directamente (2025). El material no registra derivación alguna.
  - **Formulación recomendada:** "en 2025 la idea aparece vinculada explícitamente a Naval por dos vías".

Las demás atribuciones son correctas y están bien separadas de las ideas del autor:

- Wilber/holon y Koestler (contexto complementario);
- Kevin Kelly vía Welsh;
- Naval como fuente de "escape competition";
- Myers-Briggs, con su validez cuestionada;
- Hormozi y "sell to the rich", como alternativa y no como tesis de Koe;
- Paul Graham para "do things that don't scale";
- el tweet no identificado del life coach;
- Codie Sanchez, con la grafía "Cody" anotada;
- el patrón de los cursos de freelancing.

### 7. Argumentos construidos por capas reducidos a su conclusión

Sin hallazgos. Las cadenas largas se conservan paso a paso y en varios casos se explicitan como cadena:

- realidad interconectada → persona interconectada → negocio no compartimentable (U-008-010, U-011-228, U-027-147);
- U-011-159: identidad → perspectiva → contenido → audiencia que comparte perspectiva → meta → modelo holístico;
- U-016-013: el valor se percibe por identidad, de ahí el yo pasado;
- U-010-158 (los tres problemas, con la objeción intermedia);
- U-016-130 (el bucle contenido → producto → mejora y la lectura precisa de "you can't really fail");
- U-012-099 (la objeción "what if everyone goes down the same path?" y su respuesta);
- U-013-058 (el win-win de la intersección fitness/marketing).

### 8. Conceptos usados antes de introducirse

- **MENOR — "meaning economy".**
  - **Dónde aparece:** 19.4 (U-015-178): "Everyone in what he calls the meaning economy (Chapter 36)".
  - **El problema:** es la primera aparición del término en el libro (no figura en los capítulos 1–18) y no lleva glosa. Solo remite al capítulo 36, donde se desarrolla.
  - **Qué falta:** media frase de glosa.

Los demás términos nuevos del capítulo se glosan en su primera aparición: interest graph, influencer economy frente a creator economy, value creator, second subconscious, time under attention, Ship 30 for 30, Digital Economics/Modern Mastery.

---

## Capítulo 20 — El generalista y el segundo Renacimiento

### 2. Unidades declaradas como cubiertas pero solo mencionadas

Sin hallazgos. Casos verificados:

- **Fábrica de alfileres** (U-010-268), con contexto complementario que precisa la cifra de Smith.
- **Productivity as God** (U-022-209), **instituciones y escuela** (U-010-269, U-027-195, U-016-213).
- **Great Pirates** (U-006-084, U-006-085, U-013-204): los ocho pasos, la lección y las tres matizaciones.
- **"Only slaves"** (U-019-080, U-013-210), con la nota sobre Eriksen.
- **Pájaro de pico largo** (U-012-085, U-006-087), **one-trick pony** (U-012-044) y **culturista lesionado** (U-012-045), con la tipología de los tres modos de fallo.
- **Heinlein** (U-007-046/U-001-009, U-001-010/U-007-047, U-010-219), con el autotest del pañal.
- **Specialists are tools / attached to the skill** (U-010-226, U-013-206).
- **Schmachtenberger y la variante "deep specialist"** (U-006-083, U-012-096).
- **Artificial stupidity**: U-006-020, U-006-021, U-006-026 (con el límite "nothing magical about meat"), U-006-028 y U-021-218.
- **Hyper-specialists y labor as leverage** (U-012-086, U-019-060).
- **Tool builder en sus siete versiones** (U-019-055, U-006-025, U-006-088, U-027-193, U-024-227, U-013-207, U-012-141, U-010-291, U-014-191).
- **Definición del generalista**: U-012-052 y U-010-265 (con vessel), además de U-012-053, U-010-279, U-013-205, U-027-196, U-016-257, U-019-052 y U-012-043.
- **Skill stacking**: U-013-036, U-013-038, U-013-039 (el alfabeto circular), U-012-056, U-023-033, U-027-103, U-007-105, U-023-169 y U-013-066.
- **La secuencia de híbridos** (U-011-138, U-011-139, U-012-023, U-017-188, U-013-177, U-026-146, U-025-218, U-022-119).
- **Specific knowledge** (U-011-012, U-011-013, U-011-014, U-011-070, U-008-194, U-021-206).
- **Sección 20.3 completa**, incluido el cubo (U-011-147), con su tabla y su advertencia geométrica.
- **Sección 20.4 completa**: U-018-040, U-012-074 (con el contexto del deadlift), U-010-344, U-011-009, U-027-082, U-011-214, U-010-069, U-011-213, U-012-018, U-012-089, U-012-136, U-011-182, U-016-045, U-016-111, U-003-154, U-016-161 y U-013-035.

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

Sin hallazgos. Están todas las cifras y casos con su estatus:

- 20/48.000 alfileres;
- 50 productos en seis meses;
- 120.000 seguidores en una semana;
- $50k–$300k, $5–10M, $1–5M con márgenes del 90–95 %;
- 20 millones de libros en 50 años;
- top 10–25 % con la autocorrección de "$100 a day" a "a month";
- 500–1.000 true fans;
- los $100M de Zuckerberg;
- animación de 8 horas a 1;
- fases emo/bodybuilder/raver;
- neuro philosophy;
- el caso del videógrafo.

El único detalle omitido ("society is no longer fragmented", U-023-129) es irrelevante.

### 4. Términos acuñados no definidos u homogeneizados

- **MENOR — "hyper-specialists", segunda acepción (léxico: U-006-105, 2024-07).**
  - **Lo que registra el léxico:** además del sentido usado en 20.1 (las computadoras como hiperespecialistas que reemplazan al especialista humano), la acepción "hyper Specialists / deep generalists": computadoras y humanos como "a great combo but not too effective on their own".
  - **Lo que deja el capítulo:** solo la primera acepción, en la que la máquina es amenaza. La relación complementaria no aparece.
  - **Dónde está:** el capítulo 36 la desarrolla.
  - **Qué falta:** una remisión en 20.1, porque el capítulo 20 es la sede del término y la acepción complementaria matiza su lectura.

Los demás términos del Anexo B están definidos en su sentido propio y distinguidos de su sentido común o de terceros. Entre ellos:

- **Sentido propio frente a sentido común:** generalist (por la meta, no por la amplitud); vessel frente a especialidad; specific knowledge en el sentido de Naval, con la advertencia sobre la segunda acepción del autor.
- **Términos de terceros, distinguidos como tales:** deep generalist (de tercero), artificial stupidity y don't be a tool (de Eriksen), five intrinsic drivers (atribuidos a Kotler).
- **Términos del autor, definidos en su sentido propio:**
  - del diagnóstico: programmed to be replaced, prestige of specialization, productivity as a priority, labor as leverage, cycle of centralization and decentralization, AI religion;
  - del generalista: span, specialized generalism y sus variantes, master/strategist, skill stack, skill tree (comparado con su otro uso en el capítulo 10), surface area, unique model of the world, ability to figure it out, become nobody, Curiosity Compass;
  - de la época: second Renaissance y sus renombres, digital renaissance man, global town square, decentralized education system;
  - de la aspiración: everyone is an entrepreneur, the future of work is play, getting paid to play, fountainhead of value, futureproof.

### 5. Cambios de posición (Anexo A) no presentados o resueltos indebidamente

- **MENOR — EV-187 (shiny object syndrome) en su tramo de 2026.**
  - **Lo que dice el capítulo (20.2, "Shiny object syndrome: good and bad"):** resume la evolución, y para 2026 solo da la versión negativa: "in 2026 he says some of his early businesses failed 'thanks to shiny object syndrome'".
  - **Lo que omite:** la defensa de enero de 2026 (U-010-282), del mismo video que más usa el capítulo ("If you have multiple interests, do not waste the next 2-3 years"): cada interés deja un "residue" y "your shiny object syndrome has been trying to tell you this whole time" que la especialización frena el desarrollo.
  - **Por qué importa:** en 2026 la etiqueta se usa en los dos sentidos. Presentarla solo como negativa inclina la lectura de la evolución.
  - **Dónde está:** el capítulo 4 (líneas 660 y 705) tiene esa entrada.
  - **Qué falta:** mencionarla aquí o remitir al capítulo 4.
- **MENOR — EV-003 (conspiración frente a propiedad del sistema), presentación de diciembre de 2025.**
  - **Lo que hace el capítulo (20.1):** presenta bien la convivencia de las dos versiones y remite al capítulo 2 para la sistémica. Al citar la autocita de *Purpose and Profit* (U-013-204, 2025-12-21), enumera como matizaciones solo "just a metaphor", "whether it's a conspiracy theory or not" y "taken out of context".
  - **Lo que omite:** en ese mismo video Koe da la formulación sistémica ("It doesn't have to be a conspiracy theory for the system to naturally take shape of the subconscious desires of the humans at the top", U-013-209), que el capítulo 2 recoge.
  - **Por qué importa:** sin esa remisión, diciembre de 2025 puede leerse como un endurecimiento ("largely true") cuando en realidad es la convivencia de las dos versiones en un mismo video.
  - **Matiz:** no hay resolución indebida; el capítulo declara la tensión no resuelta.
- **MENOR — EV-182 (generalista, especialista e híbridos), puntos intermedios de 2024.**
  - **Lo que hace el capítulo:** su tabla de seis formulaciones se presenta como "the sequence" y concluye que "the weight given to depth... grows steadily toward the 2026 Musashi version".
  - **Lo que omite:** dos puntos de 2024 que el Anexo A incluye: "intelligence stems from generalism, not specialism" (U-020-141, en el capítulo 6) y "most people never master one domain; dominar uno acelera los demás" (U-023-199, 2024-07, en el capítulo 15). El segundo adelanta a 2024 la revalorización de la profundidad que el capítulo sitúa en 2025–2026.
  - **Qué falta:** remitir a los capítulos 6 y 15 o añadir esas filas.

**Presentadas correctamente:**

- EV-121, con remisión al capítulo 15.
- EV-144: la tensión topic tree frente a "all the niching down you need", con la vuelta al mapa en junio de 2026 y la lectura por etapas.
- EV-180, EV-184 (deep generalist frente a deep specialist, sin forzar intención), EV-207, EV-231, EV-239 (con remisión a los capítulos 25 y 36), EV-240 y EV-246.

EV-238 (AGI) no aparece aquí, salvo la excepción de Eriksen, pero tiene sede en el capítulo 36.

### 6. Fuentes de terceros cuya atribución se perdió, se confundió o se alteró

- **MENOR — Estatus de atribución de la cita de Schmachtenberger.**
  - **Lo que dice el capítulo (20.1):** "Koe frames several videos with a quotation he attributes to Daniel Schmachtenberger" e incluye entre esos usos "the opening thesis of the February 2025 video on multiple interests".
  - **Lo que registra el material:** la unidad de ese video (U-010-215) tiene origen "propia" y no consigna la atribución. El léxico ("deep generalist") anota que "dos filas lo registran como de Dan Koe".
  - **El problema:** la atribución no es uniforme en el corpus, y el capítulo la presenta como si Koe nombrara siempre a Schmachtenberger.
  - **Qué falta:** una nota de que en algunas apariciones la cita figura sin autor. La atribución al tercero como fuente de la idea es correcta.

Las demás atribuciones son correctas y precisas:

- Adam Smith, con la cifra precisada;
- Fuller, con la aplicación a la escuela marcada como de Koe;
- Heinlein (*Time Enough for Love*);
- Devon Eriksen: la subsección entera se declara suya y "transcribed as Devon Erickson";
- Naval: specific knowledge, labor as leverage, "top monkey" y "seven billion";
- la cita de da Vinci, marcada como "attributed";
- "jack of all trades", atribuida por Koe a Shakespeare, con contexto sobre Greene;
- Musashi, con el vínculo con Cook-Greuter/Torbert como contexto;
- Alan Watts frente a la fórmula propia "the art of living is getting paid to play";
- Kotler para los cinco drivers, sin atribuir en la fuente;
- Kevin Kelly, sin atribuir en la fuente;
- ikigai, Nosedive, Zuby y los YouTubers de fitness.

### 7. Argumentos construidos por capas reducidos a su conclusión

Sin hallazgos. Se conservan con su secuencia:

- los ocho pasos de los Great Pirates, con la lección y las tres matizaciones;
- el argumento del tool builder, reconstruido en cinco pasos;
- el paralelo de la imprenta en cinco pasos, señalando el paso contestable;
- la cadena de Eriksen (tarea específica → ceguera al contexto → amenaza solo al especialista → "don't be a tool");
- la de labor as leverage (especialización → maquinización → automatización);
- la de skill stacking (tope por habilidad → resultados prometibles → ranking contra la parálisis);
- la secuencia top 25 % → ramificar → ser seguido por uno mismo → producto.

### 8. Conceptos usados antes de introducirse

- **MENOR — "personal monopoly".**
  - **Dónde aparece:** 20.1, en la discrepancia de la cita de Schmachtenberger (U-012-096): "become a 'niche of one' or create your 'personal monopoly'".
  - **El problema:** es la primera aparición del término en el libro (no figura en los capítulos 1–19) y se usa sin glosa.
  - **Dónde se desarrolla:** en los capítulos 23, 27 y 33. El léxico lo registra como adaptado de Naval: volverse irreemplazable persiguiendo la curiosidad genuina.
  - **Qué falta:** una glosa breve o una remisión.

Los demás términos están introducidos antes o se glosan en su primera aparición: metacrisis (capítulo 2), synthesizer (18), skill tree (10), Spiral Dynamics (4, con remisión al 38), beginner hell (15 y 19), Art of Focus, Purpose and Profit, interest-based education, Cortex y value creator.
