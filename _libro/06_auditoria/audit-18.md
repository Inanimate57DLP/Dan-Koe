# Auditoría de cobertura — Lote 18 (capítulos 35 y 36)

Auditor independiente, Fase 5. Este reporte cubre los puntos 2 a 8 del prompt del auditor para `05_capitulos_en/cap-35.md` y `05_capitulos_en/cap-36.md`. El material de contraste son `04b_material/cap-35.md` y `04b_material/cap-36.md`. El punto 1 (IDs no cubiertos) ya lo verificó un script y queda fuera de este reporte.

## Resumen

| Capítulo | PÉRDIDAS | MENORES |
|---|---|---|
| 35 — Agencia y autosuficiencia | 0 | 6 |
| 36 — La economía del individuo en la era de la IA | 0 | 5 |

**Método y muestra.**

- Leí completos los dos capítulos: 1.156 líneas en el 35 y 693 en el 36.
- **Capítulo 35.** Del material leí el campo `desarrollo`, con ejemplos, cita, origen y tensión, del 100 % de las 121 unidades.
- **Capítulo 36.** Leí completas unas 95 de las 152 unidades, más del 60 %. Las elegí con prioridad por tipo: framework, proceso, método, historia, metáfora, dato, término acuñado, fuente de tercero y argumento. De las demás revisé título, ejemplos y tensión.
- **Control automático.** En los dos capítulos busqué en el texto cada cita del campo `desarrollo` y del campo `cita`, en ventanas de cinco palabras. En el capítulo 35 todas las unidades tienen coincidencia literal. En el 36 hubo cinco unidades sin coincidencia (U-013-164, U-007-199, U-012-126, U-012-146 y U-012-179). Las revisé a mano y las cinco están desarrolladas con otras palabras.
- **Anexo A.** Revisé el 100 % de las entradas: 14 en el capítulo 35 y 21 en el 36.
- **Anexo B.** Comprobé de forma automática la presencia de todos los términos: 79 en el 35 y 97 en el 36. Leí completas todas las entradas de los dos capítulos.
- **Anexo C.** Revisé todas las entradas: 14 en el 35 y 24 en el 36.
- **Otros capítulos.** Cuando el anexo citaba unidades asignadas a otros capítulos, verifiqué con `grep` en qué capítulo se cubren. Para la progresión consulté `04_arquitectura.md`.

**Juicio global.** Los dos capítulos tienen una fidelidad muy alta:

- Conservan casi literalmente las cadenas argumentales numeradas: la cadena de ocho pasos de Eriksen, el ciclo de la catástrofe, la tríada de soberanía como ciclo, el silogismo de *Purpose and Profit*, la cadena parálisis → metas asignadas → reemplazo y la anatomía del sentido.
- Conservan los ejemplos con sus cifras y separan con cuidado lo que es de terceros de lo que es del autor: Eriksen, Bloom, Vitali, Bush, Signal, Shapiro, Narayanan y Kapoor, y el clip sin identificar.
- Presentan sin resolverlas indebidamente casi todas las tensiones del Anexo A.

No encontré ninguna unidad reducida a una frase cuando traía mecanismo y ejemplos, así que no registro PÉRDIDAS. Los hallazgos son de otros tres tipos:

- Pasos intermedios de evolución que se omiten en las series cronológicas.
- Un término (*perspective*) glosado con un sentido genérico.
- Un concepto (*three generators*) usado en el capítulo 35 antes de su desarrollo en el 36, con glosas que no coinciden.

Al final de cada capítulo dejo una observación, no contabilizada, sobre frases del proceso editorial que se filtraron al texto.

---

## Capítulo 35 — Agencia y autosuficiencia

### 2. Unidades declaradas como cubiertas pero solo mencionadas

Sin hallazgos. Todas las unidades de tipo framework, proceso, método, caso, metáfora, dato y argumento están explicadas con su mecanismo, sus condiciones y sus ejemplos. Algunos ejemplos:

- **35.1**
  - Las dos formulaciones de agencia de Eriksen y su cadena de ocho pasos (U-006-007, U-006-008).
  - La tipología fácil/imposible/difícil con sus ejemplos (U-006-013) y la comparación explícita con los "three buckets" (U-023-221).
  - Las cinco prácticas (U-023-223) y el proceso de diciembre de 2025 (U-013-221).
  - El caso de Ian y el contrapunto de Vitali (U-006-176, U-004-066).
