# Auditoría de cobertura — Lote 12 (capítulos 23 y 24)

Auditor independiente. Fase 5. Alcance: puntos 2–8 del prompt del auditor para `05_capitulos_en/cap-23.md` y `05_capitulos_en/cap-24.md`, contrastados con `04b_material/cap-23.md` y `04b_material/cap-24.md`. El punto 1 (IDs no cubiertos) lo verificó un script y queda fuera de este reporte.

## Resumen

| Capítulo | PÉRDIDAS | MENORES |
|---|---|---|
| 23 — Estructura y atención | 0 | 6 |
| 24 — Proceso y ecosistema de contenido | 0 | 5 |

**Método y muestra.**

- Leí completos los dos capítulos.
- Comprobé que el bloque `<!-- COBERTURA: -->` de cada capítulo coincide exactamente con las unidades del material: 142 en el 23 y 145 en el 24, sin faltantes ni sobrantes.
- Del material revisé el 100 % de las unidades (no solo el 40 % exigido). En cada una leí `tipo`, `desarrollo`, `ejemplos`, `cita`, `origen`, `fuente` y `tension`, y las comparé con el texto del capítulo, sección por sección.
- Pasé además tres controles automáticos:
  - **Citas.** Busqué la cita clave de cada unidad en el capítulo, en ventanas de cuatro palabras. Las pocas sin coincidencia literal (siete en el 23 y cuatro en el 24, casi todas con cita "ninguna" o de menos de cuatro palabras) las revisé a mano. Todas están desarrolladas con otras palabras.
  - **Cifras.** Extraje todos los números de `desarrollo` y `ejemplos` de cada unidad y comprobé que aparecen en el capítulo, en cifra o en palabra. No falta ninguno.
  - **Fechas.** Contrasté la fecha que el capítulo atribuye a cada pasaje con la `fuente` de la unidad. Solo encontré los desajustes que se registran abajo.
- Revisé el 100 % de las entradas del Anexo A: 16 en el capítulo 23 y 20 en el 24. Cuando la entrada se desarrolla en otro capítulo, comprobé si el capítulo auditado remite a él.
- En el Anexo B comprobé de forma automática la presencia de todos los términos (87 en el 23 y 81 en el 24) y leí completas todas las entradas. Revisé a mano las variantes que el script no encontró: "imitate and then innovate", "journaling and writing", "structure versus content", "abstracted up a layer", "owned audience", "release date" y similares. Todas están.
- En el Anexo C leí todas las entradas: 26 en el 23 y 25 en el 24. Son menos de 30 porque el anexo no tiene más.
- Para la progresión consulté `04_arquitectura.md`. También busqué en los capítulos anteriores cada término que los capítulos usan o remiten:
  - time under attention, pain and process, conceptual survival y your own little world;
  - beginner hell, golden nugget, topic tree, value creator, permissionless leverage y monk mode;
  - Kortex, Cortex y Eden;
  - la química "up/down" y los micronutrientes;
  - las "eight steps of value creation", "saturation doesn't exist" y otros.

**Juicio global.** Los dos capítulos tienen una fidelidad muy alta. No encontré ninguna unidad con mecanismo, condiciones y ejemplos reducida a una frase, así que no registro ninguna PÉRDIDA. Conservan casi literalmente los mecanismos, las cadenas argumentales, los ejemplos y las cifras, con fuente y fecha. Por ejemplo:

- **Capítulo 23:**
  - el experimento del ghostwriter (≈100 frente a 20.000 likes);
  - las dos versiones de los diez mandamientos en tabla comparada;
  - la cadena negativity bias → conceptual survival;
  - la cadena de John Hugh ("meat boxes", "naked hot people and funny dumb memes");
  - la evolución problem → context → steps en tabla;
  - APAG con sus cuatro ejemplos;
  - la escalera PAS → pirámide → cross-domain synthesis.
