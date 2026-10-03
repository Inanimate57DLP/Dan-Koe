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

## Iteración 2 — verificación dirigida (resultado)

**Método.** Un auditor independiente, que no escribió ni corrigió estos capítulos, revisó las cuatro pérdidas corregidas en la iteración 1. Para cada una leyó el reporte de auditoría, el registro de corrección, las unidades originales en `02_unidades/` y la sección corregida, y contrastó las citas con el transcript de origen en la raíz del repositorio. Comprobó también que cada remisión apunte a una sección que existe y que efectivamente trata el contenido citado.

### 1. Cap. 11, §11.4 — detox de 30 días: VERIFICADA

- Los siete pasos aparecen en el orden del video (2025-10-26): pain and gain story (U-018-060), monk mode de 30 días con las cuatro categorías (U-018-062), caminar con la corrección de 10.000 a 7.000–8.000 pasos y el "3 by 20 method" (U-018-063, U-018-064), gimnasio (U-018-065, U-018-066), dieta de eliminación y vertical diet (U-018-067), proyecto (U-018-068 a U-018-070) y reflexión nocturna con Zeigarnik, 3-2-1, alarma de las 21:30 y cuaderno físico (U-018-071).
- Se conservan el resumen funcional del autor (U-018-072), el mecanismo del paso 1 ("you will give up in two weeks like always", "all lasting behavior change is identity change", las dos historias), las cifras y los matices: no moralizar, "at least once a year" frente a "every 6 to 12 months", y sovereignty and agency.
- Las remisiones existen y tratan el contenido: 4.2 y 17.3 (pain and gain), 40.2 (caminar, gimnasio, dieta), 9.1 (datos fisiológicos), 9.3 y 14.3 (proyecto, tutoriales) y 13.4 (reflexión).
- No se encontraron afirmaciones falsas ni invenciones.

### 2. Cap. 11, §11.4 — holistic monk mode: VERIFICADA, con una corrección menor de cita

- La estructura defensa + ofensa (U-019-161, U-019-162), la tríada good/true/beautiful con sus tres verdades (U-019-163) y la tabla de los cuatro focus habits con sus dosis (una hora, 30 minutos, 10 minutos y un entrenamiento) coinciden con el transcript `You Need To Be Extreme If You Want Your Life To Change.md`.
- La afirmación de que el transcript solo asigna parte del mapeo es exacta: el trabajo integra los tres valores y el libro representa lo verdadero. Para la meditación y el entrenamiento no asigna ninguno.
- Remisiones verificadas: 39.1, 9.3, 16.2, 40.4, 9.1 y 40.2.
- **Corrección.** La cita "a prime representation of the true" no es literal. El transcript dice "a prime representation of the truth". Se corrigió en el cap. 11 (dos apariciones) y en el cap. 16, §16.2 (una aparición, la misma cita).

### 3. Cap. 32, §32.4 — tercera tensión (progress): VERIFICADA

- La subsección "Tension 3: progress" reproduce la definición del autor (U-013-234) con citas literales comprobadas en el transcript (2026-07-05): "they each build on top of each other", la serie Maslow / ego development / spiral dynamics / developmental psychology, seguridad y comodidad → pertenencia y estatus → "deeper meaning, purpose, and experience", "AI can't just pin down exactly where you are", "you're essentially able to read people's minds when you get it right" y la regresión a la supervivencia bajo estrés o pérdida de dinero, con mayor susceptibilidad a la explotación.
- Se enlaza con la ética de §32.2 (U-013-235) y con "work them up the ladder" (U-013-236).
- El contexto complementario (Maslow, Loevinger/Cook-Greuter, Beck/Cowan/Graves) está separado de lo que dice el autor.
- Las remisiones cruzadas 32.4 ↔ 38.2 existen y ya no se anulan entre sí. La remisión a "levels of mind" (cap. 4, §4.7) también existe.
- Sin errores.

### 4. Cap. 40, §40.1 — el framework de 2025 sobre los veintes y EV-280: CORREGIDA

Se confirmó el error que había señalado el intento previo. La reconstrucción de la iteración 1 seguía el reporte `audit-20.md`, y ese reporte asignaba mal las piezas.

