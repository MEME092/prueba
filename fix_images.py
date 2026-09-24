import html
import os
import re
from pathlib import Path

from database import SessionLocal
from models import Article

STATIC_ROOT = Path("public/static")
IMAGE_ROOT = STATIC_ROOT / "img"


def image_path(featured_image: str) -> Path:
    relative_path = featured_image.removeprefix("/static/")
    return STATIC_ROOT / relative_path


def svg_text_lines(title: str, max_length: int = 42) -> list[str]:
    words = title.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if current and len(candidate) > max_length:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines[:5]


def generate_svg(title: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    escaped_title = html.escape(title)
    lines = svg_text_lines(title)
    title_markup = "".join(
        f'<tspan x="600" dy="{58 if index else 0}">{html.escape(line)}</tspan>'
        for index, line in enumerate(lines)
    )
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 675" role="img" aria-labelledby="title desc">
  <title id="title">{escaped_title}</title>
  <desc id="desc">Imagen técnica del artículo {escaped_title}</desc>
  <defs>
    <linearGradient id="background" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0f172a"/>
      <stop offset="1" stop-color="#1e3a8a"/>
    </linearGradient>
    <linearGradient id="border" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#38bdf8"/>
      <stop offset="1" stop-color="#34d399"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="675" fill="url(#background)"/>
  <circle cx="1040" cy="95" r="190" fill="#38bdf8" opacity=".08"/>
  <circle cx="130" cy="610" r="250" fill="#34d399" opacity=".06"/>
  <rect x="42" y="42" width="1116" height="591" rx="28" fill="none" stroke="url(#border)" stroke-width="3" opacity=".65"/>
  <path d="M120 520h960M170 155h860" stroke="#94a3b8" stroke-width="1" opacity=".2"/>
  <text x="600" y="275" text-anchor="middle" fill="#f8fafc" font-family="Arial, Helvetica, sans-serif" font-size="42" font-weight="700">{title_markup}</text>
  <rect x="365" y="515" width="470" height="52" rx="26" fill="#0f172a" stroke="#38bdf8" stroke-opacity=".5"/>
  <text x="600" y="548" text-anchor="middle" fill="#a7f3d0" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="600">Probado en Laboratorio CUC</text>
</svg>
'''
    destination.write_text(svg, encoding="utf-8")


def main() -> None:
    if not STATIC_ROOT.is_dir():
        raise FileNotFoundError(f"No existe la carpeta estática montada: {STATIC_ROOT}")

    db = SessionLocal()
    try:
        articles = db.query(Article).order_by(Article.id).all()
        missing: list[tuple[str, Path]] = []
        for article in articles:
            destination = image_path(article.featured_image)
            if not os.path.exists(destination):
                missing.append((article.title, destination))
                generate_svg(article.title, destination)

        regenerated = [destination for _, destination in missing if os.path.exists(destination)]
        print(f"Artículos escaneados: {len(articles)}")
        print(f"Imágenes faltantes detectadas: {len(missing)}")
        print(f"Imágenes regeneradas con éxito: {len(regenerated)}")
        if missing:
            for title, destination in missing:
                print(f"- {title} -> {destination}")
    finally:
        db.close()


if __name__ == "__main__":
    main()