- **Capítulo 24:**
  - los tres inventarios para llenar el outline (preguntas, elements, predictable forms) en tabla cruzada;
  - el iceberg y el catfish;
  - las cifras de Reels, Twitter y YouTube frente a los 3–4 millones;
  - las versiones del ecosistema en tabla;
  - la historia de Ryan Deiss reinterpretada;
  - la escalera de validación;
  - el plan de lanzamiento;
  - la posición sobre la IA en orden cronológico, con sus dos tensiones no resueltas.

Las atribuciones a terceros están cuidadas. El contexto complementario está marcado y es correcto: Minto, Whitman, E. St. Elmo Lewis, Maya Angelou, Pascal, Freytag, Schwartz, Kevin Kelly, Eric Ries, Masterson y Forde, Lieberman.

Los hallazgos son matices de tres tipos:

- dos errores de datación causados por pasajes de 2022 que reaparecen en la compilación de 2024;
- varias tensiones del Anexo A que el capítulo presenta solo en parte o sin remitir al capítulo donde se desarrollan;
- una corrección de Koe a un invitado que no se menciona;
- un concepto que se usa antes de introducirse.

---

## Capítulo 23 — Estructura y atención

### 2. Unidades declaradas como cubiertas pero solo mencionadas

Sin hallazgos. Todas las unidades de tipo framework, proceso, método, historia, caso, ejemplo, metáfora, dato, término acuñado, fuente de tercero y argumento están explicadas con su mecanismo, sus condiciones y sus ejemplos. Algunos ejemplos:

- **Training wheels y separación estructura/contenido** (U-015-109, U-009-126, U-008-163, U-015-112, U-010-323, U-016-288): con el desglose del post "how to get ahead of 99%", la reescritura "meditation sprints", la matriz 3×3 y el 80/20 del contenido.
- **La objeción de autenticidad** (U-014-088, U-015-128, U-015-068, U-014-095, U-014-100): con sus tres razones, "paint between the lines" y el ejemplo keto.
- **Pyramid principle en sus dos posiciones** (U-014-091 como "meta framework" y U-022-199 como framework "intermedio"): con la cita de Hormozi y la regla de preguntar "why" de tres a cinco veces.
- **Hooks:**
  - el regalo (U-014-190);
  - PPP con sus dos tweets (U-001-094, U-013-027 a U-013-029);
  - los seis bloques (U-013-152, U-013-153);
  - el framework de Welsh (U-005-025, U-005-026);
  - looks before depth (U-027-245, U-027-246);
  - el índice frente a la acción (U-014-146).
- **Los diez mandamientos en sus dos versiones** (U-013-107 a U-013-121 y U-015-101 a U-015-108), la tríada previa (U-011-109, U-011-238) y la legibilidad (U-013-125, U-009-202).
- **Educación, entretenimiento e inspiración en sus tres formulaciones** (U-009-014, U-013-129, U-016-074), el caso Red Bull (U-010-207) y la mesa de Stan (U-004-008 a U-004-017).
- **La historia:**
  - la mente como sense-making machine (U-014-090);
  - Eriksen (U-006-022, U-006-041, U-006-045);
  - el curiosity loop y "cold spot on the side of the bed" (U-013-123, U-027-252);
  - "your message must mimic the universe" (U-017-191);
  - sales is storytelling (U-009-248, U-001-131, U-009-134, U-009-135);
  - Sahil Bloom (U-005-117, U-005-118).
- **Long form:**
  - PAS y PASO (U-022-196, U-022-197, U-014-097);
  - BPAS (U-014-166);
  - APAG completo (U-013-150 a U-013-158);
  - cross-domain synthesis (U-022-200);
  - el análisis de lo que comparten AIDA, PAS y PASTOR (U-013-149).

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

Sin hallazgos relevantes. El control automático confirma que todas las cifras de las unidades están en el capítulo. Las únicas omisiones son triviales y no las computo:

- el ejemplo de 2025 del mandamiento 1 ("here's seven steps to achieve [desired outcome]") (U-015-102);
- la mención del tweet "how to get ahead of 99% of people" como ejemplo de convicción (U-015-106);
- el swipe file gratuito (U-013-161);
- el atajo de captura de Kortex, option+C (U-015-101).

### 4. Términos acuñados no definidos u homogeneizados

