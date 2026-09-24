# -*- coding: utf-8 -*-
"""
Ensamblador maestro para inyectar los contenidos de más de 1.500 palabras
en todos los 26 artículos de src/data/seedArticles.ts
"""

import json
import re

from generate_tramites import TRAMITES_CONTENT
from generate_python_flet import PYTHON_FLET_CONTENT
from generate_android_adb import ANDROID_ADB_CONTENT
from generate_herramientas import HERRAMIENTAS_CONTENT

# Consolidar todos los 26 contenidos
ALL_CONTENTS = {}
ALL_CONTENTS.update(TRAMITES_CONTENT)       # IDs 1 a 7
ALL_CONTENTS.update(PYTHON_FLET_CONTENT)    # IDs 8 a 13
ALL_CONTENTS.update(ANDROID_ADB_CONTENT)    # IDs 14 a 19
ALL_CONTENTS.update(HERRAMIENTAS_CONTENT)   # IDs 20 a 26

print(f"Total de artículos con contenido expandido preparado: {len(ALL_CONTENTS)}")

# Leer el archivo original src/data/seedArticles.ts
with open('src/data/seedArticles.ts', 'r', encoding='utf-8') as f:
    original_code = f.read()

# Extraer el bloque previo a INITIAL_ARTICLES
prefix_match = re.search(r'([\s\S]*?export const INITIAL_ARTICLES:\s*Article\[\]\s*=\s*)(\[[\s\S]*?\]);\s*$', original_code)
if not prefix_match:
    raise ValueError("No se pudo localizar el array INITIAL_ARTICLES en src/data/seedArticles.ts")

header_code = prefix_match.group(1)
raw_articles_json = prefix_match.group(2)

articles = json.loads(raw_articles_json)
print(f"Total de artículos cargados desde seedArticles.ts: {len(articles)}")

verification_results = []

for article in articles:
    art_id = article["id"]
    if art_id in ALL_CONTENTS:
        new_content = ALL_CONTENTS[art_id]
        article["content"] = new_content
        
        # Conteo de palabras sobre el texto despojado de etiquetas HTML
        clean_text = re.sub(r'<[^>]+>', ' ', new_content)
        words = len(re.findall(r'\b\w+\b', clean_text))
        
        # Calcular tiempo de lectura estimado (aprox. 130 palabras por minuto para guías técnicas)
        article["read_time_minutes"] = max(12, round(words / 130))
        
        verification_results.append((art_id, article["title"], words))
        assert words >= 1500, f"Error: Artículo ID {art_id} solo tiene {words} palabras (< 1500)"
    else:
        raise ValueError(f"Falta contenido para el artículo con ID {art_id}")

print("\n--- RESULTADOS DE VERIFICACIÓN DE PALABRAS POR ARTÍCULO ---")
for art_id, title, count in verification_results:
    print(f"✓ Artículo #{art_id:02d}: {count:4d} palabras | {title[:50]}...")

# Escribir el nuevo archivo src/data/seedArticles.ts
updated_json = json.dumps(articles, ensure_ascii=False, indent=2)
new_file_content = header_code + updated_json + ";\n"

with open('src/data/seedArticles.ts', 'w', encoding='utf-8') as f:
    f.write(new_file_content)

print(f"\n¡Éxito total! Se actualizaron {len(articles)} artículos en src/data/seedArticles.ts.")
print("Todos los 26 artículos cumplen estrictamente la condición de MÍNIMO 1.500 palabras.")
