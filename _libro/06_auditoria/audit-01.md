# Auditoría de cobertura — Lote 01 (capítulos 01 y 02)

Auditor independiente. Fase 5. Alcance: puntos 2–8 del prompt del auditor para `05_capitulos_en/cap-01.md` y `05_capitulos_en/cap-02.md`, contrastados con `04b_material/cap-01.md` y `04b_material/cap-02.md`. El punto 1 (IDs no cubiertos) lo verificó un script y queda fuera de este reporte.

## Resumen

| Capítulo | PÉRDIDAS | MENORES |
|---|---|---|
| 01 — La Matrix: cómo se programa una mente | 0 | 10 |
| 02 — Las instituciones del camino por defecto y la salida consciente | 0 | 6 |

**Método y muestra.**

- Leí completos los dos capítulos.
- Del material revisé el campo `desarrollo` (más ejemplos, cita, origen y tensión) del 100 % de las unidades: 211 en el capítulo 01 y 215 en el 02. Lo comparé con el texto del capítulo sección por sección.
- Además pasé un control automático. Busqué en el capítulo la cita clave de cada unidad, en ventanas de cinco palabras. Las pocas unidades sin coincidencia literal (5 en el capítulo 01 y 6 en el 02) las revisé a mano, y todas están desarrolladas con otras palabras.
- Revisé el 100 % de las entradas del Anexo A: 26 en el capítulo 01 y 20 en el 02.
- En el Anexo B comprobé la presencia de todos los términos (173 en el 01 y 127 en el 02) y leí completas unas 40 entradas por capítulo. Prioricé los términos acuñados, las palabras comunes con sentido propio y los términos de terceros.
- En el Anexo C leí todas las entradas (unas 33 en el 01 y 37 en el 02).
- Para la progresión consulté `04_arquitectura.md`.

**Juicio global.** Los dos capítulos tienen una fidelidad muy alta. Conservan los mecanismos, las condiciones, las cadenas argumentales numeradas, los ejemplos, las cifras y las metáforas de casi todas las unidades. Marcan las fuentes de terceros con contexto complementario y presentan las tensiones del Anexo A sin resolverlas indebidamente. No encontré ninguna unidad que el capítulo reduzca a una sola frase cuando el material traía mecanismo y ejemplos. Por eso no registro ninguna PÉRDIDA. Los hallazgos son matices: un error de datación, términos que se usan antes de definirse, dos atribuciones de terceros que se pierden y un término glosado con su sentido estándar en lugar del sentido del autor.

---

## Capítulo 01 — La Matrix: cómo se programa una mente

### 2. Unidades declaradas como cubiertas pero solo mencionadas

Sin hallazgos de PÉRDIDA. Todas las unidades de tipo framework, proceso, método, historia, caso, metáfora, dato y argumento están explicadas con su mecanismo y sus ejemplos. Algunos ejemplos:

- El bucle de nueve pasos (U-023-214), en tabla.
- Las seis capas de la social matrix (U-023-205 a U-023-212).
- La cadena de evolución genes→memes (U-024-143 y U-024-144).
- Los tres signos de la mente cerrada (U-017-077, U-017-078 y U-017-080), en tabla y con su mecanismo.
- El proceso de intelligent imitation en sus dos numeraciones (U-014-031, U-023-098, U-023-100 y U-023-103).
- Los arquetipos y metatypes con las cuatro listas completas (U-024-127 a U-024-132).
- La cadena del desajuste evolutivo en siete pasos (U-015-159), con los detalles de U-018-023 a U-018-026.
- Los ciclos anidados (U-023-019), en tabla.
- Los tres encuadres del ejemplo del converso vegano (U-026-255, U-020-084 y U-026-195).

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

- **MENOR — U-023-208 (capa 4 de la social matrix).** El capítulo omite el último eslabón de la circularidad que da el autor: "Teachers trained on government-provided material that found its way into information sources". Todo lo demás está (Google, Wikipedia, la fe en estudios no validados, "This should just terrify you"). Debería ir en §1.1, "The social matrix: a loop that reproduces itself", al final de la capa 4.
- **MENOR — U-023-141 (purpose crisis).** Se pierde el vínculo explícito que el autor hace entre la dopamina y el flow: la dopamina "plays a crucial role in flow but goes beyond". El capítulo solo dice que eso explica por qué la dopamina se volvió un tema popular. Debería ir en §1.3, "The consequence: a purpose crisis".

### 4. Términos acuñados no definidos u homogeneizados

