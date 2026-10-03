# Auditoría de cobertura — Lote 05 (capítulos 09 y 10)

Auditor independiente. Fase 5. Alcance: puntos 2–8 del prompt del auditor para `05_capitulos_en/cap-09.md` y `05_capitulos_en/cap-10.md`, contrastados con `04b_material/cap-09.md` y `04b_material/cap-10.md`. El punto 1 (IDs no cubiertos) lo verificó un script y queda fuera de este reporte. No se corrigió nada.

## Resumen

| Capítulo | PÉRDIDAS | MENORES |
|---|---|---|
| 09 — Del propósito superficial al life's work: el proyecto | 0 | 5 |
| 10 — La vida como juego: flow y el borde | 0 | 6 |

**Método y muestra.**

- Leí completos los dos capítulos (553 y 982 líneas).
- Capítulo 09: leí el campo `desarrollo` (más ejemplos, cita, origen y tensión) del 100 % de las 123 unidades del material y lo comparé sección por sección con el capítulo.
- Capítulo 10: pasé un control automático sobre las 193 unidades. Busqué en el capítulo las citas de cada unidad (`desarrollo` y `cita`) en ventanas de cinco palabras. Después revisé a mano unas 50 unidades: todas las que tuvieron menos del 80 % de coincidencia literal y una muestra de las de tipo framework, proceso, método, historia, caso, dato, metáfora, término acuñado y fuente de tercero. Todas las de baja coincidencia literal están desarrolladas con otras palabras.
- Anexo A: revisé las 18 entradas de cada capítulo.
- Anexo B: comprobé todas las entradas (68 en el 09 y 79 en el 10) contra el texto del capítulo.
- Anexo C: leí todas las entradas (18 en el 09 y 13 en el 10; el anexo no tiene más).
- Para la progresión consulté `04_arquitectura.md` y busqué en los capítulos 01–08 los términos que el 09 y el 10 usan sin definir.

**Juicio global.** Los dos capítulos tienen una fidelidad muy alta. Conservan los mecanismos, las condiciones, las cadenas argumentales numeradas, los ejemplos, las cifras y las metáforas de prácticamente todas las unidades. Algunos ejemplos son la tabla de niveles del propósito, las seis definiciones de proyecto en tabla, los cinco componentes del Clarity Catalyst, la cronología de los cinco impulsores del flow, las ocho formulaciones del tactical stress en tabla y los cuatro focus blockers. Marcan con cuidado las fuentes de terceros y las atribuciones inferidas (Wilber, Maslow, Kotler, Csikszentmihalyi, Carse, Nguyen, Parkinson). También presentan las tensiones del Anexo A sin resolverlas indebidamente.

No encontré ninguna unidad reducida a una frase cuando el material traía mecanismo, condiciones y ejemplos. Por eso no registro ninguna PÉRDIDA. Los hallazgos son matices:

- una conflación de dos fuentes en una frase;
- entradas de evolución presentadas de forma incompleta o con una remisión equivocada;
- tres términos usados sin glosa;
- una interpretación propia del autor sobre Csikszentmihalyi que se omite;
- un detalle menor de ejemplo.

---

## Capítulo 09 — Del propósito superficial al life's work: el proyecto

### 2. Unidades declaradas como cubiertas pero solo mencionadas

Sin hallazgos. Todas las unidades de tipo framework, proceso, método, historia, metáfora, dato y argumento están explicadas con su mecanismo y sus ejemplos. Algunos ejemplos:

- Los cuatro niveles del propósito (U-016-095 a U-016-110), con tabla de entrada y salida, la ley "transcend and include" y el reset.
- Job, career y calling (U-016-114 a U-016-116, U-016-055 y U-012-206), con tabla y la cadena completa de la complacencia.
- Las seis definiciones de proyecto (U-010-065, U-017-121, U-017-197, U-021-116, U-018-069, U-024-222 y U-021-205), en tabla.
- Los seis pasos para arrancar un proyecto, con la unión de U-021-120 y U-018-070.
- La progresión de public personal projects en siete pasos (U-007-214).
- Los tres criterios de un buen proyecto (U-022-231).
- Los cinco componentes del Clarity Catalyst (U-023-190).
- Las historias del gimnasio, del bench press con Jerry y del progressive overload (U-003-134, U-020-182 y U-022-118).

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