- **35.2**
  - Los siete rasgos del Irreplaceable individual, en tabla (U-016-010).
  - El ciclo de la catástrofe, en seis pasos (U-027-173).
  - La tríada de soberanía con sus tres eslabones (U-010-270 a U-010-276).
- **35.3**
  - El método de Bloom (U-005-100, U-005-101), integrado en una tabla.
- **35.4**
  - El silogismo de *Purpose and Profit* (U-024-234).
  - El proceso del value creator, en tabla (U-016-200).
- **35.5**
  - La cronología de los stacks, con todas las versiones del material y sus ejemplos: Photoshop, el curso de agencia, el fondo mutuo y la canción, los no-code tools, la imprenta, Sam Altman, Eden y la escalera ebook → curso → cohorte → comunidad.

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

Sin hallazgos que alcancen el nivel de MENOR. Solo se omiten detalles triviales, que no cuento:

- El nombre transcrito "Chris Lang" del ejemplo de CI 180–200 (U-006-012).
- El segundo ejemplo de Eden, la secuencia de correos de siete días (U-012-201).
- La identificación de la "imagen usada antes en el video" como la del pájaro (U-027-090).

### 4. Términos acuñados no definidos u homogeneizados

- **MENOR — *perspective*, tercer nivel de la jerarquía post-IA (U-012-196; definición del autor en U-012-199, cubierta en el capítulo 3).**
  - **Qué dice el capítulo.** La tabla de §35.5, en "Agency at the top: the five levels of the post-AI hierarchy", glosa *perspective* como "The unique vantage point from which one sees problems and solutions". Remite a 3.3, 18.3 y 27.5. Debajo añade que los roles de *taste*, *perspective* y *persuasion* "summarize how the corpus uses those terms elsewhere".
  - **Qué dice el autor.** En ese mismo video define *perspective* de otro modo. Es "expanding your human capacity". La equipara a "perspective development", sinónimo de desarrollo del ego. Al desarrollarse, te vuelves "less conformist, less ideological, less dogmatic", y eso permite "genuine agency and sophisticated curation".
  - **Qué se pierde.** El libro reemplaza ese sentido técnico por uno de diccionario, el de "punto de vista". Con eso pierde el vínculo que cierra el capítulo: la jerarquía de 2026 vuelve a la conformidad con la que empieza §35.1.
  - **Dónde debería ir.** En la tabla de §35.5 o en el párrafo siguiente, con la definición del autor o al menos con remisión a donde se desarrolla.
- La glosa de *three generators*, que el capítulo da con sentidos distintos de los del capítulo 36, se trata en el punto 8.

Los demás términos del Anexo B están definidos con su sentido propio, a veces de forma explícita:

- *unemployable* con su sentido invertido.
- *comforting conformity*, *iterate without permission*, *scientists of their own lives*, *ideas beget behavior*, *code for your life* y *stepping stone goal*.
- *external locus of control*, con su contexto de Rotter.
- *greenfield development*, *bottleneck* y *necessary/sufficient*.
- *persistent principles*, *micro skill stack*, *umbrella skills*, *evergreen skills* en sus dos contenidos sucesivos y *results-oriented skills*.
- *true value is creative*, *world of replaceability* e *infinite game*, este último con el contexto de Carse.

### 5. Cambios de posición (Anexo A) no presentados o resueltos indebidamente

Las 14 entradas del Anexo A están presentadas, en general con la etiqueta correcta de refinamiento, contradicción no resuelta o renombre con pérdida de atribución. Lo que falta son escalones intermedios.

- **MENOR — tipología fácil/difícil/imposible: la versión de diciembre de 2025 (U-013-197, cubierta en el capítulo 7; léxico *easy / difficult / impossible goals*, acepción 2025-12; contexto de EV-236).**
  - **Lo que hace el capítulo.** §35.1, en "Koe's version: three buckets of goals", compara a Eriksen (2024-12) solo con la versión de octubre de 2025. Afirma que Koe estrechó lo "imposible" a "outside the laws of physics" y que así agrandó la categoría de lo difícil.
  - **Lo que omite.**
    - En el video de diciembre de 2025 que el capítulo usa a fondo, la tipología es el *third tell* de la alta agencia: "high agency people believe in the difficult".
    - En esa versión, lo imposible vuelve a ser relativo a una posición: "impossible goals are only impossible right now", es decir, "until we complete the series of difficult goals". Eso lo acerca de nuevo a la definición psicológica de Eriksen.
  - **Por qué importa.**
    - El capítulo cita el *first tell* y el *second tell* de ese video, pero no el tercero.
    - El capítulo 7 (§7.4) remite de forma explícita: "Chapter 35 develops the concept of agency to which 'believe in the difficult' belongs".
    - El ejercicio 2 de §35 se basa solo en la definición de octubre.
  - **Dónde debería ir.** En §35.1, al final de "Koe's version: three buckets of goals", como cuarto paso de la serie.
