# Correcciones — Lote 17 (capítulos 33 y 34)

Fase 5. Corrección de `05_capitulos_en/cap-33.md` y `05_capitulos_en/cap-34.md` según `06_auditoria/audit-17.md`. La auditoría no registró PÉRDIDAS. Registró 3 MENORES en cada capítulo. Los seis hallazgos quedaron corregidos y ninguno se descartó.

## Capítulo 33 — Construir el producto

| # | Hallazgo | Acción | Estado |
|---|---|---|---|
| 1 | §33.1 y §33.4: elementos 1 y 2 de la oferta de 2025 (U-009-170, U-009-171 y U-009-172) y pasos de 2022 sin remisión. Además, la afirmación de que la numeración era "inferida" era inexacta y había frases de proceso. | **§33.1:** reemplacé la frase sobre el "material asignado" por remisiones explícitas para cada paso, con su contenido esencial:<br>• Paso 1, la cita de Kotler → §10.4.<br>• Pasos 2 y 3, aprender construyendo, *permissionless apprenticeship* y documentar → §14.5.<br>• Paso 4, la experimentación con StrongLifts y las dietas → §15.4.<br>• Paso 6, *sell what's already selling*, 2 Hour Writer y los $130.000 → §26.3.<br>**§33.4:** Koe numera los elementos. El texto lo dice ahora y remite a §17.4 para los elementos 1 y 2. Amplié la glosa del elemento 2 en la tabla. Añadí el párrafo *"The big problem and the desired outcome, in brief"*: transformación como "the only thing that sells", la dependencia del elemento 1, "a body that commands respect" y "vanity / therapy". | Corregido |
| 2 | §33.5, EV-209: la tabla "How the position moved" omitía tres escalones. | Añadí tres filas, cada una con remisión:<br>• Febrero de 2025: "education of the future", U-010-247 → §31.5.<br>• Mayo de 2025: espacios con *prompts*, "externalized clone", U-019-145 → §30.7.<br>• Junio de 2026: "information products are abundant… I don't think they will die", U-010-337 → §30.7.<br>Integré los *wrappers* (U-008-189) en la fila de enero de 2026. Añadí un párrafo que pone en relación los dos enunciados de junio de 2026 (13 y 28 de junio) y la matización de enero de 2026, sin elegir ganador. | Corregido |
| 3 | §33.5, "The unique system": remitía a §31.3 para la reversión de la entropía. | Ahora remite a §31.1 (reversión de la entropía mediante sistemas) y a §31.3 (creación de valor). | Corregido |

**Limpiezas globales (cap. 33).**

- Frases de proceso eliminadas o reescritas: 7, en 5 pasajes.
  - "The material assigned to this chapter only details step 5" y "elaborated in separate units".
  - "reconstructed from the units available" y "The material assigned to this chapter details elements 3 to 6".
  - "Koe's material on these decisions" → "Koe's guidance on these decisions".
  - "The material of this section…" → "The passages of this section…".
  - "Two smaller units give…" → "Two shorter passages give…".
- Marcas normalizadas: 0. Ya estaban en inglés: 79 **Source:**, 6 **Complementary context:**, `### Exercises` y todos los títulos de sección.
- COBERTURA: añadí U-008-189, U-009-170, U-009-171, U-009-172, U-010-247, U-010-337 y U-019-145, porque ahora se presentan con su contenido. Pasa de 111 a 118 IDs.

## Capítulo 34 — El dinero

| # | Hallazgo | Acción | Estado |
|---|---|---|---|
| 1 | §34.1: "scam" tratada solo en una de sus dos acepciones. | Junto a la frase sobre el scam añadí las dos acepciones del autor:<br>• Primera, con criterio positivo, del *roadmap* de diciembre de 2022 repetido en la compilación de febrero de 2024: prometer y no entregar, "If you can't deliver and don't refund, that's a scam" → §23.5.<br>• Segunda, de agosto de 2024: lo que alguien llama así cuando no ve el beneficio → §32.6.<br>Precisé qué haría del producto inferior un scam: la promesa incumplida sin reembolso. | Corregido |
| 2 | §34.4, EV-258: diversificar frente a concentrar quedaba resumido sin el matiz ni la continuación. | Reescribí el párrafo e incluí:<br>• La cifra de Welsh: 10 negocios de $50.000 frente a uno de $500.000, siguiendo a Vassallo → §17.6.<br>• El acuerdo parcial de Koe: diversificar la mayoría y "go all in" ante el impulso de hacer *monk mode*, U-005-060 → §11.4.<br>• La concentración como "the only way to get rich" (agosto de 2025).<br>• "build your own thing and commit to it and accept no other option" (junio de 2026, U-012-209) → §6.4.<br>• El "depression apartment" como cobertura (agosto de 2026, U-022-136, término atribuido a "Devon") → §17.6.<br>Dejé la contradicción sin resolver y señalé los contextos distintos, como hace el registro. | Corregido |
| 3 | §34.2: la remisión de "survival and status stages" apuntaba a los capítulos 4 y 38. | Ahora remite al capítulo 9 (niveles de propósito, con criterios de entrada y salida de la *status stage*). | Corregido |

**Limpiezas globales (cap. 34).**

- Frases de proceso reescritas: 6.
  - "Two features of the material" → "of the sources".
  - "the material supports both" → "the sources support both".
  - "The richest material here" → "The richest discussion here".
  - "gathers the material that pushes back" → "gathers the passages that push back".
  - "What the material does not show" → "What the corpus does not show".
  - "The last material on enough" → "The last passage on enough".
- Marcas normalizadas: 0. Ya estaban en inglés: 117 **Source:**, 9 **Complementary context:**, `### Exercises` y todos los títulos.
- COBERTURA: añadí U-001-131, U-005-059, U-005-060, U-012-209, U-019-019 y U-022-136. Pasa de 128 a 134 IDs.

## Verificación con grep (fuera del bloque COBERTURA)

- `U-0`, `EV-`, `cluster`, `Fuente:`, `Contexto complementario` y `Ejercicios`: 0 coincidencias en los dos capítulos.
- ` unit`: quedan solo usos legítimos del contenido, no del proceso editorial.
  - Cap. 33: "one additional unit" (coste marginal) y "stock-keeping units" (SKUs).
  - Cap. 34: la definición de Koe "money is a unit of value" y sus repeticiones, y "units of currency" (cita).
- "material": quedan solo usos de contenido, como "material world", "material pursuits", "raw material", "course material" o "marketing materials".

## Extensión final

- Capítulo 33: 24.716 palabras en todo el archivo; antes, 24.148.
- Capítulo 34: 30.183 palabras en todo el archivo; antes, 29.790.