- **MENOR — "mental monopoly" (U-001-131).**
  - **El capítulo:** en 23.5 ("Your story is your brand") escribe "one has a personal monopoly, or what Koe calls a **mental monopoly**". Lo usa como sinónimo de personal monopoly, sin definirlo ni remitir.
  - **El léxico** (`03c_lexico.md`) registra dos acepciones:
    - (2022–2024) "tener grandes ideas que la gente asocia contigo";
    - (2024-02) "historia propia más consejos accionables en línea".
  - **Los otros capítulos:**
    - El capítulo 18 (18.4) ya presentó "the mental monopoly" con la primera acepción ("big ideas that stick in people's heads").
    - El capítulo 27 (27.5) explica que en el mismo video Koe pasa de usar ambos términos como sinónimos a presentar el mental monopoly como "the next thing" más allá del personal monopoly.
  - **El problema:** el lector del 23 encuentra la equivalencia sin aviso, y choca con la definición que ya leyó en el 18.
  - **Debería ir:** en 23.5, una frase que marque que aquí se usa con su segunda acepción y que remita a 18.4 y 27.5.

### 5. Cambios de posición no presentados o "resueltos" indebidamente

Presentes y bien tratados:

- **EV-146** (training wheels frente a "resist the template"), con resolución marcada como lectura del corpus.
- **EV-150** (atención o ideas), como tensión no resuelta.
- **EV-152** (de tres hooks a diez mandamientos).
- **EV-153** (fast content y epistemic commons), sin retractación de la defensa del hook.
- **EV-156** (pirámide y problema primero), como refinamiento.
- **EV-158** (estructura de 1.000 palabras), en tabla.
- **EV-213** (excluir a la audiencia).
- **EV-216** (frameworks de copywriting).
- **EV-220** ("manipulation").
- **EV-300** (cifra truncada de Digital Economics).
- **EV-109** ("as a beginner prescriptions are very good").
- **EV-160**, con remisión al capítulo 24, que efectivamente lo desarrolla.
- **EV-021, EV-054 y EV-151**: en la medida que corresponde al capítulo.

Hallazgos:

- **MENOR — EV-150, datación de "the name of the game" (U-001-069).**
  - **El problema:** el recuadro "An unresolved tension: attention or ideas?" de 23.2 dice: "In 2024 he called capturing attention 'the name of the game'". Pero U-001-069 es la reaparición, en la compilación del 2024-02-06, de un pasaje del video "The Rise Of The Value Creator" del 2022-10-31 (U-011-108; misma secuencia que U-011-109 y U-011-110).
  - **La contradicción interna:** el propio capítulo, en 23.3 ("From three hooks to ten commandments"), fecha ese mismo pasaje en octubre de 2022.
  - **Efecto:** la cronología de la alternancia queda distorsionada. En realidad Koe dijo en octubre de 2022 tanto "the value inside does not matter until you catch attention" (día 9) como "the name of the game" (día 31), y en diciembre de 2022 "it's about valuable ideas". El recuadro sugiere un vaivén de vuelta en 2024 que no existe. La conclusión (no hay resolución cronológica) se mantiene.
  - **Debería ir:** en 23.2, fechar en octubre de 2022 y anotar que reaparece en 2024.
- **MENOR — EV-154, polo "fluff" ausente del recuadro.**
  - **Lo que tiene el capítulo:** el recuadro "An unresolved tension: actionable or philosophical?" de 23.4 reconstruye la cronología: 2022, marzo y mayo de 2023, enero de 2024, 2025 y 2026.
  - **Lo que omite**, del lado favorable a lo filosófico:
    - "I love fluff" (U-008-017, 2023-03-12);
    - las semillas no prescriptivas (U-027-094, 2023-06);
    - la defensa de sus piezas largas frente al 90 % que pide "cut the fluff" (U-020-145, 2024-08).
  - **Por qué importa:** son los puntos que equilibran la tensión. Se desarrollan en 22.5 ("Perspective over prescription: in defense of 'fluff'"), pero el recuadro no remite allí, y el lector ve una serie inclinada hacia lo accionable.
  - **Debería ir:** en 23.4, una frase con remisión a 22.5.

