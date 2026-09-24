import React, { useState, useRef } from 'react';
import { Article, CategorySlug } from '../types';
import { CATEGORIES } from '../data/seedArticles';
import { ArrowLeft, Save, Upload, Code, Eye, Sparkles } from 'lucide-react';

interface AdminNewArticleProps {
  onSave: (newArticle: Omit<Article, 'id'>) => void;
  onCancel: () => void;
}

export const AdminNewArticle: React.FC<AdminNewArticleProps> = ({ onSave, onCancel }) => {
  const [title, setTitle] = useState('');
  const [slug, setSlug] = useState('');
  const [excerpt, setExcerpt] = useState('');
  const [content, setContent] = useState(`<h2>Introducción</h2>
<p>Explica aquí de forma clara y directa el problema real que vas a solucionar...</p>

<h2>Paso a paso verificado</h2>
<ol>
  <li>Primer paso técnico con instrucciones precisas.</li>
  <li>Segundo paso indicando los comandos o botones exactos.</li>
</ol>

<h2>💡 Probado por nosotros</h2>
<p>Verificamos este procedimiento en nuestro equipo de laboratorio, confirmando que funciona sin errores ni riesgos.</p>`);
  const [categorySlug, setCategorySlug] = useState<CategorySlug>('tramites');
  const [author, setAuthor] = useState('Andrés');
  const [status, setStatus] = useState<'Publicado' | 'Borrador'>('Publicado');
  const [featuredImage, setFeaturedImage] = useState('https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1200&q=80');
  const [activeTab, setActiveTab] = useState<'edit' | 'preview'>('edit');
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleGenerateSlug = () => {
    const generated = title
      .toLowerCase()
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-+|-+$/g, '');
    setSlug(generated);
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      const objectUrl = URL.createObjectURL(file);
      setFeaturedImage(objectUrl);
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSave({
      title,
      slug: slug || title.toLowerCase().replace(/[^a-z0-9]+/g, '-'),
      excerpt,
      content,
      category_slug: categorySlug,
      author,
      status,
      featured_image: featuredImage,
      created_at: new Date().toISOString().replace('T', ' ').substring(0, 19),
      read_time_minutes: Math.max(3, Math.ceil(content.split(/\s+/).length / 200))
    });
  };

  return (
    <div className="max-w-5xl mx-auto px-4 py-8">
      <div className="flex items-center justify-between mb-6 pb-4 border-b border-slate-200">
        <div className="flex items-center gap-3">
          <button
            onClick={onCancel}
            className="p-2 rounded-lg text-slate-500 hover:text-slate-800 hover:bg-slate-100 transition-colors"
          >
            <ArrowLeft className="w-5 h-5" />
          </button>
          <div>
            <h1 className="text-2xl font-bold text-slate-900">Crear Nuevo Artículo</h1>
            <p className="text-xs text-slate-500">Insertará un nuevo registro en la tabla Article de SQLite</p>
          </div>
        </div>

        <button
          onClick={handleSubmit}
          className="inline-flex items-center gap-2 px-5 py-2.5 text-sm font-semibold text-white bg-indigo-600 hover:bg-indigo-700 rounded-lg transition-colors shadow-sm"
        >
          <Save className="w-4 h-4" />
          <span>Publicar / Guardar</span>
        </button>
      </div>

      <form onSubmit={handleSubmit} className="space-y-6">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div className="lg:col-span-2 space-y-5">
            <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs space-y-4">
              <div>
                <label className="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1.5">
                  Título del Artículo
                </label>
                <input
                  type="text"
                  value={title}
                  onChange={(e) => setTitle(e.target.value)}
                  onBlur={() => { if (!slug) handleGenerateSlug(); }}
                  required
                  placeholder="Ej: Guía completa para conectar Flet con SQLite..."
                  className="w-full px-3.5 py-2.5 text-sm border border-slate-300 rounded-lg focus:ring-2 focus:ring-indigo-500 font-medium"
                />
              </div>

              <div>
                <div className="flex items-center justify-between mb-1">
                  <label className="text-xs font-bold uppercase tracking-wider text-slate-700">
                    Slug URL
                  </label>
                  <button
                    type="button"
                    onClick={handleGenerateSlug}
                    className="text-xs text-indigo-600 hover:text-indigo-800 font-semibold flex items-center gap-1"
                  >
                    <Sparkles className="w-3 h-3" />
                    Auto-generar
                  </button>
                </div>
                <input
                  type="text"
                  value={slug}
                  onChange={(e) => setSlug(e.target.value)}
                  required
                  className="w-full px-3.5 py-2 text-xs font-mono border border-slate-300 rounded-lg focus:ring-2 focus:ring-indigo-500 bg-slate-50"
                />
              </div>

              <div>
                <label className="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1.5">
                  Extracto / Meta Resumen
                </label>
                <textarea
                  value={excerpt}
                  onChange={(e) => setExcerpt(e.target.value)}
                  rows={2}
                  required
                  className="w-full px-3.5 py-2 text-sm border border-slate-300 rounded-lg focus:ring-2 focus:ring-indigo-500"
                  placeholder="Resumen atractivo para los lectores y motores de búsqueda..."
                />
              </div>
            </div>

            <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs">
              <div className="flex items-center justify-between pb-3 mb-3 border-b border-slate-200">
                <div className="flex items-center gap-1">
                  <button
                    type="button"
                    onClick={() => setActiveTab('edit')}
                    className={`inline-flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-semibold ${
                      activeTab === 'edit' ? 'bg-indigo-600 text-white' : 'text-slate-600 hover:bg-slate-100'
                    }`}
                  >
                    <Code className="w-3.5 h-3.5" />
                    Editor HTML
                  </button>
                  <button
                    type="button"
                    onClick={() => setActiveTab('preview')}
                    className={`inline-flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-semibold ${
                      activeTab === 'preview' ? 'bg-indigo-600 text-white' : 'text-slate-600 hover:bg-slate-100'
                    }`}
                  >
                    <Eye className="w-3.5 h-3.5" />
                    Vista Previa
                  </button>
                </div>
              </div>

              {activeTab === 'edit' ? (
                <textarea
                  value={content}
                  onChange={(e) => setContent(e.target.value)}
                  rows={14}
                  required
                  className="w-full p-4 font-mono text-xs sm:text-sm border border-slate-300 rounded-lg focus:ring-2 focus:ring-indigo-500 bg-slate-900 text-slate-100 leading-relaxed"
                />
              ) : (
                <div 
                  className="prose prose-slate max-w-none p-4 border rounded-lg bg-slate-50"
                  dangerouslySetInnerHTML={{ __html: content }}
                />
              )}
            </div>
          </div>

          <div className="space-y-5">
            <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs space-y-4">
              <h3 className="text-xs font-bold uppercase tracking-wider text-slate-700 border-b pb-2">
                Clasificación
              </h3>

              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1">Estado</label>
                <select
                  value={status}
                  onChange={(e) => setStatus(e.target.value as 'Publicado' | 'Borrador')}
                  className="w-full px-3 py-2 text-sm border border-slate-300 rounded-lg"
                >
                  <option value="Publicado">Publicado</option>
                  <option value="Borrador">Borrador</option>
                </select>
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1">Categoría</label>
                <select
                  value={categorySlug}
                  onChange={(e) => setCategorySlug(e.target.value as CategorySlug)}
                  className="w-full px-3 py-2 text-sm border border-slate-300 rounded-lg"
                >
                  {CATEGORIES.map(c => (
                    <option key={c.slug} value={c.slug}>{c.name}</option>
                  ))}
                </select>
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1">Autor</label>
                <input
                  type="text"
                  value={author}
                  onChange={(e) => setAuthor(e.target.value)}
                  className="w-full px-3 py-2 text-sm border border-slate-300 rounded-lg"
                />
              </div>
            </div>

            <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs space-y-4">
              <h3 className="text-xs font-bold uppercase tracking-wider text-slate-700 border-b pb-2">
                Imagen Destacada (/static/img/)
              </h3>
              <div className="aspect-video w-full rounded-lg overflow-hidden border border-slate-200 bg-slate-100">
                <img src={featuredImage} alt="Destacada" className="w-full h-full object-cover" />
              </div>
              <input
                type="file"
                ref={fileInputRef}
                onChange={handleFileChange}
                accept="image/*"
                className="hidden"
              />
              <button
                type="button"
                onClick={() => fileInputRef.current?.click()}
                className="w-full py-2 px-3 border border-slate-300 rounded-lg text-xs font-semibold text-slate-700 hover:bg-slate-50 flex items-center justify-center gap-1.5"
              >
                <Upload className="w-3.5 h-3.5" />
                <span>Seleccionar imagen...</span>
              </button>
            </div>
          </div>
        </div>
      </form>
    </div>
  );
};