| Video (2025-07-27) | Versión de la iteración 1 | Fuente |
|---|---|---|
| Trap 1: "don't listen to anyone who doesn't have the life you want" | Correcta | U-025-173, U-025-174 |
| Trap 2: "get your taste of distractions fast" (juventud como moneda) | Correcta en lo sustancial | U-025-175, U-025-177 |
| Trap 3: "do everything in your power to not get a job", que cierra con el remedio "you need to start a business… right now" | Ponía "start a business" como *thing to do* 1 | U-025-178, U-025-179, U-025-180 (prerrequisito U-025-178) |
| Thing to do 1: "set goals that [expletive] scare you" (cosmic pull, "10 goals 10 years", Parkinson's law for goals, la empresa de 1 millón frente a la de 100 millones) | **Faltaba por completo** | U-025-185 a U-025-188 |
| Thing to do 2: "make as much money as you can" | Correcta | U-025-189 (y U-025-190 a U-025-194) |
| Thing to do 3: "self-actualize" | Correcta, sin el método asociado | U-025-195, U-025-196 |

**Qué se corrigió en `cap-40.md`:**

- **Lista de las seis piezas.**
  - La trampa 3 incluye ahora el remedio del negocio, con su condición: el autor lo generaliza solo para quien coincidió con él hasta ese punto. Incluye también el argumento del desafío creciente, la "tutorial phase of the job" y las remisiones a 10.7, 29.5 y 30.6.
  - El *thing to do* 1 pasa a ser "set goals that scare you", con el ejercicio "10 goals 10 years", la ley de Parkinson aplicada a metas y el argumento de la empresa de 1 millón frente a la de 100 millones. Remite a 7.5 y 34.3.
  - Se completaron el *thing to do* 2 (dinero como habilidad, 15.1; "deeply spiritual", 315 libras, 9.4) y el *thing to do* 3 (el hábito de consultar a la versión más alta de uno mismo con cuatro preguntas pareadas, 4.5).
  - Se añadió "you become what you focus on" a la trampa 3.
  - Todas las remisiones llevan ahora el número de sección, y se verificó cada una.
- **Tabla 2023 frente a 2025.** Step 1 = "Set goals that scare you ('10 goals 10 years')". Trap 3 = "Getting a job (remedy: start a business now)".
- **Párrafo de análisis.** Decía que "the business moves from third place to first". Ahora dice que el negocio sale de la lista de pasos sin salir del video, porque pasa a ser el remedio de la trampa 3. También precisa que el cuerpo deja de ser un paso propio, aunque sigue presente: como dominio ("mind, body, spirit, finances") y en los "health issues" del self-sabotage.
- **Párrafo sobre EV-280.** Se ajustó la descripción del cambio de contenido. Se mantienen las dos listas con fecha, sin elegir ganador, y la razón que da el autor.
- **Nota terminológica sobre "tutorial phase".** Se añadió que el sentido negativo reaparece en el mismo video ("the tutorial phase of the job").
- **Bloque COBERTURA del cap. 40.** Se añadieron U-025-181, U-025-182, U-025-185, U-025-186, U-025-187, U-025-188, U-025-193, U-025-194 y U-025-196 como remisiones.

### Frases residuales del proceso editorial (40 capítulos)

Búsqueda con grep: "not in the material", "corpus excerpt", "this chapter's material", "the material assigned", "not developed here", "in the material", "gathered material", "not reconstructed", "not reproduced here", "the corpus does not preserve", "not developed further here", "developed elsewhere in the corpus" y variantes. Los patrones literales del encargo ya no aparecen. Se encontraron y corrigieron cuatro frases de la misma familia: afirmaban que algo no estaba o no se desarrollaba, sin remisión. Las cuatro eran falsas o estaban incompletas.

1. **Cap. 30, §30.2.** "The corpus does not preserve all of the steps of each stage… what survives in the recordings is the first step of stage one, the second of stage two and the first of stage three". Era **falso**: el transcript de 2022-12-18 y las unidades U-007-143 a U-007-155 contienen los nueve pasos. Se reescribió con los nueve pasos y sus remisiones (23.1, 25.6, 15.3, 24.2, 18.4), con **Source:**. Se añadieron al bloque COBERTURA las unidades U-007-143, U-007-144, U-007-145, U-007-148, U-007-150, U-007-154 y U-007-155.
2. **Cap. 20.** "The distinction between job, career and calling… is not developed in the passage itself". Era **inexacto**: el mismo video la desarrolla minutos después (U-016-113 a U-016-116). Se resumieron las tres definiciones y se añadió la remisión al capítulo 9, §9.2.
3. **Cap. 28.** "another passage in the corpus, not developed further here, which places 'become an authority'…". Se identificó el pasaje (la progresión de febrero de 2025, U-009-147) y se remitió al capítulo 30, §30.7, y al 29, §29.4.
4. **Cap. 28.** "his example, developed elsewhere in the corpus, is the bodybuilder Chris Bumstead". Se añadió la remisión al capítulo 7, §7.4.

Además, en el **cap. 11, §11.2**, "'Living in accordance with nature' is not developed into a theory here" se reformuló como una afirmación sobre el pasaje de 2022. Se añadieron las dos reapariciones de la fórmula: *Meditations*, en 40.5, y "earning in accordance with nature", en 36.6.

Las demás menciones de "the corpus does not…" que quedan en los capítulos son juicios de fidelidad sobre el autor ("the corpus does not reconcile…", "does not say whether…") y no vocabulario del proceso editorial, así que se mantuvieron. Las menciones a gráficos "not recoverable" del transcript (caps. 4, 18 y 35) describen un límite real de la fuente y también se mantuvieron.

**Resultado de la iteración 2.** De las cuatro pérdidas, tres quedan verificadas y una corregida (cap. 40). Hubo además una corrección de cita literal (caps. 11 y 16) y cinco frases residuales corregidas (caps. 11, 20, 28 ×2 y 30). No se ejecutó git.
