import os
import secrets
import shutil
import uuid
from datetime import datetime
from typing import Optional

from fastapi import FastAPI, Request, Form, File, UploadFile, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.responses import HTMLResponse, RedirectResponse, PlainTextResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from models import Article

# Crear tablas en SQLite tecnologia_gente_normal.db si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Tecnología para Gente Normal",
    description="Blog tecnológico práctico de Andrés (CUC)."
)

# Montar directamente los assets originales del frontend Vite
app.mount("/static", StaticFiles(directory="public/static"), name="static")

if os.path.isdir("dist/assets"):
    app.mount("/assets", StaticFiles(directory="dist/assets"), name="assets")

# Configurar motor de plantillas Jinja2
templates = Jinja2Templates(directory="templates")

security = HTTPBasic()
ADMIN_USERNAME = "andres"
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "CambiaEstaClaveAdmin-2026!Segura")


def verify_admin(credentials: HTTPBasicCredentials = Depends(security)):
    valid_username = secrets.compare_digest(credentials.username, ADMIN_USERNAME)
    valid_password = secrets.compare_digest(credentials.password, ADMIN_PASSWORD)

    if not (valid_username and valid_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de administrador incorrectas",
            headers={"WWW-Authenticate": "Basic"},
        )

    return credentials.username

# Categorías definidas con metadatos
CATEGORIES = {
    "tramites": {
        "name": "Trámites Digitales",
        "description": "Guías paso a paso para realizar trámites gubernamentales y universitarios en Colombia por internet sin intermediarios."
    },
    "python-flet": {
        "name": "Python & Flet",
        "description": "Tutoriales directos de programación práctica, interfaces gráficas multiplataforma con Flet y automatización con Python."
    },
    "apps-moviles": {
        "name": "Apps Móviles",
        "description": "Optimización de teléfonos Android, eliminación de bloatware, privacidad y trucos reales sin instalar porquerías."
    },
    "herramientas": {
        "name": "Herramientas",
        "description": "Software libre, utilidades de Windows y Linux para estudiantes y profesionales que quieren productividad sin pagar licencias abusivas."
    }
}

# -------------------------------------------------------------------
# RUTAS PÚBLICAS OPTIMIZADAS PARA SEO
# -------------------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request, db: Session = Depends(get_db)):
    articles = (
        db.query(Article)
        .filter(Article.status == "Publicado")
        .order_by(Article.created_at.desc())
        .all()
    )
    recent_articles = articles[:4]

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "recent_articles": recent_articles,
            "articles": articles,
            "categories": CATEGORIES,
        },
    )

@app.get("/categoria/{category_slug}", response_class=HTMLResponse)
async def category_view(request: Request, category_slug: str, db: Session = Depends(get_db)):
    if category_slug not in CATEGORIES:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")

    articles = (
        db.query(Article)
        .filter(Article.category_slug == category_slug, Article.status == "Publicado")
        .order_by(Article.created_at.desc())
        .all()
    )
    return templates.TemplateResponse(
        request=request,
        name="category.html",
        context={
            "request": request,
            "articles": articles,
            "category_slug": category_slug,
            "category": CATEGORIES[category_slug],
        },
    )

@app.get("/articulo/{slug}", response_class=HTMLResponse)
async def article_detail(request: Request, slug: str, db: Session = Depends(get_db)):
    article = db.query(Article).filter(Article.slug == slug, Article.status == "Publicado").first()
    if not article:
        raise HTTPException(status_code=404, detail="Artículo no encontrado")
    
    # Artículos relacionados en la misma categoría
    related_articles = (
        db.query(Article)
        .filter(Article.category_slug == article.category_slug, Article.id != article.id, Article.status == "Publicado")
        .limit(3)
        .all()
    )

    category = CATEGORIES.get(article.category_slug, {"name": article.category_slug})

    return templates.TemplateResponse(
        request=request,
        name="article.html",
        context={
            "request": request,
            "article": article,
            "related_articles": related_articles,
            "category": category,
        },
    )