- **MENOR — U-007-215 (los proyectos como resultados tangibles).** En §9.3 ("From project to product") el capítulo recoge el ejemplo del email marketing y el del planner. Omite el paso siguiente que da la unidad: "craft persuasive arguments in your email sequences, practicing writing, speaking, marketing and sales through a results-oriented skill". Es un detalle de ejemplo y el principio ("you can't improve what you haven't created") está.

### 4. Términos acuñados no definidos u homogeneizados

- **MENOR — "independent income" (y "education business").**
  - El léxico define *independent income* como un ingreso que no depende de un empleador ni de plataformas y que requiere vender un producto.
  - En §9.2 ("You make money to create") el capítulo solo dice que "the *education business* and *independent income* are his terms, and both are developed in Part X".
  - Luego §9.3 usa el término con peso argumental sin glosarlo: "a project is the only qualification you need to start earning an independent income". El lector lo recibe con su sentido de diccionario.
  - Bastaría una glosa de una línea en §9.2.

### 5. Cambios de posición (Anexo A) no presentados o resueltos indebidamente

Están bien presentadas, con su clasificación correcta, las entradas EV-049, EV-050, EV-051, EV-053, EV-082, EV-087, EV-108, EV-203, EV-204, EV-256, EV-275, EV-282, EV-295 y EV-298.

- **MENOR — EV-273 (postura ante la salud): conflación de fuentes y razón omitida.**
  - En §9.1 ("The body underpins everything") el capítulo escribe: "In 2023, in conversation with Dickie Bush, Koe said that the details of diet barely matter, called excessive self-optimization a 'destructive self-improvement game,' and defended a degree of 'degeneracy' against what he called the 'Huberman cult.'"
  - Según EV-273, la defensa de la "degeneracy" frente al "Huberman cult" es de otro video (U-026-228, 2023-10-02), no de la conversación con Dickie Bush (2023-03-16). La frase atribuye las dos cosas al mismo contexto.
  - Además, el capítulo afirma que el autor "gives no explicit reason for the change". La entrada registra un matiz: U-018-067 dice que es no dogmático, pero que todos deberían hacer una dieta de eliminación.
  - También se omite el detalle de que el estilo de vida "se arma como Legos" (U-002-089).
- **MENOR — EV-195 (¿hay que emprender?): faltan el "antes" de 2023 y el paso de 2024-09.**
  - La sección "Do you have to start a business?" (§9.4) presenta bien las posiciones de febrero, junio, julio y octubre de 2024 y la de Sahil Bloom (2025-01). La reconciliación de formulación y no de fondo es correcta y no se resuelve indebidamente.
  - Omite, sin embargo, el punto de partida de 2023 que registra la entrada: "The only way to escape is to build your own thing" (U-016-198, 2023-08) frente a "no renunciar al empleo de golpe, this is a long-term game" (U-024-082, 2023-07).
  - Omite también el paso de 2024-09 en que el emprendimiento es "la única forma de crear nuevo desafío" (U-016-103). Esa unidad está en el capítulo 10, pero aquí falta la remisión.
  - El campo "evolución" del clúster C-T03a-23 menciona expresamente U-024-082 y U-005-095.
  - Debería ir en §9.4, al inicio de la serie cronológica.
- **MENOR — EV-239 (code y media).** En §9.4 ("The internet as the vessel…") el capítulo dice que Koe "recommends content, and notes that even code eventually requires content" (2026). La presenta como posición estable, sin avisar que es el punto de llegada de una oscilación registrada entre 2022 y 2026. En ese recorrido el autor pasa por "no hace falta programar", por "aprender código y contenido is not optional" y por la primacía de media sobre code, y se aparta explícitamente de Naval. No hay remisión al capítulo que trata esa evolución.

### 6. Fuentes de terceros cuya atribución se perdió, se confundió o se alteró

Sin hallazgos adicionales. Están bien atribuidas o marcadas como inferidas:

- Ken Wilber: circle of care, transcend and include, holon tenet en "destruction of the lower".
- Maslow, Kotler (impulsores y MTP) y Robert Greene (life's task).
- Alan Watts, Naval ("go do something great…", permissionless leverage) y "Paul", posiblemente Paul Graham.
- Walt Disney, con el cambio de atribución de EV-256.
- Dickie Bush ("gateway drug", "forcing function") y Darwin, posiblemente vía *Rest*.
- Steve Jobs, griegos y romanos, Jordan Peterson, Huberman y Marco Aurelio.

La conflación de EV-273 (punto 5) es un error de contexto entre dos videos del propio autor, no de atribución a terceros.

### 7. Argumentos construidos por capas reducidos a su conclusión

Sin hallazgos. Las cadenas se conservan paso a paso. Por ejemplo:

- La del creador (U-007-004).
- La de la complacencia del empleo (U-016-055).
- La del proyecto como lente (U-022-229), reconstruida además en seis pasos.
- El silogismo proyecto → propósito (U-010-065).
- La de la ética "selflessness requires selfish values" (U-027-023 y U-007-133).

### 8. Conceptos usados antes de introducirlos (progresión)

Sin hallazgos de peso. Los términos que el capítulo usa de capítulos posteriores llevan remisión explícita:

- mentally obese y cheap dopamine (cap. 11);
- infinite game y flow (cap. 10);
- 4-Hour Workday (cap. 12);
- default mode network (cap. 6, con contexto complementario).

Los demás ya aparecen en los capítulos 01–08:

- one-person business, level of mind y Purpose-Path-Priority;
- intelligent imitation, NPC y flow state.

---

## Capítulo 10 — La vida como juego: flow y el borde

### 2. Unidades declaradas como cubiertas pero solo mencionadas

Sin hallazgos. Todas las unidades revisadas están desarrolladas con su mecanismo, sus condiciones y sus ejemplos. Por ejemplo:

- Las cuatro propiedades compartidas por juegos, negocios y sociedad (U-003-015 y U-023-226).
- Frame, rules, mechanics y feedback, con tabla (U-023-237 a U-023-244 y U-003-034 a U-003-041).
- Gamify your life en tres pasos (U-023-265).
- Los cinco "boxes" del flow con anti-goals (U-018-085).
- Los cuatro focus blockers (U-017-224 a U-017-228).
- La cronología completa de los cinco impulsores (U-020-197, U-014-015, U-026-036, U-005-137, U-023-176, U-023-177, U-019-036 y U-019-152).
- El modelo de autoconsciencia y egocentrismo (U-023-248 y U-003-191), con la cascada del grano (U-003-192 y U-003-238).
- La cadena de seis pasos "stagnation equals death" (U-017-060).
- Tactical stress, con sus ocho formulaciones en tabla, la cronología 2018–2021, las estrategias, el one-rep max y las cinco condiciones.

Los únicos elementos que el capítulo declara no desarrollar son dos de las seis estrategias del video de 2023 ("launching a product before building it" y "emotional transmutation"). No tienen unidad propia en el material, y el capítulo lo dice expresamente.

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

- **MENOR — U-003-236 (el flow como "nature's signal").**
  - La unidad de 2024-02 cierra la descripción del gráfico desafío/habilidad con una interpretación propia: "The Flow State arguably a Peak experience a spiritual experience once you tap into that state I believe that's nature['s] signal that you are doing something right."
  - El capítulo usa la primera parte de la unidad (la descripción de los ejes) en §10.5, "The skill–challenge graphic", pero omite esta frase. El Anexo C la destaca entre los añadidos propios del autor sobre Csikszentmihalyi ("el flow como 'nature's signal'").
  - Debería ir en §10.5, tras la cita de 2024, o en §10.4, "Flow, the now and the spiritual traditions", donde encaja con la lectura espiritual del flow.

### 4. Términos acuñados no definidos u homogeneizados

- **MENOR — "in-formation".**
  - En §10.5, "The mind as a digestive system of reality", el capítulo cita "everything is in formation" sin glosar el juego de palabras.
  - El léxico lo registra como término acuñado con dos sentidos. En el primero, la vida es información "en formación" y un juego es un flujo estructurado de información. En el segundo, la información es cambiante e impermanente.
  - El lector puede tomar "in formation" como errata o en su sentido de diccionario.
- **MENOR — "ignorance tax".**
  - En §10.6, "The definitions", se lee: "Koe distinguishes tactical stress from what he calls the ignorance tax, describing them as similar but different."
  - El término no se define. Además el capítulo lo atribuye a Koe ("what he calls"). El léxico lo registra como término de tercero: "lo que cuesta no saber cómo hacer algo bien", acuñado por Alex Hormozi y llegado vía Dickie Bush.
  - Es su primera aparición en el libro; el término se trata recién en el capítulo 34. Ver también los puntos 6 y 8.
- **MENOR — "everyone is an entrepreneur".**
  - En §10.7, "Entrepreneurship as an infinite game", la frase de 2025 "I think everyone should be an entrepreneur" (U-005-096) se trata en su sentido corriente: todos deberían montar un negocio.
  - El léxico registra para esta familia de expresiones ("everyone is an entrepreneur" y "entrepreneurship is for everyone") un sentido propio. En él, todos ya aportan valor y algunos simplemente deciden ponerle precio. Incluye U-005-096 entre sus IDs.
  - El capítulo discute la fuerza de la recomendación ("How strong is the claim?") y menciona la redefinición como "state of mind", pero no este sentido, que es precisamente el que la suaviza.
  - Basta una remisión al capítulo 28.

### 5. Cambios de posición (Anexo A) no presentados o resueltos indebidamente

Están bien presentadas EV-019, EV-033, EV-038, EV-046, EV-055, EV-087, EV-088, EV-092 (incluido el choque con la preparación en 2026, sin resolverlo), EV-103 (con la autocita inexacta), EV-195, EV-228, EV-229, EV-234, EV-257, EV-265 y EV-295.

- **MENOR — EV-054 (la metáfora del videojuego se reformula): remisión equivocada.** La tabla de versiones de §10.2, "One metaphor, several versions", cierra con la fila de 2025-12: "Six components (including boss, mission, quests, rules) and a 'force field' — Mentioned in the corpus record; not developed in this chapter". Esa versión sí está desarrollada en el capítulo 08, que explica el "force field" y sus componentes. La tabla debería remitir allí en lugar de presentarla como un dato solo registrado.
- **MENOR — EV-043 (tamaño de la meta): presentado como secuencia.**
  - En §10.5, "Clarity, and the level-1 problem", el capítulo contrapone dos remedios. El de 2022, repetido en 2024, es reencuadrar la meta ante un rival de nivel 50. El de 2025 es elegir desafíos de nivel 2 a 4. Los presenta como "the earlier version" y "the later one".
  - EV-043 registra que la recomendación de apuntar "just above your level… level two aims for level four, not 100" ya existe en 2023-10 (U-026-210). Las dos líneas, metas enormes y desafíos cercanos, "conviven sin dirección cronológica".
  - El capítulo no las resuelve indebidamente: las reconcilia por contexto y remite al capítulo 8. Pero el marco "antes y después" sugiere una evolución que el registro no sostiene.

### 6. Fuentes de terceros cuya atribución se perdió, se confundió o se alteró

- **MENOR (contado en el punto 4) — "ignorance tax".** Atribuido a Koe ("what he calls") cuando el léxico lo registra como término de Alex Hormozi llegado vía Dickie Bush.
- Lo demás está correctamente tratado:
  - Csikszentmihalyi: la cita de "conscious personal creation" nombrada en 2022 y sin atribuir en 2024; el pasaje de *Flow* sobre los juegos citado sin nombre; la atribución variable del gráfico, incluido el "I made it up" irónico.
  - Kotler: con el "doesn't say this directly".
  - *The Molecule of More*, como fuente del par "here and now" y "future".
  - C. Thi Nguyen, Carse, Parkinson (no nombrado por el autor) y Donald Hoffman.
  - Sócrates, la cita no atribuida sobre vivir en el borde (U-027-052), Dickie Bush ("opposite of lifestyle inflation") y Alan Watts.

### 7. Argumentos construidos por capas reducidos a su conclusión

Sin hallazgos. Se conservan completas:

- la cadena del personaje (aprendizaje → autoconcepto → percepción → resultado; U-003-048 y U-023-250);
- la cadena de seis pasos de U-017-060;
- la cadena de Sahil Bloom sobre la pérdida de desafío (U-005-096);
- la cadena causal del flow por elección propia (U-001-079);
- las tres razones del calculated risk (U-027-212).

### 8. Conceptos usados antes de introducirlos (progresión)

- **MENOR (contado en el punto 4) — "ignorance tax".** Se usa en §10.6 sin definición, y el libro lo explica recién en el capítulo 34.
- En lo demás, sin hallazgos. Los conceptos de capítulos posteriores llevan remisión explícita:
  - *The Molecule of More*, up world y down world, cheap dopamine y earned dopamine (cap. 11);
  - 4-Hour Workday (cap. 12);
  - true education (Parte VI y cap. 35).

  "Earned dopamine" aparece por primera vez en el libro en §10.1, pero queda glosado por la propia cita de U-018-039 ("they take time and effort… they are earned dopamine"). War mode y monk mode ya se introducen en los capítulos 01–08.
