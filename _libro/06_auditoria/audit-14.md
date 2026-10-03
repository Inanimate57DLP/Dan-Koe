# Auditoría de cobertura — Lote 14 (capítulos 27 y 28)

Auditor independiente, fase 5. Este reporte cubre los puntos 2 a 8 del prompt del auditor para `05_capitulos_en/cap-27.md` y `05_capitulos_en/cap-28.md`, contrastados con `04b_material/cap-27.md` y `04b_material/cap-28.md`. El punto 1 (IDs no cubiertos) lo verificó un script y queda fuera de este reporte.

## Resumen

| Capítulo | PÉRDIDAS | MENORES |
|---|---|---|
| 27 — La marca personal | 0 | 4 |
| 28 — El negocio como obra de vida | 0 | 3 |

**Método y muestra**

- Leí completos los dos capítulos: 1.098 líneas el 27 y 1.100 el 28.
- Pasé dos controles automáticos sobre el 100 % de las unidades (143 en el capítulo 27 y 163 en el 28).
  - **Citas.** Busqué la cita clave de cada unidad en el capítulo, en ventanas de cinco palabras.
  - **Datos concretos.** Busqué en el capítulo los nombres propios y las cifras de los campos `desarrollo` y `ejemplos` de cada unidad.
- Revisé a mano todas las unidades sin coincidencia literal o con nombres o cifras ausentes: unas 25 en el capítulo 27 y unas 30 en el 28. Todas están desarrolladas con otras palabras, o lo que falta es ruido de transcripción (por ejemplo, "Merrick Health" o "Soul bra"), que el capítulo declara ilegible.
- Leí completos los campos `desarrollo`, `ejemplos` y `tension` de más del 40 % de las unidades de cada sección. Prioricé los frameworks, los procesos, los casos, los datos, los términos acuñados y los argumentos.
  - En el capítulo 27 leí entera la sección 27.7 y todas las ideas de clúster.
  - En el capítulo 28 leí entera la sección 28.1 y las unidades de los clústeres de pilares, palancas, rutas y secuencias.
- **Anexo A (evolución).** Revisé el 100 % de las entradas: 20 en el capítulo 27 y 13 en el 28.
- **Anexo B (léxico).** Comprobé automáticamente la presencia de todos los términos: 85 entradas en el capítulo 27 y 105 en el 28. Leí completas unas 35 entradas por capítulo. Prioricé los términos acuñados, los de terceros y las palabras comunes con sentido propio.
- **Anexo C (fuentes).** Leí todas las entradas: 20 en el capítulo 27 y 17 en el 28.
- **Progresión.** Consulté `04_arquitectura.md` y verifiqué con búsquedas en los capítulos anteriores que los conceptos y las remisiones cruzadas estuvieran ya introducidos.

**Juicio global.** Los dos capítulos son de una fidelidad excepcional. Recorren las unidades casi una por una y conservan las cifras, los ejemplos, las fuentes y las fechas.

- Incluyen tablas de evolución para las definiciones de marca, la Trust Matrix, la cadena del diferenciador, los pilares, las palancas, la lectura de "7 billion companies" y las secuencias núcleo.
- Presentan sin resolver indebidamente todas las tensiones del Anexo A. Ejemplos: 3–6 frente a 6–12 meses; "niche" frente a meta amplia; "cannot get saturated" frente a "things can become saturated quite quickly"; "traffic before offer" frente a vender desde el inicio; copiar frente a crear.
- Marcan con contexto complementario las fuentes de terceros.

No encontré ninguna unidad reducida a una frase cuando el material traía mecanismo, condiciones y ejemplos, así que no registro ninguna PÉRDIDA. Los hallazgos son glosas o remisiones imprecisas y un par de términos tratados con otro sentido.

---

## Capítulo 27 — La marca personal

### 2. Unidades declaradas como cubiertas pero solo mencionadas

Sin hallazgos de PÉRDIDA. Las unidades de mayor peso están desarrolladas con su mecanismo y sus ejemplos:

- **Definiciones de la marca.** La definición de 2023 y su trasfondo (U-016-205, U-011-197, U-012-135) y las cuatro etiquetas de la marca, en tabla (U-019-014, U-006-129, U-015-153, U-016-275).
- **Public resume.** Las siete versiones, con sus resultados mínimo y máximo (U-011-027, U-001-046, U-008-052, U-010-086, U-020-111, U-009-193, U-014-037).
- **Perfil.** La trayectoria del perfil y la bio, con la plantilla "I write about A, B and C" (U-013-053, U-009-239, U-009-241) y el caso de las bios de Justin Welsh (U-005-050).
- **La marca como mundo.** "Brand is an environment", con sus cinco consecuencias (U-015-071, U-010-307), la digital house, la marca invisible y el ejemplo de Paul Graham (U-010-311).
- **Arquitectura comercial.** La infinite niche y la ciudad (U-010-099, U-010-107, U-010-126, U-010-135); "build a world, not a funnel", con sus cinco componentes, y las cinco variantes, en tabla; el digital tool stack (U-008-137).
- **Dirección de la marca.** El método de tres pasos del brand goal (U-012-067, U-012-069); las cuatro herramientas de articulación (U-009-118, U-009-123, U-010-351, U-016-278); la cadena identidad → perspectiva → metas del pilar de marca (U-007-212).
- **Trust Matrix.** Reconstruida desde 2022 (U-007-137, U-001-153, U-013-052, U-009-069, U-009-071, U-014-059, U-015-138, U-015-139).
- **Diferenciador.** La cadena completa hasta el swap test (U-001-034 … U-012-193), con el café con L-teanina, Udemy, Zuby, DeepSeek y Typeform.
- **Saturación.** Los cinco grupos de argumentos, incluidas las cuatro razones de 2023 (U-008-019 a U-008-022) y la matización de 2026 (U-008-177).
- **Muerte de la marca personal.** Sus tres arquetipos (U-015-036 a U-015-053, U-014-148, U-016-129, U-007-146).

MENOR (1):

- **Tensión sin explicitar entre U-009-239 y U-009-118.** El material anota que U-009-239 (2024: "they're not following the profile…") matiza U-009-118 (2023: articular la marca en la web, la landing y la bio, sugiriendo meta, problema y puente). El capítulo trata las dos unidades en secciones distintas (27.1 y 27.3) y su síntesis afirma que las cuatro herramientas "treat the bio as a late, compressed output rather than a starting point". No señala que la herramienta de noviembre de 2023 es precisamente un método para la bio y el perfil, ni que la de 2024 la relega. La tensión debería anotarse en 27.3, en "Articulating the brand", junto al párrafo de convergencia.

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

Sin hallazgos. Se conservan:

- **Números.** 10.000 y 50.000 seguidores; 40.000 USD de título; 300–1.000 y 200–700 cuentas seguidas; menos del 1 % de creadores; 300–500 USD por hora; 10.000–100.000 vistas semivirales; 10.000 USD al mes; la mitad de los canales con un millón de suscriptores; cuentas de más de 300.000 seguidores; ciclos de 10–15 y 2–3 años.
- **Metáforas.** El diamante bajo presión, la casa digital, la ciudad, el Marvel Cinematic Universe, planting a flag, la montaña, el foso, el wrapper y los superpoderes.
- **Historias.** Twitter → YouTube, Threads, la planificación con música y Hamza.
- **Procesos.** Las cuatro preguntas de Cortex, las tres preguntas de 2026, los cuatro principios de 2026 y la cadena de seis pasos del moat.

### 4. Términos acuñados no definidos o tratados con sentido genérico

MENOR (2):

