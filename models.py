from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from database import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    slug = Column(String(255), unique=True, index=True, nullable=False)
    excerpt = Column(Text, nullable=False)
    content = Column(Text, nullable=False)  # HTML semántico estricto renderizado con | safe
    category_slug = Column(String(100), nullable=False, index=True)
    author = Column(String(100), default="Andrés", nullable=False)
    featured_image = Column(String(255), nullable=False)  # ej. /static/img/foto.jpg
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    status = Column(String(50), default="Publicado", nullable=False)  # Publicado / Borrador

    def __repr__(self):
        return f"<Article {self.id}: {self.title}>"
