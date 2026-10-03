# Auditoría de cobertura — Lote 16 (capítulos 31 y 32)

Este reporte es de un auditor independiente, en la Fase 5. Cubre los puntos 2 a 8 del prompt del auditor para `05_capitulos_en/cap-31.md` y `05_capitulos_en/cap-32.md`. Los contrasté con `04b_material/cap-31.md` y `04b_material/cap-32.md`. El punto 1 (IDs no cubiertos) lo verificó un script y queda fuera de este reporte.

## Resumen

| Capítulo | PÉRDIDAS | MENORES |
|---|---|---|
| 31 — Qué es el valor | 0 | 6 |
| 32 — Persuasión y marketing | 1 | 5 |

**Método y muestra.**

- Leí completos los dos capítulos: 975 líneas el 31 y 1021 el 32.
- Del material leí el 100 % de las unidades de las cinco secciones del capítulo 31 y de las seis del 32, con todos sus campos (desarrollo, ejemplos, cita, origen y tensión). Las comparé sección por sección con el texto del capítulo.
- Revisé el 100 % del Anexo A: 15 entradas en el 31 y 15 en el 32.
- En el Anexo B comprobé la presencia de todos los términos: 88 en el 31 y 72 en el 32. Leí completas todas las entradas del 31 y unas 30 del 32. Prioricé los términos acuñados, las palabras comunes con sentido propio y los términos de terceros.
- En el Anexo C leí todas las entradas, unas 20 por capítulo.
- Para la progresión consulté `04_arquitectura.md`. Para verificar remisiones busqué con grep en los demás capítulos (`cap-19`, `cap-22`, `cap-23`, `cap-28`, `cap-34`, `cap-36`, `cap-38` y `cap-40`).

**Juicio global.** Los dos capítulos tienen una fidelidad muy alta. Conservan casi literalmente los mecanismos, las cadenas argumentales, los ejemplos, las cifras y las metáforas de las unidades. También presentan con cuidado las tensiones del Anexo A y separan las fuentes de terceros con contexto complementario.

- **Capítulo 31.** No tiene pérdidas. Sus hallazgos son matices: definiciones del autor sobre "value" sin remisión, cambios de posición que se presentan solo en parte y un término que se usa antes de introducirse.
- **Capítulo 32.** Tiene una PÉRDIDA. La tercera de las "three tensions" (progress) se presenta como si el autor no la hubiera definido y se reconstruye con otro contenido. La definición del autor, sin embargo, existe en el corpus (U-013-234). El capítulo 38 la desarrolla y remite de vuelta a la §32.4.

---

## Capítulo 31 — Qué es el valor

### 2. Unidades declaradas como cubiertas pero solo mencionadas

No hay hallazgos. Todas las unidades de tipo framework, proceso, método, historia, caso, metáfora, dato, término acuñado, fuente de tercero y argumento están desarrolladas con su mecanismo, sus condiciones y sus ejemplos. Algunos ejemplos:

- La cadena entropía → evolución → propósito (U-003-232, U-024-065), con la cita no atribuida y el tractor (U-003-063, U-017-012, U-017-013).
- La value equation de 2024 (U-027-247, U-027-248, U-027-262).
- Los ocho pasos de value creation, desarrollados paso por paso (U-011-161 a U-011-176), y la tabla de correspondencias con los nueve Legos (U-013-083).
- Los macronutrientes y micronutrientes con su ejemplo de la 4-Hour Workday (U-027-250 a U-027-260).
- Las cinco variantes de la fórmula de transformación, en tabla (U-008-066, U-009-136, U-009-224, U-016-033, U-026-163).
- Las objeciones a los info-productos (U-006-111, U-006-113, U-008-106, U-009-154, U-016-026, U-006-115, U-007-193).
- El caso del curso de agencia de Billy Willson (U-010-001, U-010-004, U-007-106, U-010-006).

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

- **MENOR — U-010-001 (primer curso de negocios).**
  - La unidad fecha la compra "six years before the video" (2023-01). Eso sitúa la compra hacia 2017.
  - El capítulo conserva el resto: la desconfianza previa, Udemy, la cifra ambigua "9.99 or 9.97" y "a huge chunk out of my finances". Omite la datación.
  - Debería ir en §31.5, "The author's case: the six-figure agency course", primer párrafo.

### 4. Términos acuñados no definidos u homogeneizados

