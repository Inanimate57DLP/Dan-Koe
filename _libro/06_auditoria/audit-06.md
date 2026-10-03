# Auditoría de cobertura — Lote 06 (capítulos 11 y 12)

Auditor independiente. Fase 5. Alcance: puntos 2–8 del prompt del auditor para `05_capitulos_en/cap-11.md` y `05_capitulos_en/cap-12.md`, contrastados con `04b_material/cap-11.md` y `04b_material/cap-12.md`. El punto 1 (IDs no cubiertos) lo verificó un script y queda fuera de este reporte. No se corrigió nada.

## Resumen

| Capítulo | PÉRDIDAS | MENORES |
|---|---|---|
| 11 — Dopamina, consumo y entorno | 2 | 7 |
| 12 — La 4-Hour Workday | 0 | 7 |

**Método y muestra.**

- Leí completos los dos capítulos (714 y 697 líneas).
- Capítulo 11: leí el material completo. Comparé con el capítulo el campo `desarrollo`, más ejemplos, cita, origen y tensión, del 100 % de las 116 unidades. También revisé las 18 entradas del Anexo A, las 74 del Anexo B y las 19 del Anexo C.
- Capítulo 12: leí el material completo. Comparé el 100 % de las 160 unidades, las 21 entradas del Anexo A, las 21 del Anexo C y las 94 del Anexo B. De estas últimas, busqué en el texto unas 40 de forma dirigida y leí la definición completa de 20.
- Cuando el capítulo remite a material de otro capítulo, o dice que "el material" no trae algo, busqué la unidad en `02_unidades/` y su asignación en los bloques COBERTURA de `05_capitulos_en/`. Para la progresión consulté `04_arquitectura.md` y busqué en los capítulos 01–10 los términos que el 11 y el 12 usan sin definir.

**Juicio global.** Los dos capítulos son muy fieles. Conservan casi literalmente los mecanismos, las cadenas numeradas, las cifras, los ejemplos y las tensiones. Algunos ejemplos:

- el gráfico de la psicología del deseo;
- los cuatro nombres del polo positivo de la dopamina;
- los tres motivos del aburrimiento verdadero;
- el protocolo de 7 días;
- la tabla del alcohol;
- los Ten Commandments;
- las cinco versiones del orden del día;
- las cuatro formulaciones de Koe's Law;
- las tres etapas con sus presupuestos de tiempo.

Las fuentes de terceros están bien marcadas, con contextos complementarios prudentes (Lieberman, Jung, Pascal/Naval, Wilber, Kotler, Clear, Pang, Zeigarnik). Las dos PÉRDIDAS del capítulo 11 tienen la misma causa. El capítulo afirma que el material "no trae" o "no desarrolla" una parte de un framework, pero esa parte existe en el corpus y está asignada a otros capítulos. El resultado es un protocolo o un framework truncado, con una afirmación falsa y sin remisión.

---

## Capítulo 11 — Dopamina, consumo y entorno

### 2. Unidades declaradas como cubiertas pero solo mencionadas

**PÉRDIDA 1. El protocolo de detox de 30 días está truncado y el capítulo afirma algo falso sobre su orden** (U-018-062, U-018-072; Anexo A EV-090; sección 11.4, "The 30-day dopamine detox").

- **Qué dice el corpus.** El video de 2025 numera siete pasos de forma explícita:
  1. pain and gain story (U-018-060);
  2. monk mode de 30 días (U-018-062);
  3. caminar 7.000–8.000 pasos y el "3 by 20 method" (U-018-063, U-018-064);
  4. gimnasio (U-018-065, U-018-066);
  5. dieta de eliminación, la vertical diet de Stan Efferding (U-018-067);
  6. proyecto (U-018-068 a U-018-070);
  7. reflexión nocturna de 10 minutos, con el efecto Zeigarnik y el marco 3-2-1 (U-018-071).
