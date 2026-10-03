# Auditoría de cobertura — Lote 20 (capítulos 39 y 40)

Auditor independiente. Fase 5. Alcance: puntos 2 a 8 del prompt del auditor para `05_capitulos_en/cap-39.md` y `05_capitulos_en/cap-40.md`, contrastados con `04b_material/cap-39.md` y `04b_material/cap-40.md`. El punto 1 (IDs no cubiertos) lo verificó un script y queda fuera de este reporte.

## Resumen

| Capítulo | PÉRDIDAS | MENORES |
|---|---|---|
| 39 — Felicidad, lucha y los capítulos de la vida | 0 | 13 |
| 40 — La buena vida: desarrollo holístico, relaciones y espiritualidad | 1 | 11 |

**Método y muestra.**

- Leí completos los dos capítulos (783 y 716 líneas).
- Del material leí el 100 % de las unidades de las siete secciones del capítulo 39 y de las seis del capítulo 40. Comparé el `desarrollo`, los `ejemplos`, la `cita` y la `tension` de cada unidad con el texto del capítulo.
- Revisé todas las entradas del Anexo A: 30 en el capítulo 39 y 15 en el 40.
- En el Anexo B revisé todas las entradas del 39 (unas 150) y del 40 (unas 90). Para cada término comprobé si el capítulo lo define y en qué sentido.
- En el Anexo C revisé todas las entradas: 19 en el 39 y 32 en el 40. Comprobé la atribución y los contextos complementarios.
- Cuando el capítulo declaraba que un contenido "no se conserva" o que "se desarrolla en otro lugar", busqué las unidades en `02_unidades/`. Luego localicé su capítulo de cobertura con los bloques `<!-- COBERTURA: -->`.
- Para la progresión consulté `04_arquitectura.md` y busqué con grep la primera aparición de los conceptos en los capítulos anteriores.

**Juicio global.** Los dos capítulos tienen una fidelidad muy alta.

- Conservan casi todos los mecanismos, las cadenas argumentales (numeradas cuando el material las numera), los ejemplos, las cifras y las historias. Entre ellas: la tormenta de Catalina, el Porsche GT3, Warren Buffett, la Life Dinner y el 3 by 20.
- Separan con cuidado lo que es del autor de lo que es de los invitados (Dickie Bush, Justin Welsh, Sahil Bloom).
- Presentan las tensiones del Anexo A sin resolverlas indebidamente, salvo un caso.

Los hallazgos se concentran en un patrón repetido: el capítulo declara que un contenido "no se conserva en el material" o que "se desarrolla en otro lugar". En realidad ese contenido existe en el corpus y está cubierto en otro capítulo, pero no se remite a él. En un caso (capítulo 40, la versión de 2025 sobre los 20 años) esto deja incompleto un framework y una comparación evolutiva. Lo marco como PÉRDIDA.

---

## Capítulo 39 — Felicidad, lucha y los capítulos de la vida

### 2. Unidades declaradas como cubiertas pero solo mencionadas

No encontré ninguna PÉRDIDA. Todas las unidades de tipo framework, proceso, método, historia, caso, metáfora, dato y argumento están explicadas con su mecanismo y sus ejemplos. Algunos ejemplos:

- La cadena de U-027-035 en cinco pasos, que el capítulo reconstruye como prosa sin perder ningún eslabón.
- Los cuatro pasos de U-026-246, U-026-247, U-026-251 y U-026-248.
- La historia completa de U-024-001: Moab, Halo 3, el ferry, los remos naranjas y los pájaros que se comen la comida.
- Los tres generadores de U-012-182 a U-012-185, en tabla y con WALL-E.
- Las tres prácticas de satisfacción (U-024-074, U-024-075 y U-024-077).
- Las seis versiones del ciclo de fases, en tabla y desarrolladas por separado.
- La cadena de premature transcendence (U-024-173 y U-024-174), numerada.

Hallazgos MENORES:

- **MENOR — Pilar 3 de la confianza (Practice) sin desarrollar y con texto de producción filtrado (U-027-098).**
  - **Qué pasa en el capítulo.** El 39.5 dice: "The material available for this chapter does not include Koe's detailed development of the third pillar, so it is not reconstructed further here."
  - **Dónde está el contenido.** Existe en U-027-103 ("Pillar 3 — Practice": skill trees en el juego de la vida, no puedes acceder a nuevas habilidades sin practicar las disponibles, el "beginner's hell hump"). Está cubierto en el capítulo 20 (línea 362) como principio de skill tree, sin decir que es el tercer pilar de la confianza.
  - **Otro ejemplo disperso.** El ejemplo personal del pilar 2 (U-027-102: los vecinos que lo encontraban intimidante porque camina "beelining") está en el capítulo 26.
  - **Efecto.** El lector del 39.5 ve un framework de cuatro pilares con uno vacío y una nota sobre "el material".
  - **Dónde debería ir.** En el 39.5 basta un resumen de dos frases y una remisión al capítulo 20 y al 26. Hay que eliminar la frase sobre "the material".
- **MENOR — Ejemplo de la cinta de correr declarado irrecuperable (U-025-006).**
  - **Qué pasa en el capítulo.** El 39.3 dice: "(The unit records that he illustrates the point with a treadmill example; the details are not recoverable from the material.)"
  - **Dónde está el contenido.** El capítulo 7 (línea 75) cuenta el ejemplo completo: en la cinta piensa en qué sería de su vida sin el gimnasio y "somehow I just get very very pissed".
  - **Dónde debería ir.** En el 39.3 se puede remitir al capítulo 7 y eliminar la nota.

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

- **MENOR — Los tres episodios de "mental turmoil" de "Happiness Is A Skill" (U-026-235 y U-026-237).**
  - **Qué pasa en el capítulo.** El 39.6 dice que el video "begins from three hard periods in Koe's life (the details of which belong to the video's opening and are not reproduced here)".
  - **Dónde está el contenido.** Los tres episodios (el arresto por marihuana en el campus, el e-commerce fallido financiado con deuda en el quinto año de universidad y la ruptura en Costa Rica) están en el capítulo 2 (línea 619). La lección que deja ("some lessons can't be taught", U-026-236) está en el capítulo 15.
  - **Efecto.**
    - U-026-237 empieza con "All three experiences shared…", y sin los episodios la definición de mental turmoil pierde su referente.
    - El 39.3 usa la ruptura en Costa Rica como "unhappy reference point" sin decir que es el tercero de esos episodios.
  - **Dónde debería ir.** En el 39.6, una frase con los tres episodios y una remisión al capítulo 2.
- **MENOR — Los cuatro "focus habits" (U-019-163).**
  - **Qué pasa en el capítulo.** El 39.1 dice que "the habits themselves are developed elsewhere in the book", sin indicar dónde.
  - **Dónde está el contenido.** Están cubiertos en el capítulo 11 (U-019-161 y U-019-164) y, en parte, en el 40.2 y el 40.4 ("one workout", "one meditation").
  - **Dónde debería ir.** Basta con poner la remisión explícita en el 39.1.

### 4. Términos acuñados no definidos u homogeneizados

- **MENOR — "Limbo" con un solo sentido.**
  - **Qué pasa en el capítulo.** El 39.6 presenta el limbo (2025-05, U-023-254 y U-023-255) solo como la fase en que la gente queda atrapada.
  - **El otro sentido.** El léxico registra una segunda acepción: "limbo is the laboratory" (2025-08, U-018-109), el estado perdido como espacio de cambio en el que se inclina uno hacia el dolor. Está cubierta en el capítulo 4 (línea 160).
  - **Efecto.** El 39.7, sede de la fase perdida, no la menciona ni remite a ella.
- **Sin otros hallazgos.**
  - El capítulo define con su sentido propio todas las palabras comunes que el Anexo B marca: happiness, enjoyment, suffering/pain, balance, freedom/autonomy, authenticity, expectation, what should be, tension, recognition y personal sovereignty. En dos casos (suffering y balance) marca el cambio de sentido.
  - También señala las homonimias de "marinating" (tres usos), "middle" y "resistance".

### 5. Cambios de posición no presentados o "resueltos" indebidamente

El capítulo presenta bien EV-057, EV-063, EV-065, EV-066, EV-082, EV-085, EV-090, EV-097, EV-113, EV-119, EV-265, EV-267, EV-269, EV-277, EV-278, EV-279, EV-284 y EV-286. En EV-267 y EV-279 deja explícito que la reconciliación es una lectura del libro, no del autor. Hallazgos MENORES:

- **MENOR — EV-271 (disfrute frente a placer).**
  - **Qué pasa en el capítulo.** El 39.1 fija "enjoyment" en su sentido de 2022: la palabra para el amor de los místicos, que nace de la conexión.
  - **Qué falta.** El desplazamiento del criterio: primero la profundidad perceptiva (U-024-009), luego "investing vs spending attention" (U-024-079, 2023) y por último "enjoyment is found in progress" (U-018-134, 2023-11; U-023-175, 2024).
  - **Efecto.** El lector queda con un solo sentido de un término que cambia.
  - **Dónde debería ir.** En el 39.1.
- **MENOR — EV-266 (definiciones de la felicidad).**
  - **Qué falta.** La definición hipotética de 2023-08: "if happiness is the feeling we get when our attention is distracted from the vast unhappiness in the world" (U-016-203, cubierta en el capítulo 11).
  - **Cita sin fuente.** La definición como calma ("happiness is being fine… calm") se cita sin fuente ni fecha. Es U-016-241, de 2025-08, cubierta en el capítulo 11.
  - **Dónde debería ir.** En el 39.1.
- **MENOR — EV-270 (libertad, soberanía y autonomía).**
  - **Qué pasa en el capítulo.** La tabla del 39.5 termina en 2025-09 y declara la evolución "a refinement, not a reversal".
  - **Qué falta.** Las formulaciones que, según EV-270, incorporan la agencia a la definición de libertad: "the most dangerous threat to society is someone who isn't reliant on it" (U-023-088), "a free man is defined as someone who acts on their interests…" (U-012-051), el "free individual" que "doesn't need permission" (U-025-203) y la tríada self-education, self-interest y self-sufficiency (U-010-270 a U-010-276).
  - **Dónde debería ir.** Una fila o una remisión al capítulo 35.
- **MENOR — EV-276 (sentirse perdido: ¿normal o peligroso?).**
  - **Qué pasa en el capítulo.** El 39.7 recorre 2023-01, 2023-06 y 2025-05.
  - **Qué falta.** El punto final de la evolución: "being lost is a decision point… the void is where success is born" (U-022-125, 2026-08, cubierta en el capítulo 5), con la metáfora del cuarto que se vuelve pocilga sin que lo notes.
  - **Efecto.** Es justo la formulación que reconcilia "normal" y "peligroso".
  - **Dónde debería ir.** Al cierre del apartado "Why the lost phase is dangerous".
- **MENOR — EV-019 (gradual frente a extremo).**
  - **Qué pasa en el capítulo.** El 39.6 presenta "flip the switch… become a completely different person" y "go a little insane" (U-017-206 y U-025-095) como la posición de Koe.
  - **Qué no se marca.** No señala que conviven con el registro gradual, que el mismo capítulo expone: "higher lows", la intensity trap, "take profits". EV-019 lo clasifica como contradicción no resuelta.
  - **Dónde está tratado.** El capítulo 4 lo trata (línea 108).
  - **Dónde debería ir.** En el 39.6 falta una frase de remisión.
- **MENOR — EV-067 (consistencia).**
  - **Qué pasa en el capítulo.** El 39.6 introduce "I personally don't think that consistency is the route…" como "a reversal of a common belief".
  - **Qué no se marca.** Es también un giro respecto de posiciones del propio autor: "a system is a process of doing the same thing every day" (U-026-083, 2022) y "consistency is key" (U-020-137, 2024-08).
  - **Dónde debería ir.** En el 39.6.

### 6. Fuentes de terceros con atribución perdida, confundida o alterada

Las atribuciones del Anexo C están bien conservadas: Nietzsche, Alan Watts, Leo Gura/Actualized.org, Greg McKeown, Csikszentmihalyi, *The Molecule of More*, Dickie Bush, Justin Welsh, Deida, "even moderation", "flow triggers", "finger at the moon" y la tríada clásica. Los contextos complementarios son correctos: *El Anticristo* §2, Brickman y Campbell 1971, Fitzgerald, Setiya, Kotler, *Fullmetal Alchemist* y la segunda flecha. Un hallazgo MENOR:

- **MENOR — "Hate is the obstruction of love" (U-027-080).**
  - **Qué pasa en el capítulo.** Lo presenta como idea propia de Koe, sin notar el eco de la cita de Anthony de Mello que el autor usa en 2022: "remove the obstruction from your heart and you have love" (U-026-056).
  - **Por qué importa.** El léxico registra los dos términos como vecinos, y el capítulo 2 (línea 661) atribuye la fórmula a de Mello.
  - **Dónde debería ir.** Una nota de contexto complementario en el 39.3.