# -------------------------------------------------------------------
# PÁGINAS LEGALES
# -------------------------------------------------------------------

@app.get("/sobre-el-autor", response_class=HTMLResponse)
async def about_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="legal/about.html",
        context={"request": request},
    )

@app.get("/politica-de-privacidad", response_class=HTMLResponse)
async def privacy_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="legal/privacy.html",
        context={"request": request},
    )

@app.get("/privacidad")
async def privacy_alias():
    return RedirectResponse(url="/politica-de-privacidad", status_code=status.HTTP_301_MOVED_PERMANENTLY)

@app.get("/politica-de-cookies", response_class=HTMLResponse)
async def cookies_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="legal/cookies.html",
        context={"request": request},
    )

@app.get("/cookies")
async def cookies_alias():
    return RedirectResponse(url="/politica-de-cookies", status_code=status.HTTP_301_MOVED_PERMANENTLY)

@app.get("/aviso-legal", response_class=HTMLResponse)
async def terms_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="legal/terms.html",
        context={"request": request},
    )

@app.get("/terminos-y-condiciones")
async def terms_alias():
    return RedirectResponse(url="/aviso-legal", status_code=status.HTTP_301_MOVED_PERMANENTLY)

@app.get("/contacto", response_class=HTMLResponse)
async def contact_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="legal/contact.html",
        context={"request": request},
    )

# -------------------------------------------------------------------
# ENDPOINTS TÉCNICOS DE INDEXACIÓN (ads.txt, sitemap.xml, robots.txt)
# -------------------------------------------------------------------

@app.get("/ads.txt", response_class=PlainTextResponse)
async def ads_txt():
    """
    Archivo ads.txt para declarar el proveedor de publicidad del sitio.
    Reemplazar pub-XXXXXXXXXXXXXXXX con tu código real recibido tras la aprobación.
    """
    return "google.com, pub-1234567890123456, DIRECT, f08c47fec0942fa0\n"

@app.get("/robots.txt", response_class=PlainTextResponse)
async def robots_txt(request: Request):
    host = request.headers.get("host", "tecnologiaparagentenormal.com")
    protocol = "https" if "https" in str(request.url) else "http"
    return f"""User-agent: *
Allow: /
Disallow: /admin/
Disallow: /static/img/tmp/

Sitemap: {protocol}://{host}/sitemap.xml
"""

@app.get("/sitemap.xml")
async def sitemap_xml(request: Request, db: Session = Depends(get_db)):
    articles = db.query(Article).filter(Article.status == "Publicado").all()
    host = request.headers.get("host", "tecnologiaparagentenormal.com")
    protocol = "https" if "https" in str(request.url) else "http"
    
    xml_content = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml_content.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    
    # URL principal
    xml_content.append(f"""  <url>
    <loc>{protocol}://{host}/</loc>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>""")

    # Páginas legales
    for legal in ["sobre-el-autor", "politica-de-privacidad", "politica-de-cookies", "aviso-legal", "contacto"]:
        xml_content.append(f"""  <url>
    <loc>{protocol}://{host}/{legal}</loc>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>""")

    # Artículos publicados
    for art in articles:
        date_str = art.created_at.strftime("%Y-%m-%d")
        xml_content.append(f"""  <url>
    <loc>{protocol}://{host}/articulo/{art.slug}</loc>
    <lastmod>{date_str}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>""")

    xml_content.append('</urlset>')
    return Response(content="\n".join(xml_content), media_type="application/xml")

# -------------------------------------------------------------------
# PANEL DE ADMINISTRACIÓN (/admin) & TAREA 1 (CRUD)
# -------------------------------------------------------------------