- **MENOR — "value" (léxico, palabra común con sentido propio).**
  - El capítulo dedicado a definir el valor no menciona dos de las definiciones que registra el léxico:
    - "the relationship between what you do, why you do it, how you do it and who benefits from that equation" (U-026-156, 2023-12/2024-03).
    - "value is ideas written from the lens of a specific goal or problem" (U-009-213, U-008-058, 2023-03).
  - Tampoco remite a donde se tratan: la primera está en el capítulo 34 y la segunda en el 22.
  - El problema se agrava porque el §22.1 del capítulo 22 afirma que la definición "relationship between…" se trata "in passages treated in Part XI". La Parte XI no la trata. La remisión del capítulo 22 apunta al lugar equivocado.
  - Debería ir en §31.1, "Value as structured communication, sense-making and a signal of meaning". Allí basta una nota que sitúe estas definiciones junto a las de 2024, con remisión a los capítulos 22 y 34.
- **MENOR — "tell a story / make a map / enforce a habit" (U-009-163).**
  - El capítulo presenta el aforismo de 2025 en §31.4, "A product is a system for behavior change", y dice que el autor "does not develop the line further".
  - El léxico registra la versión de 2023 del mismo marco: brand = tell a story, content = make a map, product = create a game, marketing = sell to yourself. El capítulo 19 la desarrolla en una tabla (cap-19, línea 308).
  - En la versión de 2023, el producto era "create a game" (proyectos personales públicos). En 2025 pasa a "enforce a habit". Ese cambio, y la remisión al capítulo 19, faltan.
  - Debería ir en §31.4, junto al aforismo.

### 5. Cambios de posición (Anexo A) no presentados o resueltos indebidamente

Las 15 entradas del Anexo A están presentadas, casi siempre de forma explícita y sin resolverlas indebidamente: EV-008, EV-110, EV-113, EV-171, EV-187, EV-209, EV-211, EV-218, EV-219, EV-224, EV-226, EV-237 y EV-242. Las excepciones son estas:

- **MENOR — EV-231 (¿desaparece el empleo?).**
  - La tabla de posiciones sobre el trabajo y la IA de §31.1, "If a machine can replace your job", recoge "on the horizon of complete removal". Después concluye: "The underlying thesis does not change: evolution solves the problem of labor".
  - EV-231 registra una corrección implícita de esa tesis: el empleo se transforma y se elitiza, en lugar de desaparecer. Las fuentes son "I don't see employment going away" (U-012-090, 2024-06) y "the jobs of the future will be reserved for the elite… the entry level is going extinct" (U-010-238, 2025-02).
  - El capítulo 36 trata esta evolución, pero el 31 no la menciona ni remite a ella. Por eso la frase "the underlying thesis does not change" queda como una resolución que la entrada no respalda.
  - Debería ir en §31.1, como fila adicional de la tabla o como nota con remisión al capítulo 36.
- **MENOR — EV-274 (espiritualidad y negocio).**
  - El capítulo presenta solo el paso 2023 → 2024, de "understanding your part in the whole" a "discovering… transcending" (§31.1, "Spirituality as your part in the whole"). Lo califica como refinamiento.
  - Omite el punto de partida de 2022, en el que lo místico no se articula y el bodhisattva de Watts equilibra lo místico y lo material (U-023-024, U-023-028).
  - Omite también el punto de llegada de 2024-11: las metas prácticas "are not anti-spiritual, they are spirituality" (U-021-059, U-021-060).
  - Así se pierde el "cambio exacto" que registra la entrada: de equilibrar dos planos a integrarlos.
  - El capítulo 40 contiene ambos extremos. Falta al menos la remisión desde §31.1.

### 6. Fuentes de terceros con atribución perdida, confundida o alterada

No hay hallazgos en este capítulo.

- Las atribuciones se conservan y se separan correctamente:
  - La cita no atribuida "Evolution is forced on us…".
  - Zero HP Lovecraft, Naval y Chris Paik ("Pake").
  - Justin Welsh, con el testimonial flywheel, aggregation y give freely.
  - Eddie Shlainer, con curtain language a través de Welsh.
  - Dickie Bush, como articulador de una idea de Koe.
  - Matt Ogus, Billy Willson, la escritura religiosa y *The Gentle Seduction*.
- La inconsistencia de fecha de *Cashvertising* entre los capítulos 31 y 32 se reporta en el capítulo 32.

### 7. Argumentos construidos por capas reducidos a su conclusión

No hay hallazgos. Las cadenas se conservan paso a paso:

- La espiritualidad: conexión → dinero → contradicción → definición positiva.
- La value equation: caos → sistemas → metas → problemas.
- Las premisas de "information products are the greatest product one can sell".
- La secuencia mente → acción → resultado → atribución de "brand is transformation".

### 8. Violaciones de progresión

- **MENOR — "level three creator" / "level-one creator" (U-015-182).**
  - §31.5, "Why information is 'the greatest product one can sell'", usa el modelo de los tres niveles de creador: "a developed ('level three') creator", "anyone can become a level-one creator".
  - Ese modelo se desarrolla en el capítulo 38 (U-015-180 está en su bloque COBERTURA). Antes solo aparece una mención de pasada en el capítulo 2 (línea 709).
  - La glosa "developed" ayuda, pero falta una remisión al capítulo 38 o una explicación mínima de los tres niveles.