- **"Big idea synthesis" glosado con un sentido ajeno (U-007-137, U-001-153; léxico "growth / authenticity / authority" y "big idea").** En 27.4 el capítulo define "big idea" como "a central concept around which a long piece is built". También atribuye la síntesis a "the second-tier thinker of Chapter 18".
  - En el léxico, "big idea" (U-011-172, U-011-176) es otra cosa: un resumen de una frase que ilustra el valor ("Uber is the modern taxi service").
  - El "second tier" del capítulo 18 es una categoría de desarrollo (Spiral Dynamics y Wilber) de un video de 2025. Proyectarla sobre un framework de 2022 es anacrónico.
  - La remisión pertinente sería el sintetizador ("the way of the synthesizer", 18.4) o la big idea en su sentido de 2023.
- **"Infinite game" sin anclaje (U-012-189; léxico "world of replaceability / infinite game").** En 27.6 ("Not winner-takes-all") se cita "this infinite game where you can just experience this growth…" sin remitir al sentido que el capítulo 10 (10.7) dio al término. Tampoco recoge la acepción del léxico: el camino del problem solver como salida de la reemplazabilidad. El lector puede tomarlo como expresión de diccionario.

### 5. Cambios de posición no presentados o resueltos indebidamente

Sin hallazgos. Las entradas del Anexo A con sede en este capítulo están presentadas con fechas y razones o con la ausencia de razón del autor: EV-164, EV-165, EV-171, EV-176, EV-180, EV-181, EV-183, EV-186, EV-189, EV-190, EV-214, EV-221, EV-225, EV-231, EV-241, EV-248 y EV-251. La reconciliación de EV-241 (personas insaturables, formatos saturables) se ofrece como lectura y conserva el cambio de tono. Las entradas cuya sede es otro capítulo (EV-163, EV-177, EV-193) están desarrolladas en los capítulos 25, 18 y 28.

### 6. Fuentes de terceros con atribución perdida, confundida o alterada

Sin hallazgos. Las atribuciones se conservan con su grado de adaptación:

- Naval ("8 billion monopolies").
- "Kevin", del que se adapta "online character".
- Justin Welsh ("walking business", "there's already a me out there", "validation, not competition").
- Las fuentes con contexto complementario: Paul Graham, Anthony de Mello, Eckhart Tolle, Greg O'Gallagher, Zuby, Derek (More Plates More Dates), MrBeast, Lunchly y Prime, DeepSeek y Typeform, Maslow (sin nombre en la transcripción, como se advierte) y Wilber.
- "Some people on Twitter", a quienes Koe atribuye la tesis del app layer, separada de su extensión propia.

### 7. Argumentos por capas reducidos a su conclusión

Sin hallazgos. Se conservan completas las cadenas principales:

- El public resume, con sus premisas y sus dos resultados.
- La cadena identidad → historia → perspectiva → metas → filtro → unicidad, con su condición de movimiento.
- Los seis pasos del moat (moats → DeepSeek → la inteligencia tiende a cero → app layer → everything is a wrapper → tú).
- Las cuatro razones mecánicas contra la saturación.
- La escalera de ofertas que "educates and creates the customers".

### 8. Violaciones de progresión

MENOR (1):

- **Remisión con nombre alterado.** En 27.5 ("The last defensible moat") se remite a "Chapter 22's principle of 'remembering more than innovating'". La sección del capítulo 22 se titula "Reminding More Than Innovating" (22.5). El principio es recordar a otros, no recordar uno mismo, y la alteración cambia el sentido de la remisión.

Las demás remisiones hacia delante se anuncian como tales y no se usan como presupuesto: "value is behavior change" (capítulo 31), "systems economy" (capítulo 33), "doers and directors" (capítulo 36), "escape velocity" (capítulo 37) y Wilber (capítulo 38). Los conceptos previos que el capítulo usa están introducidos antes: intelligent imitation, big irrational goal, purpose/path/priority, perspective vessel, direct response (capítulo 15) y lead magnet.

---

## Capítulo 28 — El negocio como obra de vida

### 2. Unidades declaradas como cubiertas pero solo mencionadas

Sin hallazgos de PÉRDIDA. Las unidades de mayor peso están explicadas con su mecanismo y sus ejemplos:

- **28.1.** La cadena "personal growth equals business growth" (U-009-083, U-009-219); las seis exigencias del negocio, en tabla (U-027-110 a U-027-113, U-027-123); el proyecto de salud medible con el hígado de res (U-010-078).
- **28.2.** Las cinco versiones de "solve your own problems" (U-005-139, U-009-019, U-011-205, U-011-209, U-017-201); los seis pasos de "profit off your purpose"; las dos variantes de "offline it's growth / improvement" (U-005-140, U-003-156, U-009-013), con el análisis de "set a goal"; los tres escenarios del planner (U-010-067, U-013-086, U-019-087); el holistic solution en tres subpasos (U-008-039); el "30 days of walks" (U-024-060).
- **28.3.** La redefinición del emprendimiento (U-010-236, U-005-135, U-012-138) y el aporte de Sahil Bloom, con su ejercicio del bloc de notas (U-005-097, U-005-098). Las advertencias contra las ideas de startup, "landing on Saturn" y la LLC a partir de 50.000 USD (U-008-104, U-006-109, U-007-201, U-012-101).
- **28.4.** Las capas del one-person business (U-007-049, U-007-050, U-006-116); el cambio de 2.0 (U-007-210); las seis razones, en tabla; las cuatro rutas de carrera, en tabla (U-010-061, U-011-219, U-013-090, U-023-188); la evolución de "7 billion companies", en tabla.
- **28.5.** "It's all traffic and offers", con el cálculo del afiliado (U-007-072, U-007-073), el caso de dos ventas de 150 USD al día (U-008-097), el paralelo de las citas en tres versiones (U-008-051, U-025-051, U-016-016), JK Molina (U-007-122) y las ocho versiones de la secuencia núcleo, en tabla.
- **28.6.** Las diez formulaciones de los pilares, en tabla; las cuatro preguntas de producto (U-009-130); las tres preguntas de 2022 (U-007-173); "you are every department" (U-002-113, U-009-096); las tres versiones de las palancas, en tabla, con "simple math" y sus cifras discrepantes (EV-263).

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

Sin hallazgos. Se conservan:

- **Números.** El cálculo completo del afiliado (30 % y 50 %, 100 USD por cuatro retweets, 1 millón de impresiones, 30 %, 1.000 visitas, 5 %, 50 compradores, 2.400 USD de beneficio); 2 × 150 USD, 80 visitas, 2,5 % y 10.000 impresiones; "95 percent"; los umbrales de 50.000 USD para la LLC, 100.000 USD a 3–5 millones al año, 5–10 millones al año, 5–6 años y 2–4 años; el ebook de 50 citas a 10 USD; los 0,05 USD por encuesta.
- **Historias.** La agencia de diseño web, la cena de Welsh con el CEO del unicornio, Ralph Lauren vía Ryan Ayala con el short de algodón, Coca-Cola, PatientPop y Mark Roberge (estas dos, en el capítulo 27) y Rework/Shark Tank.
- **Metáforas.** Los macronutrientes y micronutrientes, la business keto diet, Saturno, la cacería moderna, el grifo, full circle y la camiseta negra.

### 4. Términos acuñados no definidos o tratados con sentido genérico

MENOR (1):

- **"Lever-moving actions" disuelto en paráfrasis (U-025-051; léxico "lever moving actions").** En 28.5 ("It's all traffic and offers") el texto dice "the business actions that move the lever are building distribution". La unidad usa el término acuñado lever-moving actions, que en el léxico equivale a los fundamentals o a las tareas prioritarias cuantificables y que capítulos anteriores ya introdujeron (12, 13 y 30, entre otros). El capítulo no lo nombra ni remite a su definición, de modo que la expresión se lee en su sentido genérico.

Los demás términos con sentido propio se marcan como tales y se definen: business (con la definición legal de 2024), starving artist, full circle, forcing function (de Bush), self-monetization, mental monetization, gatekeeper mindset, public market, education business, positive aim (atribuido a Peterson), consume-and-save mindset, present purpose, measurable personal project, purpose-oriented project, intrinsic philosophy y evergreen vessels.