- **MENOR — EV-232: los "three superpowers" de agosto de 2025 faltan en la cronología de stacks (U-025-201, cubierta en §36.1).**
  - §35.5 reconstruye los stacks desde enero de 2023 hasta junio de 2026, y lo resume en la tabla de "How the stack changed, and what stayed constant". Pasa de "Feb 2025 / Medium and message" a "Feb 2026 / Post-AI skill hierarchy".
  - Omite el escalón que EV-232 sitúa como primer "Después": learning, persuasion y execution.
  - El capítulo 36 (§36.1, "The three superpowers") remite de vuelta: "Section 35.5 treats those stacks in detail". La serie, así, queda incompleta en el lugar que la arquitectura le asigna.
  - **Dónde debería ir.** Una fila en la tabla de §35.5 o una frase en "The post-AI skill hierarchy (2026)".
- **MENOR — EV-234: "Agency is only so much" (2026) no aparece en la corrección de 2026 de §35.1.**
  - "The 2026 correction: 'high agency' as a buzzword" presenta la crítica de junio de 2026 (U-012-213).
  - No recoge que EV-234 incluye la fórmula "Agency is only so much" entre los "Después". El capítulo 36 la desarrolla en §36.5, "Vibe coding", con el gráfico de apps, y la presenta como calificación notable de la tesis del capítulo 35.
  - En §35.1 no hay ni la frase ni una remisión a §36.5. La serie "the most important skill → the meta-skill → not the only one thing" queda sin su último escalón.
- **MENOR — EV-270: la serie sobre la definición de libertad empieza en 2024.**
  - **Lo que hace el capítulo.** §35.2, en "How the definition of freedom developed", presenta la serie como "cumulative" y la resume en una tabla de tres filas: mayo de 2024, agosto de 2025 y enero de 2026.
  - **Lo que omite.** Dos escalones registrados:
    - El punto de partida de 2021: la "personal sovereignty that everyone's after" de la conversación con Justin Welsh (U-005-003, cubierta en el capítulo 39).
    - La variante de julio de 2025 del *free individual*: "do what they want with their life", lo que "requires them to learn how to learn, learn how to earn, and learn how to think" (U-022-044, cubierta en el capítulo 5; acepción 2025-07 del léxico *free individual*).
  - **Por qué importa.** Esta última variante es justo la intermedia entre el *free man* de 2024 y el *free individual* de agosto de 2025.
  - **Dónde debería ir.** En la tabla de §35.2 o, al menos, con remisión a los capítulos 5 y 39.

### 6. Fuentes de terceros con atribución perdida, confundida o alterada

Sin hallazgos. El capítulo es ejemplar en este punto:

- Separa a Eriksen de Koe en cada paso y marca la apropiación sin atribución de la tipología de "three buckets".
- Señala que la fórmula de tres ingredientes puede venir del artículo "The third ingredient of success".
- Deja la autoría del método de identificar y resolver problemas en Bloom ("it is his, not Koe's") y la de la lección de tolerancia en Vitali.
- Atribuye la definición del verdadero egoísta a Rand, con contexto.
- Deja ambigua la cita de "poppy Nal" y el clip "this time it's real", y ofrece a Harari solo como contexto complementario.
- Atribuye el *future-proof skill stack* a un post de Eriksen, adaptado por Koe.
- Aclara que la comparación del "pump" es de Schwarzenegger.
- Recoge a Krishnamurti, a Sam Altman, el uso del diccionario como punto de partida y el ejemplo de Sócrates.

### 7. Argumentos construidos por capas reducidos a su conclusión

Sin hallazgos. Las cadenas se conservan completas y a menudo se hacen explícitas:

- La cadena de ocho pasos del feedback loop de Eriksen (U-006-008).
- La cadena de cinco pasos de "problems are infinite" (U-018-164).
- El ciclo de la catástrofe (U-027-173).
- Los tres eslabones de la tríada (U-010-276).
- El silogismo de *Purpose and Profit*, con evaluación de sus premisas (U-024-234).
- El argumento "the viability of the skill, not the vision" (U-016-069).

