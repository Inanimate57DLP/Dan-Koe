# Correcciones — Lote 14 (capítulos 27 y 28)

Corrección de los hallazgos de `audit-14.md` sobre `05_capitulos_en/cap-27.md` y `05_capitulos_en/cap-28.md`, más las limpiezas globales de vocabulario editorial y la nota adicional sobre la remisión al capítulo 9.

Nota sobre el reporte: la tabla resumen de la auditoría indica 3 hallazgos MENORES para el capítulo 28, pero el cuerpo del reporte solo desarrolla 2 (secciones 4 y 6). Se corrigieron los 2 desarrollados; no hay un tercero identificable.

## Capítulo 27 — The Personal Brand

Hallazgos de la auditoría: 0 PÉRDIDAS, 4 MENORES. Todos corregidos.

1. **Tensión sin explicitar entre U-009-239 (2024) y U-009-118 (2023)** — Corregido. En 27.3, "Articulating the brand", el párrafo de convergencia ya no dice que las cuatro herramientas tratan la bio como un producto tardío: ahora dice que eso vale para las tres últimas. Se añadió la tensión con sus fechas:
   - La herramienta de noviembre de 2023 es un método para la web, la landing y la bio (meta, problema, puente), ilustrado con una bio del propio Koe.
   - En septiembre de 2024 Koe relega el perfil ("they're not following the profile, they're following the content"), con remisión a 27.1.
   - Se señala que el autor no presenta lo segundo como corrección de lo primero y que las dos posiciones no son estrictamente contradictorias, sin elegir ganadora. Se anota también que las herramientas de 2026 siguen el énfasis posterior.
2. **"Big idea synthesis" glosado con un sentido ajeno y atribuido al "second-tier thinker"** — Corregido. En 27.4 se eliminó la referencia anacrónica al pensador de segundo nivel del capítulo 18. La glosa se ancla ahora en el mismo roadmap de diciembre de 2022, que trata la sección 18.4:
   - En la tercera etapa el creador se reposiciona como **synthesizer**, que desarrolla "big ideas that stick in people's heads" (el mental monopoly) y lo hace mejor en formato largo.
   - Se distingue explícitamente la acepción técnica de 2023 de *big idea* ("a one sentence summary… that illustrates the value", "Uber is the modern taxi service"), con remisión al capítulo 31 y una advertencia para no confundir ambas.
3. **"Infinite game" sin anclaje (U-012-189)** — Corregido. En 27.6, "Not winner-takes-all", se añadió una glosa integrada en la prosa con los dos sentidos del término:
   - El de la sección 10.7: juego sin final, cuyas reglas y metas evolucionan, frente al juego finito. Se indica que la distinción viene de Carse y que Koe la usa sin atribuirla.
   - El de la sección 2.5, con la cita de *The Art of Focus*: el camino del problem solver como salida del "world of replaceability", enamorándose de los problemas "from superficial to metaphysical".
   - Se explicitó la capa argumental: un mercado winner-takes-all es un juego finito, y un juego infinito no se agota porque haya otros jugadores.
4. **Remisión con nombre alterado al capítulo 22** — Corregido. "Remembering more than innovating" pasa a "reminding more than innovating" (sección 22.5). Se aclaró el sentido: recordar a otros verdades que ya conocen a medias.

**Nota adicional (instrucción del coordinador)** — Corregido. "the practical unit of change" pasa a "the practical vehicle of change", en coherencia con el título de la sección 9.3 ("The Project as the Practical Vehicle").

**Limpiezas globales, capítulo 27**

- **Frases de proceso eliminadas: 22.** Las 18 menciones de "the source material…" y las 4 de "in the material" / "in this material" se reescribieron en lenguaje de libro. Ejemplos: "the corpus records…", "is best read as…", "the corpus leaves the tension standing", "the oldest version in the corpus". Se suma "unit of change", corregida por la nota adicional.
- **Usos comunes de "material" ajustados por precaución: 2** ("the raw material (interests and skills)", "fitness programs").
- **Marcas normalizadas: 0.** El capítulo ya usaba `**Source:**`, `**Complementary context:**` y `### Exercises`, y todos los títulos de sección estaban en inglés.
- **Bloque COBERTURA:** intacto. No se incorporaron unidades nuevas: las adiciones remiten a capítulos donde esas unidades ya se desarrollan (18, 31, 10, 2).

## Capítulo 28 — The Business as Life's Work

Hallazgos desarrollados en la auditoría: 0 PÉRDIDAS, 2 MENORES. Ambos corregidos.

1. **"Lever-moving actions" disuelto en paráfrasis (U-025-051)** — Corregido. En 28.5, "It's all traffic and offers", se restituyó el término literal (**lever-moving actions**) y se añadió una glosa integrada:
   - Es un término acuñado que, en el mismo video del 2023-03-30, Koe equipara con "the fundamentals, or the principles".
   - Designa las pocas tareas prioritarias, diarias y cuantificables que mueven una meta, y se reconocen por los patrones repetidos entre fuentes (con remisión a la sección 12.7).
   - Son los levers del escalón inferior de la jerarquía de metas (capítulo 8), y cuáles son depende de la etapa (capítulo 30).
   - Se explicitó la consecuencia: una vez que existe una oferta, la palanca diaria es la distribución.
2. **Atribución conjetural añadida (U-005-048 frente a U-007-210)** — Corregido. En 28.6, "You are every department", se eliminó la sugerencia de que la redefinición de junio de 2023 proviene de Welsh. Ahora el texto dice que:
   - El corpus no establece filiación.
   - Koe usa la fórmula en contextos propios (febrero de 2023, sobre la formación de la marca; ver sección 27.2).
   - Es un giro común del marketing.
   - La coincidencia se lee como convergencia de conclusiones, no como préstamo.

**Limpiezas globales, capítulo 28**

- **Frases de proceso eliminadas: 1.** "outside this chapter's material" pasa a "in the corpus, not developed further here".
- **Marcas normalizadas: 0.** Ya estaban en inglés.
- **Usos comunes revisados y conservados:** "raw material", "assigned routine" y "assigned career", que no son vocabulario editorial.
- **Bloque COBERTURA:** intacto. Sin unidades nuevas.

## Verificación

Se ejecutó un `grep` sobre ambos capítulos, excluido el bloque COBERTURA, con los patrones "U-0", "EV-", " unit", "cluster", "Fuente:" y "source material".

- No queda ningún ID, "cluster", "Fuente:" ni "source material".
- Las únicas coincidencias de " unit" son falsos positivos de palabras comunes: "unites" (capítulo 27, línea 934) y "unity" (capítulo 28, líneas 642 y 646).

**Palabras finales** (incluido el bloque COBERTURA):

| Capítulo | Palabras |
|---|---|
| 27 | 32.901 (antes, 32.463) |
| 28 | 33.713 (antes, 33.524) |
