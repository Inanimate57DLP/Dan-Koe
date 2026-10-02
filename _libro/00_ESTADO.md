# 00 — ESTADO DEL PROYECTO

- **CORPUS_PATH resuelto:** `.` (raíz del repositorio). La ruta configurada `Transcripts YouTube Referentes/Dan Koe` no existe; los transcripts están en la raíz.
- **Directorio de trabajo:** `_libro/` (en la raíz)
- **Rama de trabajo:** `libro-maestro-dan-koe` (creada desde `origin/main`, commit 1396995)
- **Último commit:** 331d353 Fase 4: capítulo 14 redactado
- **Fase actual:** Fase 4 en curso — redacción de capítulos en inglés (15/40), 3 subagentes en paralelo; instrucciones en /tmp (regenerables con los scripts descritos en Notas).

## Números
- Archivos: 164 · Palabras del corpus: 1.095.022 · Lotes: 27 (ver `01b_lotes.md`)

## Fase 1 — lotes extraídos
- lote-001: 158 unidades ✔
- lote-002: 136 unidades ✔
- lote-003: 261 unidades ✔
- lote-004: 166 unidades ✔
- lote-005: 142 unidades ✔
- lote-006: 193 unidades ✔
- lote-007: 220 unidades ✔
- lote-008: 196 unidades ✔
- lote-009: 270 unidades ✔
- lote-010: 366 unidades ✔
- lote-011: 240 unidades ✔
- lote-012: 234 unidades ✔
- lote-013: 248 unidades ✔
- lote-014: 200 unidades ✔
- lote-015: 213 unidades ✔
- lote-016: 299 unidades ✔
- lote-017: 236 unidades ✔
- lote-018: 198 unidades ✔
- lote-019: 171 unidades ✔
- lote-020: 200 unidades ✔
- lote-021: 231 unidades ✔
- lote-022: 232 unidades ✔
- lote-023: 273 unidades ✔
- lote-024: 244 unidades ✔
- lote-025: 225 unidades ✔
- lote-026: 271 unidades ✔
- lote-027: 264 unidades ✔
- **Total parcial:** 6087 unidades en 27/27 lotes

## Fase 4 — capítulos escritos
- cap-01.md: 42937 palabras, 211 IDs en COBERTURA ✔
- cap-02.md: 38722 palabras, 215 IDs en COBERTURA ✔
- cap-03.md: 33183 palabras, 169 IDs en COBERTURA ✔
- cap-04.md: 38742 palabras, 194 IDs en COBERTURA ✔
- cap-05.md: 25186 palabras, 119 IDs en COBERTURA ✔
- cap-06.md: 36932 palabras, 172 IDs en COBERTURA ✔
- cap-07.md: 36700 palabras, 157 IDs en COBERTURA ✔
- cap-08.md: 38099 palabras, 171 IDs en COBERTURA ✔
- cap-09.md: 27748 palabras, 123 IDs en COBERTURA ✔
- cap-10.md: 40009 palabras, 193 IDs en COBERTURA ✔
- cap-11.md: 29398 palabras, 116 IDs en COBERTURA ✔
- cap-12.md: 31100 palabras, 160 IDs en COBERTURA ✔
- cap-13.md: 30738 palabras, 136 IDs en COBERTURA ✔
- cap-14.md: 37201 palabras, 192 IDs en COBERTURA ✔
- cap-15.md: 41518 palabras, 202 IDs en COBERTURA ✔
- **Total:** 15/40 capítulos

## Notas
- Herramientas para reanudar: `_libro/99_herramientas/` contiene las plantillas de prompts (extracción, etiquetado, consolidación, síntesis, arquitectura, redacción) y los scripts (index.py → units.json; bytheme.py/split.py → 02c; gather.py → 02e; expand.py/material.py → 04b_material y chapters.json). Los scripts usan rutas en /tmp/claude-0; si la sesión se reinicia, copia los .json y .py de 99_herramientas a /tmp/claude-0 y regenera. Para redactar un capítulo NN: rellenar `write_prompt.txt` ([N], [NN], [TITULO], [IDS] desde chapters.json, [PALABRAS]).
- Etiquetas: los capítulos 01–04 pueden usar marcas en español o inglés (Fuente/Source, Contexto complementario/Complementary context, Ejercicios/Exercises); se normalizan en el ensamblaje.