### 8. Conceptos usados antes de introducirlos (progresión)

- **MENOR — *three generators* (struggle, status, curiosity) en §35.1, con glosas que no coinciden con su desarrollo en §36.6 (U-012-197 frente a U-012-179).**
  - **Lo que hace el capítulo 35.** "Agency as 'the most important skill' and as the meta-skill" presenta los *three generators* como método para practicar la agencia: struggle como "deliberate choices", status como "money as fuel for agency" y curiosity como "filtering signal from noise". Después afirma: "The phrase 'three generators' is used in this source without a full definition of the framework; the corpus presents it in passing".
  - **Lo que hace el capítulo 36.** El mismo video de febrero de 2026 sí desarrolla el framework, como *generators of meaning*. §36.6, en "The anatomy of meaning", los define como struggle (engine of progress), curiosity (direction of progress) y status (proof of contribution).
  - **Qué se produce.** Hay tres problemas:
    - Un concepto se usa en el capítulo 35 antes de introducirse en el 36, sin remisión hacia adelante.
    - La afirmación de que el corpus solo lo menciona "in passing" es inexacta.
    - El lector recibe dos juegos de glosas sin que se reconcilien. Por ejemplo, *status* aparece primero como dinero-combustible y después como prueba de contribución.
  - **Dónde debería ir.** En §35.1, una remisión a §36.6 y la mención de que el autor los usa en los dos sentidos.

Las demás referencias hacia adelante van glosadas en el lugar y no las cuento como violaciones: *director* (36.4), *vibe coding* (36.5), Cook-Greuter y *conformist* (38), *chosen struggle* (39), autonomía frente a libertad (39.5) y Kortex (37).

**Observación (no contabilizada).** Una frase del proceso editorial se filtró al texto. En §35.5, debajo de la tabla de la jerarquía post-IA, dice: "since this chapter's material contains only the list and the order for them". Habla del material de trabajo, no del corpus, y además es inexacta, porque el corpus sí trae las definiciones del autor (U-012-198 a U-012-200; ver el punto 4).

---

## Capítulo 36 — La economía del individuo en la era de la IA

### 2. Unidades declaradas como cubiertas pero solo mencionadas

Sin hallazgos de PÉRDIDA. Las unidades de tipo framework, proceso, metáfora, dato, término acuñado y argumento están desarrolladas con su mecanismo y sus ejemplos. Algunos ejemplos:

- **36.1**
  - La tabla de cifras sin fuente, que expone la inconsistencia del 36 % (U-009-004 frente a U-006-073).
  - Las tres capas, en tabla, y los tres superpowers (U-025-200, U-025-201).
- **36.2**
  - El diagrama escuela frente a creator economy, en tabla (U-008-007).
  - El mapa del videojuego, en tabla (U-023-130).
  - El ciclo de la lluvia, evaluado como argumento por analogía (U-008-113).
  - La tabla de posiciones sobre el código (EV-239).
- **36.3**
  - "Predictable inputs" (U-010-230).
  - Los ejemplos de Canva, la caption Gen Z y los blog posts (U-012-129).
  - El paso de "paid less" a "paid nothing" (U-016-049).
  - Technicians frente a creators, en tabla (U-019-003).
  - El debate con Dickie Bush, *WALL-E* incluido (U-002-044, U-002-047).
- **36.4**
  - La fórmula "AI needs direction", en tabla (U-013-186).
  - La función ejecutiva (U-018-160).
  - Patterson y el ghostwriter (U-012-130, U-018-161).
  - El gorila teleoperado y "time is a compression algorithm" (U-013-214).
- **36.5**
  - La tragamonedas frente al digital employee, en tabla (U-021-167 a U-021-171).
  - El guion de ChatGPT criticado línea a línea (U-021-170).
  - El iceberg (U-012-127).
  - La tabla de Signal (U-012-154).
  - El procedimiento de seis pasos (U-012-155).
  - OpenClaw y la Mac Mini (U-016-259).
- **36.6**
  - Silicio frente a carbono (U-025-212, U-013-226).
  - La serie de nombres de la meaning economy, en tabla (U-006-110 a U-014-127).
  - Shapiro (U-012-174).
  - Los cuatro actos (U-012-172).
  - Killers, pillars y generators (U-012-179).

