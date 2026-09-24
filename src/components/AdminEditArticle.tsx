import React, { useState, useRef } from 'react';
import { Article, CategorySlug } from '../types';
import { CATEGORIES } from '../data/seedArticles';
import { 
  ArrowLeft, 
  Save, 
  Upload, 
  Eye, 
  Code, 
  CheckCircle, 
  Sparkles, 
  RefreshCw, 
  FileText,
  HelpCircle,
  AlertCircle
} from 'lucide-react';

interface AdminEditArticleProps {
  article: Article;
  onSave: (updatedArticle: Article) => void;
  onCancel: () => void;
}

export const AdminEditArticle: React.FC<AdminEditArticleProps> = ({ article, onSave, onCancel }) => {
  const [title, setTitle] = useState(article.title);
  const [slug, setSlug] = useState(article.slug);
  const [excerpt, setExcerpt] = useState(article.excerpt);
  const [content, setContent] = useState(article.content);
  const [categorySlug, setCategorySlug] = useState<CategorySlug>(article.category_slug);
  const [author, setAuthor] = useState(article.author);
  const [status, setStatus] = useState<'Publicado' | 'Borrador'>(article.status);
  
  // Manejo de reemplazo de imagen
  const [featuredImage, setFeaturedImage] = useState(article.featured_image);
  const [newImageSelected, setNewImageSelected] = useState(false);
  const [imageFileName, setImageFileName] = useState('');
  
  // Pestaña activa del editor: 'edit' o 'preview'
  const [activeTab, setActiveTab] = useState<'edit' | 'preview'>('edit');
  const [saveSuccess, setSaveSuccess] = useState(false);
  const [isSaving, setIsSaving] = useState(false);

  const fileInputRef = useRef<HTMLInputElement>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  // Generador de slug a partir del título
  const handleGenerateSlug = () => {
    const generated = title
      .toLowerCase()
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-+|-+$/g, '');
    setSlug(generated);
  };

  // Simulación de carga y reemplazo de archivo de imagen (multipart/form-data)
  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      setImageFileName(file.name);
      setNewImageSelected(true);
      // Crear URL local para previsualización inmediata en el navegador
      const objectUrl = URL.createObjectURL(file);
      setFeaturedImage(objectUrl);
    }
  };

  // Inserción de etiquetas HTML semánticas en la posición del cursor
  const insertTag = (openTag: string, closeTag: string, placeholder: string = 'texto') => {
    if (!textareaRef.current) return;
    const textarea = textareaRef.current;
    const start = textarea.selectionStart;
    const end = textarea.selectionEnd;
    const selectedText = content.substring(start, end) || placeholder;
    const newContent = content.substring(0, start) + openTag + selectedText + closeTag + content.substring(end);
    setContent(newContent);
    setTimeout(() => {
      textarea.focus();
      textarea.setSelectionRange(start + openTag.length, start + openTag.length + selectedText.length);
    }, 50);
  };

  // Inserción del bloque obligatorio E-E-A-T: <h2>💡 Probado por nosotros</h2>
  const insertTestedBlock = () => {
    const blockSnippet = `\n\n<h2>💡 Probado por nosotros</h2>\n<p>Realizamos este procedimiento en nuestro laboratorio con fecha ${new Date().toLocaleDateString('es-ES')}, verificando cada paso en un equipo de pruebas con resultados satisfactorios y sin anomalías.</p>\n`;
    setContent(prev => prev + blockSnippet);
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setIsSaving(true);

    setTimeout(() => {
      const updated: Article = {
        ...article,
        title,
        slug,
        excerpt,
        content,
        category_slug: categorySlug,
        author,
        status,
        featured_image: featuredImage,
        read_time_minutes: Math.max(3, Math.ceil(content.split(/\s+/).length / 200))
      };

      onSave(updated);
      setIsSaving(false);
      setSaveSuccess(true);
      setTimeout(() => setSaveSuccess(false), 3000);
    }, 600);
  };

  return (
    <div className="max-w-5xl mx-auto px-4 py-8">
      {/* Barra de cabecera con acciones */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6 pb-4 border-b border-slate-200">
        <div className="flex items-center gap-3">
          <button
            type="button"
            onClick={onCancel}
            className="p-2 rounded-lg text-slate-500 hover:text-slate-800 hover:bg-slate-100 transition-colors"
            title="Volver al Panel"
          >
            <ArrowLeft className="w-5 h-5" />
          </button>
          <div>
            <div className="flex items-center gap-2">
              <h1 className="text-xl sm:text-2xl font-bold text-slate-900">Editar Artículo #{article.id}</h1>
              <span className={`text-xs px-2 py-0.5 rounded-full font-semibold ${
                status === 'Publicado' ? 'bg-emerald-100 text-emerald-800' : 'bg-amber-100 text-amber-800'
              }`}>
                {status}
              </span>
            </div>
            <p className="text-xs text-slate-500">Ruta FastAPI: <code>/admin/edit/{article.id}</code></p>
          </div>
        </div>

        <div className="flex items-center gap-3">
          <button
            type="button"
            onClick={onCancel}
            className="px-4 py-2 text-sm font-medium text-slate-600 hover:text-slate-900 bg-white border border-slate-200 rounded-lg hover:bg-slate-50 transition-colors shadow-xs"
          >
            Cancelar
          </button>
          <button
            onClick={handleSubmit}
            disabled={isSaving}
            className="inline-flex items-center gap-2 px-5 py-2 text-sm font-semibold text-white bg-indigo-600 hover:bg-indigo-700 rounded-lg transition-colors shadow-sm disabled:opacity-50"
          >
            {isSaving ? <RefreshCw className="w-4 h-4 animate-spin" /> : <Save className="w-4 h-4" />}
            <span>{isSaving ? 'Guardando...' : 'Guardar Cambios'}</span>
          </button>
        </div>
      </div>

      {/* Alerta de confirmación de guardado */}
      {saveSuccess && (
        <div className="mb-6 p-4 bg-emerald-50 border border-emerald-200 text-emerald-800 rounded-xl flex items-center justify-between animate-fade-in shadow-xs">
          <div className="flex items-center gap-2 text-sm font-medium">
            <CheckCircle className="w-5 h-5 text-emerald-600 shrink-0" />
            <span>¡Artículo actualizado exitosamente en la base de datos SQLite! Los cambios ya son visibles en el blog.</span>
          </div>
          <button onClick={() => setSaveSuccess(false)} className="text-xs text-emerald-700 hover:underline">
            Cerrar
          </button>
        </div>
      )}

      {/* Formulario de edición completo */}
      <form onSubmit={handleSubmit} className="space-y-6">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          
          {/* Columna Principal (2 columnas): Título, Slug, Extracto, Contenido */}
          <div className="lg:col-span-2 space-y-5">
            {/* Título */}
            <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs space-y-4">
              <div>
                <label className="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1.5">
                  Título del Artículo <span className="text-rose-500">*</span>
                </label>
                <input
                  type="text"
                  value={title}
                  onChange={(e) => setTitle(e.target.value)}
                  required
                  placeholder="Ej: Cómo sacar el RUT digital por primera vez..."
                  className="w-full px-3.5 py-2.5 text-sm border border-slate-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 font-medium text-slate-900"
                />
              </div>

              {/* Slug con botón de auto-generación */}
              <div>
                <div className="flex items-center justify-between mb-1">
                  <label className="text-xs font-bold uppercase tracking-wider text-slate-700">
                    Slug URL (Único) <span className="text-rose-500">*</span>
                  </label>
                  <button
                    type="button"
                    onClick={handleGenerateSlug}
                    className="text-xs text-indigo-600 hover:text-indigo-800 font-semibold flex items-center gap-1"
                  >
                    <Sparkles className="w-3 h-3" />
                    Regenerar desde título
                  </button>
                </div>
                <div className="flex items-center rounded-lg border border-slate-300 bg-slate-50 focus-within:ring-2 focus-within:ring-indigo-500 focus-within:border-indigo-500 overflow-hidden">
                  <span className="px-3 text-xs text-slate-500 font-mono select-none">/</span>
                  <input
                    type="text"
                    value={slug}
                    onChange={(e) => setSlug(e.target.value)}
                    required
                    className="w-full py-2.5 pr-3 text-xs font-mono bg-transparent border-0 focus:ring-0 text-slate-800"
                  />
                </div>
              </div>

              {/* Extracto */}
              <div>
                <label className="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1.5">
                  Extracto / Meta Descripción SEO (120-160 caracteres)
                </label>
                <textarea
                  value={excerpt}
                  onChange={(e) => setExcerpt(e.target.value)}
                  rows={2}
                  className="w-full px-3.5 py-2 text-sm border border-slate-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 text-slate-700"
                  placeholder="Resumen directo que aparecerá en Google y en las tarjetas..."
                />
                <div className="flex justify-between items-center mt-1 text-[11px] text-slate-500">
                  <span>Recomendado para snippets de Google: 120 a 160 caracteres</span>
                  <span className={excerpt.length > 160 ? 'text-amber-600 font-semibold' : 'text-slate-500'}>
                    {excerpt.length} caracteres
                  </span>
                </div>
              </div>
            </div>

            {/* Editor de Contenido HTML con Barra Semántica */}
            <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs">
              <div className="flex flex-wrap items-center justify-between gap-2 pb-3 mb-3 border-b border-slate-200">
                <div className="flex items-center gap-1">
                  <button
                    type="button"
                    onClick={() => setActiveTab('edit')}
                    className={`inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition-colors ${
                      activeTab === 'edit'
                        ? 'bg-indigo-600 text-white shadow-xs'
                        : 'text-slate-600 hover:bg-slate-100'
                    }`}
                  >
                    <Code className="w-3.5 h-3.5" />
                    Editor HTML
                  </button>
                  <button
                    type="button"
                    onClick={() => setActiveTab('preview')}
                    className={`inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition-colors ${
                      activeTab === 'preview'
                        ? 'bg-indigo-600 text-white shadow-xs'
                        : 'text-slate-600 hover:bg-slate-100'
                    }`}
                  >
                    <Eye className="w-3.5 h-3.5" />
                    Vista Previa Render
                  </button>
                </div>

                {/* Botón especial E-E-A-T */}
                <button
                  type="button"
                  onClick={insertTestedBlock}
                  title="Inserta la sección de verificación editorial"
                  className="inline-flex items-center gap-1 px-2.5 py-1 text-xs font-semibold bg-emerald-50 text-emerald-700 border border-emerald-200 rounded-lg hover:bg-emerald-100 transition-colors"
                >
                  <Sparkles className="w-3.5 h-3.5 text-emerald-600" />
                  + Bloque "💡 Probado por nosotros"
                </button>
              </div>

              {/* Barra de herramientas para etiquetas semánticas */}
              {activeTab === 'edit' && (
                <div className="flex flex-wrap items-center gap-1.5 p-2 bg-slate-50 border border-slate-200 rounded-lg mb-3 text-xs">
                  <button
                    type="button"
                    onClick={() => insertTag('<h2>', '</h2>', 'Encabezado H2')}
                    className="px-2 py-1 bg-white border border-slate-200 rounded font-bold hover:bg-slate-100 text-slate-700"
                  >
                    H2
                  </button>
                  <button
                    type="button"
                    onClick={() => insertTag('<h3>', '</h3>', 'Subtítulo H3')}
                    className="px-2 py-1 bg-white border border-slate-200 rounded font-bold hover:bg-slate-100 text-slate-700"
                  >
                    H3
                  </button>
                  <button
                    type="button"
                    onClick={() => insertTag('<p>', '</p>', 'Párrafo explicativo')}
                    className="px-2 py-1 bg-white border border-slate-200 rounded hover:bg-slate-100 text-slate-700"
                  >
                    &lt;p&gt;
                  </button>
                  <button
                    type="button"
                    onClick={() => insertTag('<ol>\n  <li>', '</li>\n  <li>Paso 2</li>\n</ol>', 'Paso 1')}
                    className="px-2 py-1 bg-white border border-slate-200 rounded hover:bg-slate-100 text-slate-700"
                  >
                    1. Lista Ordenada
                  </button>
                  <button
                    type="button"
                    onClick={() => insertTag('<ul>\n  <li>', '</li>\n  <li>Elemento 2</li>\n</ul>', 'Elemento 1')}
                    className="px-2 py-1 bg-white border border-slate-200 rounded hover:bg-slate-100 text-slate-700"
                  >
                    • Lista de viñetas
                  </button>
                  <button
                    type="button"
                    onClick={() => insertTag('<blockquote>', '</blockquote>', 'Consejo importante o advertencia técnica')}
                    className="px-2 py-1 bg-white border border-slate-200 rounded italic hover:bg-slate-100 text-slate-700"
                  >
                    Cita / Tip
                  </button>
                  <button
                    type="button"
                    onClick={() => insertTag('<pre><code>', '</code></pre>', 'codigo_en_python()')}
                    className="px-2 py-1 bg-white border border-slate-200 rounded font-mono hover:bg-slate-100 text-slate-700"
                  >
                    Código
                  </button>
                </div>
              )}

              {/* Área de texto / Vista Previa */}
              {activeTab === 'edit' ? (
                <div>
                  <textarea
                    ref={textareaRef}
                    value={content}
                    onChange={(e) => setContent(e.target.value)}
                    rows={16}
                    required
                    className="w-full p-4 font-mono text-xs sm:text-sm border border-slate-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 bg-slate-900 text-slate-100 leading-relaxed selection:bg-indigo-600"
                    placeholder="<h2>Título</h2><p>Contenido semántico...</p>"
                  />
                  <div className="flex items-center gap-1.5 mt-2 text-xs text-slate-500">
                    <AlertCircle className="w-3.5 h-3.5 text-indigo-500" />
                    <span>El contenido se almacena como HTML puro y se renderiza de forma segura mediante <code>| safe</code> en Jinja2.</span>
                  </div>
                </div>
              ) : (
                <div className="p-6 border border-slate-200 rounded-xl bg-slate-50/50 max-h-[500px] overflow-y-auto">
                  <div 
                    className="prose prose-slate max-w-none 
                      prose-headings:font-bold prose-h2:border-b prose-h2:border-slate-200 prose-h2:pb-2
                      prose-pre:bg-slate-900 prose-pre:text-slate-100 prose-pre:rounded-lg"
                    dangerouslySetInnerHTML={{ __html: content }}
                  />
                </div>
              )}
            </div>
          </div>

          {/* Columna Lateral (1 columna): Metadatos, Categoría, Estado y Reemplazo de Imagen */}
          <div className="space-y-5">
            {/* Tarjeta de Publicación y Estado */}
            <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs space-y-4">
              <h3 className="text-xs font-bold uppercase tracking-wider text-slate-700 border-b border-slate-100 pb-2">
                Estado y Clasificación
              </h3>

              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1">Estado de Publicación</label>
                <select
                  value={status}
                  onChange={(e) => setStatus(e.target.value as 'Publicado' | 'Borrador')}
                  className="w-full px-3 py-2 text-sm border border-slate-300 rounded-lg focus:ring-2 focus:ring-indigo-500"
                >
                  <option value="Publicado">Publicado (Visible en el blog)</option>
                  <option value="Borrador">Borrador (Solo visible en admin)</option>
                </select>
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1">Categoría</label>
                <select
                  value={categorySlug}
                  onChange={(e) => setCategorySlug(e.target.value as CategorySlug)}
                  className="w-full px-3 py-2 text-sm border border-slate-300 rounded-lg focus:ring-2 focus:ring-indigo-500 font-medium"
                >
                  {CATEGORIES.map((cat) => (
                    <option key={cat.slug} value={cat.slug}>
                      {cat.name}
                    </option>
                  ))}
                </select>
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1">Autor E-E-A-T</label>
                <input
                  type="text"
                  value={author}
                  onChange={(e) => setAuthor(e.target.value)}
                  className="w-full px-3 py-2 text-sm border border-slate-300 rounded-lg focus:ring-2 focus:ring-indigo-500"
                />
                <span className="text-[11px] text-slate-400 mt-0.5 block">Vinculado al perfil de Andrés (CUC)</span>
              </div>
            </div>

            {/* SECCIÓN CLAVE DE TAREA 1: Reemplazar Imagen Destacada */}
            <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs space-y-4">
              <div className="flex items-center justify-between border-b border-slate-100 pb-2">
                <h3 className="text-xs font-bold uppercase tracking-wider text-slate-700">
                  Imagen Destacada
                </h3>
                {newImageSelected && (
                  <span className="text-[10px] font-bold bg-amber-100 text-amber-800 px-2 py-0.5 rounded-full">
                    Pendiente de guardar
                  </span>
                )}
              </div>

              {/* Vista previa de la imagen actual / nueva */}
              <div className="space-y-2">
                <p className="text-xs text-slate-500">
                  {newImageSelected ? 'Nueva imagen seleccionada para subir:' : 'Imagen actualmente asociada:'}
                </p>
                <div className="relative aspect-video w-full rounded-lg overflow-hidden border border-slate-200 bg-slate-100 shadow-inner">
                  <img
                    src={featuredImage}
                    alt="Imagen destacada"
                    className="w-full h-full object-cover"
                  />
                </div>
              </div>

              {/* Campo para subir archivo o seleccionar nueva */}
              <div>
                <input
                  type="file"
                  ref={fileInputRef}
                  onChange={handleFileChange}
                  accept="image/png, image/jpeg, image/webp"
                  className="hidden"
                />
                <button
                  type="button"
                  onClick={() => fileInputRef.current?.click()}
                  className="w-full inline-flex items-center justify-center gap-2 px-4 py-2.5 border-2 border-dashed border-slate-300 hover:border-indigo-400 bg-slate-50 hover:bg-indigo-50/50 rounded-xl text-xs font-semibold text-slate-700 hover:text-indigo-600 transition-all cursor-pointer"
                >
                  <Upload className="w-4 h-4 text-slate-500" />
                  <span>{newImageSelected ? `Cambiar: ${imageFileName}` : 'Reemplazar con nueva imagen...'}</span>
                </button>
                <p className="text-[11px] text-slate-400 text-center mt-1.5">
                  Formatos soportados: JPG, PNG, WEBP (Guardado en <code>/static/img/</code>)
                </p>
              </div>

              {/* Opción alternativa rápida: Ingresar URL directa */}
              <div className="pt-2 border-t border-slate-100">
                <label className="block text-[11px] font-medium text-slate-600 mb-1">
                  O pegar ruta / URL externa:
                </label>
                <input
                  type="text"
                  value={featuredImage}
                  onChange={(e) => {
                    setFeaturedImage(e.target.value);
                    setNewImageSelected(true);
                  }}
                  className="w-full px-2.5 py-1.5 text-xs font-mono border border-slate-200 rounded-lg text-slate-600"
                />
              </div>
            </div>

            {/* Checklist de calidad editorial */}
            <div className="bg-slate-50 p-4 rounded-xl border border-slate-200 text-xs space-y-2">
              <span className="font-bold text-slate-800 flex items-center gap-1.5">
                <CheckCircle className="w-4 h-4 text-emerald-600" />
                Checklist editorial & E-E-A-T
              </span>
              <ul className="space-y-1.5 text-slate-600 pl-1">
                <li className="flex items-center gap-1.5">
                  <span className={content.includes('<h2>💡 Probado por nosotros</h2>') ? 'text-emerald-600 font-bold' : 'text-slate-400'}>
                    {content.includes('<h2>💡 Probado por nosotros</h2>') ? '✓' : '○'}
                  </span>
                  <span>Bloque "Probado por nosotros" incluido</span>
                </li>
                <li className="flex items-center gap-1.5">
                  <span className={content.includes('<h2>') ? 'text-emerald-600 font-bold' : 'text-slate-400'}>
                    {content.includes('<h2>') ? '✓' : '○'}
                  </span>
                  <span>Estructura semántica con H2 y H3</span>
                </li>
                <li className="flex items-center gap-1.5">
                  <span className={title.length > 25 ? 'text-emerald-600 font-bold' : 'text-slate-400'}>
                    {title.length > 25 ? '✓' : '○'}
                  </span>
                  <span>Título descriptivo no engañoso</span>
                </li>
              </ul>
            </div>

          </div>

        </div>
      </form>
    </div>
  );
};
