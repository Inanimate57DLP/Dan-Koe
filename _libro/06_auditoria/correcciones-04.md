# Correcciones — Lote 04 (capítulos 07 y 08)

Fase 5. Correcciones aplicadas a `05_capitulos_en/cap-07.md` y `05_capitulos_en/cap-08.md` según `06_auditoria/audit-04.md`. La auditoría no registró PÉRDIDAS; los seis hallazgos MENORES se corrigieron todos. No se incorporaron unidades nuevas, por lo que los bloques `<!-- COBERTURA: ... -->` quedan intactos.

## Capítulo 07 — Anti-visión y visión

| # | Hallazgo | Acción |
|---|---|---|
| 1 | MENOR — "Focus Formula" rotulada como *purpose-path-priority* en §7.1 ("Marinating in the pain"). | **Corregido.** Ahora dice "the purpose-process-priority framework treated in Chapter 8, section 8.2", con la aclaración de que "process" pasó a "path" solo en versiones posteriores (remisión a §7.2). Queda coherente con §7.2 y §8.2. |
| 2 | MENOR — "intensity trap" sin glosa antes del capítulo 10 (§7.5, "Goals that scare you"). | **Corregido.** Se añadió la glosa según U-017-218 (2024-10): burnout y saturación por sostener la intensidad demasiado tiempo en vez de pasar a la consistencia; "take profits" y "drop down to a new baseline and maintain the progress you've made". Se mantiene la remisión al capítulo 10. |
| 3 | MENOR — "flow model" sin glosa antes del capítulo 10 (§7.5, "Thinking big in business"). | **Corregido.** Glosa de una frase: equilibrio desafío/habilidad adaptado de Csikszentmihalyi (desafío muy por encima de la habilidad produce ansiedad; muy por debajo, aburrimiento), con remisión al capítulo 10. Se explicita la lógica del consejo ("the remedy is to raise the skill, so self-educate"). |
| 4 | MENOR — Remisión interna inexacta "(section 7.1)" en §7.3 ("From one sitting to a running note"). | **Corregido.** La remisión ahora indica con precisión qué trata §7.1: la otra mitad de la instrucción, identificar esas cosas "as problems to be solved". La lista de contenidos de la running note queda en §7.3, donde ya estaba. |

## Capítulo 08 — Metas, plan y propósito

| # | Hallazgo | Acción |
|---|---|---|
| 1 | MENOR — Capas de la creation pyramid glosadas en forma genérica y sin remisión (§8.3, tabla), con la frase "The table above gives only what the narration supports". | **Corregido.** Se precisaron las filas Process, Drive y Focus de la tabla y se sustituyó la frase final por un párrafo que desarrolla cada capa en una o dos oraciones con remisión: process como experimento científico (observar, investigar, hipótesis, experimento, analizar, resultado) con paciencia, rendición y fe (U-026-032/033 → capítulo 15); drive intrínseco con los cinco impulsores de Steven Kotler (curiosidad, pasión, propósito, autonomía, maestría), con énfasis en los tres primeros (U-026-036 → capítulo 10); focus como "focus matrix" (profundo/estrecho/convergente frente a amplio/abierto/divergente, cruzado con inconsciente/consciente) (U-026-038 → capítulo 6). |
| 2 | MENOR — Homónimo "attention anchor(s)" no señalado (§8.6, "Chapters, puzzles and exhausted visions"). | **Corregido.** Se añadió una advertencia: en 2023 (U-023-069) los "attention anchors" son preguntas, en plural; en el pasaje de 2025 tratado en §7.2 (U-025-101) "an attention anchor" es la visión misma, la "sturdy mental house". Se indica qué comparten (la función de sostener la atención en segundo plano). |
| 3 | MENOR — "North Star" en dos sentidos dentro del capítulo sin remisión (§8.3 y §8.6). | **Corregido.** En §8.3 se añadió un paréntesis que anuncia el segundo sentido y remite a §7.1 y §8.6. En §8.6 se añadió una frase que distingue el propósito del momento (2023) de la visión lejana (2025), remite a §7.1 y advierte que los dos usos coinciden en función, no en distancia. |

## Limpiezas globales

- **Vocabulario del proceso editorial eliminado:** 4 frases o expresiones reescritas en el capítulo 08 (ninguna en el 07):
  - "the 2025 list is reconstructed from the units of that video, and two of its rules (6 and 7) cannot be identified with confidence from the material" → "has to be reconstructed from the passages of that video that survive in the corpus ... from them".
  - Dos celdas de tabla "Not identifiable in the material" → "Not identifiable in the corpus".
  - "The table above gives only what the narration supports" → reemplazada por el párrafo de capas del hallazgo 1.
- **Desambiguación preventiva de "unit":** para que el control con grep quede limpio, se reformularon 4 usos legítimos de "unit" que podían confundirse con vocabulario de proceso: "practical unit of change" → "practical vehicle of change" (cap. 07 y cap. 08), "a unit of projection" → "the scale of projection" (cap. 07) y "a unit of work" → "a container for the work" (cap. 08).
- **Marcas normalizadas:** 0. Los dos capítulos ya usaban `**Source:**` (144 en el 07 y 154 en el 08), `**Complementary context:**` y `### Exercises`. Todos los títulos de sección ya estaban en inglés.

## Verificación con grep (fuera del bloque COBERTURA)

- `U-0`: 0 coincidencias en ambos capítulos.
- `EV-`: 0 coincidencias en ambos capítulos.
- `cluster`: 0 coincidencias en ambos capítulos.
- `Fuente:`: 0 coincidencias en ambos capítulos.
- `" unit"`: 0 en el capítulo 08. En el capítulo 07 queda 1, que es una cita textual de Koe que se conserva: "an absolute unit of an individual" (§7.1, "The author's own anti-vision as engine"). No es vocabulario de proceso.

## Extensión final (palabras, sin el bloque COBERTURA)

- Capítulo 07: 36.803 palabras.
- Capítulo 08: 38.438 palabras.