---

## Capítulo 32 — Persuasión y marketing

### 2. Unidades declaradas como cubiertas pero solo mencionadas

- **PÉRDIDA — La tensión de progreso (tercera de las three tensions; U-013-234, asignada al capítulo 38). Afecta también a los puntos 6 y 7.**
  - **Qué dice el capítulo.** En §32.4, "From eight human desires to three tensions", el capítulo afirma que el video define a fondo las dos primeras tensiones y que la tercera "is defined mainly through the levers that pull it". Añade: "The material gathered here does not contain a standalone definition of the progress tension". Después la reconstruye por su cuenta como "the desire to move toward a better state, which, in Koe's broader writing, also links to the 'progress' stages of Spiral Dynamics".
  - **Qué dice el corpus.** La definición del autor existe en el mismo video (2026-07-05, 10:20–11:29):
    - Las tres tensiones "each build on top of each other. People kind of evolve through the stages", según el patrón de "Maslow's hierarchy, the stages of ego development, spiral dynamics, developmental psychology in general".
    - Primero se necesitan seguridad y comodidad, luego pertenencia y estatus, y solo después "they crave deeper meaning, purpose, and experience".
    - La gente puede desear cualquiera de las tres en distintos momentos ("AI can't just pin down exactly where you are"). Leer el nivel de otro es una habilidad difícil: "you're essentially able to read people's minds when you get it right".
    - Bajo estrés o tras perder dinero se regresa a la supervivencia, donde se es "more susceptible to exploitation".
  - **Qué se pierde.**
    - La estructura acumulativa y secuencial del modelo. Las tres tensiones son etapas que se apoyan unas en otras, no tres puntos de presión paralelos.
    - El contenido real de la tercera tensión: sentido, propósito y experiencia, no un genérico "estado mejor".
    - La regresión y su consecuencia ética, que conecta directamente con la ética de §32.2 y con "work them up the ladder".
    - La atribución correcta: la fuente es una adaptación de Maslow, del ego development y de Spiral Dynamics, no "progress stages of Spiral Dynamics", que no es una formulación del autor ni de Spiral Dynamics.
  - **Agravante.** El capítulo 38 trata U-013-234 y dice que las tensiones están "developed in Section 32.4". Las dos remisiones se cruzan y ninguno de los dos capítulos presenta el marco completo donde se anuncia.
  - **Dónde debería ir.** En §32.4, como subsección "Tension 3: progress", entre "Tension 2: identity" y "Who is in which tension". La afirmación de que no hay definición debe eliminarse.

Fuera de este caso no hay hallazgos. Las demás unidades están desarrolladas con su mecanismo y sus ejemplos:

- Los seis elementos de U-004-146, en tabla.
- La integración de la Shadow, en sus cuatro pasos (U-008-003, U-016-167, U-016-169, U-016-171).
- Las cinco palancas y sus ejemplos (U-013-240 a U-013-247).
- Las cuatro versiones del nivel 5 de awareness, en tabla.
- El cuestionario de seis preguntas (U-009-260) y el guion de DM en cuatro pasos (U-009-263).
- La landing page, en tabla y con el ejemplo "Attention Marathon" (U-009-186 a U-009-188).
- Los lead magnets (U-010-146, U-010-147) y el caso de John Hu (U-008-153, U-015-155).

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

No hay hallazgos. Todos los ejemplos y cifras del material están presentes:

- Hot Pockets, el ayuno intermitente y la biomechanical movement therapy.
- Los cien DMs semanales en CapCut y el ebook con 40 → 500 seguidores y $3.000.
- La ratio de 50–100 compradores por cada comentario negativo y los $1.000 por cuatro sesiones.
- El currículum de $10 y los 3,9 millones de vistas de "You're Not Forgetful".
- El ángulo "crappy" de la promoción y los ocho a diez lead magnets con sus nombres.

### 4. Términos acuñados no definidos u homogeneizados

- **MENOR — "market sophistication" (léxico: cuatro sentidos).**
  - En §32.3, "Schwartz's five stages", el capítulo presenta el cambio como un paso único: de la definición propia de 2023 ("awareness of the products and services available") al modelo de etapas de Schwartz de 2026.
  - Omite dos usos intermedios que registra el léxico:
    - En 2025-05 (U-012-163, "market sophistication / cookie cutter"), la sofisticación sube y el formato estándar cambia cada mes.
    - En 2025-08 (U-025-208), los outputs genéricos inundan el mercado, aburren y "el péndulo vuelve".
  - Estos usos muestran que el término siguió en uso, con sentidos dinámicos, entre las dos definiciones. Falta al menos una mención o remisión, por ejemplo al capítulo 15, que usa el término en ese sentido móvil.

