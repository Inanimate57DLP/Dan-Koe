# Auditoría de cobertura — Lote 19 (capítulos 37 y 38)

Este reporte es de un auditor independiente, en la Fase 5. Cubre los puntos 2 a 8 del prompt del auditor para `05_capitulos_en/cap-37.md` y `05_capitulos_en/cap-38.md`. Los contrasté con `04b_material/cap-37.md` y `04b_material/cap-38.md`. El punto 1 (IDs no cubiertos) lo verificó un script y queda fuera de este reporte.

## Resumen

| Capítulo | PÉRDIDAS | MENORES |
|---|---|---|
| 37 — La trayectoria del autor y el paso de una persona a un equipo | 0 | 3 |
| 38 — Mapas del desarrollo de la consciencia | 0 | 3 |

**Método y muestra.**

- Leí completos los dos capítulos: 748 líneas el 37 y 836 el 38.
- Del material leí el 100 % de las unidades, con todos sus campos (desarrollo, ejemplos, cita, origen, fuente y tensión): 109 unidades del capítulo 37 (seis secciones) y 125 del 38 (cinco secciones). Las comparé sección por sección con el texto del capítulo.
- Revisé el 100 % del Anexo A: 18 entradas EV en el 37, 20 en el 38, y la tabla de renombres.
- En el Anexo B comprobé la presencia de todos los términos: 89 en el 37 y 72 en el 38. Busqué con grep cada término acuñado, cada término de invitado y cada palabra común con sentido propio, y leí la definición de todas las entradas.
- En el Anexo C leí todas las entradas: 21 por capítulo.
- Para verificar remisiones y progresión consulté `04_arquitectura.md`. También busqué con grep en `cap-01`, `cap-02`, `cap-03`, `cap-04`, `cap-06`, `cap-10`, `cap-12`, `cap-13`, `cap-17` y `cap-18`. Comprobé que existen las 24 secciones a las que remite el capítulo 38 (1.2, 1.4, 2.5, 2.7, 2.9, 3.2–3.5, 4.3, 4.5, 4.7, 5.2, 5.5, 6.3–6.5, 10.6, 17.1, 17.5, 17.6, 18.4, 32.4 y 36.2) y que contienen lo que el capítulo dice.
- Verifiqué dos afirmaciones contra el corpus:
  - La cita sobre la pre/trans fallacy, en la transcripción de "A Full Guide To Reinvent Your Entire Life".
  - Las unidades de arquetipos U-024-127 a U-024-132, en `02_unidades/lote-024.md`.

**Juicio global.** Los dos capítulos tienen una fidelidad excepcional. Conservan casi literalmente los mecanismos, las cadenas argumentales, las cifras, los ejemplos y las metáforas de las unidades, y en general atribuyen con precisión quién dice qué. Un ejemplo es la separación sistemática entre Koe, los fundadores de Stan (John Hugh y Vitali) y los cofundadores de Kortex (Matt y Ari). También presentan todas las entradas EV del Anexo A, con sus dos lados y sin resolverlas indebidamente. No encontré pérdidas.

Los hallazgos son matices:

- **Capítulo 37.** Un término de invitado sin nombrar y dos variantes biográficas del Anexo A que se reportan solo en parte.
- **Capítulo 38.** Lo más relevante es una afirmación falsa sobre el corpus: dice que la transcripción "no enumera los arquetipos" de Human 3.0. Esa enumeración existe y el capítulo 1 la desarrolla. A eso se suman una cronología de atribución (dominator/actualization hierarchies) que omite un antecedente de enero de 2023 y una tensión del Anexo A sin remisión.

---

## Capítulo 37 — La trayectoria del autor y el paso de una persona a un equipo

### 2. Unidades declaradas como cubiertas pero solo mencionadas

No hay hallazgos. Todas las unidades de tipo historia, caso, dato, framework, proceso, método, heurística, metáfora, fuente de tercero y argumento están desarrolladas con su mecanismo, sus condiciones y sus ejemplos. Algunos ejemplos verificados:

- **El catálogo de fracasos** (U-007-097 a U-007-111, U-014-135, U-015-131, U-015-132). Cada negocio aparece con su lección, sus cifras (los $3,000 del padre, el sujetador de diamantes, el erizo Momo, los $250–400 de alquiler) y la tabla de variantes entre versiones.
- **Las tres lecturas del fracaso** (U-011-007, U-015-088, U-024-039), incluidos "avalanche called insight" y "a click click click".
- **Las cifras de ingresos** (todo el clúster C-T17-23), en tabla cronológica, con la distinción revenue/profit y las incoherencias que el capítulo señala.
- **Los 27 principios de The Art of Focus** (U-017-140), completos, con la nota de que el principio 8 se infiere.
- **Los levels of uncertainty** (U-024-237), con la tabla y la tensión con el "glitch" del apartamento caro.
- **El proceso del centro de ayuda de Eden con Claude** (U-008-183), paso por paso.
- **El caso Kortex completo** (U-015-185 a U-015-213), etapa por etapa: CRUD app, "own the IP", sync engine, el rebuild en Japón, "blurple branding", AI slop/artisan, el logo de Flora y el rollout escalonado.
- **Las unidades de Stan** (U-004-039 a U-004-085): bottlenecks, 10x person, contratación, referral flywheel, alineación, Pop Quiz y meta time. Están con sus cifras: 40 empleados, 15 contrataciones con 13 referidos, "~30 million ARR" y "50 is the number where it breaks".

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

- **MENOR — EV-289 (préstamos estudiantiles).**
  - **Qué registra el corpus.** EV-289 recoge tres cifras que no cuadran:
    - "$2,000 in loans even with a full-ride scholarship" (U-017-179, 2024-01).
    - "$20,000 en préstamos estudiantiles" (U-016-041, 2024-05; U-004-088, 2026-05).
    - "$8,000 de deuda total como junior" (U-015-132, 2025-06).
  - EV-289 añade que los $2,000 podrían ser un error de transcripción frente a los $20,000.
  - **Qué deja el capítulo.** La tabla de variantes de §37.1, fila "Debt", solo dice: "$8,000 of total debt as a college junior (2025); other videos mention student loans of different amounts". La beca completa aparece aparte, como "a scholarship-supported college education (mentioned in other videos)".
  - **Qué falta.** Las dos cifras concretas y la advertencia sobre la posible transcripción errónea.
  - **Dónde debería ir.** §37.1, "The catalogue of failures", tabla de variantes, fila "Debt".

### 4. Términos acuñados no definidos u homogeneizados

- **MENOR — "features, features, features" (término de invitado, Vitali, U-004-040).**
  - El léxico lo registra como el nombre del error de construir funciones por entusiasmo tecnológico en lugar de resolver problemas. También anota su relación con "death by complexity".
  - El capítulo desarrolla la idea en §37.3, "Customer first, and the core job to be done", con "get excited about technology…" y "We are not here building features, we are here solving problems". Pero no usa ni define el término; la búsqueda de "features, features" da cero resultados.
  - Todos los demás términos de invitado del bloque T18 están nombrados y definidos: death by complexity, people company, first principle signal, arbitrary problems, half X designers, single-threaded, zones of genius, the crud of running the back end, meta time / doing time, versions of reality, top nodes down the tree, broken record, yin-yang model, step function, stuck in the mud, tech hole, speed limit y own the IP.
  - **Dónde debería ir.** §37.3, primer párrafo de "Customer first, and the core job to be done", junto a la cita de Vitali.

No hay más hallazgos.

