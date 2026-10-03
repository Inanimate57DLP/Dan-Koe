# 00 — ESTADO DEL PROYECTO

- **CORPUS_PATH resuelto:** `.` (raíz del repositorio). La ruta configurada `Transcripts YouTube Referentes/Dan Koe` no existe; los transcripts están en la raíz.
- **Directorio de trabajo:** `_libro/` (en la raíz)
- **Rama de trabajo:** `libro-maestro-dan-koe` (creada desde `origin/main`, commit 1396995)
- **Último commit:** c62d1f7 Fase 5: auditoría capítulos 03-04
- **Fase actual:** Fase 5 COMPLETA (iteración 1: 4 pérdidas + 218 menores corregidos; iteración 2: verificación dirigida — 3 verificadas, 1 corregida (cap. 40), 5 frases residuales y 1 cita corregidas; sin pérdidas materiales pendientes). Fase 6 COMPLETA (`07_libro_en.md`). Fase 7 en curso: léxico de traducción (partes 1–3 listas; 4 en curso).

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
- cap-16.md: 31927 palabras, 141 IDs en COBERTURA ✔
- cap-17.md: 39242 palabras, 156 IDs en COBERTURA ✔
- cap-18.md: 29829 palabras, 114 IDs en COBERTURA ✔
- cap-19.md: 31957 palabras, 156 IDs en COBERTURA ✔
- cap-20.md: 28522 palabras, 126 IDs en COBERTURA ✔
- cap-21.md: 26818 palabras, 136 IDs en COBERTURA ✔
- cap-22.md: 29083 palabras, 128 IDs en COBERTURA ✔
- cap-23.md: 31963 palabras, 142 IDs en COBERTURA ✔
- cap-24.md: 31645 palabras, 145 IDs en COBERTURA ✔
- cap-25.md: 41140 palabras, 204 IDs en COBERTURA ✔
- cap-26.md: 39900 palabras, 210 IDs en COBERTURA ✔
- cap-27.md: 32319 palabras, 143 IDs en COBERTURA ✔
- cap-28.md: 33378 palabras, 163 IDs en COBERTURA ✔
- cap-29.md: 30362 palabras, 148 IDs en COBERTURA ✔
- cap-30.md: 29203 palabras, 149 IDs en COBERTURA ✔
- cap-31.md: 28445 palabras, 125 IDs en COBERTURA ✔
- cap-32.md: 26227 palabras, 110 IDs en COBERTURA ✔
- cap-33.md: 24035 palabras, 111 IDs en COBERTURA ✔
- cap-34.md: 29661 palabras, 128 IDs en COBERTURA ✔
- cap-35.md: 33371 palabras, 121 IDs en COBERTURA ✔
- cap-36.md: 32772 palabras, 152 IDs en COBERTURA ✔
- cap-37.md: 30140 palabras, 119 IDs en COBERTURA ✔
- cap-38.md: 29273 palabras, 125 IDs en COBERTURA ✔
- cap-39.md: 33212 palabras, 177 IDs en COBERTURA ✔
- cap-40.md: 29098 palabras, 141 IDs en COBERTURA ✔
- **Total:** 40/40 capítulos

## Notas
- Herramientas para reanudar: `_libro/99_herramientas/` contiene las plantillas de prompts (extracción, etiquetado, consolidación, síntesis, arquitectura, redacción) y los scripts (index.py → units.json; bytheme.py/split.py → 02c; gather.py → 02e; expand.py/material.py → 04b_material y chapters.json). Los scripts usan rutas en /tmp/claude-0; si la sesión se reinicia, copia los .json y .py de 99_herramientas a /tmp/claude-0 y regenera. Para redactar un capítulo NN: rellenar `write_prompt.txt` ([N], [NN], [TITULO], [IDS] desde chapters.json, [PALABRAS]).
- Etiquetas: los capítulos 01–04 pueden usar marcas en español o inglés (Fuente/Source, Contexto complementario/Complementary context, Ejercicios/Exercises); se normalizan en el ensamblaje.