- **Qué dejó el capítulo.** Escribe: "of which the gathered material reconstructs the first two in detail… The material does not give the exact order of the remaining steps, so the table below lists the elements by function rather than by number". El orden sí existe. El capítulo 13 incluso lo usa: llama a la reflexión "the seventh and last step of his thirty-day dopamine detox protocol (Chapter 11…)". Los pasos 3–7 están en los capítulos 04, 17, 40, 09, 14 y 13, y el capítulo 11 no remite a ninguno. El lector recibe el protocolo central de la sección sin cinco de sus siete pasos y con una afirmación incorrecta. Además, el paso 1 queda en una frase: falta su mecanismo ("all lasting behavior change is identity change", dos historias viscerales, "you will give up in two weeks like always").
- **Dónde debería ir.** En la sección 11.4, en la tabla de elementos: numerar los siete pasos en su orden real y remitir a cada capítulo sede.

**PÉRDIDA 2. Al holistic monk mode le falta su "offense", y la remisión apunta a un capítulo equivocado** (U-019-161, U-019-162, U-019-164; véanse U-019-163 en el capítulo 39, U-019-166 en el 09, U-019-168 en el 16 y U-019-169 en el 40; sección 11.4, "Monk mode: the popular version…" y "Successful people disappear").

- **Qué dice el corpus.** El framework tiene dos partes: defensa (eliminar distracciones) y ofensa ("form four focus habits"). Los cuatro hábitos son un proyecto, un libro, una meditación y un entrenamiento. U-019-163 los fundamenta en "the good, the true and the beautiful", definidos como verdad intersubjetiva, objetiva y subjetiva.
- **Qué dejó el capítulo.** Escribe: "The offense belongs to the organization of focused work and is not developed in the material of this chapter". La ofensa no está en el capítulo 12, sino repartida entre los capítulos 39, 09, 16 y 40. Además, el capítulo presenta "one project, one book, one meditation, one workout" en otro apartado, como "plan de seis meses" (U-019-164), sin decir que esos cuatro hábitos *son* la ofensa del holistic monk mode. Así se rompe la estructura defensa + ofensa. Tampoco define la tríada good/true/beautiful, que usa ("the transcript does not specify which… corresponds to which of the three values").
- **Dónde debería ir.** En la sección 11.4: unir el plan de seis meses con la ofensa, dar la definición de la tríada (o remitir al 39.x) y corregir la remisión.

**MENOR 1. El plano físico está mal caracterizado** (U-017-106; U-017-109 en el capítulo 04; sección 11.3).

- **Qué dejó el capítulo.** "The physical plane, the third, concerns the bodily environment and is not developed in the units gathered here".
- **Qué dice el corpus.** U-017-109 no trata del entorno corporal. Trata de los "settlements" de personas que se acomodan y se justifican mutuamente, y de que dónde vives es "the single most important decision". El capítulo 04 (línea 448) lo desarrolla.
- **Corrección sugerida.** Corregir la caracterización y remitir al capítulo 04.

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

**MENOR 2.** Faltan dos detalles del diálogo sobre el alcohol (sección 11.5):

- En U-002-075 desaparece el dato de los "15 months" sin alcohol de Dickie Bush. Es la evidencia de su postura.
- En U-002-074 desaparece el "first martini" de la cena que Koe cuenta como victoria.

No hay otras pérdidas de ejemplos ni de números. Algunos que el capítulo conserva:

- Corolla y Ferrari;
- la luna de miel de 2–4 semanas;
- los 50 bits por segundo;
- los 10.000–15.000 pasos;
- los 4–5 días de recuperación;
- las preguntas de las 11:00 a las 21:00;
- la cámara;
- el romero.

### 4. Términos acuñados no definidos u homogeneizados

**MENOR 3. War mode aparece solo en su segunda acepción** (Anexo B, "war mode", acepción 2025-03; U-025-100 y U-025-119 en el capítulo 04; U-025-120 en el 10; sección 11.4).

- **Qué dice el corpus.** En el video de marzo de 2025, war mode es la fase de ejecución que cierra la secuencia Vision → Clarity → Identity. Su paso 1 es un compromiso físico e irreversible, como raparse, sin plan B. El título de la propia U-025-126 es "War mode step 4".
- **Qué dejó el capítulo.** Lo presenta solo como "attack… say yes to everything", sin decir que es la etapa de un proceso y sin remitir a los capítulos 04 y 10.

Fuera de esto, el capítulo define con cuidado los 74 términos del Anexo B, incluidas las palabras comunes con sentido propio: disappear, rip the Band-Aid off, monk mode, sabbatical, flip the script, problem y vessel.

