# Auditoría de cobertura — Lote 08 (capítulos 15 y 16)

Auditor independiente. Fase 5, puntos 2 a 8 del prompt del auditor, aplicados a `05_capitulos_en/cap-15.md` y `05_capitulos_en/cap-16.md` y contrastados con `04b_material/cap-15.md` y `04b_material/cap-16.md`. Un script ya verificó el punto 1 (IDs no cubiertos), así que queda fuera de este reporte. No se corrigió nada; este documento solo reporta.

## Resumen

| Capítulo | PÉRDIDAS | MENORES |
|---|---|---|
| 15 — The Mechanics of Skill and the Path of Mastery | 0 | 5 |
| 16 — Reading, Note-Taking and Learning with AI | 0 | 4 |
| **Total** | **0** | **9** |

**Método y muestra.**

- Leí completos los dos capítulos (930 y 728 líneas).
- Hice un control automático sobre el 100 % de las unidades: 202 del capítulo 15 y 141 del 16.
  - Busqué en el capítulo la cita y el campo `desarrollo` de cada unidad, en ventanas de cinco palabras.
  - Busqué también los nombres propios y las cifras de `desarrollo` y `ejemplos` que no aparecían en el capítulo.
  - Cada caso que el control marcó como dudoso lo revisé a mano.
- Leí a mano el campo `desarrollo` completo de una muestra que prioriza los tipos framework, proceso, método, historia, caso, metáfora, dato, término acuñado, fuente de tercero y argumento:

| Sección | Unidades leídas a mano |
|---|---|
| 15.1 | 42/42 |
| 15.2 | 26/34 |
| 15.3 | 13/26 |
| 15.4 | 17/41 |
| 15.5 | 18/18 |
| 15.6 | 9/19 |
| 15.7 | 22/22 |
| 16.1 | 7/18 |
| 16.2 | 42/42 |
| 16.3 | 17/44 |
| 16.4 | 27/37 |

  En las secciones con menos del 40 % leído a mano (15.6, 16.1 y 16.3), el control automático no encontró casi ninguna unidad sin correspondencia literal: casi todas superan el 70 % de coincidencia literal. Las que quedaron por debajo las leí a mano.
- Revisé el 100 % de las entradas del Anexo A: 27 en el capítulo 15 y 18 en el 16.
- Anexo B: comprobé la presencia de todos los términos (119 en el 15 y unos 90 en el 16) y leí la definición de cada uno. Leí completas unas 20 entradas en el 15 y 12 en el 16.
- Anexo C: revisé todas las entradas (22 en el 15 y 42 en el 16).
- Para el punto 8 consulté `04_arquitectura.md` y los capítulos anteriores.

**Juicio global.** Los dos capítulos son de una fidelidad excepcional.

- Conservan casi literalmente el mecanismo, las condiciones, los ejemplos y las cifras de las unidades.
- Reconstruyen paso a paso los procesos numerados (Mastery Method, entrepreneurial method, self-experimentation en cinco y seis pasos, anomaly research, dissect and distill, Core Notes, las cuatro opciones de instrucciones, el flujo de YouTube en siete prompts).
- Citan las dos fuentes en las unidades fusionadas.
- Marcan las cifras retóricas como tales y presentan sin resolverlas las tensiones del Anexo A, incluidas las de plazos (EV-104), overwhelm (EV-117), errores frente a teoría (EV-122), resúmenes (EV-114) y second brain (EV-111).

No hay ninguna unidad con mecanismo y ejemplos reducida a una frase. Los hallazgos son matices: un error de cronología, una tabla de evolución incompleta, una atribución implícita, un vínculo editorial presentado como del autor y algunos términos sin glosa.

---

## Capítulo 15 — The Mechanics of Skill and the Path of Mastery

### 2. Unidades declaradas como cubiertas pero solo mencionadas