### 6. Atribución de fuentes de terceros perdida, confundida o alterada

Las atribuciones están cuidadas:

- **Welsh:** "The framework is entirely Welsh's".
- **Stan:** las ideas son de Hugh y Vitali, salvo "make tangibility tangible", que es de Koe.
- **Eriksen:** "These are Eriksen's ideas, not Koe's".
- **Bloom:** se presenta como suyo.
- **Alan Watts:** con la incertidumbre del "scop".
- **Cialdini:** solo lectura recomendada, no fuente de la tríada.
- **Contexto complementario:** Neil Patel, Deida, Red Bull (en sus dos versiones, la de Hugh y la de Koe), James Clear, Minto, Whitman, Schwartz y Pascal.

Hallazgo:

- **MENOR — Eriksen, "intelligence is stories" (U-006-022, U-006-041), sin la corrección de Koe.**
  - **El capítulo:** en 23.5 ("Executive function as storytelling: Devon Eriksen") recoge que Koe "mentions an article in which Eriksen defined intelligence as the ability to tell stories". Después construye una inferencia: "If the same faculty does both, then the skill of structuring a post and the skill of planning a life are not merely analogous; they are exercises of one capacity".
  - **Lo que omite:** en esa misma conversación Koe discrepa de la noción (U-006-011): "maybe intelligence wasn't the right word for me to use but perspective", la capacidad de "create a story because you can see further". Eriksen, por su parte, reformula el debate como "effectiveness".
  - **Dónde está:** el Anexo C registra la discrepancia, y los capítulos 3 (3.3) y 38 (38.3) la desarrollan.
  - **El problema:** el lector recibe la tesis del invitado sin saber que el autor la corrigió. La inferencia del capítulo está marcada como propia, pero se apoya en ella.
  - **Debería ir:** en 23.5, una frase con remisión a 3.3.

### 7. Argumentos por capas reducidos a su conclusión

Sin hallazgos. Las cadenas argumentales se conservan paso a paso, entre ellas:

- las tres razones de U-014-088, con la ironía final "keep getting the results you've been getting";
- la cadena negativity bias → amenaza a la identidad → supervivencia conceptual (U-013-110);
- la cadena de seis pasos de John Hugh (U-004-009);
- looks → depth → oportunidades, con la lectura "you only care about the looks until you are exposed to the depth" (U-027-245, U-027-246);
- promotions → why → transformation → story (U-009-134);
- lead → agitación → superación → testimonios → frontera de la estafa (U-001-131);
- las tres mecánicas comunes de los frameworks y las tres entregas posteriores (U-013-149).

### 8. Conceptos usados antes de introducirlos

- **MENOR — "the eight steps of value creation" (U-011-177).**
  - **El problema:** en 23.6 ("Copywriting: what it is and what its frameworks share") el capítulo da una instrucción operativa que el lector no puede seguir: "pair them with what he calls the eight steps of value creation (presented in Chapter 31)", y "everything 'above the fold' is where one tries to fit and summarize all eight steps". No dice cuáles son los ocho pasos: awareness, angle, big problem, unique mechanism, benefits, proof, big idea y risk reversal (capítulo 31, "The eight steps: 'marketing Legos'").
  - **Diferencia con otras remisiones adelantadas:** los "micronutrients, discussed in Chapter 31" de 23.5 van glosados ("the smaller elements of value"). Aquí no hay glosa.
  - **Debería ir:** en 23.6, una enumeración de una línea de los ocho pasos o una glosa.

No encontré otras violaciones. Los demás términos se introducen antes o se glosan donde aparecen:

- **Introducidos en capítulos anteriores:**
  - time under attention (21);
  - pain and process (17);
  - law of conceptual survival (3);
  - your own little world (8 y 11);
  - beginner hell (22);
  - value creator (18).
- **Glosados en el capítulo:** los levels of awareness, con contexto complementario y remisión al 32; "anomaly", con remisión al 26; la etapa "achiever", con remisión al 38.

### Nota adicional (datación)