### 5. Cambios de posición (Anexo A) no presentados o resueltos indebidamente

**MENOR 4. La felicidad en EV-266 queda incompleta y con una cronología equivocada** (sección 11.2, "What happiness is, and what it is not").

- **Qué falta.** El capítulo dice que Koe "later integrates the formula into a framework of his own", pero no dice qué añade: "connection to something greater than yourself", con la creatividad como vehículo de ambos términos (U-027-224 y U-012-133, en el capítulo 39). También omite las dos definiciones de febrero de 2023: los dos tipos de felicidad sostenidos por el sense of mastery (U-026-240) y la felicidad que necesita un punto de referencia infeliz (U-026-242). La primera procede del mismo video que el capítulo cita en "A philosophical sense of mastery".
- **El error.** El capítulo cierra con "the Nietzschean formula belongs to a pole of progress and the calm one to a pole of peace, two components Koe later combines". Pero el par peace/progress ya aparece en febrero de 2023 (U-026-240), antes de la cita de Nietzsche (noviembre de 2023) y de la definición de calma (2025). "Later" invierte la cronología.

**MENOR 5. Falta el contrapunto de EV-019** (sección 11.4, "War mode" y holistic monk mode). El capítulo presenta bien la alternancia entre gradual y extremo. Omite, en cambio, la formulación de agosto de 2025 que el Anexo A registra en sentido contrario: "changing your life doesn't mean packing up, moving across the country" (U-025-216, en el capítulo 35). Con ella, la tensión frente a war mode y frente a "disappear" se vería completa.

Las demás entradas del Anexo A están presentadas sin resolución indebida: EV-021, 090, 091, 093, 094, 095, 097, 098, 099, 102, 128, 134, 258, 265, 271 y 296.

### 6. Fuentes de terceros cuya atribución se perdió, se confundió o se alteró

**MENOR 6. La atribución de "Here and Now" y del espacio peripersonal/extrapersonal** (sección 11.1, contexto complementario de "The up world and the down world").

- **Qué dejó el capítulo.** Atribuye a Lieberman y Long los "Here and Now neurotransmitters" y el espacio peripersonal/extrapersonal, y añade que "Koe's lists are his own summaries". Así sugiere que Koe no usa ese vocabulario.
- **Qué dice el corpus.** En 2024 Koe habla él mismo de "here and nows" y de "peripersonal space" (U-018-029, en el capítulo 39). El Anexo C, en la entrada de *The Molecule of More*, lo registra como adaptación del autor. La atribución al libro es correcta, pero la frase oculta que el autor adoptó esos términos.

Todo lo demás está correctamente atribuido:

- Lieberman, nombrado en 2024 y no en 2022;
- Jung y el shadow work como adaptación;
- la cita "de Naval" con la nota sobre Pascal;
- Nietzsche, con la pérdida posterior de atribución;
- el proverbio árabe;
- Taleb, capítulo 7 de *Antifragile*;
- *WALL-E*;
- Kotler y Wilber como parecidos no atribuidos;
- Vassallo;
- Welsh y Bush, separados de Koe.

### 7. Argumentos construidos por capas reducidos a su conclusión

**MENOR 7. Falta un eslabón en la cadena del video del detox** (U-018-055, en el capítulo 10; sección 11.4).

- **Qué dice el corpus.** El video de 2025 encadena: salience network (U-018-054) → la sobreestimulación destruye el flow porque sube el umbral de lo estimulante, según la relación habilidad/desafío de Csikszentmihalyi (U-018-055) → los tres motivos del aburrimiento → la soberanía y la vida "composed of flow states" (U-018-059).
- **Qué dejó el capítulo.** Omite el segundo eslabón y no remite al capítulo 10. Por eso el cierre en el flow parece un añadido y no la conclusión de la cadena.

Las PÉRDIDAS 1 y 2 también pertenecen a este punto: un protocolo de siete pasos y un framework de dos partes quedan reducidos a sus primeras piezas. Las cadenas numeradas que el capítulo sí reproduce completas son:

- el oscilador armónico (U-024-007);
- el doble golpe de dopamina (U-025-035);
- la adicción a sentirse mal (U-025-011);
- los tres casos de meta frente al scroll (U-020-059).