Sin hallazgos. Todas las unidades de alta prioridad están desarrolladas con su mecanismo y sus ejemplos. Por ejemplo:

- La Mastery Method (U-020-066), en tabla y repartida luego por las secciones.
- Los ejemplos de Photoshop y copywriting (U-020-077, U-020-078), incluido el árbol con canales y layer mask.
- El puzzle de técnicas y el ejemplo del español (U-020-174, U-020-175).
- La analogía de los 315 lb (U-020-181).
- El cuaderno "My Scientific Projects" en siete pasos (U-024-028).
- El entrepreneurial method paso por paso (U-007-021 a U-007-032).
- Person A y Person B en sus dos versiones (U-027-135, U-024-241).
- La cadena riesgo → sentido (U-027-172), en tabla.
- El caso Kortex (U-015-184, U-015-212), con la atribución ambigua Matt/Ari señalada.
- El modelo mind building (U-020-091), en tabla.
- Bulking and cutting, con la atribución a Dickie Bush de la imagen de la obesidad (U-002-078).

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

Sin hallazgos que alcancen el nivel de MENOR. A título informativo, sin contabilizarlas, se omiten tres trivialidades:

- "dedicate time to finding ideas to channel into your work" (U-025-122);
- el ejemplo de "8 hours a day at the gym" (U-020-091);
- la cifra "$40,000" del título universitario aparece como "forty thousand dollars", así que no es una pérdida.

### 4. Términos acuñados no definidos u homogeneizados

- **MENOR — "pure focus" (léxico: *pure focus*).**
  - Qué tiene el léxico: dos sentidos. En 2025-08 es el estado en que input y output se funden y "dejas de existir"; en 2024–2025, el enfoque total activado por tactical stress.
  - Qué hace el capítulo: §15.2 ("Controlling your reaction…", último párrafo) lo glosa como "the state in which attention is entirely on the task", que es un sentido casi de diccionario. Remite al capítulo 10 para el mecanismo.
  - Impacto: el capítulo 10 sí recoge el sentido propio ("loss of self, merging with the task"), así que la pérdida es menor. Aun así, aquí convendría la glosa del autor o una remisión explícita a esa definición.
- **MENOR — Cortex / Kortex.**
  - Qué hace el capítulo: en §15.2 ("Reverse engineering and emulation") y en §15.7 ("The mind as the digestive system of reality") el software se llama "Cortex, his note-taking software at the time". En §15.5 ("A series of necessary mistakes: Kortex") aparece "Kortex, a second-brain app".
  - Impacto: el capítulo no dice que es el mismo producto con dos grafías. El lector puede pensar que son dos herramientas. El capítulo 16 lo aclara ("Kortex (spelled Cortex in many sources)"), pero llega después.

### 5. Cambios de posición (Anexo A) no presentados o resueltos indebidamente

Las 27 entradas del Anexo A están presentadas. Entre ellas, EV-019, EV-021, EV-051, EV-068, EV-104 (en tabla, con la reconciliación del propio autor), EV-107, EV-109, EV-116, EV-117 (en tabla de dos columnas, sin resolverla indebidamente), EV-118, EV-120, EV-121, EV-122, EV-123, EV-175, EV-178, EV-182, EV-215, EV-228, EV-267 y EV-302. Hay dos excepciones parciales:

- **MENOR — Cronología de "Nature's Compass" invertida (léxico *Nature's Compass*; U-020-081, U-026-121, U-020-060).**
  - Qué dice el capítulo, en §15.5, "Nature's Compass: mistakes as negative feedback": "Chapter 1 noted an earlier use of 'Nature's Compass' (2023) as the name for experimentation itself, the way out of a meaningless life; the 2023 Mastery Method narrows it to mistakes as feedback."
  - Qué dicen las fuentes: ese sentido ("the path out of meaningless living… it's experimentation", U-026-121) viene de `If Your Life Is Spiraling Out Of Control…`, 2024-03-10. Es tres meses posterior a la Mastery Method (2023-12-17). El otro uso de 2023 que cita el capítulo 1 (U-020-060) sale del mismo video de la Mastery Method.
  - Impacto: no hubo un uso "anterior" que luego se estrechara. El orden es el inverso: primero los errores como feedback negativo (2023-12) y después la experimentación como salida del sinsentido (2024-03). Lo confirma el léxico, que fecha los sentidos en 2023, 2024-03-10, 2023/2025 y 2024-12.
- **MENOR — EV-108 (secuencias de aprendizaje con nombre), incompleta.**
  - Qué dice el capítulo, en §15.1, "The Mastery Method": enumera 2022, 2023-12, 2024 y 2025 (los tres insights) y concluye que "the names, the number of steps and the theoretical frame change".
  - Qué falta: el último escalón que registra EV-108. En 2026 aparece "learning as a cybernetic output process" e "ideal mind" (U-021-196, U-021-197, U-021-223, U-021-227). Falta también el cambio exacto de marco, "de dopamina/novedad a cibernética".
  - Impacto: tal como queda, el lector puede tomar los tres insights de 2025 como la versión final. Ese material se trata en los capítulos 6, 14 y 16, así que basta una remisión.

### 6. Fuentes de terceros con atribución perdida, confundida o alterada

Sin hallazgos. El capítulo atribuye correctamente las fuentes de terceros:

- George Leonard, Leo Gura, Harrington Emerson (con la variante anónima de 2024 y la atribuida), Musashi, Naval ("you don't learn business" y "10,000 iterations"), Robert Greene, el estoicismo, Orange Book, Justin Welsh, *Cashvertising*, Ogilvy, Russell Brunson, Hormozi, Andrew Tate (con la aclaración "not a fan"), Dickie Bush (la imagen de la obesidad es suya y la extensión bulking/cutting es de Koe), Matt y Ari, Elon Musk/Tesla y Optimus, y los programas de entrenamiento y dietas.
- Añade contexto complementario rotulado para Eisler/Wilber, Schwartz, Hebb, Epicteto, Hemingway y teoría de juegos.

### 7. Argumentos por capas reducidos a su conclusión

Sin hallazgos. El capítulo conserva las cadenas completas, entre ellas:

- el argumento en tres pasos de "learning to walk" (U-018-140);
- la inferencia desde la abundancia de información (U-022-103);
- la cadena experiencia → pattern recognition → adquisición de habilidades (U-004-092);
- la cadena de cuatro eslabones riesgo → sentido (U-027-172), en tabla;
- el doble argumento, informacional y fenomenológico, del fracaso (U-013-072);
- la distinción entre camino asignado y camino propio (U-027-201).

### 8. Conceptos usados antes de introducirlos

- **MENOR — "anti-niche" (U-020-083).**
  - Dónde: §15.4, "Your life's projects as science projects".
  - Qué hace el capítulo: cierra con "(he refers to his previous video on the 'anti-niche')", sin glosa ni remisión.
  - Dónde se desarrolla: en el capítulo 19 ("I am my own niche", "the anti-niche", "nicheless"). El mismo párrafo remite bien a la Parte VII para "you are the niche"; aquí falta lo mismo.

Los demás conceptos de capítulos anteriores se usan con remisión o glosa: mental body (cap. 3), tactical stress e infinite game (cap. 10), Clarity Catalyst (cap. 14), hierarchy of goals (cap. 8), psychic entropy (cap. 5), level of mind (cap. 4), NPC (cap. 1) y true education (cap. 2). Los conceptos de capítulos posteriores llevan glosa breve: curiosity loop, market sophistication, premortem, mental real estate y Eden.

---

## Capítulo 16 — Reading, Note-Taking and Learning with AI

### 2. Unidades declaradas como cubiertas pero solo mencionadas

Sin hallazgos. Las unidades de alta prioridad están desarrolladas con sus pasos, condiciones y ejemplos. Por ejemplo:

- La cadena causal del consumidor (U-027-187), numerada.
- La secuencia de seis pasos (U-027-093).
- El ejercicio de anomalías (U-015-141), en cinco pasos con su análisis.
- Los dos ejemplos de disección (U-004-103, U-009-203).
- Las cuatro causas por las que se lee mal (U-021-151).
- La lectura en dos capas con IA (U-021-149 a U-021-161), en tabla, con el ejemplo completo de "deep generalism".
- La plantilla de siete campos (U-014-036) y Core Notes (U-015-075), en tabla, con su comparación.
- El flujo semanal de Kortex (U-014-103 a U-014-108).
- El canvas de Eden (U-015-203).
- Las herramientas de 2026 (U-021-221, U-021-222), con la explicación de embeddings.
- Los tres study partners (U-021-114, U-021-125, U-021-127).
- El metaprompt de landing page (U-012-158).
- Las cuatro opciones de instrucciones (U-021-172 a U-021-176), en tabla.
- Las fases (U-021-180) y el flujo de YouTube en siete prompts (U-021-191).

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

Sin hallazgos que alcancen el nivel de MENOR. A título informativo, el capítulo omite dos detalles de producto de U-014-108 y U-020-126: la app móvil y de escritorio con hoja de ruta pública, y las fechas de lanzamiento de septiembre y noviembre. No tienen peso conceptual.

### 4. Términos acuñados no definidos u homogeneizados

Sin hallazgos. El capítulo define con el sentido del autor:

- las palabras comunes con sentido propio: consumer, researcher, fluff, context, swipe file, performative act, prompt engineering y system prompt;
- los términos acuñados: hermetic law of use, mental masturbation, edge of understanding, anomalies, web of ideas, behavior change through identity change, golden nuggets, database of intellectual property, Core Notes, elements, Legos, idea museum, idea density, false god, second subconscious, meaning space, ideal mind, close the loop, little employees, meta prompt, orchestrating, prompt library e intellectual sparring partner.

### 5. Cambios de posición (Anexo A) no presentados o resueltos indebidamente

Están presentadas EV-104, EV-106 (con la tensión frente a "the purpose of knowledge is action"), EV-107, EV-111 (con su tabla por periodos y sin presentarla como corrección declarada, igual que la fuente), EV-112, EV-114, EV-115, EV-118, EV-119, EV-120, EV-125, EV-128 (Z-Library y "10,000 words"), EV-149 y EV-292. EV-108 y EV-291 corresponden a otros capítulos.

- **MENOR — EV-113 ("¿Leer libros es aprender?"), presentada sin anclaje.**
  - Qué dice el capítulo, en §16.2, "Immersion: three books and the economics of effort": "In some passages Koe says that reading books is not learning and that books read without a project are a form of entertainment; in others, like this one, he tells the reader to burn through three books." No da fechas ni fuentes.
  - Qué se pierde: el contraste más agudo de la entrada. El mismo video de 2024-07-21 que dice "buy three books… burn through them" (U-023-198) dice también "reading a business book without having a business is kind of dumb" (U-023-192). Además, la posición se radicaliza: "reading books is not learning" (U-020-075, 2023-12) y "is just creating more chaos" (U-024-221, 2025-09).
  - Qué se conserva: la propuesta de lectura del capítulo (ver el mundo frente a aprender a hacer) se presenta correctamente como no resuelta por el autor.

### 6. Fuentes de terceros con atribución perdida, confundida o alterada

- **MENOR — *Purpose and Profit* y "deep generalism" sin atribución (U-021-156, U-021-161).**
  - Dónde: §16.2, "Reading in two layers".
  - Qué hace el capítulo: muestra el reading companion y el flujo "make sense of a topic or idea" leyendo *Purpose and Profit* y preguntando por "the concept of deep generalism". Presenta ambos como si fueran un libro y un concepto cualesquiera.
  - Qué omite: *Purpose and Profit* es el libro gratuito del propio Koe (así lo identifica el capítulo 8). Además, el Anexo C (entrada Daniel Schmachtenberger) registra "deep generalist" como idea que Koe adopta de Schmachtenberger.
  - Impacto: se pierden las dos atribuciones. El lector no sabe que el ejemplo es el autor leyendo su propia obra, ni que el concepto viene de un tercero.
- **MENOR — "tribe of mentors" → "intellectual sparring partner", vínculo editorial presentado como del autor (U-019-120, U-021-184).**
  - Dónde: §16.4. En "Study partners…" se lee: "The tribe of mentors is developed later, in more detail, as the intellectual sparring partner described below". En "The intellectual sparring partner" se lee: "A related device turns the 'tribe of mentors' idea into a method".
  - Qué dicen las unidades: U-019-120 (2025-05) no da detalles de implementación, y U-021-184 (2025-11) no usa la expresión "tribe of mentors".
  - Impacto: la relación entre ambos dispositivos es una inferencia razonable del capítulo, no un desarrollo declarado por el autor. Debería marcarse como lectura propia. El contexto complementario sobre Tim Ferriss sí está bien rotulado.

Las demás atribuciones son correctas:

- Naval ("read what you love…"), Cal Newport (closing push), Feynman (cita recordada sin precisión), la atribución dudosa al fundador de Nvidia (marcada como conjetura de Koe), "pollinator 3000", Sahil Bloom, Odysseas, Matt ("search engine for your memories") frente a Koe ("curated space"), Dickie Bush ("it's like synthesis") y Brandon Sanderson.
- April Lyn Alter, Ali Abdaal, Hormozi y "Caleb Rston" (con la grafía señalada).
- La tradición del commonplace book y Smart Notes/Zettelkasten, con contexto rotulado.
- Las salvedades del propio Koe sobre Dispenza y *The Kybalion*.
- La identificación de *Story* (McKee), *Great Leads*, *Breakthrough Advertising* y *The Systems View of Life*.

### 7. Argumentos por capas reducidos a su conclusión

Sin hallazgos. El capítulo reconstruye completos:

- la cadena hacia atrás del consumidor, en cinco eslabones;
- la cadena de los cuatro problemas de lectura hasta "50 years old with the intellectual maturity of a 15-year-old";
- el argumento contra "AI makes reading irrelevant" (la búsqueda solo devuelve lo que una identidad sabe preguntar);
- el argumento entrópico contra los resúmenes (veinte resúmenes frente a un libro);
- la secuencia de 2026 curar → capturar → cerrar el ciclo con un proyecto.

### 8. Conceptos usados antes de introducirlos

- **MENOR — Menciones de conceptos posteriores sin glosa ni remisión.**
  - "Spiral Dynamics", en §16.2, "Non-linear reading…": se nombra como tema de lectura del autor y se desarrolla en el capítulo 38.
  - "Currency of agency", en §16.3, "2026: the second brain as a false god": solo aparece dentro de la cita y se desarrolla en la Parte XII.
  - "Unique mechanism, unique selling proposition", en §16.4, "Becoming AI-first…": son términos de la Parte XI.
  - Impacto: todas son menciones de paso, sin peso argumental en este capítulo, pero ninguna lleva glosa ni remisión.

Los demás conceptos tienen el soporte necesario:

- Los de capítulos anteriores se usan con remisión explícita: goal as lens (cap. 6), cheap dopamine y entropic/syntropic (cap. 11 y Parte III), build to learn y tutoriales (cap. 14), pattern recognition y overwhelm (cap. 15), true education y la crítica de la escuela prusiana (Parte I), y self-reflective consciousness (cap. 3).
- Los de capítulos posteriores llevan glosa breve: synthesizer (cap. 18), taste (cap. 18), vessel/creative firepower y you are the niche (Parte VII).