### 7. Argumentos por capas reducidos a su conclusión

Sin hallazgos. Las cadenas largas se conservan paso a paso:

- expectativa, percepción, elecciones y "bricks" (U-027-041);
- la proyección, que genera tensión, que lleva a sentirse perdido, que solo resuelve el "aligned movement" (U-027-035);
- los cinco pasos de "winning the game is how you discover it's the wrong game";
- el argumento del nivel 50 en "collapse into one";
- la secuencia de salida de la fase perdida (U-026-108).

### 8. Violaciones de progresión

- **MENOR — "Psychic muscle".**
  - **Qué pasa en el capítulo.** El término y "expand and contract the mind" se usan en el 39.2 (pain vs suffering), con una remisión explícita: "(the practice is described in Section 39.4)".
  - **Por qué es menor.** El término es exclusivo de este capítulo y la remisión es honesta. Aun así, el 39.2 apoya la distinción pain/suffering en una práctica que el lector todavía no conoce.
- **Sin otros hallazgos.** Los conceptos de capítulos anteriores aparecen después de su sede: creation pyramid en el 7, Prigogine en el 5, meaning economy en el 36, flow triggers en el 10, Cortex y monk mode.

---

## Capítulo 40 — La buena vida: desarrollo holístico, relaciones y espiritualidad

### 2. Unidades declaradas como cubiertas pero solo mencionadas

- **PÉRDIDA — El framework de 2025 sobre los 20 años queda reducido a una de sus seis piezas (U-025-172, U-025-175).**
  - **Qué tenía la unidad.** U-025-172 presenta el video "I'm 28. Here's How To Get Ahead Of Most 20 Year Olds" como "three traps to avoid and three things to do".
  - **Qué dejó el capítulo.** El 40.1 ("The 2025 reframing") dice: "He offers three traps to avoid and three things to do (of which the corpus excerpt preserves the trap of treating youth as currency, discussed above)." Esa afirmación es falsa respecto del corpus, porque las otras cinco piezas existen y están cubiertas en otros capítulos:

    | Pieza | Unidades | Capítulo de cobertura |
    |---|---|---|
    | Trap 1: no escuchar a quien no tiene la vida que quieres (el 99 %, que empuja al realismo, el presupuesto y el empleo hasta los 50); "deliberate ignorance" | U-025-173, U-025-174 | 1 |
    | Trap 3: el empleo ("if I got a job like most people, I would end up like most people"); el gimnasio que saltó como diseñador web | U-025-178, U-025-179 | 2 |
    | Thing to do #1: empezar un negocio ya | U-025-180 | 10 |
    | Thing to do #2: ganar tanto dinero como puedas | U-025-189 | 34 |
    | Thing to do #3: self-actualize ("if your life's overarching aim isn't self-actualization, it's self-sabotage") | U-025-195 | 5 |

  - **Efecto.**
    - El 40.1 es la sede de la evolución EV-280 y no reconstruye la estructura del video ni remite a esas piezas.
    - Se pierde el contraste sustantivo entre las dos versiones. En 2023 las trampas son conditioning, dopamine y comforts, y los pasos son body, mind y business. En 2025 las trampas pasan a ser escuchar al 99 %, tratar la juventud como moneda y el empleo, y los pasos pasan a ser negocio, dinero y autorrealización. En la lista de 2025 desaparece "build your body first".
  - **Dónde debería ir.** En el 40.1, "The 2025 reframing": una tabla 2023 frente a 2025 con las tres trampas y los tres pasos de cada versión, y remisiones a los capítulos 1, 2, 5, 10 y 34. Hay que eliminar la frase sobre "the corpus excerpt". Ver también el punto 5.

Fuera de este caso no encontré unidades reducidas a una mención. Están desarrolladas con mecanismo, ejemplo y cifras:

- los siete motivos de "life hits you like a truck";
- los ocho "whys" de la caminata, el método de gamificación en tres pasos con sus reglas y el 3 by 20;
- el volumen de entrenamiento (de 8 a 12 series y al fallo), el desayuno de frontloading y la vertical diet;
- el caso de Justin Welsh (911, 10 millas, 40 libras);
- todo el material de Sahil Bloom (kairos, Buffett, la caja de Netflix de 90 minutos, el Harvard Study, el eject button, tourists frente a locals, la Life Dinner);
- la cadena teleológica de U-021-059;
- el argumento del lenguaje de U-023-010;
- "think of a bird";
- el bodhisattva;
- las jerarquías de dominación frente a las de actualización.