### 8. Conceptos usados antes de introducirlos (progresión)

Sin hallazgos.

- Los términos que podrían parecer adelantados ya aparecen en capítulos previos:
  - default mode network, en el capítulo 06;
  - mental bodybuilding, en los capítulos 03, 04, 06 y 07;
  - Musashi, en el capítulo 08;
  - Cortex, en los capítulos 04, 05, 07 y 09.
- Las anticipaciones a capítulos posteriores llevan remisión y una glosa mínima: 4-Hour Workday (capítulo 12), path of mastery (15), lectura (16) y agency (35).

**Observación fuera de conteo.** El capítulo filtra lenguaje del proceso editorial en varios lugares: "the units gathered here", "the gathered material reconstructs…", "the unit gathering this passage reads it as…", "the corpus's evolution notes". En los casos de las PÉRDIDAS 1 y 2 y de la MENOR 1, esas frases son además las que introducen la afirmación incorrecta.

---

## Capítulo 12 — La 4-Hour Workday

### 2. Unidades declaradas como cubiertas pero solo mencionadas

Sin hallazgos. Todas las unidades de tipo framework, proceso, método, historia, caso, dato y argumento están desarrolladas con su mecanismo, sus condiciones y sus ejemplos. Por ejemplo:

- la historia del título de Ferriss, con su inconsistencia "in college" frente a "as a kid";
- "problem" como desviación de un estándar;
- los once mandamientos con remisiones;
- las cuatro razones de "por qué cuatro";
- el caso de JK Molina;
- la tabla de horas reales;
- la aritmética del millón;
- la priority ladder bloque por bloque, con el rogue thought;
- la escala de cinco tipos de deadline;
- el desayuno como deadline con dientes;
- el energy calendar de Sahil en tres pasos;
- las cinco versiones del orden del día;
- Koe's Law en cuatro formulaciones y tres etapas, con presupuestos de tiempo y cifras;
- los fundamentals en cuatro etapas.

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

**MENOR 1. Falta el pez dorado** (U-026-206, sección 12.4, "The pseudo-deadline and Parkinson's law"). El capítulo recoge que Koe llama a su tactical stress "quite similar" a la ley de Parkinson, pero omite que en la misma frase lo compara también con "the goldfish", la metáfora del pez que crece según el tamaño de su pecera. El capítulo 10 puede tenerla, pero aquí la comparación queda amputada.

### 4. Términos acuñados no definidos u homogeneizados

**MENOR 2. Falta el término "hard cutoff"** (U-019-076; Anexo B, "hard reset", variante "hard cutoff / hard transition"; sección 12.4). El capítulo presenta el gimnasio solo como "the Parkinson's law of my work". Omite el término propio que la unidad registra ("hard cut off") y su vecino "hard transition" (U-003-261, en el capítulo 08). El Anexo B advierte que "hard reset" tiene dos sentidos distintos con el mismo nombre. El capítulo no ofrece al lector el puente para no confundirlos cuando en el capítulo 13 aparezca el hard reset de 30 minutos.

El resto del Anexo B está definido o glosado. Por ejemplo:

- baseline;
- frontload;
- taper up, con la nota sobre el uso inverso;
- gravity;
- Legos;
- second 9-to-5;
- distraction potential;
- nature's filter;
- intention of evolution;
- procrastinator's edge;
- energy profile;
- life treadmill;
- self-made lifestyle;
- status game;
- creative firepower, vessel y currency.

### 5. Cambios de posición (Anexo A) no presentados o resueltos indebidamente

**MENOR 3. EV-067 aparece como una progresión lineal** (sección 12.7, "Repetition and iteration"). El capítulo narra la secuencia "repetitive" → "persistent" (2023-03) → "consistency is overrated" (2023-07) → "consistency maintains, doesn't create" (2024-10). Omite el paso atrás de agosto de 2024, cuando Koe vuelve a decir "consistency is key" al elegir una rutina que encaje en la vida (U-020-137, en el capítulo 13). Sin ese dato, la evolución parece una línea recta, cuando el Anexo A la registra como un ir y venir.

**MENOR 4. A la tabla de EV-068 le faltan dos estados** (sección 12.4, tabla de duración de bloques):

