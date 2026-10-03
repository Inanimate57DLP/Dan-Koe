# 06 — Auditoría de cobertura (Fase 5)

## Método

- **Punto 1 (cobertura global de IDs):** verificado por script contra los bloques `<!-- COBERTURA -->` de los 40 capítulos.
- **Puntos 2–8:** 20 auditores independientes (ninguno escribió capítulos), uno por par de capítulos, con lectura completa del capítulo y revisión del material (en la práctica, 60–100 % de las unidades de cada capítulo; todas las entradas de evolución y fuentes; ≥30 entradas de léxico). Reportes: `06_auditoria/audit-01.md` … `audit-20.md`.
- **Corrección:** 20 correctores (uno por par) aplicaron cada hallazgo y limpiaron el vocabulario de proceso editorial; registro en `06_auditoria/correcciones-01.md` … `correcciones-20.md`.

## 1. IDs no cubiertos
- Unidades totales: 6087 · absorbidas por fusión en Fase 2: 260 · declaradas en algún bloque COBERTURA: 6087 · **no cubiertas: 0**.
- Durante la corrección se añadieron a los bloques COBERTURA unidades usadas como remisión o contexto cruzado (por eso algunas aparecen en más de un capítulo).

## Resultado por capítulo (iteración 1)

| Cap. | PÉRDIDAS | MENORES | Estado |
|---|---|---|---|
| 01 | 0 | 10 | corregido |
| 02 | 0 | 6 | corregido |
| 03 | 0 | 10 | corregido |
| 04 | 0 | 10 | corregido |
| 05 | 0 | 4 | corregido |
| 06 | 0 | 2 | corregido |
| 07 | 0 | 3 | corregido |
| 08 | 0 | 3 | corregido |
| 09 | 0 | 5 | corregido |
| 10 | 0 | 6 | corregido |
| 11 | 2 | 7 | corregido |
| 12 | 0 | 7 | corregido |
| 13 | 0 | 4 | corregido |
| 14 | 0 | 3 | corregido |
| 15 | 0 | 5 | corregido |
| 16 | 0 | 4 | corregido |
| 17 | 0 | 4 | corregido |
| 18 | 0 | 3 | corregido |
| 19 | 0 | 5 | corregido |
| 20 | 0 | 6 | corregido |
| 21 | 0 | 4 | corregido |
| 22 | 0 | 7 | corregido |
| 23 | 0 | 6 | corregido |
| 24 | 0 | 5 | corregido |
| 25 | 0 | 7 | corregido |
| 26 | 0 | 6 | corregido |
| 27 | 0 | 4 | corregido |
| 28 | 0 | 3 | corregido |
| 29 | 0 | 5 | corregido |
| 30 | 0 | 6 | corregido |
| 31 | 0 | 6 | corregido |
| 32 | 1 | 5 | corregido |
| 33 | 0 | 3 | corregido |
| 34 | 0 | 3 | corregido |
| 35 | 0 | 6 | corregido |
| 36 | 0 | 5 | corregido |
| 37 | 0 | 3 | corregido |
| 38 | 0 | 3 | corregido |
| 39 | 0 | 13 | corregido |
| 40 | 1 | 11 | corregido |
| **Total** | **4** | **218** | todos corregidos, 0 descartados |

## Pérdidas materiales detectadas y corregidas

1. **Cap. 11 — detox de 30 días:** el capítulo afirmaba que el corpus no ordenaba los siete pasos; se restituyeron los siete pasos con su mecanismo y remisiones.
2. **Cap. 11 — holistic monk mode:** faltaba la parte de 'offense' (cuatro focus habits y la tríada good/true/beautiful); restituida.
3. **Cap. 32 — tercera tensión (progress):** el capítulo la reconstruía sin base; se restituyó la definición del autor (etapas acumulativas tipo Maslow/ego development/Spiral Dynamics; sentido, propósito y experiencia; regresión bajo estrés y su consecuencia ética).
4. **Cap. 40 — framework de 2025 sobre los veintes:** solo se desarrollaba una de seis piezas y se daba por resuelto el cambio 2023→2025; se reconstruyeron las tres trampas y las tres acciones, y se presentan ambas listas fechadas.

## Patrones de hallazgos MENORES (todos corregidos)

- Pasos de evolución omitidos en tablas de cambios de posición (se añadieron con fecha y fuente, sin elegir ganador).
- Atribuciones a terceros imprecisas (Naval, Schmachtenberger, Hormozi vía Dickie Bush, Vitali, Pang, de Mello, Ogilvy, Carse, Eriksen).
- Términos acuñados o palabras con sentido propio sin glosa en su primera aparición, o usados antes de su capítulo (se añadieron glosas y remisiones).
- Remisiones internas erróneas entre capítulos.
- Errores de datación por pasajes de 2022–2023 reeditados en las compilaciones de 2024.
- Vocabulario del proceso editorial filtrado al texto ('units', 'cluster', 'material', IDs): eliminado en los 40 capítulos (limpieza verificada por grep).

## Iteración 2 (verificación)

Ver sección al final (verificación dirigida de las pérdidas corregidas).

## Estado tras correcciones

- Palabras del libro en inglés (40 capítulos. sin comentarios): 1.345.930