- **MENOR — "finite games" (léxico: *infinite game / finite games*).** En §1.7 ("A case study: the diet prophet") se cita "You can notice these finite games and choose not to play them". No hay definición ni remisión al §10.7, donde la arquitectura ubica el par finito/infinito. El lector recibe el término con su sentido de diccionario.
- **MENOR — "hierarchy of goals".** Aparece en §1.2 ("the ordered consciousness or the hierarchy of goals", en una cita) y en §1.7 ("That, he says, is the purpose of a hierarchy of goals") sin glosa. El léxico lo registra como término propio con sentido técnico: la estructura de meta final, sub-metas y checkpoints. El capítulo 02 lo define recién en §2.1, y la arquitectura lo desarrolla en el §8.1. Ver también el punto 8.

### 5. Cambios de posición (Anexo A) no presentados o resueltos indebidamente

Las 26 entradas del Anexo A están presentadas, casi siempre con su cita a `03b_evolucion.md`. Las que pertenecen a otros capítulos, como la EV-002 y la EV-003 sobre la escuela, se derivan de forma explícita al capítulo 2.

- **MENOR — EV-005 (conformidad: de enemigo a herramienta consciente).**
  - El capítulo cita EV-005 en §1.7 ("The three signs of close-mindedness", segundo signo) como apoyo de un matiz sobre la *selfish perspective*. Ese no es el contenido de la entrada. EV-005 registra el paso de "the problem is that we conform" a "we're all conformist in some ways... it can be used like a tool" (U-013-194, 2025-12).
  - A su vez, §1.3 ("Chosen problems and the axis of suffering") presenta "Conformity is the default state, and 'we don't want conformity, we want creativity'" (U-027-222, 2025-01) sin avisar que el autor matiza esa posición después. El cambio se desarrolla en el capítulo 35, pero aquí no hay remisión.
- **MENOR — EV-025 (autenticidad frente a imitación).** §1.4 ("Intelligent imitation") presenta los momentos 2022, 2023 y 2026. Omite el escalón intermedio que registra la entrada: en 2025 el autor responde con su ensayo escolar a quienes ven un alter ego como inauténtico (U-025-096). Si la unidad se cubre en otro capítulo, aquí falta al menos la remisión.

### 6. Fuentes de terceros con atribución perdida, confundida o alterada

- **MENOR — "deep generalist" (Daniel Schmachtenberger).** §1.3 ("The mind as an operating system made of goals") cita "study the generalized principles of nature and become a deep generalist" como formulación del autor. El léxico y el Anexo C registran el término como de Schmachtenberger, adoptado por el autor como identidad *future-proof*. El capítulo remite al capítulo 20, pero no menciona el origen. Schmachtenberger aparece en el mismo capítulo (§1.5) solo por los *epistemic commons*.
- **MENOR — finitos/infinitos (James P. Carse).** El Anexo C registra que el vocabulario de juegos finitos e infinitos procede de Carse y que el autor no lo nombra. §1.7 lo usa sin el contexto complementario que el capítulo da a casi todas las demás fuentes.
- **MENOR — "hierarchy of goals" y Csikszentmihalyi.** El léxico asocia el término a Csikszentmihalyi en el material. El capítulo menciona a Csikszentmihalyi para *order in consciousness* (§1.2) y *psychic entropy* (§1.5), pero no para este término.

No hay otros hallazgos. Están bien atribuidas las fuentes de McKenna, Hoffman, actualize.org/Leo Gura, Krishnamurti, Dawkins (memes), Herman/Chomsky, Thiel/Girard, Maltz, Graham y Cialdini vía Dickie Bush, Devon Eriksen, Wilson Mizner, Kleon, Emerson, de Mello ("born asleep"), *The Kybalion*, el test del malvavisco, *WALL-E* y la cita de autoría incierta sobre los ensayos.

### 7. Argumentos por capas reducidos a su conclusión

Sin hallazgos. El capítulo conserva explícitamente todas las cadenas:

- La percepción respaldada por el condicionamiento, en cuatro pasos (U-023-003).
- La trayectoria por defecto, en cinco pasos (U-024-032).
- La cadena meta→aprendizaje, en cuatro pasos (U-006-078 y U-013-166).
- La cadena información→condicionamiento→identidad→conducta→trayectoria (U-014-115).
- El desajuste evolutivo, en siete pasos (U-015-159).
- Los mecanismos de los tres signos de la mente cerrada.

### 8. Conceptos usados antes de introducirlos