- 2023-07: el "mental lifting", cuatro series de 20 minutos que progresan a cuatro de 45 y exceden la "one hour of focused work" del mismo video (U-017-123, en el capítulo 15);
- 2024-04: tres bloques de 60–90 minutos (U-018-187, en el capítulo 05).

El primero es justamente el caso en que la regla de la hora se contradice dentro de un video.

**MENOR 5. La tabla de EV-286 termina en 2024-12** (sección 12.1, "How many hours the author actually works"). Omite el dato de mayo de 2025: le gustan los días de 16 horas, aunque no para toda la vida, y tras dos meses de sobretrabajo por la carrera de la IA su escritura sufrió (U-019-131 en el capítulo 39 y U-019-142 en el 37). Es el dato más reciente, y el que mejor muestra el costo del exceso según el propio autor. No hay remisión.

**MENOR 6. EV-082, de "one thing" a "one mission", no aparece** (sección 12.3, "'Focus on one thing' and its hidden premise"). El capítulo trata el matiz de 2023 y el single bottleneck de 2026. Omite el desplazamiento de diciembre de 2024: "you don't focus on one thing, you focus on one mission which requires you to learn many things" (U-027-191, en el capítulo 19). Tampoco da la razón del cambio: enfocarse en una sola cosa vuelve a la persona dependiente y reemplazable. Basta una remisión.

Las demás entradas del Anexo A están presentadas sin resolución indebida: EV-063, 065, 071, 072, 074, 075, 078, 079, 080, 081, 085, 086, 109, 196, 202 y 206. Destaca el tratamiento de los noctámbulos como contradicción abierta y de la atribución perdida de la frase de Pang. EV-108 no aplica a este capítulo.

### 6. Fuentes de terceros cuya atribución se perdió, se confundió o se alteró

Sin hallazgos. El capítulo atribuye correctamente las fuentes de terceros:

- Ferriss, solo el título;
- Newport, el término y la cita, no la práctica;
- Pang, con la pérdida de atribución documentada;
- Naval: la regla de creatividad y "work like a lion";
- Parkinson, con la paráfrasis floja señalada;
- Zeigarnik, con la advertencia sobre la evidencia;
- Clear, distinguiendo el eslogan del libro;
- Pomodoro;
- Daniel Fazio, con la transcripción dudosa;
- JK Molina;
- Sahil Bloom: energy calendar, eject button y batching;
- Vitali, separando su definición de trabajo de la de Koe y marcando que relata la lección del *2 Hour Writer*;
- Dickie Bush, con "not never, but not now" y la "inconvenient truth";
- Justin Welsh, con "eliminate, automate, delegate".

### 7. Argumentos construidos por capas reducidos a su conclusión

**MENOR 7. Solo aparece el primero de los tres pilares** (U-017-040; U-017-043 en el capítulo 14 y U-017-046 en el 28; sección 12.6, "The first pillar: eliminate what you don't like"). El video de junio de 2023 construye las cuatro horas sobre tres pilares:

1. eliminar lo que no te gusta;
2. concentrarse en las actividades de mayor leverage, con una relación tiempo/dinero que debe bajar al crecer;
3. el crecimiento compuesto de la audiencia lectora, porque el negocio necesita tráfico y oferta.

El capítulo titula "The first pillar" sin decir que hay otros dos y sin remitir a ellos. La estructura del argumento se pierde, aunque el contenido existe en otros capítulos.

Las cadenas centrales están completas:

- identidad → problema → solución;
- el cutoff como restricción que fuerza la evolución;
- estrés → mente cerrada → imposibilidad de rediseñar el trabajo;
- Parkinson → Koe's Law, en sus tres etapas, con el cierre "fixed hours, rising income".

### 8. Conceptos usados antes de introducirlos (progresión)

Sin hallazgos. Los términos heredados tienen sede previa y el capítulo remite a ella:

- Focus Matrix, open loops, default mode network y la cita de Parkinson, en el capítulo 06;
- Focus Formula, daily levers y Newport, en el 08;
- tactical stress, en el 10;
- meaningful dopamine, en el 11;
- entropía y raise the baseline, en el 05.

Las anticipaciones llevan glosa y remisión: mental metabolism (capítulo 13), tutorial hell (14), seasons (39) y la historia del client work (29–30).
