# Correcciones — Lote 07 (capítulos 13 y 14)

Fase 5. Corrección de `05_capitulos_en/cap-13.md` y `05_capitulos_en/cap-14.md` según `06_auditoria/audit-07.md`. La auditoría no registró PÉRDIDAS. Registró 4 hallazgos MENORES en el capítulo 13 y 3 en el 14. Se corrigieron todos y no se descartó ninguno.

## Capítulo 13 — Descanso, rutina y mantenimiento del orden

### Hallazgos

1. **MENOR — "polarity" con la acepción de Dickie Bush (§13.1, "The polarity of work and rest").** **Corregido.**
   - Se reescribió el párrafo de 2023. Ahora explica que Koe habla mientras coincide con Bush en no dejar nunca de trabajar, y que el "again" remite al uso que Bush acababa de hacer del término: "balance through extremes", alternar intensidad total y apagado total en cada escala (12 semanas / 1 semana; 50 / 10 minutos), con su cita.
   - Se separan explícitamente las dos acepciones: la de Bush es un reparto de la intensidad en el tiempo; la de Koe es una definición recíproca de trabajo y descanso.
   - Se añadió una remisión al capítulo 39 (§39.4), donde se desarrolla la acepción de Bush y la respuesta de Koe.
   - Se añadió U-002-035 al bloque COBERTURA.
2. **MENOR — EV-076, el building como episodio o como hábito diario (§13.2).** **Corregido.**
   - Se añadió un párrafo tras "Four kinds of change appear" que presenta las tres posiciones con fecha:
     - 2024-02: construir no es permanente; quizá seis semanas, una o dos veces al año.
     - 2024-04: la primera hora de cada día "has to be building".
     - 2024-12: un bloque diario dedicado a un proyecto trabajado "in kind of like a sprint".
   - Se indica que el autor no explica el cambio. La lectura por escalas (temporada frente a bloque diario) se marca como lectura del libro, sin elegir ganador.
   - Se añadió una remisión a §5.5 y las unidades U-003-223 y U-018-187 al bloque COBERTURA.
3. **MENOR — Pang (*Rest*) y la frase reutilizada sin atribución (§13.1).** **Corregido.**
   - En "What rest is, and what it is not" se eliminó la afirmación errónea de que Koe reutiliza sin atribución "rest gets the right things done", un error heredado del Anexo C. En su lugar se aclara que la frase que reutiliza sin atribuir es otra: la del hombre creativo que "doesn't work at all".
   - En "Rest, the secret of the greats" se añadió el seguimiento de esa frase: en febrero de 2024 Koe la lee como de Pang, y en diciembre de 2024 abre un video con ella sin atribución. Se cita la fuente y se remite a §12.1 ("Optimize for creativity, not productivity").
   - Se añadió U-018-151 al bloque COBERTURA.
4. **MENOR — "creativity block" usado antes de definirse (§13.2, bloque de noviembre de 2023).** **Corregido.** Se añadió en el primer uso una glosa breve ("his term, defined in section 13.3, for time set aside to hunt for ideas outside the productive work blocks").

### Limpiezas globales

- **Frases de proceso eliminadas: 1.** "The corpus registers this as a change of emphasis…" pasó a "It is a change of emphasis for which the author gives no explanation". La frase errónea sobre Pang ya se reescribió en el hallazgo 3.
- No había IDs, "unit", "cluster", "material" con sentido editorial ni "annex" en la prosa. Los usos de "material" que quedan son comunes, por ejemplo "educational material".
- **Marcas normalizadas: 0.** Todas estaban ya en inglés: 116 marcas **Source:**, 7 **Complementary context:** y `### Exercises`. Los títulos de sección ya estaban en inglés.
- **Verificación con grep, fuera del bloque COBERTURA:** 0 apariciones de "U-0", "EV-", " unit", "cluster" y "Fuente:".
- **Bloque COBERTURA:** pasa de 136 a 140 IDs.