Las cinco capacidades humanas (U-013-212) solo se nombran para tres de sus cinco elementos. Como la unidad misma solo trae los nombres, no lo registro como PÉRDIDA: lo trato en el punto 7.

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

Sin hallazgos. Se conservan:

- La historia de la Golden Age con los burritos, el Dr Pepper, Halo 3 y el anestesiólogo.
- La "self-sufficient Utopia" con sus productos.
- Marcus Aurelius, Marques Brownlee y los "zip files for your mind".
- Las cifras de 60 %, 80 %, 90 %, 46,6 %, $250 → $480 mil millones, 95 %, 90 % del S&P 500 y $200–1.000 en créditos.
- Los cinco tipos de empleo que sobreviven.

### 4. Términos acuñados no definidos u homogeneizados

- **MENOR — los *five ingredients* en el ejercicio 8.**
  - **Lo que hace el ejercicio.** Dice "the 'five ingredients' Koe says most vibe coders lack (agency, taste, persistence, iteration, persuasion and distribution)". Enumera seis elementos y cuenta la agencia entre lo que les falta.
  - **Por qué no cuadra.**
    - El término del autor (U-012-212; léxico *five ingredients of success*) es una lista cerrada: agency, taste, persuasion, persistence e iteration.
    - El propio §36.5 ("Vibe coding") sostiene lo contrario: "Agency gets you to build the app... The graph shows what happens when only the first ingredient is present". Es decir, a los vibe coders les sobra agencia y les falta lo demás.
  - **Dónde debería ir.** Hay que corregir el ejercicio 8 para que coincida con §36.5 y con la lista del autor.

Los demás términos del Anexo B están definidos, varios con aviso explícito de que se usan con sentido propio:

- *making it*, *creator economy*, *slop*, *body of work*, *dead internet*, *vibe coding* y *market sophistication* (Schwartz aplicado a la IA).
- *executive function*, con su doble origen: Eriksen y Koe.
- *mental plane*, *abstract up a layer*, *authenticity at scale*, *homogeneous output*, *slop spectrum* y *artisanesque*.
- *potential for failure*, *illusory retirement*, *lower class of the creator economy*, *earning in accordance with nature* y *full life cycle of knowledge*.

### 5. Cambios de posición (Anexo A) no presentados o resueltos indebidamente

Las 21 entradas del Anexo A están presentadas o remitidas al capítulo que las desarrolla: EV-109, EV-126, EV-127, EV-237, EV-239, EV-240, EV-241, EV-242, EV-243, EV-247, EV-248, EV-249, EV-250 y EV-253 se presentan con su tensión. Lo que falta son escalones intermedios en tres series.

- **MENOR — EV-231 (¿desaparece el empleo?): el 2024 aparece como una sola posición.**
  - **Lo que hace el capítulo.** §36.3, en "The entry level is going extinct", reconstruye la serie: 2023 con "complete removal", 2024 con "I don't see employment going away" y 2025 con "the NBA of jobs" y "entrepreneurs or elite employees".
  - **Lo que omite.**
    - En febrero de 2024 el autor también dijo, sobre los trabajos manuales, "maybe in our lifetime those jobs won't exist" (U-008-118, cubierta en el capítulo 31). Eso convive con la frase de junio de 2024 que el capítulo cita como la posición de ese año.
    - En mayo de 2025 matizó la vía única del emprendimiento con el "permissionless launchpad": se puede empezar como creador y pasar después a trabajar para otros (U-019-143, cubierta en el capítulo 25).
  - **Por qué importa.** El capítulo dice que Koe "does not explain the earlier reversals". La serie que presenta es más lineal que la registrada.
- **MENOR — EV-207 (techo del negocio de una persona): falta la apuesta de Sam Altman.**
  - §36.3, en "The raised baseline in the one-person business", sigue el techo así: 2023 con "five, ten million"; 2024 con "$10 million a year"; 2026 con el modelo previo a la IA reinterpretado como "lifestyle business".
  - Omite el escalón de diciembre de 2024: la apuesta en el grupo de chat de Sam Altman por el primer negocio de una persona de mil millones (U-008-134, cubierta en el capítulo 30). Es el dato que más eleva el techo en esa serie.
  - Basta con una frase o una remisión a §30.
