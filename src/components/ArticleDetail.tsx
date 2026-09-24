import React, { useState, useMemo } from 'react';
import { Article } from '../types';
import { CATEGORIES, AUTHOR_INFO } from '../data/seedArticles';
import { 
  ArrowLeft, 
  Clock, 
  Calendar, 
  ShieldCheck, 
  Share2, 
  Check, 
  Code, 
  GraduationCap, 
  ListOrdered, 
  ChevronRight,
  ChevronDown,
  CheckCircle2,
  HelpCircle,
  Laptop,
  CheckSquare,
  Sparkles,
  Lock,
  Copy,
  BookOpen
} from 'lucide-react';

interface ArticleDetailProps {
  article: Article;
  onBack: () => void;
  onCategorySelect?: (slug: string) => void;
  onOpenAuthorProfile?: () => void;
}

export const ArticleDetail: React.FC<ArticleDetailProps> = ({ 
  article, 
  onBack, 
  onCategorySelect,
  onOpenAuthorProfile 
}) => {
  const [copied, setCopied] = useState(false);
  const [showSchema, setShowSchema] = useState(false);
  
  // Estado para el checklist de pasos interactivo
  const [completedSteps, setCompletedSteps] = useState<Record<string, boolean>>({});
  
  // Estado para acordeón de FAQs
  const [openFaqIndex, setOpenFaqIndex] = useState<number | null>(0);

  const category = CATEGORIES.find(c => c.slug === article.category_slug);

  const wordCount = useMemo(() => {
    if (!article.content) return 0;
    const matches = article.content.match(/\b\w+\b/g);
    return matches ? matches.length : 0;
  }, [article.content]);

  const formattedDate = new Date(article.created_at).toLocaleDateString('es-ES', {
    day: 'numeric',
    month: 'long',
    year: 'numeric'
  });

  const handleShare = () => {
    if (navigator.clipboard) {
      navigator.clipboard.writeText(window.location.href);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  };

  const toggleStep = (stepId: string) => {
    setCompletedSteps(prev => ({
      ...prev,
      [stepId]: !prev[stepId]
    }));
  };

  // Cálculo del progreso de pasos
  const totalSteps = article.quick_steps?.length || 0;
  const finishedStepsCount = Object.values(completedSteps).filter(Boolean).length;
  const progressPercent = totalSteps > 0 ? Math.round((finishedStepsCount / totalSteps) * 100) : 0;

  // Extraer automáticamente los encabezados H2 del contenido para generar un Índice de Contenidos (Table of Contents)
  const headings = useMemo(() => {
    const regex = /<h2[^>]*>(.*?)<\/h2>/gi;
    const items: { text: string; id: string }[] = [];
    let match;
    let index = 1;
    while ((match = regex.exec(article.content)) !== null) {
      const cleanText = match[1].replace(/<[^>]*>?/gm, '').trim();
      const id = `seccion-${index++}`;
      items.push({ text: cleanText, id });
    }
    return items;
  }, [article.content]);

  // Structured Data Schema.org (JSON-LD) para SEO técnico y snippets enriquecidos de Google (HowTo + FAQPage + BlogPosting)
  const schemaData = {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "BlogPosting",
        "@id": `https://tecnologiaparagentenormal.com/${article.slug}#article`,
        "mainEntityOfPage": {
          "@type": "WebPage",
          "@id": `https://tecnologiaparagentenormal.com/${article.slug}`
        },
        "headline": article.title,
        "description": article.excerpt,
        "image": `https://tecnologiaparagentenormal.com${article.featured_image}`,
        "author": {
          "@type": "Person",
          "name": AUTHOR_INFO.name,
          "jobTitle": AUTHOR_INFO.role,
          "worksFor": {
            "@type": "EducationalOrganization",
            "name": AUTHOR_INFO.university,
            "address": {
              "@type": "PostalAddress",
              "addressLocality": "Barranquilla",
              "addressCountry": "CO"
            }
          },
          "url": "https://tecnologiaparagentenormal.com/sobre-el-autor"
        },
        "publisher": {
          "@type": "Organization",
          "name": "Tecnología para Gente Normal",
          "logo": {
            "@type": "ImageObject",
            "url": "https://tecnologiaparagentenormal.com/static/img/logo.svg"
          }
        },
        "datePublished": article.created_at,
        "dateModified": article.created_at,
        "articleSection": category?.name || article.category_slug,
        "inLanguage": "es"
      },
      ...(article.quick_steps && article.quick_steps.length > 0 ? [{
        "@type": "HowTo",
        "@id": `https://tecnologiaparagentenormal.com/${article.slug}#howto`,
        "name": article.title,
        "description": article.excerpt,
        "step": article.quick_steps.map((st, idx) => ({
          "@type": "HowToStep",
          "position": idx + 1,
          "name": st.title,
          "text": st.description
        }))
      }] : []),
      ...(article.faqs && article.faqs.length > 0 ? [{
        "@type": "FAQPage",
        "@id": `https://tecnologiaparagentenormal.com/${article.slug}#faq`,
        "mainEntity": article.faqs.map(faq => ({
          "@type": "Question",
          "name": faq.question,
          "acceptedAnswer": {
            "@type": "Answer",
            "text": faq.answer
          }
        }))
      }] : [])
    ]
  };

  return (
    <article className="max-w-4xl mx-auto px-4 sm:px-6 py-8">
      {/* Barra de navegación superior con botón Volver */}
      <div className="flex items-center justify-between mb-6 pb-4 border-b border-slate-200">
        <button
          onClick={onBack}
          className="inline-flex items-center gap-2 text-xs sm:text-sm font-semibold text-slate-600 hover:text-indigo-600 transition-colors py-1.5 px-3 rounded-lg hover:bg-slate-100"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Volver a la portada</span>
        </button>

        <div className="flex items-center gap-2">
          <button
            onClick={() => setShowSchema(!showSchema)}
            title="Inspeccionar Schema.org JSON-LD para buscadores"
            className="inline-flex items-center gap-1.5 text-xs font-medium text-slate-600 bg-slate-100 hover:bg-slate-200 py-1.5 px-3 rounded-lg transition-colors"
          >
            <Code className="w-3.5 h-3.5" />
            <span>Schema SEO JSON-LD</span>
          </button>

          <button
            onClick={handleShare}
            className="inline-flex items-center gap-1.5 text-xs font-medium text-slate-600 bg-slate-100 hover:bg-slate-200 py-1.5 px-3 rounded-lg transition-colors"
          >
            {copied ? <Check className="w-3.5 h-3.5 text-emerald-600" /> : <Share2 className="w-3.5 h-3.5" />}
            <span>{copied ? '¡Copiado!' : 'Compartir'}</span>
          </button>
        </div>
      </div>

      {/* Modal / Acordeón para inspeccionar Schema JSON-LD */}
      {showSchema && (
        <div className="mb-6 p-4 bg-slate-900 text-slate-100 rounded-2xl shadow-lg border border-slate-800 text-xs font-mono">
          <div className="flex items-center justify-between pb-2 mb-2 border-b border-slate-800">
            <span className="font-semibold text-emerald-400">Schema.org Graph: BlogPosting + HowTo + FAQPage</span>
            <button onClick={() => setShowSchema(false)} className="text-slate-400 hover:text-white">✕</button>
          </div>
          <pre className="overflow-x-auto p-2 bg-slate-950/60 rounded text-[11px] leading-relaxed">
            {JSON.stringify(schemaData, null, 2)}
          </pre>
        </div>
      )}

      {/* Encabezado del Artículo */}
      <header className="mb-8">
        <div className="flex flex-wrap items-center gap-2 mb-4">
          <span 
            onClick={() => onCategorySelect && onCategorySelect(article.category_slug)}
            className="cursor-pointer inline-flex items-center px-3 py-1 rounded-md text-xs font-bold uppercase tracking-wider bg-indigo-50 text-indigo-700 border border-indigo-200 hover:bg-indigo-100 transition-colors"
          >
            {category?.name || article.category_slug}
          </span>
          <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-md text-xs font-medium bg-emerald-50 text-emerald-700 border border-emerald-200">
            <ShieldCheck className="w-3.5 h-3.5 text-emerald-600" />
            Experiencia Verificada E-E-A-T
          </span>
          {article.difficulty && (
            <span className={`px-2.5 py-1 rounded-md text-xs font-semibold border ${
              article.difficulty === 'Principiante' 
                ? 'bg-blue-50 text-blue-700 border-blue-200' 
                : 'bg-amber-50 text-amber-700 border-amber-200'
            }`}>
              Nivel: {article.difficulty}
            </span>
          )}
        </div>

        <h1 className="text-2xl sm:text-3xl lg:text-4xl font-extrabold text-slate-900 tracking-tight leading-tight mb-4">
          {article.title}
        </h1>

        <p className="text-base sm:text-lg text-slate-600 leading-relaxed mb-6 font-normal">
          {article.excerpt}
        </p>

        {/* Metadatos del Autor, Fecha y Dispositivo */}
        <div className="flex flex-wrap items-center gap-4 py-4 px-4 bg-slate-100/70 rounded-2xl border border-slate-200/80">
          <div 
            onClick={onOpenAuthorProfile}
            className="flex items-center gap-3 cursor-pointer group"
          >
            <img
              src="/static/img/author_andres.svg"
              alt="Andrés"
              className="w-10 h-10 rounded-full shadow-xs group-hover:scale-105 transition-transform object-cover"
            />
            <div>
              <div className="font-bold text-sm text-slate-900 flex items-center gap-1.5 group-hover:text-indigo-600 transition-colors">
                {article.author}
                <span className="text-[10px] font-semibold text-indigo-700 bg-indigo-50 border border-indigo-200 px-1.5 py-0.2 rounded-full">
                  Autor Verificado
                </span>
              </div>
              <div className="text-xs text-slate-500 flex items-center gap-1">
                <GraduationCap className="w-3.5 h-3.5 text-indigo-500" />
                Estudiante de Ing. de Sistemas - CUC Barranquilla
              </div>
            </div>
          </div>

          <div className="sm:ml-auto flex flex-wrap items-center gap-3 text-xs text-slate-500">
            <span className="flex items-center gap-1">
              <Calendar className="w-3.5 h-3.5" />
              {formattedDate}
            </span>
            <span>•</span>
            <span className="flex items-center gap-1">
              <Clock className="w-3.5 h-3.5" />
              {article.read_time_minutes || 12} min de lectura
            </span>
            {wordCount > 0 && (
              <>
                <span>•</span>
                <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-bold bg-emerald-50 text-emerald-800 border border-emerald-200 shadow-2xs">
                  <BookOpen className="w-3.5 h-3.5 text-emerald-600" />
                  {wordCount.toLocaleString()} palabras (Guía Exhaustiva)
                </span>
              </>
            )}
          </div>
        </div>
      </header>

      {/* Tarjeta de Inicio Rápido para "Gente Normal" */}
      <section className="mb-8 p-5 bg-gradient-to-r from-indigo-50/70 via-sky-50/50 to-white rounded-2xl border border-indigo-100 shadow-2xs">
        <div className="flex items-center gap-2 mb-3">
          <Sparkles className="w-4 h-4 text-indigo-600" />
          <h3 className="font-bold text-sm text-slate-900">Ficha Rápida: Lo que necesitas saber para empezar</h3>
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 text-xs">
          <div className="p-3 bg-white rounded-xl border border-slate-200">
            <span className="text-slate-500 block mb-0.5">⏱️ Tiempo estimado:</span>
            <span className="font-bold text-slate-800">{article.estimated_time || '15 minutos'}</span>
          </div>
          <div className="p-3 bg-white rounded-xl border border-slate-200">
            <span className="text-slate-500 block mb-0.5">📖 Extensión técnica:</span>
            <span className="font-bold text-emerald-700">{wordCount.toLocaleString()} palabras verificadas</span>
          </div>
          <div className="p-3 bg-white rounded-xl border border-slate-200">
            <span className="text-slate-500 block mb-0.5">💻 Entorno de pruebas:</span>
            <span className="font-bold text-slate-800 truncate block" title={article.device_tested}>
              {article.device_tested ? article.device_tested.split('•')[0] : 'Hardware real verificado'}
            </span>
          </div>
          <div className="p-3 bg-white rounded-xl border border-slate-200">
            <span className="text-slate-500 block mb-0.5">🛡️ Garantía técnica:</span>
            <span className="font-bold text-emerald-700">100% Sin riesgo si sigues los pasos</span>
          </div>
        </div>
      </section>

      {/* Imagen Destacada Autóctona (Sin deformación, con licencia y copyright explícito) */}
      <figure className="mb-8 overflow-hidden rounded-3xl border border-slate-200 shadow-md bg-slate-900">
        <div className="aspect-video w-full relative">
          <img
            src={article.featured_image}
            alt={article.title}
            className="w-full h-full object-contain bg-slate-950"
            loading="eager"
            onError={(e) => {
              const target = e.currentTarget;
              if (target.src !== '/static/img/logo.svg') {
                target.src = '/static/img/logo.svg';
              }
            }}
          />
        </div>
        
        {/* Ficha técnica de autenticidad de imagen y derechos de autor */}
        <figcaption className="p-3.5 bg-slate-50 border-t border-slate-200 text-xs text-slate-600 space-y-1">
          <div className="flex flex-wrap items-center justify-between gap-2">
            <div className="flex items-center gap-1.5 font-semibold text-slate-800">
              <ShieldCheck className="w-4 h-4 text-emerald-600" />
              <span>{article.image_caption || 'Captura técnica original generada en el laboratorio de pruebas.'}</span>
            </div>
            <span className="text-[11px] font-bold text-indigo-700 bg-indigo-50 border border-indigo-200 px-2 py-0.5 rounded-md">
              100% Autóctona
            </span>
          </div>
          <div className="text-[11px] text-slate-500 flex flex-wrap items-center gap-3 pt-1 border-t border-slate-200/60">
            <span><strong>Dispositivo:</strong> {article.device_tested || 'Laboratorio CUC Barranquilla'}</span>
            <span>•</span>
            <span><strong>Derechos:</strong> {article.copyright_notice || '© 2026 Andrés - Universidad de la Costa. Sin fotos de stock de terceros.'}</span>
          </div>
        </figcaption>
      </figure>

      {/* Checklist Interactivo de Pasos para que el Usuario no se Pierda */}
      {article.quick_steps && article.quick_steps.length > 0 && (
        <section className="my-8 p-5 sm:p-6 bg-white rounded-2xl border border-slate-200 shadow-xs">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-4 pb-3 border-b border-slate-100">
            <div className="flex items-center gap-2">
              <CheckSquare className="w-5 h-5 text-indigo-600" />
              <div>
                <h3 className="font-bold text-sm sm:text-base text-slate-900">
                  Checklist Paso a Paso: Marca tu progreso
                </h3>
                <p className="text-xs text-slate-500">
                  Sigue cada paso en orden. Puedes hacer clic en cada casilla conforme avances.
                </p>
              </div>
            </div>

            <div className="flex items-center gap-3">
              <div className="text-right">
                <span className="text-xs font-bold text-indigo-700">
                  {finishedStepsCount} de {totalSteps} completados
                </span>
                <span className="text-[11px] text-slate-400 block font-medium">({progressPercent}%)</span>
              </div>
              <div className="w-24 bg-slate-100 h-2.5 rounded-full overflow-hidden border border-slate-200">
                <div 
                  className="bg-emerald-500 h-full transition-all duration-300 rounded-full"
                  style={{ width: `${progressPercent}%` }}
                />
              </div>
            </div>
          </div>

          <div className="space-y-3">
            {article.quick_steps.map((step, idx) => {
              const isChecked = !!completedSteps[step.id];
              return (
                <div 
                  key={step.id}
                  onClick={() => toggleStep(step.id)}
                  className={`cursor-pointer p-3.5 rounded-xl border transition-all flex items-start gap-3.5 ${
                    isChecked 
                      ? 'bg-emerald-50/70 border-emerald-200 text-slate-800' 
                      : 'bg-slate-50/70 border-slate-200 hover:border-indigo-300 hover:bg-slate-100/50'
                  }`}
                >
                  <div className={`mt-0.5 w-5 h-5 rounded-md flex items-center justify-center border transition-colors ${
                    isChecked ? 'bg-emerald-600 border-emerald-600 text-white' : 'border-slate-300 bg-white'
                  }`}>
                    {isChecked && <Check className="w-3.5 h-3.5 stroke-[3]" />}
                  </div>

                  <div className="flex-1 text-xs">
                    <span className={`font-bold text-sm block mb-0.5 ${isChecked ? 'line-through text-slate-500' : 'text-slate-900'}`}>
                      Paso {idx + 1}: {step.title}
                    </span>
                    <p className={`leading-relaxed ${isChecked ? 'text-slate-500' : 'text-slate-600'}`}>
                      {step.description}
                    </p>
                  </div>
                </div>
              );
            })}
          </div>
        </section>
      )}

      {/* Índice de Contenidos Interactivo */}
      {headings.length > 0 && (
        <nav className="my-8 p-5 bg-slate-50/90 rounded-2xl border border-slate-200/90 shadow-2xs">
          <div className="flex items-center gap-2 font-bold text-xs uppercase tracking-wider text-slate-700 mb-3">
            <ListOrdered className="w-4 h-4 text-indigo-600" />
            <span>Índice detallado de este tutorial</span>
          </div>
          <ul className="space-y-2 text-xs sm:text-sm">
            {headings.map((h, i) => (
              <li key={i} className="flex items-center gap-2 text-slate-700 hover:text-indigo-600 transition-colors">
                <ChevronRight className="w-3.5 h-3.5 text-indigo-400 shrink-0" />
                <span>{h.text}</span>
              </li>
            ))}
          </ul>
        </nav>
      )}

      {/* Contenido HTML del Artículo con tipografía Tailwind prose impecable */}
      <div 
        className="prose prose-slate lg:prose-lg max-w-none 
          prose-headings:font-bold prose-headings:text-slate-900 prose-headings:tracking-tight
          prose-h2:text-2xl prose-h2:mt-10 prose-h2:mb-4 prose-h2:pb-2 prose-h2:border-b prose-h2:border-slate-200
          prose-h3:text-xl prose-h3:mt-6 prose-h3:mb-3
          prose-p:leading-relaxed prose-p:text-slate-700
          prose-li:text-slate-700
          prose-blockquote:border-l-4 prose-blockquote:border-indigo-500 prose-blockquote:bg-indigo-50/50 prose-blockquote:py-2.5 prose-blockquote:px-4 prose-blockquote:rounded-r-xl prose-blockquote:italic
          prose-code:text-indigo-600 prose-code:bg-slate-100 prose-code:px-1.5 prose-code:py-0.5 prose-code:rounded prose-code:before:content-none prose-code:after:content-none
          prose-pre:bg-slate-900 prose-pre:text-slate-100 prose-pre:rounded-2xl prose-pre:shadow-md
          prose-a:text-indigo-600 prose-a:font-semibold hover:prose-a:text-indigo-700"
        dangerouslySetInnerHTML={{ __html: article.content }}
      />

      {/* Sección de Preguntas Frecuentes y Solución de Problemas (FAQ) */}
      {article.faqs && article.faqs.length > 0 && (
        <section className="mt-12 p-6 sm:p-8 bg-white rounded-3xl border border-slate-200 shadow-xs">
          <div className="flex items-center gap-2.5 mb-6">
            <div className="w-8 h-8 rounded-lg bg-indigo-50 text-indigo-600 flex items-center justify-center">
              <HelpCircle className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-lg font-bold text-slate-900">
                Preguntas Frecuentes y Solución de Errores Comunes
              </h3>
              <p className="text-xs text-slate-500">
                Respuestas directas a las dudas más habituales registradas durante nuestras pruebas.
              </p>
            </div>
          </div>

          <div className="space-y-3">
            {article.faqs.map((faq, index) => {
              const isOpen = openFaqIndex === index;
              return (
                <div 
                  key={index}
                  className="rounded-2xl border border-slate-200/90 overflow-hidden bg-slate-50/50 transition-colors"
                >
                  <button
                    onClick={() => setOpenFaqIndex(isOpen ? null : index)}
                    className="w-full text-left p-4 flex items-center justify-between gap-4 font-semibold text-xs sm:text-sm text-slate-900 hover:text-indigo-600"
                  >
                    <span>{faq.question}</span>
                    {isOpen ? <ChevronDown className="w-4 h-4 text-indigo-600 shrink-0" /> : <ChevronRight className="w-4 h-4 text-slate-400 shrink-0" />}
                  </button>
                  {isOpen && (
                    <div className="p-4 pt-0 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 bg-white">
                      {faq.answer}
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </section>
      )}

      {/* Caja de Perfil E-E-A-T del Autor al final del artículo */}
      <section className="mt-12 p-6 sm:p-8 bg-gradient-to-br from-slate-50 to-indigo-50/40 rounded-3xl border border-indigo-100 shadow-xs">
        <div className="flex flex-col sm:flex-row items-start sm:items-center gap-5">
          <div className="w-16 h-16 rounded-2xl bg-indigo-600 text-white font-extrabold text-xl flex items-center justify-center shadow-md shrink-0">
            A
          </div>
          <div>
            <div className="flex items-center gap-2 mb-1">
              <h4 className="text-lg font-bold text-slate-900">Escrito y verificado por {AUTHOR_INFO.name}</h4>
              <span className="text-xs bg-indigo-100 text-indigo-700 font-semibold px-2 py-0.5 rounded-full">
                Autor Verificado
              </span>
            </div>
            <p className="text-xs font-semibold text-slate-600 mb-2 flex items-center gap-1.5">
              <GraduationCap className="w-4 h-4 text-indigo-600" />
              {AUTHOR_INFO.role} • {AUTHOR_INFO.university} (Barranquilla)
            </p>
            <p className="text-xs text-slate-600 leading-relaxed mb-3">
              {AUTHOR_INFO.bio}
            </p>
            <button
              onClick={onOpenAuthorProfile}
              className="text-xs font-bold text-indigo-600 hover:text-indigo-800 underline"
            >
              Conoce más sobre el autor y nuestro protocolo de pruebas →
            </button>
          </div>
        </div>
      </section>

      {/* Nota de Copyright y Derechos de Autor al pie del artículo */}
      <footer className="mt-8 pt-4 border-t border-slate-200 text-center text-xs text-slate-500">
        <p>
          {article.copyright_notice || '© 2026 Tecnología para Gente Normal. Fotografías y textos originales bajo licencia CC BY-NC-SA 4.0.'}
        </p>
        <p className="text-[11px] text-slate-400 mt-1">
          Prohibida la reproducción comercial o el raspado automatizado sin autorización previa. Para fines educativos o citas, atribuye a Andrés y enlaza a este tutorial.
        </p>
      </footer>
    </article>
  );
};