### 3. Ejemplos, historias, metáforas, procesos y números perdidos

- **MENOR — Tabla de pasos diarios (EV-073).**
  - **Qué falta.** La cifra de 2023-11, de 15 a 20 mil pasos (U-018-143, otro capítulo).
  - **Por qué es menor.** No altera el patrón que el capítulo describe (la práctica personal se mantiene alta y la prescripción baja).

### 4. Términos acuñados no definidos u homogeneizados

- **MENOR — "Tutorial phase" sin marcar la homonimia.**
  - **Qué pasa en el capítulo.** El 40.1 usa "your 20s are the tutorial phase" con valor positivo (preparación para el juego principal) y dice que la imagen "belongs to the larger metaphor of life as a video game (Chapter 10)".
  - **Los otros sentidos.** En los capítulos 2 (línea 19) y 10 (líneas 56 y 762), "tutorial phase" es la etapa de metas asignadas, de signo negativo. En el capítulo 8 es la fase de un camino que no hay que abandonar ("1% of 50 years is 6 months"). En los capítulos 11 y 14 es "skip the tutorial phase". El léxico registra cinco acepciones.
  - **Efecto.** La remisión al capítulo 10 sugiere continuidad donde hay inversión de valor.
  - **Dónde debería ir.** Una nota terminológica en el 40.1.
- **MENOR — "Degeneracy" con un solo sentido (U-026-228).**
  - **Qué pasa en el capítulo.** El 40.2 sitúa la "degeneracy" como "strategy number five" de un video sobre "tactical stress", pero solo la explica "in the narrow sense of allowing occasional excess without neurosis".
  - **Qué falta.** El léxico registra la primera acepción (2023): soltarse en exceso para sentir el costo y rebotar con energía, que es la lógica de la estrategia de estrés táctico. Sin ella no se entiende por qué la "degeneracy" figura en una lista de estrategias para salir de un bache.
  - **Dónde debería ir.** En el 40.2.
- **MENOR — "Raise the collective consciousness" con un solo sentido.**
  - **Qué pasa en el capítulo.** El 40.6 desarrolla el sentido 2022/2024: hacer conocido lo desconocido y enseñar el mapa.
  - **Qué falta.** La acepción de 2023 que registra el léxico: que la gente consciente emprenda y desplace a los negocios poco éticos. Es la cara competitiva del mismo término y conecta con "most people spread information that holistically leads to evil and destruction" (U-017-204), que sí aparece.
  - **Dónde debería ir.** En el 40.6.

### 5. Cambios de posición no presentados o "resueltos" indebidamente

El capítulo presenta bien EV-083 (con la tensión declarada abierta), EV-233, EV-266 (por remisión al 39), EV-268 (subsección "The meaning of life, revised", que incluye killers, pillars y generators), EV-274, EV-281 y EV-298. Hallazgos:

- **(Ver PÉRDIDA del punto 2) — EV-280 resuelto con evidencia incompleta.**
  - **Qué pasa en el capítulo.** Concluye: "The shift from 2023 to 2025 is a change of emphasis rather than of position." Y añade: "Both versions can hold at once."
  - **Por qué es indebido.** La conclusión se apoya solo en el marco (pérdida frente a preparación). No compara las listas de trampas y pasos, y en ellas el orden de prioridades cambia: el cuerpo deja de ser el primer paso y entran "make as much money as you can" y "self-actualize".
  - **Qué no se cuenta.** No es un hallazgo aparte: es la consecuencia de la PÉRDIDA del punto 2.
- **MENOR — EV-273 (postura ante la salud) incompleta en su sede.**
  - **Qué pasa en el capítulo.** El 40.2 enuncia el cambio "from relativizing details to giving concrete protocols".
  - **Qué falta.** Las dos piezas más fuertes del "después":
    - "cuidar el cuerpo debería ser tu trabajo de tiempo completo" (U-019-171, 2025-06);
    - los datos fisiológicos detallados del ejercicio: BDNF, BMR, mitocondrias (U-018-066, 2025-10).
  - **Dónde está el contenido.** Ambas están cubiertas en los capítulos 9 y 11.
  - **Dónde debería ir.** En el 40.2, una frase con remisión.