### 5. Cambios de posición no presentados o resueltos indebidamente

Sin hallazgos. Todas las entradas del Anexo A están presentadas:

- EV-026: la cita de "Einstein", de sin atribución a firme y luego a "supposedly", con contexto complementario.
- EV-100 y EV-173.
- EV-192: la definición de 2022 frente a la de 2.0.
- EV-193: los pilares, en tabla, con la ausencia de razón del autor.
- EV-199: las palancas.
- EV-200: "traffic before offer" frente a vender ya, explícitamente "never resolves".
- EV-203, EV-221 y EV-229 (empleado y emprendedor como estados mentales).
- EV-231: desaparición → descentralización → elitización.
- EV-239: code frente a content.
- EV-247: el UBI hasta 2024-10, con remisión al capítulo 36 para el análisis posterior.
- EV-263.

Las reconciliaciones se ofrecen como lecturas y no borran el cambio.

### 6. Fuentes de terceros con atribución perdida, confundida o alterada

MENOR (1):

- **Atribución conjetural añadida (U-005-048 frente a U-007-210).** En 28.6 ("You are every department"), tras exponer las "three pieces of the pie" de Justin Welsh, el capítulo afirma que la redefinición de 2023 del one-person business ("put yourself out there until enough people know who you are, what you do and why you do it") "repeats Welsh's phrasing almost exactly, which suggests, though Koe does not say so, where it came from".
  - El corpus no registra esa filiación.
  - Koe usa la misma fórmula en un contexto propio en febrero de 2023 (U-014-058, capítulo 27: "who you are, what you do and why you do it" sobre la formación de la marca).
  - La frase es, además, un giro común del marketing.
  - La conjetura sobra o debería marcarse con más cautela, para no sugerir un origen de tercero que la fuente no da.

Las demás atribuciones son correctas:

- Naval ("7 billion companies", "make something people want… make something you want").
- Dickie Bush (forcing function).
- Sahil Bloom ("enterprising", con el ejercicio y la "garantía" marcados como opinión del invitado).
- Justin Welsh.
- JK Molina.
- Ryan Ayala sobre Ralph Lauren.
- Rework y 37signals.
- Eugene Schwartz (levels of awareness).
- La frase de los "25 años", con su atribución popular a Franklin y la mención de Bloom.
- La no-dualidad como adaptación.

### 7. Argumentos por capas reducidos a su conclusión

Sin hallazgos. Se conservan completas las cadenas principales:

- Creatividad → expansión de la mente → oportunidades registradas → modelo de negocio elegible.
- Producto nuevo → identidad nueva.
- Valorar el negocio → valorar el propio desarrollo → energía, dinero y satisfacción.
- Meta → problema → solución → documentación → proceso replicable → transmisión.
- Startup sin experiencia → mente estrecha → idea probablemente ya intentada.
- El "simple math", con su lectura como reencuadre y no como predicción.

### 8. Violaciones de progresión

Sin hallazgos. Las remisiones hacia atrás apuntan a secciones verificadas:

- 2.4 (hunting psyche) y 2.6.
- 9.1 y 9.4.
- 10.7 (infinite games).
- 17.5 (knowing frente a understanding, con la imagen horizontal y vertical).
- 19.2 y 19.4.
- 20.4.

Las remisiones hacia delante se anuncian como tales: minimum viable offer y permission to suck (capítulo 29), el roadmap (capítulo 30), "value is perception" y positive behavior change (capítulo 31), persuasión y levels of awareness (capítulo 32), skill stack (35.5), "NBA of jobs" (36.3) y el paso a startup (capítulo 37). Los términos previos que se usan sin glosa (Eternal markets, level of mind, curiosity loop, tutorial hell, former self, high agency, digital real estate) están introducidos en capítulos anteriores.