- **MENOR — "alter ego".** En §1.2 ("A new computer with eighteen years of code") se lee: "that is where identity work and the alter ego come in", sin definición ni remisión. La arquitectura lo ubica en el §4.5.
- **MENOR — "monk mode" y "dopamine detox".** En §1.7 ("A case study: the diet prophet", Superhuman 90) se nombran como componentes del producto sin glosa ni remisión. La arquitectura los ubica en el §11.4.
- **MENOR — "hierarchy of goals" y "finite games".** Ver el punto 4: aparecen en §1.2 y §1.7, antes de su desarrollo (§2.1, §8.1 y §10.7).
- **MENOR — "psychic energy".** En §1.7, en el caso del converso vegano ("most of it is psychic energy being freed up"), se usa sin glosa. La noción de energía psíquica y orden en la consciencia es materia de la Parte III (capítulo 5).

Los demás usos anticipados llevan una remisión explícita y no son violaciones: *conceptual survival* (cap. 3), *mental body* (cap. 3), *Nature's Compass* (definido en §1.3 antes de usarse en §1.5), *flow* (cap. 10), *Human 2.0* (cap. 38), *level one thinking* (cap. 38), *deep generalist* (cap. 20) y *anti-vision* (glosado in situ).

---

## Capítulo 02 — Las instituciones del camino por defecto y la salida consciente

### 2. Unidades declaradas como cubiertas pero solo mencionadas

Sin hallazgos de PÉRDIDA. Están desarrolladas con su mecanismo, sus condiciones y sus ejemplos, entre otras:

- La cadena cibernética del default path (U-021-200).
- El experimento de los perros (U-013-198).
- El gráfico *psychology of employment* (U-012-005), en tabla.
- La definición de *force* y la definición operativa de esclavitud (U-016-184, U-016-185, U-016-202, U-012-203 y U-012-210).
- Las dos jerarquías (U-023-053) y la salida en dos pasos (U-023-060).
- La pirámide de atención con sus dos "realizations" (U-016-194 a U-016-197).
- El juego de estatus (U-027-241 a U-027-244 y U-026-226).
- Las bases tecnoeconómicas (U-018-020 y U-018-021), en tabla.
- La cadena condicional de la nueva sociedad (U-016-149), en tabla.
- El tiempo psicológico (U-026-009 a U-026-014).
- El ejemplo del culturista (U-026-071).
- La metacrisis, con sus *generator functions* y *attractors* (U-015-161, U-014-118, U-014-119 y U-015-162).
- El relato del arresto, con sus variantes de cifras.

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

- **MENOR — U-020-164.** Se pierde el remate enfático del autor: "You're probably completely wasting every second you spend learning... that is not an exaggeration". El capítulo conserva las cifras del 95 % y del menos del 1 % y "Schools train you to learn extremely slow". Debería ir en §2.2, "What school does to learning and thinking".

No hay otros hallazgos. Se conservan las cifras y los detalles relevantes:

- El 70/30, los tercios, el 25 % y el 90/9/1.
- Los $80–150K frente a 100x.
- Los $50–55k, $55k y $60k, y los $20,000, $2,000 y $8,000.
- El horario de la agencia, el GT63 S y Ship 30 con su meta de $10k.
- El programa de diversión con sus cuatro variantes de costo.

### 4. Términos acuñados no definidos u homogeneizados

- **MENOR — "unconscious competence".** En §2.6 ("Mimetic grind culture") se glosa como "mastery so internalized that its possessor cannot see or explain it". Ese es el sentido estándar del modelo de las cuatro etapas de competencia. El léxico registra el sentido propio del autor en este pasaje (2025): lo que muestra un *highlight reel* sin el proceso que hay detrás. Registra además otras tres acepciones. El capítulo aplica la acepción de diccionario a un término con sentido propio.

El resto de los términos acuñados y de las palabras comunes con sentido propio del Anexo B están definidos con el sentido del autor, entre ellos: *force*, *vessel*, *relationship with money*, *climb the ladder*, *plateau*, *the eternal known*, *new 9-to-5*, *psychological markers*, *property of the system*, *wage slave* (con sus dos versiones), *stepping stone*, *curse of knowledge* (con nota sobre el sentido usual), *autopilot* (con su segunda acepción de 2025), *the masses*, *silent observer*, *making sense* y *robotic living vs intentional living*.

### 5. Cambios de posición (Anexo A) no presentados o resueltos indebidamente

El capítulo presenta en prosa las 20 entradas del Anexo A. A diferencia del capítulo 01, no cita los ID EV. Las contradicciones no resueltas (EV-003, EV-009, EV-010, EV-011 y EV-228) se presentan como tales, con lecturas conciliadoras marcadas como interpretación.