- **MENOR.** En 23.1 ("The structure problem"), tras citar el video de febrero de 2025, el capítulo dice "Two years earlier, in a November 2023 video…". Entre noviembre de 2023 y febrero de 2025 hay unos 15 meses. Debería decir "Some fifteen months earlier" o "In November 2023".

---

## Capítulo 24 — Proceso y ecosistema de contenido

### 2. Unidades declaradas como cubiertas pero solo mencionadas

Sin hallazgos. Todas las unidades de tipo framework, proceso, método, historia, caso, metáfora, dato, término acuñado, fuente de tercero y argumento están desarrolladas con su mecanismo, sus condiciones y sus ejemplos. Algunos ejemplos:

- **El proceso semanal:**
  - los cinco componentes (U-014-189);
  - brain dump → outline "problem, insight, solution" → draft (U-021-229);
  - las cuatro páginas (U-014-102);
  - el outline con más de una semana de antelación (U-018-189);
  - el outline como "frame of reference" (U-021-119);
  - el canvas y el project board de Eden (U-016-273, U-014-199);
  - los meta documents (U-014-110);
  - las seis preguntas con la "consequential cascade" (U-021-185);
  - los elements (U-013-156), con la aclaración de sus tres acepciones;
  - las predictable forms (U-022-201);
  - el writer's block como incubación (U-023-041, U-026-029).
- **Un solo organismo:**
  - las tres capas (U-014-153, U-014-154, U-014-151, U-014-156);
  - "attention held over time", con la tensión frente a su dependencia de los tweets (U-017-067);
  - el iceberg y el catfish (U-018-009, U-018-012, U-018-014, U-018-015);
  - "building a world" (U-004-024);
  - spray and pray y traffic firepower (U-009-245).
- **El ecosistema:**
  - todas sus versiones (U-013-022, U-002-100, U-017-066, U-009-021, U-016-030, U-006-190, U-016-289, U-010-327, U-014-197, U-014-200);
  - la mecánica en tres pasos (U-009-029, U-009-031, U-009-032);
  - el caso 2 Hour Writer en sus seis relatos.
- **La newsletter como hub** (U-009-022, U-009-023, U-010-144, U-010-145, U-011-236, U-012-106, U-014-150, U-014-157, U-017-195, U-007-076, U-014-169).
- **La escalera de validación y "sell before you build"** (U-009-244, U-014-161, U-015-127, U-009-164, U-004-036, U-026-218, U-009-184, U-009-189, U-015-156, U-004-035).
- **Las once posiciones sobre la IA**, con su tabla cronológica.

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

Sin hallazgos. El control automático confirma que todas las cifras de las unidades están en el capítulo, entre ellas:

- $300, $1.000, $10.000 y 3–4 millones;
- 1,6 millones de vistas y unos 600 seguidores;
- 50 y 500 ideas validadas;
- $100.000 de Deiss;
- 50.000 lectores;
- $10 y 2,5 %;
- 1–2 semanas y 3–4 semanas;
- 10–15 tweets por hilo;
- 1.000–1.500 palabras;
- 15 minutos;
- 23 posts en 2 horas.

Las omisiones son referencias a otros videos y no las computo:

- "learn AI in ~30 minutes" (U-013-199);
- "You have about 36 months to make it" (U-023-211);
- el video sobre ideas infinitas (U-002-104).

### 4. Términos acuñados no definidos u homogeneizados

Sin hallazgos. El capítulo define o glosa explícitamente casi todo el léxico del anexo. Además señala cuándo una palabra común lleva un sentido propio, entre otras:

- brain dump, frame of reference y elements (con sus tres acepciones);
- cross-post, deplatform (con la inversión del sentido habitual), validate y prototype;
- lowest common denominator ("without any negative sense") y moat;
- vessel y one-person media company (con sus varias acepciones).

### 5. Cambios de posición no presentados o "resueltos" indebidamente

Presentes y bien tratados:

- **EV-145** (eje, dirección y cross-posting), en tabla y con la distinción entre reescribir y cross-postear.
- **EV-148**, con la puerta de entrada como desacuerdo genuino.
- **EV-149 y EV-127**, como dos tensiones no resueltas.
- **EV-155** (volumen frente a escasez).
- **EV-160** (cifras de escritura diaria).
- **EV-161** (proceso y herramientas).
- **EV-173** (anuncios).
- **EV-204** (dos sentidos de MVP).
- **EV-223** (promoción).
- **EV-301** (plazos aplicados al equipo).
- **EV-154 y EV-217**: en la medida que corresponde al capítulo.

Hallazgos:

- **MENOR — EV-148, la puerta de entrada fechada con una reemisión.**
  - **El problema:** el último párrafo de 24.4 dice "…in January 2024 he said the newsletter 'can wait'; and in 2024 he again recommended that 'everyone start a newsletter'". La tabla de 24.2 ("How the position evolved") pone en la fila de 2024 "Everyone should start a newsletter". Esa frase es U-001-073, de la compilación del 2024-02-06, que reproduce el video del 2022-10-31 (U-011-115).
  - **La contradicción interna:** el propio capítulo, en 24.4 ("Deplatform your audience"), fecha ese pasaje en octubre de 2022 y añade "repeated in the 2024 compilation".
  - **Efecto:** el "again" presenta como vuelta atrás de 2024 una recomendación de 2022.
  - **Omisión menor:** el mismo párrafo no recoge la indicación de octubre de 2023 de que 2 Hour Writer enseña a empezar por el long form "o incluso un libro" (U-004-157), que el anexo registra en esta tensión y que el capítulo 25 desarrolla.
  - **Debería ir:** en 24.2 (tabla) y 24.4, corregir la fecha y añadir la mención con remisión al 25.
- **MENOR — EV-149 y EV-127, hitos citados sin pasaje ni remisión.**
  - **El problema:** en 24.6 el capítulo da como hechos varios hitos sin mostrar el pasaje ni remitir a donde se desarrollan:
    - la fórmula de origen "from 'AI is no use for generating ideas'" (U-018-163, 2024-12; en el capítulo 15);
    - "an earlier warning not to give AI control over one's craft" (U-012-164; en el capítulo 36);
    - "In May 2025 Koe said that AI does not make people stupider" (U-012-146) y "by August… 'a surefire way to become stupid'" (U-025-209), ambos en el capítulo 36.
  - **Hitos de EV-149 que no aparecen:**
    - "de 100 posts, uno publicable" (U-012-127, 2025-02);
    - la decisión de agosto de 2025 sobre cuándo usar la IA y cuándo escribir a mano (U-025-222).
  - **Por qué importa:** el capítulo nunca remite al 36 (36.4–36.5), que es el que reúne esos pasajes. La tabla de 24.6 queda sin el sustento del primer polo, el escéptico, que se cita entre comillas.
  - **Debería ir:** en 24.6, dos o tres frases o una remisión explícita a 15 y 36.
- **MENOR — EV-166, el recuento de seguidores presentado sin la corrección.**
  - **El capítulo:** en 24.4 presenta "follower count no longer represents audience size… An email list is the new status symbol" (U-014-150) como nueva premisa del argumento de la lista. Concluye: "The corpus describes this line of argument not as a change of position but as an expansion". La frase es correcta para el argumento de la lista.
  - **Lo que no dice:** sobre los seguidores, EV-166 registra una corrección. Entre 2022 y 2023 Koe medía su leverage en seguidores y se burlaba de quien decía que no importaban (U-007-126, U-004-139).
  - **Dónde está:** el capítulo 25 (25.4) y el 26 (26.1) lo presentan como "a genuine change of position". El 24 no lo marca ni remite.
  - **Debería ir:** en 24.4, una frase con remisión a 25.4.
- **MENOR — EV-200, "sell before you build" sin la tensión de la secuencia de arranque.**
  - **El capítulo:** en 24.5 ("Sell before you build") presenta el método como la respuesta de Koe "developed mainly in 2023–2025".
  - **Lo que omite:** EV-200 lo registra como contradicción no resuelta frente a otras indicaciones del corpus:
    - "we need traffic before we need an offer";
    - "become an authority" antes del producto digital (U-009-147);
    - el "data-driven product" tras 6–12 meses;
    - "I would build the service first so you can make money faster" (U-008-154, 2024-12).
  - **Dónde está:** los capítulos 28 (28.5), 29 (29.4) y 33 (33.3) presentan la tensión. El 24 no remite.
  - **Debería ir:** en 24.5, una frase de remisión a 29.4.