### 5. Cambios de posición (Anexo A) no presentados o resueltos indebidamente

Las 15 entradas están presentadas: EV-152, EV-181, EV-200, EV-206, EV-209, EV-210, EV-211, EV-212, EV-213, EV-215, EV-217, EV-223, EV-232 y EV-233 con buen detalle, y EV-212 y EV-223 incluso en tabla. Las salvedades son estas:

- **MENOR — EV-220 (uso de "manipulation").**
  - En §32.2, "Persuasion is not manipulation", el capítulo presenta el cambio como lineal: uso neutro en agosto de 2023 (U-013-081) → uso peyorativo "by March and September 2024". Concluye que "only the word moved".
  - La entrada registra que ya en 2022 el autor llamaba estafa a la "exploitation and manipulation toward a non-mutual benefit" (U-007-131; U-001-131), con sentido peyorativo. El capítulo 23 recoge ese pasaje.
  - El uso neutro de 2023 es, por tanto, una oscilación dentro de un uso mayoritariamente peyorativo, no el punto de partida de una evolución. Debería ir en el párrafo "The vocabulary itself changed", con la cita de 2022.
- **MENOR — EV-193 (los pilares del one-person business).**
  - §32.5 presenta dos veces el marketing como "fourth pillar": "selling to yourself", en 2023-06, y "pillar 4 (marketing)", en 2024-07.
  - No advierte que ese pilar recibió varios nombres (monetization, marketing, offer, promotion) ni que en 2026 desaparece: "the three pillars, which used to be four… are brand, content, and product" (U-010-296).
  - Los capítulos 19, 21 y 28 lo tratan. Falta una nota o remisión en §32.5, sobre todo porque la sección defiende la promoción como pilar indispensable.

### 6. Fuentes de terceros con atribución perdida, confundida o alterada

- **(Ver la PÉRDIDA del punto 2.)** La tensión de progreso se atribuye a unas "'progress' stages of Spiral Dynamics" que no existen como tales. La adaptación del autor es de Maslow, del ego development, de Spiral Dynamics y de la psicología del desarrollo en conjunto (U-013-234). El propio Anexo C (entrada Spiral Dynamics) la describe como "insumo de… la tensión de progreso del marketing".
- **MENOR — *Cashvertising* (Drew Eric Whitman).** La fecha es inconsistente entre capítulos. El contexto complementario de §31.3 ("Step 2: the eight human desires") la fecha en 2008, y el de §32.4 ("From eight human desires to three tensions"), en 2009. Hay que unificar.

Las demás atribuciones están bien separadas:

- Schwartz, con su atribución oscilante documentada.
- Goethe, con la nota sobre Schelling.
- Naval y "poppy Nal", con la ambigüedad declarada.
- Justin Welsh y los trust tripwires, John Hu y Stan, Michael (Modern Mastery), Zeigarnik, Jung (Shadow) y Carnegie.

### 7. Argumentos construidos por capas reducidos a su conclusión

- **(Ver la PÉRDIDA del punto 2.)** El modelo de 2026 se construye por capas: supervivencia → identidad → progreso, cada una apoyada en la anterior, con regresión posible. En el capítulo queda reducido a tres tensiones paralelas y cinco palancas.

Las demás cadenas se conservan:

- Los cuatro pasos de la Shadow.
- Las cuatro formulaciones de "sales equals survival".
- La cadena final de §32.1: experiencia → naturaleza humana → capa base → iceberg → práctica.
- La ética como diagnóstico (modo supervivencia → manipulación → desarrollo).

### 8. Violaciones de progresión

- **MENOR — Modelos de etapas de desarrollo usados antes de su introducción.**
  - La arquitectura dice que el capítulo 32 "requiere el capítulo 31 y la estructura de escritura (capítulo 23)". Sin embargo, la introducción declara: "From Chapter 4 and Chapter 38 it needs the *level of mind*". Es una dependencia explícita de un capítulo posterior.
  - A lo largo del capítulo se usan sin introducirlos:
    - Las "stages" a las que el value creator ayuda a subir (§32.2, "A tool only as ethical as the hand that holds it").
    - Las "nine stages of ego development (Actualized.org)" y Spiral Dynamics, "both of which Chapter 38 discusses" (§32.3, "Content at each level").
    - Las "survival and identity stages" del 90–95 % (§32.4, "Who is in which tension").
  - Esos modelos se presentan en el capítulo 38. Las remisiones hacia adelante existen, pero el lector de la §32.4 necesita el modelo de etapas para entender "work them up the ladder". Se puede resolver introduciéndolo en esa sección; ver la PÉRDIDA del punto 2.
