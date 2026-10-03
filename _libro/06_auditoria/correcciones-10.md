# Correcciones — Lote 10 (capítulos 19 y 20)

Fase 5. Correcciones aplicadas a `05_capitulos_en/cap-19.md` y `05_capitulos_en/cap-20.md` según `06_auditoria/audit-10.md`. La auditoría no registró ninguna PÉRDIDA. Registró 5 hallazgos MENORES en el capítulo 19 y 6 en el capítulo 20. Se corrigieron los 11 y no se descartó ninguno.

---

## Capítulo 19 — You Are the Niche

### Hallazgos

1. **MENOR, punto 4: "niche" en su sentido propio (cosmovisión).** Corregido. En 19.2 ("Nicheless: your identity is your niche"), después de la definición práctica, se agregó un párrafo con las otras dos definiciones literales del autor: "a perspective or worldview" y "the frame of big goals and burning problems that compose your worldview". El párrafo explica que las tres definiciones describen lo mismo en tres niveles (cosmovisión, metas y problemas, intereses) y remite al capítulo 22 (sección 22.1, "The niche as a perspective or worldview") y a 19.4.

2. **MENOR, punto 5: EV-193 (las metáforas de los pilares).** Corregido.
   - Se añadió a la tabla de versiones la fila de marzo de 2023 (story / school / map, de "The Future Of One-Person Businesses").
   - Se reescribió la frase sobre la migración de "map" con las dos versiones citadas y fechadas.
   - Se agregó un cierre que enumera las versiones no incluidas en la tabla: what/how/why (2022-12), macronutrients (2023-11), "your philosophy is your brand" (2024-01) y las cuatro de 2026, incluida la de junio, en la que "map" vuelve a content. El cierre remite al capítulo 28 (sección 28.6) para la secuencia completa.
   - Se agregó U-008-025 al bloque COBERTURA.

3. **MENOR, punto 6: origen de "niche of one".** Corregido.
   - El título de la subsección pasó a "The earliest appearance of the term: Justin Welsh".
   - Se eliminó la afirmación "did not originate with Koe". En su lugar, el texto dice que el corpus no determina quién acuñó la frase, que Koe la usa como nombre propio de su tesis y que la primera aparición registrada es de Welsh (2021). Eso solo muestra que la frase ya circulaba, no quién la originó.
   - Así desaparece el choque con la introducción del capítulo.

4. **MENOR, punto 6: dirección de la influencia en "escape competition through authenticity".** Corregido. Se reescribió la primera frase de la subsección:
   - la idea ya está en la respuesta de Koe a Welsh en 2021 ("makes it so nobody can compete with you"), y el corpus no le asigna fuente;
   - en 2025 aparece vinculada explícitamente a Naval por dos vías: un invitado (John Hugh) y el propio Koe.

5. **MENOR, punto 8: "meaning economy" sin glosa.** Corregido. En 19.4 se añadió una glosa breve en la primera aparición ("his name for the emerging economy in which people are paid for meaning rather than for utility, because meaning is becoming the scarcest good"). La remisión al capítulo 36 se mantiene.

### Limpiezas globales

- **Frases de proceso eliminadas o reescritas: 7.**
  - "reconstructed from the surrounding material" → "surrounding passages";
  - "source of the material" → "source of the writing";
  - "the beginner's material" → "the beginner's raw material", que es el término de Dickie Bush citado en la línea anterior;
  - "the sources assigned to this chapter, together with one documented elsewhere in the corpus" → "the main variants recorded in the corpus";
  - "The material assigned to this chapter does not develop these steps" → "Koe does not develop these steps in detail in this version of the process";
  - "The transcripts assigned to this chapter do not describe..." → "The corpus does not describe...";
  - "his one-person business material" → "his one-person business videos".
- **Marcas normalizadas: 0.** El capítulo ya usaba `**Source:**`, `**Complementary context:**` y `### Exercises`, y todos los títulos estaban en inglés.
- Se conservaron los usos de "raw material", porque es vocabulario del autor y de sus invitados ("your raw material"), y el uso común de "material" en "registered as material" (19.7). Ninguno es vocabulario del proceso editorial.

### Verificación

`grep -v COBERTURA cap-19.md | grep -E "U-0|EV-| unit|cluster|Fuente:"` no devuelve resultados.

---

## Capítulo 20 — The Generalist and the Second Renaissance

### Hallazgos

1. **MENOR, punto 4: segunda acepción de "hyper-specialists".** Corregido. En 20.1 ("Hyper-specialists and the fading of labor as leverage") se añadió un párrafo con la acepción complementaria de julio de 2024: "Computers are hyper specialists, humans are deep generalists, a great combo but not too effective on their own", junto con la respuesta sobre escritores y programadores ("if they aren't in control of the vision").
   - El párrafo explica cómo encajan las dos acepciones: amenaza para quien compite con la máquina en su terreno, socio para quien la dirige.
   - Remite al capítulo 36 (sección 36.4).
   - Se agregó U-006-105 a COBERTURA.

