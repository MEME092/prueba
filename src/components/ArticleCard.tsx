import React, { useMemo } from 'react';
import { Article } from '../types';
import { CATEGORIES } from '../data/seedArticles';
import { Clock, CheckCircle2, ArrowRight, ShieldCheck, BookOpen } from 'lucide-react';

interface ArticleCardProps {
  article: Article;
  onSelect: (article: Article) => void;
  featured?: boolean;
}

export const ArticleCard: React.FC<ArticleCardProps> = ({ article, onSelect, featured = false }) => {
  const category = CATEGORIES.find(c => c.slug === article.category_slug);

  const wordCount = useMemo(() => {
    if (!article.content) return 0;
    const matches = article.content.match(/\b\w+\b/g);
    return matches ? matches.length : 0;
  }, [article.content]);

  const getCategoryBadgeClass = (slug: string) => {
    switch (slug) {
      case 'tramites':
        return 'bg-emerald-50 text-emerald-800 border-emerald-200';
      case 'python-flet':
        return 'bg-indigo-50 text-indigo-800 border-indigo-200';
      case 'apps-moviles':
        return 'bg-amber-50 text-amber-800 border-amber-200';
      case 'herramientas':
        return 'bg-sky-50 text-sky-800 border-sky-200';
      default:
        return 'bg-slate-50 text-slate-700 border-slate-200';
    }
  };

  const formattedDate = new Date(article.created_at).toLocaleDateString('es-ES', {
    day: 'numeric',
    month: 'short',
    year: 'numeric'
  });

  return (
    <article 
      onClick={() => onSelect(article)}
      className={`group cursor-pointer flex flex-col bg-white rounded-2xl border border-slate-200/80 shadow-xs hover:shadow-xl hover:border-indigo-300 transition-all duration-300 overflow-hidden ${
        featured ? 'md:col-span-2 md:grid md:grid-cols-2 md:items-center' : ''
      }`}
    >
      {/* Contenedor de Imagen Destacada (Con relación de aspecto 16:9 fija para evitar deformación) */}
      <div className={`relative overflow-hidden bg-slate-950 ${featured ? 'h-full min-h-[260px]' : 'aspect-video w-full'}`}>
        <img
          src={article.featured_image}
          alt={article.title}
          loading="lazy"
          onError={(e) => {
            const target = e.currentTarget;
            if (!target.src.endsWith('/default-placeholder.svg')) {
              target.src = '/static/img/default-placeholder.svg';
            }
          }}
          className="w-full h-full object-cover transition-transform duration-500 ease-out group-hover:scale-105"
        />
        <div className="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-end p-4">
          <span className="text-white text-xs font-semibold flex items-center gap-1.5 drop-shadow-md">
            Ver tutorial paso a paso <ArrowRight className="w-3.5 h-3.5" />
          </span>
        </div>

        {/* Badge de Categoría sobre la imagen */}
        <div className="absolute top-3 left-3 flex flex-wrap gap-1.5">
          <span className={`inline-flex items-center px-2.5 py-1 rounded-md text-xs font-bold border backdrop-blur-md shadow-xs ${getCategoryBadgeClass(article.category_slug)}`}>
            {category?.name || article.category_slug}
          </span>
          {article.difficulty && (
            <span className="inline-flex items-center px-2 py-0.5 rounded-md text-[11px] font-semibold bg-white/90 text-slate-800 shadow-xs">
              {article.difficulty}
            </span>
          )}
        </div>

        {/* Sello de verificación E-E-A-T */}
        <div className="absolute top-3 right-3">
          <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-slate-900/85 text-emerald-400 backdrop-blur-xs border border-white/20 shadow-xs">
            <CheckCircle2 className="w-3 h-3 text-emerald-400" />
            <span>Probado 100%</span>
          </span>
        </div>
      </div>

      {/* Contenido textual de la tarjeta */}
      <div className="flex flex-col flex-1 p-5 md:p-6 justify-between">
        <div>
          <div className="flex flex-wrap items-center gap-2 text-xs text-slate-500 mb-2">
            <span>{formattedDate}</span>
            <span>•</span>
            <span className="flex items-center gap-1">
              <Clock className="w-3.5 h-3.5 text-slate-400" />
              {article.read_time_minutes || 12} min
            </span>
            {wordCount > 0 && (
              <>
                <span>•</span>
                <span className="inline-flex items-center gap-1 text-[11px] font-semibold text-emerald-700 bg-emerald-50 border border-emerald-200/80 px-1.5 py-0.5 rounded">
                  <BookOpen className="w-3 h-3 text-emerald-600" />
                  {wordCount >= 1500 ? `+${Math.floor(wordCount / 100) * 100} palabras` : `${wordCount} palabras`}
                </span>
              </>
            )}
          </div>

          <h3 className={`font-bold text-slate-900 group-hover:text-indigo-600 transition-colors line-clamp-2 leading-snug tracking-tight ${
            featured ? 'text-xl md:text-2xl mb-3' : 'text-lg mb-2'
          }`}>
            {article.title}
          </h3>

          <p className="text-slate-600 text-sm line-clamp-2 leading-relaxed mb-4">
            {article.excerpt}
          </p>
        </div>

        {/* Footer de la tarjeta con Autor */}
        <div className="pt-4 border-t border-slate-100 flex items-center justify-between">
          <div className="flex items-center gap-2.5">
            <div className="w-7 h-7 rounded-full bg-indigo-100 border border-indigo-200 text-indigo-700 font-bold text-xs flex items-center justify-center">
              A
            </div>
            <div className="text-xs">
              <span className="font-semibold text-slate-800">{article.author}</span>
              <span className="text-slate-500 block text-[11px]">Estudiante CUC Barranquilla</span>
            </div>
          </div>
          
          <span className="text-xs font-semibold text-indigo-600 flex items-center gap-1 group-hover:translate-x-1 transition-transform">
            Abrir tutorial <ArrowRight className="w-3 h-3" />
          </span>
        </div>
      </div>
    </article>
  );
};
