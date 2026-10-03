# Correcciones — Lote 19 (capítulos 37 y 38)

Corrige los hallazgos de `06_auditoria/audit-19.md`. La auditoría no registró PÉRDIDAS. Registró tres hallazgos MENORES en cada capítulo. Los seis están corregidos.

## Capítulo 37 — The Author's Trajectory and the Step from One Person to a Team

### Hallazgos

1. **MENOR — EV-289 (préstamos estudiantiles): cifras incompletas en la tabla de variantes de §37.1.** Corregido.
   - La fila "Debt" ahora recoge las cuatro versiones con su fecha:
     - "$2,000 in loans even with a full-ride scholarship" (2024-01).
     - "$20,000 of student loans" con "nearly a full-ride scholarship" (2024-05), tras un primer "10 to 20 thou".
     - Unos $20.000 "and growing" (2026-05).
     - $8.000 de deuda total como estudiante de tercer año (2025-06).
   - Después de la tabla añadí un párrafo. Dice que las cifras no cuadran, que los $2.000 podrían ser un error de transcripción frente a los $20.000 (algo que el corpus no permite confirmar) y que Koe no explica los $8.000.
   - Unidades incorporadas al bloque COBERTURA: U-017-179, U-016-041 y U-004-088.
2. **MENOR — "features, features, features" (término de invitado, Vitali): término no nombrado.** Corregido.
   - En §37.3, "Customer first, and the core job to be done", el término aparece con su nombre literal y su definición: construir una función tras otra por entusiasmo tecnológico en lugar de resolver un problema real del cliente.
   - Lo enlacé con "We are not here building features, we are here solving problems".
   - En el párrafo sobre "death by complexity" añadí su relación con ese término: son el mismo error visto desde la empresa y desde el cliente.
3. **MENOR — EV-290 (la lista de los siete negocios): faltaban las versiones de 2026.** Corregido.
   - Añadí a la tabla de variantes de §37.1 la fila "Composition of the seven". Recoge las versiones de 2022, 2024, 2026-05 (arte digital, fotografía, varias agencias, dropshipping dos veces y un e-commerce) y 2026-08 ("Facebook ads, SEO, drop shipping, web design, digital art and a few more").
   - El párrafo posterior a la tabla explica que el número "siete" se mantiene estable y la composición no, y que la variación llega hasta 2026.
   - Unidades incorporadas al bloque COBERTURA: U-004-087 y U-022-106.

### Limpiezas globales

- **Frases de proceso eliminadas o reescritas: 27.**
  - 20 marcas **Source:** que remitían a entradas de evolución (EV-067, EV-160, EV-286, EV-287, EV-289/EV-290, EV-291, EV-292 con "the units cited above", EV-294, EV-297 dos veces, EV-299, EV-301, EV-302, EV-303 dos veces, EV-304, EV-305, EV-306 y EV-307) o a un clúster ("evolution notes for cluster C-T12a-34"). Todas se sustituyeron por los títulos de los videos con su fecha, tomados de las unidades correspondientes. La que citaba la ruta `_libro/03b_evolucion.md` también desapareció.
  - 7 usos de "material" en sentido editorial, reescritos como "this story", "the biographical account", "what follows", "the discussion of", "the corpus" (dos veces) y "this book's synthesis of Sections 37.2 to 37.6".
- **Marcas normalizadas: 0.** El capítulo ya usaba **Source:**, **Complementary context:** y `### Exercises`, y todos los títulos ya estaban en inglés.
- **Verificación con grep, fuera del bloque COBERTURA:** 0 coincidencias de "U-0", "EV-", "cluster", "Fuente:" y " unit"/"units".

**Palabras finales:** 31.158 (antes 30.258).

## Capítulo 38 — Maps of the Development of Consciousness

### Hallazgos

1. **MENOR — Arquetipos y metatipos de Human 3.0: el capítulo afirmaba que la transcripción no los enumera.** Corregido.
   - Eliminé la frase falsa de §38.4, "The structure: quadrants, levels, phases, traits".
   - En su lugar hay un párrafo con:
     - Las definiciones literales de arquetipo y metatipo.
     - Las cuatro progresiones por cuadrante: NPC → player → creator; incel → Chad → sigma; religion → atheism → mysticism; job → career → calling.
     - Ejemplos de las listas por nivel, con la advertencia del autor de que "are just examples".
     - El metatipo de ejemplo "the outlier", con su definición.
   - El párrafo remite al capítulo 1 (Section 1.4, "Archetypes and metatypes: NPC as a level") para las listas completas y para la discusión del ejemplo.
   - Unidades incorporadas al bloque COBERTURA: U-024-127, U-024-128, U-024-130, U-024-131 y U-024-132.
2. **MENOR — EV-023 (dominator / actualization hierarchies): faltaba el antecedente de enero de 2023 en la cronología de la atribución.** Corregido.
   - El párrafo "The first change is attribution" de §38.1 empieza ahora con U-023-053 y U-023-054 ("Society Is A Pyramid Scheme", 2023-01-15). Ahí la distinción aparece en marco wilberiano y con los mismos ejemplos, y se cita su consecuencia práctica ("have to create their own"), con remisión a la Section 2.5.
   - El párrafo presenta las tres etapas sin elegir ganador: marco wilberiano (2023-01), uso sin fuente (2023-03) y atribución explícita al libro (2023-07 y 2024-03).
   - La fila "Definition 1" de la tabla dice ahora "2023-01, 2023-03, 2024-03".
   - Unidades incorporadas al bloque COBERTURA: U-023-053 y U-023-054.
3. **MENOR — EV-136 (¿existen las ideas originales?): el nivel 4 "generative" no señalaba la tensión ni remitía a otro capítulo.** Corregido.
   - En §38.2, "Lines, levels and altitudes", después de la definición del nivel 4, añadí la contradicción con "nobody has original ideas, absolutely nobody" (2024) y con "largely a myth" (enero de 2025).
   - Indiqué que Koe no la reconcilia. Lo más cercano es su "tap into level four occasionally", que presenta el nivel generativo como raro, no como imposible.
   - Añadí la remisión al capítulo 18 (Section 18.3, "The evolution of the originality question").

**Matiz no contado como hallazgo (EV-018, U-025-114, 2025-03).** No lo incorporé. La unidad solo alude de pasada a "you go up and down, but there's a baseline", dentro de un argumento sobre el alter ego. Esa idea ya está tratada en §38.5 (estados, etapas y regresión), y la auditoría confirma que la omisión no altera la presentación del cambio.

### Limpiezas globales

- **Frases de proceso eliminadas o reescritas: 1.** "the material spans 2023 to 2026" pasó a ser "the corpus spans 2023 to 2026".
- **Marcas normalizadas: 0.** El capítulo ya usaba **Source:**, **Complementary context:** y `### Exercises`, y todos los títulos ya estaban en inglés.
- **Verificación con grep, fuera del bloque COBERTURA:** 0 coincidencias de "U-0", "EV-", "cluster" y "Fuente:".
  - Quedan 18 apariciones de "unit"/"units". Todas son contenido legítimo, no vocabulario editorial:
    - El término acuñado del autor "units of mind".
    - "units of thought", de Alan Watts.
    - La definición de Wilber "a holon is the unit of everything".
    - "a unit within the hierarchy", en la cita sobre la célula cancerosa, y "dominating unit" en la tabla.
    - "its basic unit (the holon)".

**Palabras finales:** 29.825 (antes 29.356).