- **MENOR — EV-095 (alcohol) incompleta.**
  - **Qué pasa en el capítulo.** El 40.2 reúne bien las posiciones de 2021, 2023-03, 2023-10 y 2025-01.
  - **Qué falta.**
    - "Emborracharse no es un error si no hay responsabilidades significativas a la mañana siguiente" (U-024-244, 2025), que refuerza el polo permisivo.
    - El matiz de U-002-074: Dan dice haber "ganado" por moderación antes de concordar con Dickie en que el cero es mejor mientras se construye.
- **MENOR — EV-275 (dominios de la vida): la tabla del 40.1 omite formulaciones.**
  - **La más temprana.** "Mind, body, spirit with business as your vessel" (U-005-001, 2021-12), que ya contiene la idea del negocio como vessel que el capítulo desarrolla luego.
  - **Otras.** La de 2023-12, con las relaciones dentro de spirit (U-020-074), y "health, wealth, relationships, happiness: the only things that matter in life" (U-026-140, 2024-03).

### 6. Fuentes de terceros con atribución perdida, confundida o alterada

Las atribuciones son correctas en general: Sahil Bloom y lo que llega a través de él (griegos, Brad Feld, Pygmalion, Harvard Study, Lindy), Dickie Bush, Justin Welsh, Berkhan y DeLauer, Stan Efferding, Ray Peat, Huberman, Bryan Johnson, Sócrates, McKenna, Watts, Marco Aurelio, Carse, Eisler y Wilber, la filosofía perenne y el taoísmo. Los contextos complementarios son exactos: Jenofonte, *Memorabilia* III.12; Feld y Batchelor, *Startup Life*; el estudio de Harvard desde 1938; Huxley 1945; el podómetro japonés. Hallazgos MENORES:

- **MENOR — "Awareness" en la lista de libros (U-011-090).**
  - **Qué pasa en el capítulo.** El 40.4 deja el título como "unclear whether a separate title is meant".
  - **Pista no aprovechada.** Es muy probablemente *Awareness*, de Anthony de Mello, autor que Koe cita en 2022 ("remove the obstruction…"; capítulo 2, línea 661).
  - **Dónde debería ir.** Una nota de contexto complementario con la identificación probable, marcada como conjetura.
- **MENOR — Joe Dispenza (U-026-011).**
  - **Qué pasa en el capítulo.** El 40.4 presenta la explicación de Dispenza como "neuroscience-based account" sin recoger que el propio Koe lo califica de "potentially pseudoscience" en su lista de relecturas (Anexo C).
  - **Efecto.** El capítulo otorga a la fuente una autoridad científica que el autor mismo pone en duda.

### 7. Argumentos por capas reducidos a su conclusión

Sin hallazgos. Se conservan:

- los cinco pasos que llevan de la meta teleológica a "goals are spirituality";
- los cuatro movimientos del argumento sobre el lenguaje (U-023-010);
- la estructura del eject button (opciones abundantes, que hacen salir antes de la lucha compartida, lo que deja todo en la superficie);
- el argumento de Dickie Bush sobre el costo de llegar frente al costo de mantener;
- la cascada de estándares (U-017-110);
- los dos pasos del sentido de la vida, con su vínculo explícito con la arquitectura del libro.

### 8. Violaciones de progresión

- **MENOR — Remisión errónea.**
  - **Qué dice el capítulo.** El contexto complementario sobre *The Power of Now* en el 40.4 dice que fue un catalizador "by Koe's account elsewhere… (Chapter 1)".
  - **Dónde está en realidad.** El relato del "catalyst to it all" está en el capítulo 2 (línea 611). El capítulo 1 solo anticipa la anécdota y remite al 2.
- **MENOR — Definición usada antes de presentarla.**
  - **Qué pasa en el capítulo.** El 40.1 apoya el desglose del argumento "business is the vessel… bridged by spirit" en la definición de espiritualidad como "connection to something greater than yourself", que se presenta en el 40.4 ("Spirit, for Koe, is connection to something greater than yourself (section 40.4)").
  - **Por qué es menor.** La remisión es explícita y el término ya aparece en el 39.1 (la fórmula de la felicidad).
- **Sin otros hallazgos.** False transformation (capítulo 4), eternal markets (capítulos 7 y 19), default mode network (capítulos 5 y 6), meaningful dopamine (capítulo 11), teleología (capítulo 3), holon (capítulo 38) e infinite game (capítulos 1 y 2) se usan después de su introducción.