- Los términos acuñados del autor están definidos con su sentido propio: nothing happens then everything happens (con sus renombres), avalanche called insight, beginner hell, I am the market research, success is counterintuitive, force multiplier (con sus dos sentidos y la atribución de uno a Sam Altman), the skill of making money, passion project, cash flow business, vessel for personal growth, forcing my hand, deeper underlying truth, breathing room, marching in place, blurple branding y clean slate.
- El capítulo distingue los dos sentidos de "dissonance" (fase del cambio de identidad frente a disonancia del mensaje del producto). También aclara que "outlier" y "Karma" tienen sentido propio.

### 5. Cambios de posición no presentados o resueltos indebidamente

- **MENOR — EV-290 (la lista de los siete negocios).**
  - La tabla de variantes de §37.1 recoge las versiones de 2022, 2024 y 2025. Omite las dos de 2026:
    - U-004-087 (2026-05): arte digital, fotografía, agencias, dropshipping dos veces y un e-commerce.
    - U-022-106 (2026-08): Facebook ads, SEO, dropshipping, diseño web, arte digital "y algunos más".
  - Ninguna añade negocios nuevos. Pero confirman lo que EV-290 llama "el número siete es estable; la composición no", y extienden la variación hasta 2026.
  - **Dónde debería ir.** §37.1, tabla de variantes (filas "Agencies" o "Duration"), o una frase tras la tabla.

El resto del Anexo A está presentado con sus dos lados y sin resolverse indebidamente:

- EV-067: consistencia frente a persistencia e iteración. Se vincula con la tensión "persist or quit" de §37.3.
- EV-160 y EV-286: horas de escritura y de trabajo.
- EV-287: cifras de ingresos, con la observación de que no cuadran.
- EV-291: del "one-person business guy" a fundador. Incluye la posición de junio de 2023 (U-007-211), que contradice la de marzo.
- EV-292: Cortex → Kortex → Eden, en tabla.
- EV-294: Superhuman 90.
- EV-297: los libros.
- EV-299: escritor o no.
- EV-301: los plazos.
- EV-302: la estrategia "educación primero" frente al balance de 2025. El capítulo admite que el corpus no dice si el curso se ejecutó.
- EV-303: los contratistas autónomos y el trabajo presencial.
- EV-304 y EV-305: las dos tensiones de §37.3. Se presentan como no resueltas por los hablantes, y la reconciliación se marca como lectura del libro.
- EV-306 y EV-307: las tensiones entre los cofundadores de Stan.

### 6. Fuentes de terceros con atribución perdida, confundida o alterada

No hay hallazgos.

- Los marcos de §37.3 a §37.6 se atribuyen de forma sistemática a John Hugh, a Vitali, a Matt o a Ari. Donde la transcripción es ambigua, el capítulo lo dice: por ejemplo, la táctica del referral flywheel, "most likely John".
- Valve (T-shaped) se atribuye a Koe como quien lo cita.
- Twitter se presenta como lectura de Vitali, con la cifra del 80 % que Koe da en otro video. Verifiqué la cifra en `02_unidades/lote-006.md` ("fired 80% of Twitter staff").
- "Make something people want" se atribuye a Paul Graham / Y Combinator, como contexto complementario.
- "Jobs to be done" (Christensen) y "zone of genius" (Gay Hendricks) se marcan como usados por los invitados sin atribución.
- El shipyard es de Dickie Bush, y "mastery facility / physical synthesis" es la reformulación de Koe.
- El distribution studio es de Justin Welsh.
- "Procrastination disguised as productivity" se atribuye correctamente a Koe, conforme al Anexo C (Dickie Bush).

### 7. Argumentos por capas reducidos a su conclusión

No hay hallazgos. Las cadenas se conservan paso por paso:

- El argumento de los tres pasos de Vitali para los diez ingenieros (U-004-039).
- La cadena de los levels of uncertainty (U-024-237).
- El "own the IP": infraestructura, después miles de horas, después "what kind of company are we?" (U-015-194).
- El paso de deadline a stress test, a sync engine y a "deeper underlying truth" (U-015-195, U-015-210).
- La apuesta por la distribución (U-013-079, U-009-040).