### 6. Atribución de fuentes de terceros perdida, confundida o alterada

Las atribuciones están cuidadas:

- **Welsh:** "The position here is Welsh's; Koe's contribution is agreement".
- **Conrad (Teachable):** vía Vitali, "The advice is Conrad's, relayed by Vitali".
- **Naval:** con la extensión marcada como de Koe.
- **Lieberman:** con contexto complementario sobre Morning Brew.
- **Deiss:** con la reinterpretación de Koe y la advertencia de no citar las cifras.
- **Kevin Kelly:** "1,000 true fans" sin autor nombrado por Koe.
- **Jim Claire:** identidad no confirmada.
- **Eriksen:** "clearly marked as the guest's view".
- **Max Planck Institute:** como hallazgo de tercero sin detalles.
- **Cook-Greuter:** como material ajeno resumido con IA.
- **Breakthrough Advertising y Great Leads:** con sus autores como contexto complementario.
- **Stan:** con advertencia sobre la relación personal del autor con su equipo.

Hallazgo:

- **MENOR — "Gary Halbert or David Ogilvy" (U-026-029): la incertidumbre se deja abierta sin remitir a la aclaración posterior del corpus.**
  - **El capítulo:** en 24.1 ("Writer's block as incubation") dice: "The attribution should not be firmed up: the transcript does not settle which copywriter, if either, described this practice". Eso es correcto para el video de 2022.
  - **Lo que omite:** en mayo de 2025 (U-019-125) Koe atribuye sin vacilar a David Ogilvy el mismo patrón, con una paráfrasis de su cita: investigación intensiva, luego desconexión, y "big ideas come from the unconscious", que debe estar "well-informed". El Anexo C lo registra en la entrada de David Ogilvy, y el capítulo 13 (13.1) lo desarrolla.
  - **Debería ir:** en 24.1, una frase que diga que en 2025 Koe atribuye el patrón a Ogilvy, con remisión a 13.1.

### 7. Argumentos por capas reducidos a su conclusión

Sin hallazgos. Las cadenas se conservan completas, entre ellas:

- cinco segundos por tweet → 6–8 horas con Tolle → "power… is how much attention you hold over time" → el long form como pilar (U-017-067);
- la analogía del autor nuevo en Amazon → "short form is your base" (U-014-151);
- el tweet que solo funciona con las "moving pieces" del long form (U-022-177);
- la ingenuidad inicial y la reinterpretación de la historia de Deiss (U-014-157);
- el método de 2 Hour Writer: meta clara → prueba semanal → "newsletter-centric" (U-015-081, U-010-326);
- "don't use AI to write for you" = "don't use AI to articulate your opinions and beliefs", con el caso de las nueve etapas y "it creates a gap that you can then go learn and fill" (U-021-230);
- la sorpresa que no se puede pedir (U-014-126);
- la inteligencia frente a la creatividad (U-021-152).

### 8. Conceptos usados antes de introducirlos

Sin hallazgos que computar. Lo que podría parecer adelantado se introduce antes o se glosa donde aparece:

- **Introducidos en capítulos anteriores:**
  - golden nugget (22);
  - la química "down" (11);
  - default mode network (12–13);
  - goal as lens (6);
  - topic tree (22);
  - broad catch, specific sale (19);
  - permissionless leverage (9);
  - productivity y creativity mode (10 y 13);
  - Eden y Cortex/Kortex (desde el 16).
- **Con contexto complementario:** los levels of awareness, aunque se desarrollan en el 32.
- **Glosados en el capítulo:** Cook-Greuter, con remisión al 38; Cortex University ("his cohort program").

Las referencias a los capítulos 26, 27, 30, 33, 35 y 37 son remisiones adelantadas con glosa suficiente.