- **MENOR — EV-238 (la AGI): falta la posición de Eriksen.**
  - §36.4, en el párrafo final de "What current AI is not", resume la evolución: 2024-12 con la AGI como algo futuro, 2025-08 con las ASI, 2025-12 con "are we not already AGI?" y 2026-01 con la "basic foundation for survival".
  - EV-238 incluye en el "Antes" la posición de Eriksen, del mismo mes de 2024: "There's nothing magical about meat". Una persona artificial consciente es teóricamente posible, y la IA actual es una herramienta con la que podríamos "integrate... where the line between us and the tool starts to blur" (U-006-026, cubierta en el capítulo 20).
  - Ese antecedente prepara el "Will we not be AGI?" de diciembre de 2025, que el capítulo presenta sin él.
  - **Dónde debería ir.** En §36.4, con una remisión al capítulo 20.

### 6. Fuentes de terceros con atribución perdida, confundida o alterada

Sin hallazgos. El tratamiento es cuidadoso:

- Separa la cita de Sam Altman de las tres capas, que son de Koe.
- Atribuye *accelerant of polarity* a Bush ("Bush's, not Koe's").
- Deja el análisis económico de los ingresos en Shapiro y la postura personal en Koe.
- Atribuye la tabla AI-native a Signal y las adaptaciones a Koe.
- Señala que el criterio "delegate, automate or leave it" es "plausible rather than certain" de Naval.
- Corrige la atribución de "ChatGPT is bullshit" con contexto (Hicks, Humphries y Slater frente a Narayanan y Kapoor) y marca la lectura de Koe como interpretación propia.
- Propone a Deutsch como posible fuente no acreditada de las cinco capacidades, con reserva.
- Marca la cita AI-native sin atribuir y el clip sin identificar ("chth").
- Atribuye la secuencia de Balaji con su aviso de paráfrasis, y Maslow, Hurst y Lyotard como contexto complementario.

### 7. Argumentos construidos por capas reducidos a su conclusión

- **MENOR — las cinco capacidades humanas: variation, selection y attention quedan como etiquetas (U-013-212; desarrollo en U-013-215 a U-013-218, cubiertas en los capítulos 15, 18, 6 y 3).**
  - **Lo que hace el capítulo.** §36.4, en "What current AI is not", desarrolla bien computation y transformation. En la tabla, las tres capacidades del *idea space* aparecen como "Part of how knowledge is created", repetido tres veces. Debajo dice: "the corpus develops them elsewhere in connection with how knowledge is created", sin decir dónde.
  - **Qué falta.** La conclusión "AGI does not seem like it can surpass us in any way" descansa en las cinco capacidades. Las capas que sostienen las tres últimas existen en capítulos anteriores:
    - Las dos funciones del conocimiento (capítulo 15).
    - El mapa de luz y sombra del *idea space* (capítulo 18).
    - La selección como corrección de errores cibernética (capítulo 6).
    - La atención como cambio de lentes (capítulo 3).
  - **Efecto.** El lector recibe la conclusión apoyada solo en dos de sus cinco patas.
  - **Dónde debería ir.** En §36.4, una frase por capacidad o, al menos, la remisión concreta a esos capítulos.

Las demás cadenas se conservan:

- Parálisis → planes ajenos → metas asignadas → reemplazo (U-006-155), con su paso a paso explícito.
- De "predictable inputs" a la "slop" (U-010-230).
- El argumento de mercado commodity/exploit (U-016-299).
- La relación entre killers, pillars y generators (U-012-179).
- El mecanismo económico de los freelancers (U-009-004).

### 8. Conceptos usados antes de introducirlos (progresión)

Sin violaciones en el capítulo 36. Usa con remisión a capítulos anteriores, o glosa en el lugar, todos los conceptos previos:

- *market sophistication* (32.3), *epistemic commons* (1.5), *invest energy* (29.2) y el efecto protégé (Parte VI).
- *five ingredients* (18.5), *taste* (18.5) y *vessel* (9).
- *slop*, glosado en §36.3 antes de usarse en 36.4 y 36.5.

El problema de progresión de *three generators* afecta al capítulo 35 y está registrado allí.

**Observación (no contabilizada).** Dos frases del proceso editorial se filtraron al texto:

- En §36.4: "The units of this chapter reconstruct the first two capabilities in detail; the last three are only named here" y "the material suggests an uncredited source".
- En §36.6, debajo de la tabla de la anatomía del sentido: "The units of this chapter give the framework and the function of each generator; Koe develops each generator in more detail in units treated in Chapter 39".

Hablan de "unidades" y "material" de trabajo, no del corpus.