### 8. Conceptos usados antes de introducirlos

No hay hallazgos.

- El capítulo explica las remisiones hacia delante: "seasons", con remisión al capítulo 39; la tabla de los 27 principios, con remisión a los capítulos 38 y 39; y los "levels of mind" de la Parte XIV.
- "Seasons" e "intensity phase" ya están introducidos en los capítulos 12 y 13.
- "Dissonance" está introducido en el capítulo 4.
- La "law of conceptual survival" está introducida en el §3.4.

---

## Capítulo 38 — Mapas del desarrollo de la consciencia

### 2. Unidades declaradas como cubiertas pero solo mencionadas

No hay hallazgos. Las 125 unidades están desarrolladas con su mecanismo, sus condiciones y sus ejemplos. Algunos ejemplos verificados:

- **Holones y relaciones.**
  - El holón y sus cadenas múltiples (U-003-120, U-023-047).
  - "Existence is relationship" (U-003-121).
  - El ejercicio de la miel (U-003-122, U-023-050).
  - Las tres características de los "units of mind" y el razonamiento mentalista (U-010-110 a U-010-114).
- **Jerarquías.** Las dos definiciones de dominator hierarchy, con la tabla y la célula cancerosa aplicada al creador intermedio (U-002-051, U-003-125, U-010-113, U-010-124).
- **Orden desde el caos.** La cadena Prigogine → whole parts → psychic entropy (U-019-155 a U-019-157), con la advertencia de qué eslabón es ciencia y cuál interpretación. También "life is problem-solving" (U-024-104).
- **AQAL.** Las dieciséis preguntas de los cuadrantes (U-022-054 a U-022-059).
- **Lines, levels and altitudes.** Los niveles 0–4, first/second tier, el criterio de "seguir pensando", el skill tree y la meseta del líder (U-022-079 a U-022-099).
- **Cook-Greuter.** Las nueve etapas en sus dos versiones (U-021-087 a U-021-106, U-022-014 a U-022-020, U-025-147), con los ocho rasgos de la etapa unitiva y la cita literal.
- **Human 3.0.** La estructura, los cuadrantes, los unlocks, los niveles, los channels y su proceso, los glitches y su riesgo, y la false transformation (U-024-098 a U-024-126).
- **Los tres niveles de contenido** (U-015-163 a U-015-180).
- **Estados, etapas y regresión.** Los estados y etapas con el caso de ingresos (U-023-032 a U-023-036, U-023-034, U-017-222) y las cinco versiones de la regresión.

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

- **MENOR — Arquetipos y metatipos de Human 3.0 (U-024-127, U-024-128, U-024-130, U-024-131, U-024-132; cubiertos en el capítulo 1).**
  - **Qué dice el capítulo.** §38.4, "The structure: quadrants, levels, phases, traits", línea 567: "The transcript names archetypes and metatypes but does not list the specific archetypes; they are not reconstructed here."
  - **Por qué es inexacto.** La afirmación es falsa respecto del corpus. La transcripción de "A Full Guide To Reinvent Your Entire Life" (29:47–31:37) y sus unidades contienen:
    - La definición de arquetipo y de metatipo.
    - Las progresiones por cuadrante: NPC → player → creator; incel → Chad → sigma; religion → atheism → mysticism; job → career → calling.
    - Listas de arquetipos posibles por nivel en los cuatro cuadrantes, como program, sleeper, echo; questioner, skeptic; synthesizer, architect, meta-mind; couch potato… longevity optimizer.
    - El metatipo de ejemplo "the outlier".
  - **Dónde está desarrollado.** El capítulo 1 lo desarrolla en la sección "Archetypes and metatypes: NPC as a level" (`cap-01.md`, líneas 405–420). El material no se pierde para el libro.
  - **Consecuencia.** El capítulo que es sede de Human 3.0 contradice al capítulo 1 y no remite a él. El lector que llega al §38.4 recibe una información errónea sobre el corpus.
  - **Dónde debería ir.** §38.4, en sustitución de la frase de la línea 567. Basta con resumir las cuatro progresiones y remitir al capítulo 1 para las listas y el ejemplo "the outlier".

