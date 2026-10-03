# Correcciones — Lote 09 (capítulos 17 y 18)

Base: `06_auditoria/audit-09.md`. La auditoría no registró PÉRDIDAS; se atendieron los siete hallazgos MENORES (cuatro en el capítulo 17 y tres en el 18). Todos quedaron corregidos; ninguno se descartó.

## Capítulo 17 — How to Think

### Hallazgos

1. **MENOR — Liver King (U-007-163), sección 17.1, "Selective skepticism and other signs of a closed mind".** Corregido. En el párrafo de los tres grupos de consumidores de información se añadió el ejemplo: Koe menciona a Liver King como referencia del tipo "snake oil salesman", aclara que no vende cursos y que no quiere entrar en el drama, y el nombre solo sirve para señalar el tipo de figura que lleva a descartar toda la categoría. La fuente y la fecha (2022-12-04) se mantienen.
2. **MENOR — término acuñado "partial thinking" (U-024-103), sección 17.1, "The 'smart but dumb' phenomenon".** Corregido. En el párrafo que cita el video de octubre de 2025 se nombra el término en negrita y se define: resolver un problema de un dominio con el modelo de otro. Se indica que solo aparece una vez en el corpus y se distingue de "smart but dumb", su término vecino: este nombra a la persona (2026) y "partial thinking" nombra la operación (2025).
3. **MENOR — remisión equivocada de "pain and gain story" (U-018-061), sección 17.3, "Personal context".** Corregido. La remisión al capítulo 7 se sustituyó por una glosa: son dos historias, una sobre dónde termina la vida si nada cambia y otra sobre quién llega a ser uno si cambia. Se remite al capítulo 4 (4.2), donde funciona como detonante del cambio, y al capítulo 11, como primer paso del protocolo de dopamine detox. Se conserva la relación con la anti-visión y la visión del capítulo 7 como "forma narrativa", que es lo que dicen los capítulos 4 y 11.
4. **MENOR — remisión equivocada de "conscious conditioning" (U-021-085), sección 17.5, "What it takes to reach a new stage".** Corregido. Ahora remite al capítulo 1, donde se introduce el término, y cita la frase en que aparece: el personaje principal "creates themselves through years of conscious conditioning".

### Limpiezas globales

- **Frases de proceso eliminadas: 4.**
  - "The last cluster of this section" → "The last strand of this section".
  - "is not documented in the unit" → "is not documented in the video".
  - "the smallest unit of resistance" → "the smallest act of resistance".
  - "the project as practical unit" → "the project as the practical vehicle of change".
- **Marcas normalizadas: 0.** No había ninguna marca en español (`Fuente:`, `Contexto complementario:`, `Ejercicios`): las 155 marcas **Source:** y las 26 **Complementary context:** ya estaban en inglés, igual que el encabezado `### Exercises` y todos los títulos de sección.
- El bloque COBERTURA quedó intacto. No se añadieron unidades, porque todas las que se trataron ya estaban en él.

## Capítulo 18 — Creativity, Originality and Taste

### Hallazgos

1. **MENOR — segunda acepción de "articulation" (U-010-321, U-010-322), sección 18.6, "Articulation requires a body of work".** Corregido. Se añadió un párrafo que separa las dos acepciones:
   - **Primera acepción:** organizar el pensamiento y ponerlo en palabras, y partir de un problema en una conversación.
   - **Segunda acepción (enero de 2026):** "Ideas are cheap, but articulation of the ideas is expensive". La estructura de la idea pesa más que la idea misma, y la habilidad consiste en reescribir la misma idea desde muchos ángulos.

   El párrafo indica cómo se conectan las dos acepciones y remite al capítulo 22, sección 22.5 ("Ideas are cheap, articulation is expensive"), donde está la sede de la segunda. Esas unidades no se añadieron a COBERTURA, porque su sede es el capítulo 22.
2. **MENOR — EV-268, el sentido de la vida (U-012-015), sección 18.1, "You are a creator: the human as toolbuilder".** Corregido. Después de la frase "arguably the meaning of human existence is to create" (2023-12) se presentan las dos versiones con sus fechas:
   - **Versión de 2023:** formulaciones sueltas.
   - **Versión de enero y febrero de 2026:** los meaning generators (struggle como motor, curiosity como dirección y status, rebautizado como recognition, como prueba de contribución), dentro del marco del futuro del trabajo con IA.

   Se aclara que Koe no presenta la versión de 2026 como corrección de la de 2023, sino como sistematización, y no se elige ganador. Remite al capítulo 39 (sección 39.2).
3. **MENOR — identidad de "Devon" en 18.6, "When articulation fails: the podcast problem" (U-022-186).** Corregido. Se añadió una nota: el "Devon" que edita los videos aparece solo con el nombre de pila en la transcripción, nada en la fuente lo identifica con el escritor Devon Eriksen citado en las secciones 18.1 y 18.5, y no debe suponerse que sean la misma persona.

### Limpiezas globales

- **Frases de proceso eliminadas: 6.**
  - "developed in other units of the same video" → "developed at more length elsewhere in the same video".
  - "evolves in later material" → "evolves in later videos".
  - "in his 2025–2026 material" → "in his 2025–2026 videos".
  - "almost all of the material is from 2025 and 2026" → "almost everything Koe says about it dates from 2025 and 2026".
  - "the unit of value" → "the basis of value".
  - "the project is the unit through which" → "the project is the vehicle through which".
- **Marcas normalizadas: 0.** Las 103 marcas **Source:**, las 16 **Complementary context:**, el encabezado `### Exercises` y todos los títulos de sección ya estaban en inglés.
- El bloque COBERTURA quedó intacto, sin unidades nuevas.

## Verificación

Se ejecutó grep (sin distinguir mayúsculas) sobre los dos capítulos con los patrones "U-0", "EV-", " unit", "cluster", "Fuente", "Contexto", "Ejercicio" y "annex/anexo". Fuera del bloque `<!-- COBERTURA -->` no queda ninguna coincidencia. La única excepción es un falso positivo en el capítulo 17: " unit" dentro de "United States".

Las coincidencias de "material" que se mantienen tienen sentido de libro y no de proceso editorial: "raw material", "the material of creativity is experience", "generalism supplies the material", "your own material" (los textos propios del lector) y "the philosophical material".

## Extensión final

- Capítulo 17: 39 579 palabras (antes, 39 365).
- Capítulo 18: 30 251 palabras (antes, 29 904).