**Palabras finales del capítulo 13:** 31.187 (sin el bloque COBERTURA). Antes había unas 30.860, contando el bloque.

## Capítulo 14 — Aprender a aprender: build to learn

### Hallazgos

1. **MENOR — EV-108, secuencias de aprendizaje omitidas (§14.3, "The learning sequences, 2023–2026").** **Corregido.**
   - Se añadió un párrafo tras la tabla. Advierte que la tabla no es la serie completa y presenta, con fecha y fuente, las tres secuencias que faltaban:
     - el proceso de seis pasos y la lista goal → education + effort → experiment (2023-08), con remisión al capítulo 17 (§17.2 y §17.5);
     - el Mastery Method de siete pasos (2023-12), con remisión al capítulo 15 (§15.1);
     - los "three insights" (technique stacking, progressive overload of the mind, pure focus, 2025-08), con remisión al capítulo 15 (§15.2).
   - Se explicita el núcleo estable (proyecto, aprender al chocar con problemas, enseñar o publicar) y el cambio de marco teórico, de dopamina y novedad a la cibernética.
   - Se añadieron U-027-125, U-027-141, U-027-142, U-020-066 y U-020-166 al bloque COBERTURA.
2. **MENOR — Devon Eriksen y la conclusión "won't matter" (§14.1).** **Corregido.**
   - La frase ya no atribuye la conclusión a Koe. Ahora indica que su atribución es incierta: sigue directamente a la lista citada, en un pasaje en que Koe lee a Eriksen, y nada la separa como comentario propio. Puede ser de Eriksen leída en voz alta o una glosa de Koe.
   - Se aclara que lo claramente propio de Koe es el comentario posterior sobre agency.
3. **MENOR — Nombres de los youtubers de fitness de la "golden era" (§14.1, "The author's education").** **Corregido.**
   - Se normalizó "Elliot Holz" como Elliott Hulse, con la grafía transcrita entre paréntesis, y se añadió una identificación breve con remisión al capítulo 37, donde aparece como el estilo que Koe imitó.
   - Para Chris Lavado se registran las variantes "Levado" y "Lovato" y se indica que las transcripciones no fijan una sola grafía.
   - Se eliminó la advertencia genérica "spellings as transcribed".

**Observación fuera de los puntos 2–8.** También se corrigió. La introducción decía "three earlier pieces" y enumeraba cuatro capítulos (2, 6, 9 y 11). Ahora dice "four earlier pieces".

### Limpiezas globales

**Frases de proceso eliminadas o reescritas: 34.** Ejemplos:

- "A cluster of early passages" → "A group of early passages".
- "The smallest unit of this practice" → "The smallest form of this practice".
- "the unit of practice" → "the basic vehicle of practice".
- "it is the unit that turns a goal…" → "it is the vehicle that…".
- "('timeline fuzzy,' the source notes)" → "(the exact timeline is unclear)".
- "the chapter's material" → "the passages on learning".
- 27 menciones a "the evolution record", "the record" y "the lexicon", que remitían a los archivos de trabajo. Se reescribieron en lenguaje de libro, por ejemplo "This position later radicalizes", "It is an unresolved contradiction", "Koe gives no reason for the variation" o "which the following paragraphs trace".
- "The corpus registers a small tension" → "There is a small tension".

**Resto de la verificación:**

- **Marcas normalizadas: 0.** Todas estaban ya en inglés: 138 marcas **Source:**, 14 **Complementary context:** y `### Exercises`. Los títulos de sección ya estaban en inglés.
- **Verificación con grep, fuera del bloque COBERTURA:** 0 apariciones de "U-0", "EV-", " unit", "cluster", "Fuente:", "evolution record" y "lexicon". Los usos de "material" que quedan son comunes, por ejemplo "source material" o "inspiring material".
- **Bloque COBERTURA:** pasa de 192 a 197 IDs.

**Palabras finales del capítulo 14:** 37.488 (sin el bloque COBERTURA). Antes había unas 37.382, contando el bloque.