### 4. Términos acuñados no definidos u homogeneizados

No hay hallazgos.

- Los términos acuñados del bloque están nombrados y definidos con el sentido del autor: units of mind, whole parts, life is problem-solving, survival sponge, orienting generalizations, center of gravity, zoom out a layer, lines/levels/altitudes, surface area of thinking, monkeys copying other monkeys, conventional stage shadow, Source, level zero, cross-quadrant unlocks, channels, glitches, false transformation, fat personal trainer syndrome, level one traps, trendjackers, thought McNuggets / fortune cookie philosophy, brilliant nobodies, value creators y you are the media.
- Las palabras comunes con sentido propio están tratadas con su sentido específico, no con el de diccionario:
  - "spirit": "the connection of minds through the intangible", contrastado con el uso de la Great Chain.
  - "mind": valores, creencias y worldview.
  - "creation": ordenar la consciencia.
  - "altitude": con la nota sobre el uso de Wilber.
  - "medium and message": con sus dos sentidos distinguidos.
- El capítulo señala además que "individualist" nombra etapas distintas en mapas distintos, y que "fifth dimension" cambió de contenido.
- "Identity flips" no aparece con ese nombre, pero las fases dissonance / uncertainty / discovery remiten explícitamente al §4.3, que es su sede y lo nombra.

### 5. Cambios de posición no presentados o resueltos indebidamente

- **MENOR — EV-023 (dominator / actualization hierarchies): cronología de la atribución incompleta.**
  - **Qué dice el capítulo.** En §38.1, "Two kinds of hierarchy: dominator and actualization": "In March 2023 … Koe presents the distinction without any source, as his own way of seeing things … In July 2023 and March 2024 he ties the same distinction to Wilber." La tabla da como fechas de la definición 1 "2023-03, 2024-03".
  - **Qué omite.** El corpus tiene un antecedente anterior: U-023-053 (2023-01-15, "Society Is A Pyramid Scheme"). Allí la distinción, con sus mismos ejemplos (partículas → átomos, letras → palabras, escuelas, gobierno, "hierarchies within hierarchies"), aparece adaptada de Wilber, en el mismo video en que Koe presenta a Wilber y los holones. El capítulo cita ese video para los holones (§38.1), pero no para las jerarquías. La entrada de léxico "dominator hierarchies" registra esa variante de 2023-01-15.
  - **Consecuencia.** La secuencia "primero propia, luego atribuida" no se sostiene. Lo que muestra el corpus es un uso con marco wilberiano (enero de 2023), luego un uso sin fuente (marzo de 2023) y después la atribución explícita al libro (julio de 2023 y marzo de 2024).
  - El error procede de EV-023, pero el capítulo lo hereda sin contrastarlo con su propio material.
  - **Dónde debería ir.** §38.1, párrafo "The first change is attribution", y la fila "Definition 1" de la tabla. El capítulo 2 (§2.5) desarrolla U-023-053 y U-023-054 y remite al 38, así que bastaría una remisión cruzada.
- **MENOR — EV-136 (¿existen las ideas originales?): nivel 4 "generative" sin la tensión ni la remisión.**
  - §38.2 presenta el nivel 4 como "you create original perspectives that didn't exist before, or you come to ideas without outside influence", sin señalar que contradice el "nobody has original ideas, absolutely nobody" de 2024 y el "largely a myth" de 2025.
  - El capítulo 18 trata la tensión con cuidado y remite al 38 (`cap-18.md`, líneas 299–303). El 38 no remite de vuelta.
  - **Dónde debería ir.** §38.2, "Lines, levels and altitudes", tras la definición del nivel 4: una frase con remisión al capítulo 18.