@app.get("/admin", response_class=HTMLResponse, dependencies=[Depends(verify_admin)])
async def admin_dashboard(request: Request, db: Session = Depends(get_db)):
    articles = db.query(Article).order_by(Article.created_at.desc()).all()
    return templates.TemplateResponse(
        request=request,
        name="admin/index.html",
        context={
            "request": request,
            "articles": articles,
            "categories": CATEGORIES,
        },
    )

@app.get("/admin/nuevo", response_class=HTMLResponse, dependencies=[Depends(verify_admin)])
async def new_article_view(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="admin/new_article.html",
        context={"request": request, "categories": CATEGORIES},
    )

@app.post("/admin/nuevo", dependencies=[Depends(verify_admin)])
async def create_article(
    title: str = Form(...),
    slug: str = Form(...),
    excerpt: str = Form(...),
    content: str = Form(...),
    category_slug: str = Form(...),
    author: str = Form("Andrés"),
    status: str = Form("Publicado"),
    featured_image: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    clean_filename = f"{uuid.uuid4().hex[:8]}_{featured_image.filename.replace(' ', '_')}"
    file_location = f"public/static/img/{clean_filename}"
    
    with open(file_location, "wb+") as buffer:
        shutil.copyfileobj(featured_image.file, buffer)

    new_article = Article(
        title=title,
        slug=slug,
        excerpt=excerpt,
        content=content,
        category_slug=category_slug,
        author=author,
        status=status,
        featured_image=f"/static/img/{clean_filename}",
        created_at=datetime.utcnow()
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return RedirectResponse(url="/admin?created=true", status_code=status.HTTP_303_SEE_OTHER)

# ===================================================================
# TAREA 1: VISTA Y RUTA DE EDICIÓN DE ARTÍCULOS
# ===================================================================

@app.get("/admin/edit/{article_id}", response_class=HTMLResponse, dependencies=[Depends(verify_admin)])
async def edit_article_view(
    request: Request,
    article_id: int,
    db: Session = Depends(get_db),
):
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=404, detail="El artículo no existe")
    
    return templates.TemplateResponse(
        request=request,
        name="admin/edit_article.html",
        context={
            "request": request,
            "article": article,
            "categories": CATEGORIES,
        },
    )

@app.post("/admin/edit/{article_id}", dependencies=[Depends(verify_admin)])
async def update_article(
    article_id: int,
    title: str = Form(...),
    slug: str = Form(...),
    excerpt: str = Form(...),
    content: str = Form(...),
    category_slug: str = Form(...),
    author: str = Form(...),
    status: str = Form(...),
    featured_image: UploadFile = File(None),
    db: Session = Depends(get_db),
):
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Artículo no encontrado")

    article.title = title
    article.slug = slug
    article.excerpt = excerpt
    article.content = content
    article.category_slug = category_slug
    article.author = author
    article.status = status

    # Reemplazo seguro de imagen
    if featured_image and featured_image.filename:
        ext = os.path.splitext(featured_image.filename)[1].lower()
        if ext in [".jpg", ".jpeg", ".png", ".webp"]:
            clean_filename = f"{uuid.uuid4().hex[:8]}_{featured_image.filename.replace(' ', '_')}"
            file_location = f"public/static/img/{clean_filename}"
            
            with open(file_location, "wb+") as buffer:
                shutil.copyfileobj(featured_image.file, buffer)
            
            article.featured_image = f"/static/img/{clean_filename}"

    db.commit()
    db.refresh(article)
    return RedirectResponse(url="/admin?updated=true", status_code=status.HTTP_303_SEE_OTHER)

@app.post("/admin/delete/{article_id}", dependencies=[Depends(verify_admin)])
async def delete_article(
    article_id: int,
    db: Session = Depends(get_db),
):
    article = db.query(Article).filter(Article.id == article_id).first()
    if article:
        db.delete(article)
        db.commit()
    return RedirectResponse(url="/admin?deleted=true", status_code=status.HTTP_303_SEE_OTHER)