2. **MENOR, punto 5: EV-187 (shiny object syndrome) en 2026.** Corregido. En "Shiny object syndrome: good and bad" se incorporó la defensa de enero de 2026 (el "residue" de cada interés y "your shiny object syndrome has been trying to tell you this whole time"), con su fecha.
   - Esta versión se contrasta con el veredicto negativo de agosto de 2024 y con el relato de los negocios fallidos. Al verificar el material se precisó que ese relato es de mayo de 2026 y de otro video.
   - Se presentan las dos versiones sin elegir ganadora y se remite al capítulo 4.
   - La lectura conciliadora sigue marcada como no formulada por Koe.
   - Se agregó U-010-282 a COBERTURA.

3. **MENOR, punto 5: EV-003 en diciembre de 2025.** Corregido. Tras la autocita de *Purpose and Profit* se añadió la formulación sistémica del mismo video ("It doesn't have to be a conspiracy theory for the system to naturally take shape of the subconscious desires of the humans at the top of the pyramid"), con remisión al capítulo 2.
   - El texto aclara que diciembre de 2025 no es un endurecimiento, sino la convivencia de las dos versiones en un mismo video.
   - Esa frase se añadió a la lista de matizaciones del párrafo de estatus.
   - Se agregó U-013-209 a COBERTURA.

4. **MENOR, punto 5: EV-182, puntos intermedios de 2024.** Corregido.
   - Se agregó un párrafo con las dos formulaciones de 2024, con fecha y remisión a sus sedes:
     - "When you master one thing it becomes easier to master others… most people never master one domain", de julio de 2024 (capítulo 15, sección 15.3);
     - "Intelligence stems from generalism, not specialism", de agosto de 2024 (capítulo 6, sección 6.4).
   - Se añadieron las dos filas a la tabla de la secuencia.
   - La conclusión dejó de decir "grows steadily". Ahora indica que el crecimiento del peso de la profundidad no es lineal: ya se anuncia en julio de 2024, y el polo radical reaparece hasta diciembre de 2025.
   - Se agregaron U-020-141 y U-023-199 a COBERTURA.

5. **MENOR, punto 6: atribución de la cita de Schmachtenberger.** Corregido.
   - La frase introductoria ahora dice "a quotation that, in some of its appearances, he attributes to Daniel Schmachtenberger".
   - Se añadió una nota según la cual en algunas apariciones, entre ellas la apertura del video de febrero de 2025, Koe enuncia la línea como tesis propia sin nombrar autor, y parte del corpus la registra como suya.
   - Se mantiene a Schmachtenberger como la fuente a la que remite la cita.

6. **MENOR, punto 8: "personal monopoly" sin glosa.** Corregido. En su primera aparición (20.1, discrepancia "deep specialist") se añadió una glosa: frase adaptada de Naval Ravikant que significa volverse irreemplazable persiguiendo la curiosidad genuina, porque nadie más puede ser uno mismo. Remite al capítulo 27 (sección 27.5). También se añadió una remisión al capítulo 19 para "niche of one".

### Limpiezas globales

- **Frases de proceso eliminadas o reescritas: 21.**
  - Siete menciones a "the evolution record" ("classifies...", "lists it", "notes"), reescritas como lectura propia ("read across the corpus", "is best read as", "traced across the corpus", "remains unresolved across the corpus").
  - "The lexicon records a second use..." → "Koe also uses 'specific knowledge' in a second sense of his own".
  - Siete menciones a "the material":
    - "the material records the 2025 formulation as adapted" → "is an adaptation";
    - "The material records the attribution to Shakespeare" → "is reported here as Koe states it";
    - "the material records the quotation as 'attributed'" → "Koe presents the quotation as 'attributed'";
    - "the 2024 material" → "the 2024 videos";
    - "the image the material itself suggests" → "an image the corpus itself suggests";
    - "The material does not identify which lecture" → "Koe does not identify";
    - "The material notes a tension" → "There is a tension here".
  - "nothing in the material for this chapter settles it" → "nothing in these videos settles it".
  - "The transcript material assigned to this chapter does not develop idea 1" → "The corpus does not develop idea 1".
  - "The material assigned to this section contains several qualifications" → "Koe's statements on the subject contain several qualifications".
  - "third-party material" → "from a third party".
  - "the unit of learning" → "the basic element of learning".
  - "a discrepancy in the record" → "in the corpus".
  - "the creative worker's material" → "raw material".
- **Marcas normalizadas: 0.** El capítulo ya usaba `**Source:**`, `**Complementary context:**` y `### Exercises`, y todos los títulos estaban en inglés.

### Verificación

`grep -v COBERTURA cap-20.md | grep -E "U-0|EV-| unit|cluster|Fuente:"` devuelve una sola línea. Es un falso positivo: la cita de Koe "the expansion and unity of mind and consciousness" contiene la secuencia " unit" dentro de "unity". Con límite de palabra (`grep -w "unit"`) no hay resultados.

---

## Bloques COBERTURA

- **Capítulo 19:** se agregó U-008-025.
- **Capítulo 20:** se agregaron U-006-105, U-010-282, U-013-209, U-020-141 y U-023-199, y el bloque quedó ordenado.

En ambos casos el resto del bloque se conservó intacto.

## Extensión final (sin contar el bloque COBERTURA)

| Capítulo | Palabras |
|---|---|
| 19 | 32.339 |
| 20 | 29.343 |