Hay además un matiz que no cuento como hallazgo separado. En EV-018, el capítulo recoge las formulaciones de octubre y diciembre de 2025 hacia "lentes, no mejores". No menciona la de marzo de 2025 (U-025-114: "you go up and down, but there's a baseline"), que ya apuntaba en esa dirección. La omisión no altera la presentación del cambio.

El resto del Anexo A está presentado con sus dos lados:

- EV-004: los porcentajes, presentados explícitamente como estimaciones retóricas.
- EV-017: la sucesión de mapas, en tabla.
- EV-018: jerarquía frente a herramientas. El capítulo no atribuye a Koe la aceptación de la objeción de Eriksen.
- EV-019: gradual frente a extremo. Se presenta en dos sitios y se advierte que la reconciliación no cubre todos los casos.
- EV-024: alter ego frente a false transformation. El criterio se marca como inferencia.
- EV-028: la regresión, en sus cinco versiones.
- EV-031 y EV-032: la atribución.
- EV-057: la entropía como enemigo o como oportunidad.
- EV-061: foco frente a hábitos.
- EV-132 y EV-133: la "fifth dimension" y la escala de cinco niveles.
- EV-141: intelligence → perspective.
- EV-244: el value creator y la atención.
- EV-287: los ingresos.

### 6. Fuentes de terceros con atribución perdida, confundida o alterada

No hay hallazgos.

- El capítulo separa con cuidado lo que es de Wilber, de Cook-Greuter, de Spiral Dynamics, de Prigogine, de Watts, de Leo Gura, de Manson, de Hawkins, de Sowell y de Devon Eriksen, y lo que es de Koe.
- Señala cuándo Koe usa ideas de Wilber sin atribución: whole parts en 2025, el master pattern en 2026, la metacrisis sin Schmachtenberger y AQAL sin Wilber en el anuncio de Human 3.0.
- Marca como contexto complementario las atribuciones que Koe no hace: The Kybalion, Trungpa ("spiritual materialism"), Laloux y los colores de Wilber frente a los de Spiral Dynamics, y la Great Nest of Being.
- Corrige el título de Prigogine ("The End of Certainty").
- Verifiqué en la transcripción que la mención de la pre/trans fallacy en el §38.4 corresponde a Koe ("we'll talk about more of that later when we talk about the pre-trans fallacy"). El término es de Wilber, como dice el capítulo.

### 7. Argumentos por capas reducidos a su conclusión

No hay hallazgos. Las cadenas se conservan y a menudo se hacen explícitas:

- El argumento contra el rechazo de la jerarquía (U-010-109).
- Los tres eslabones Prigogine → whole parts → psychic entropy, con su estatus epistémico (U-019-155 a U-019-157).
- "Life is problem-solving" (U-024-104).
- El criterio de "seguir pensando" por nivel (U-022-084).
- La estructura del riesgo de los glitches (U-024-126).
- La secuencia de seis pasos para entrar en un channel (U-024-123).

### 8. Conceptos usados antes de introducirlos

No hay hallazgos imputables al capítulo 38.

- Todas sus remisiones hacia atrás apuntan a secciones que existen y contienen lo que se dice.
- Las remisiones hacia delante (capítulos 39 y 40: "higher lows", "multi-dimensionally jacked" y la longevidad) están señaladas como tales.

Hay además una observación cruzada, que no cuento en el resumen. Human 3.0 es un concepto cuya sede es el §38.4, pero se usa antes en dos capítulos:

- El capítulo 1 expone arquetipos, metatipos y el ejemplo "the outlier" del modelo (`cap-01.md`, líneas 405–420).
- El capítulo 17 (§17.1) expone la pre/trans fallacy en términos de "level one / level three" de Human 3.0.

En ambos casos la violación de progresión pertenece a esos capítulos y debería reportarla su auditor. La anoto porque explica el hallazgo del punto 3 de este capítulo.