- **MENOR — error de datación en la evolución de un eslogan.** En §2.3 ("The path of uncertainty", último párrafo) se afirma: "In 2023 the author said... 'entrepreneurship is the only long-term option for logical thinkers'... By 2025 the formula is inverted: 'the only logical option for long-term thinkers.'" Pero la forma invertida ya aparece en diciembre de 2023: U-012-006, *The Future Of Work Is Play*, 2023-12-31. El propio capítulo la cita antes, en §2.3, "The psychology of employment" ("Hence, in this video, 'entrepreneurship is the only logical option for long-term thinkers'"). La forma original es de septiembre de 2023 (U-021-031). La inversión ocurre dentro de 2023, no hacia 2025. Por eso es dudosa la lectura que se apoya en esa fecha: "shifts the emphasis from logic to time horizon".
- **MENOR — EV-052 (iterar y persistir frente a abandonar metas).** §2.1 ("The asymmetry of patience") presenta la crítica a quien "quit[s]" tras una semana sin resultados (U-025-052), y la posición queda como absoluta. No avisa que en 2025 el autor dice "you should quit more goals than you set" (U-025-128). El capítulo 7 desarrolla ese cambio, pero aquí no hay remisión.

### 6. Fuentes de terceros con atribución perdida, confundida o alterada

- **MENOR — "hierarchy of goals".** En §2.1 ("The default path as a game tutorial") se presenta como "the author's term". El léxico lo registra como uso propio asociado a Csikszentmihalyi en el material. Falta esa asociación.
- **MENOR — "specific knowledge" (Naval Ravikant).** En §2.1 ("The asymmetry of patience") aparece en negrita sin definición ni atribución. La arquitectura lo trata como término de Naval adaptado y lo desarrolla en el §20.2.

No hay otros hallazgos. Están bien atribuidos:

- Sahil Bloom / David Foster Wallace.
- Seligman ("Sellingman"), con la reserva de transcripción.
- Devon Eriksen, Cicerón y Harari como contraejemplo.
- Ken Wilber y Riane Eisler (jerarquías), Lenski y Wilber (bases tecnoeconómicas).
- Kotler (*intrinsic drivers*), con el paso de citado a no atribuido.
- Hoffman, Dispenza (con su "potentially pseudoscience"), Tolle, de Mello y JK Molina.
- Krishnamurti, Adam Smith y *The Sovereign Individual*.
- Hawkins (escala de consciencia) y Schmachtenberger.
- Dickie Bush ("golden handcuffs", "self-awareness all the way down").
- Lucas 23:34, Jordan Peterson ("what you aim at") y la idea mimética marcada como no atribuida.

### 7. Argumentos por capas reducidos a su conclusión

Sin hallazgos. Se conservan completas, entre otras:

- La cadena del cliente que paga (U-006-003).
- La cadena de Eriksen sobre el éxito como evitar el fracaso (U-006-014).
- El argumento de la esclavitud por dependencia para sobrevivir (U-016-185).
- La psicología del techo de la escalera (U-010-239).
- La caza como búsqueda de dopamina significativa (U-003-107 y U-006-156).
- La cadena condicional de la nueva sociedad (U-016-149).

### 8. Conceptos usados antes de introducirlos

- **MENOR — "specific knowledge".** Ver el punto 6: se usa en §2.1 con aspecto de término técnico; la arquitectura lo define en el §20.2.

Los demás usos anticipados llevan una remisión explícita: *law of conceptual survival* y *mental body* (cap. 3), *anti-vision* (cap. 7), *flow* (cap. 10), *holon* y *transcend and include* (cap. 38), *good dopamine* (cap. 11), *tutorial hell* (cap. 14), *value creator* (cap. 35) y *psychic entropy* (cap. 5).

---

## Observaciones fuera de los puntos 2–8 (no cuentan en el conteo)

- **Duplicaciones entre capítulos.**
  - EV-001 (de "romper" la Matrix a "entenderla") se expone dos veces casi con las mismas palabras: en §1.1 ("How the author's position on 'breaking free' changed") y en §2.9 ("Perception as a user interface").
  - La tensión EV-009 (apertura empática frente a descarte de "the masses") se expone tres veces: §1.6, §1.7 y §2.7.
  - EV-010 y EV-011 aparecen en los dos capítulos.
  - No hay pérdida de material, pero hay redundancia.
- **Convención de fuentes.** El capítulo 01 cita sistemáticamente `_libro/03b_evolucion.md (EV-xxx)` al presentar los cambios de posición. El capítulo 02 no cita ningún ID EV, aunque presenta los cambios.
