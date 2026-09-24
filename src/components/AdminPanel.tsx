import React, { useState } from 'react';
import { Article } from '../types';
import { CATEGORIES } from '../data/seedArticles';
import { 
  Plus, 
  Edit3, 
  Trash2, 
  Eye, 
  Search, 
  Filter, 
  Server, 
  FileText, 
  CheckCircle2, 
  AlertTriangle,
  ArrowRight,
  TrendingUp,
  FolderOpen
} from 'lucide-react';

interface AdminPanelProps {
  articles: Article[];
  onEdit: (article: Article) => void;
  onDelete: (id: number) => void;
  onView: (article: Article) => void;
  onCreateNew: () => void;
  onOpenProductionCenter: () => void;
  onGoToHome: () => void;
}

export const AdminPanel: React.FC<AdminPanelProps> = ({
  articles,
  onEdit,
  onDelete,
  onView,
  onCreateNew,
  onOpenProductionCenter,
  onGoToHome
}) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [categoryFilter, setCategoryFilter] = useState<string>('all');
  const [statusFilter, setStatusFilter] = useState<string>('all');
  const [articleToDelete, setArticleToDelete] = useState<Article | null>(null);

  const filteredArticles = articles.filter(art => {
    const matchesSearch = art.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
                          art.slug.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesCategory = categoryFilter === 'all' || art.category_slug === categoryFilter;
    const matchesStatus = statusFilter === 'all' || art.status === statusFilter;
    return matchesSearch && matchesCategory && matchesStatus;
  });

  const publishedCount = articles.filter(a => a.status === 'Publicado').length;
  const draftCount = articles.filter(a => a.status === 'Borrador').length;

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 py-8">
      {/* Barra superior de título y accesos rápidos */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-8 pb-6 border-b border-slate-200">
        <div>
          <div className="flex items-center gap-2">
            <span className="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
            <span className="text-xs font-bold uppercase tracking-wider text-slate-500">Panel de Administración FastAPI / SQLite</span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900 tracking-tight">
            Gestor de Contenido (CMS)
          </h1>
          <p className="text-xs sm:text-sm text-slate-500 mt-1">
            Administra los artículos de <strong>Tecnología para Gente Normal</strong>, edita contenido y gestiona imágenes.
          </p>
        </div>

        <div className="flex flex-wrap items-center gap-3">
          <button
            onClick={onOpenProductionCenter}
            className="inline-flex items-center gap-2 px-4 py-2.5 text-xs sm:text-sm font-semibold text-slate-700 bg-white border border-slate-300 hover:bg-slate-50 rounded-xl transition-all shadow-xs"
          >
            <Server className="w-4 h-4 text-indigo-600" />
            <span>Guía & Archivos VPS (Tarea 3)</span>
          </button>

          <button
            onClick={onCreateNew}
            className="inline-flex items-center gap-2 px-4 py-2.5 text-xs sm:text-sm font-semibold text-white bg-indigo-600 hover:bg-indigo-700 rounded-xl transition-all shadow-sm"
          >
            <Plus className="w-4 h-4" />
            <span>Nuevo Artículo</span>
          </button>
        </div>
      </div>

      {/* Tarjetas de estadísticas */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
        <div className="p-4 bg-white rounded-xl border border-slate-200 shadow-xs">
          <div className="flex items-center justify-between">
            <span className="text-xs font-semibold text-slate-500">Total Artículos</span>
            <FileText className="w-4 h-4 text-slate-400" />
          </div>
          <p className="text-2xl font-black text-slate-900 mt-2">{articles.length}</p>
          <span className="text-[11px] text-slate-400">En base de datos SQLite</span>
        </div>

        <div className="p-4 bg-white rounded-xl border border-slate-200 shadow-xs">
          <div className="flex items-center justify-between">
            <span className="text-xs font-semibold text-emerald-600">Publicados</span>
            <CheckCircle2 className="w-4 h-4 text-emerald-500" />
          </div>
          <p className="text-2xl font-black text-emerald-700 mt-2">{publishedCount}</p>
          <span className="text-[11px] text-emerald-600">Visibles para lectores</span>
        </div>

        <div className="p-4 bg-white rounded-xl border border-slate-200 shadow-xs">
          <div className="flex items-center justify-between">
            <span className="text-xs font-semibold text-amber-600">Borradores</span>
            <AlertTriangle className="w-4 h-4 text-amber-500" />
          </div>
          <p className="text-2xl font-black text-amber-700 mt-2">{draftCount}</p>
          <span className="text-[11px] text-amber-600">Pendientes de revisión</span>
        </div>

        <div className="p-4 bg-white rounded-xl border border-slate-200 shadow-xs">
          <div className="flex items-center justify-between">
            <span className="text-xs font-semibold text-indigo-600">Categorías</span>
            <FolderOpen className="w-4 h-4 text-indigo-500" />
          </div>
          <p className="text-2xl font-black text-indigo-700 mt-2">{CATEGORIES.length}</p>
          <span className="text-[11px] text-indigo-600">Trámites, Python, Móviles...</span>
        </div>
      </div>

      {/* Filtros y Buscador */}
      <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-xs mb-6">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-3">
          <div className="md:col-span-2 relative">
            <Search className="w-4 h-4 text-slate-400 absolute left-3 top-3" />
            <input
              type="text"
              placeholder="Buscar por título o slug..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full pl-9 pr-3 py-2 text-xs sm:text-sm border border-slate-300 rounded-lg focus:ring-2 focus:ring-indigo-500"
            />
          </div>

          <div>
            <select
              value={categoryFilter}
              onChange={(e) => setCategoryFilter(e.target.value)}
              className="w-full py-2 px-3 text-xs sm:text-sm border border-slate-300 rounded-lg focus:ring-2 focus:ring-indigo-500"
            >
              <option value="all">Todas las Categorías</option>
              {CATEGORIES.map(c => (
                <option key={c.slug} value={c.slug}>{c.name}</option>
              ))}
            </select>
          </div>

          <div>
            <select
              value={statusFilter}
              onChange={(e) => setStatusFilter(e.target.value)}
              className="w-full py-2 px-3 text-xs sm:text-sm border border-slate-300 rounded-lg focus:ring-2 focus:ring-indigo-500"
            >
              <option value="all">Todos los Estados</option>
              <option value="Publicado">Publicado</option>
              <option value="Borrador">Borrador</option>
            </select>
          </div>
        </div>
      </div>

      {/* Tabla de Artículos con botón de Editar destacado */}
      <div className="bg-white rounded-xl border border-slate-200 shadow-xs overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="bg-slate-50 border-b border-slate-200 text-[11px] font-bold uppercase tracking-wider text-slate-500">
                <th className="py-3 px-4 w-12 text-center">ID</th>
                <th className="py-3 px-4 w-20">Miniatura</th>
                <th className="py-3 px-4">Título & Slug</th>
                <th className="py-3 px-4">Categoría</th>
                <th className="py-3 px-4">Fecha</th>
                <th className="py-3 px-4">Estado</th>
                <th className="py-3 px-4 text-right">Acciones</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100 text-xs sm:text-sm">
              {filteredArticles.length === 0 ? (
                <tr>
                  <td colSpan={7} className="text-center py-10 text-slate-500">
                    No se encontraron artículos con los filtros seleccionados.
                  </td>
                </tr>
              ) : (
                filteredArticles.map((article) => {
                  const category = CATEGORIES.find(c => c.slug === article.category_slug);
                  return (
                    <tr key={article.id} className="hover:bg-slate-50/80 transition-colors">
                      <td className="py-3 px-4 text-center font-mono text-xs font-semibold text-slate-500">
                        #{article.id}
                      </td>
                      <td className="py-3 px-4">
                        <div className="w-14 h-10 rounded-md overflow-hidden bg-slate-100 border border-slate-200">
                          <img
                            src={article.featured_image}
                            alt=""
                            className="w-full h-full object-cover"
                          />
                        </div>
                      </td>
                      <td className="py-3 px-4 max-w-xs sm:max-w-md">
                        <div className="font-semibold text-slate-900 line-clamp-1 hover:text-indigo-600 cursor-pointer" onClick={() => onView(article)}>
                          {article.title}
                        </div>
                        <div className="text-[11px] font-mono text-slate-400 truncate">
                          /{article.slug}
                        </div>
                      </td>
                      <td className="py-3 px-4 whitespace-nowrap">
                        <span className="inline-block px-2 py-0.5 rounded text-[11px] font-medium bg-slate-100 text-slate-700 border border-slate-200">
                          {category?.name || article.category_slug}
                        </span>
                      </td>
                      <td className="py-3 px-4 whitespace-nowrap text-xs text-slate-500">
                        {new Date(article.created_at).toLocaleDateString('es-ES', { day: '2-digit', month: 'short' })}
                      </td>
                      <td className="py-3 px-4 whitespace-nowrap">
                        <span className={`inline-flex items-center px-2 py-0.5 rounded-full text-[11px] font-semibold ${
                          article.status === 'Publicado'
                            ? 'bg-emerald-50 text-emerald-700 border border-emerald-200'
                            : 'bg-amber-50 text-amber-700 border border-amber-200'
                        }`}>
                          {article.status}
                        </span>
                      </td>
                      <td className="py-3 px-4 whitespace-nowrap text-right">
                        <div className="flex items-center justify-end gap-1.5">
                          {/* BOTÓN EDITAR - TAREA 1 */}
                          <button
                            onClick={() => onEdit(article)}
                            title="Editar artículo e imagen"
                            className="inline-flex items-center gap-1 px-2.5 py-1.5 text-xs font-semibold text-indigo-700 bg-indigo-50 hover:bg-indigo-100 border border-indigo-200 rounded-lg transition-colors"
                          >
                            <Edit3 className="w-3.5 h-3.5" />
                            <span>Editar</span>
                          </button>

                          {/* Botón Ver */}
                          <button
                            onClick={() => onView(article)}
                            title="Ver en el blog público"
                            className="p-1.5 text-slate-500 hover:text-slate-700 hover:bg-slate-100 rounded-lg transition-colors"
                          >
                            <Eye className="w-4 h-4" />
                          </button>

                          {/* Botón Eliminar */}
                          <button
                            onClick={() => setArticleToDelete(article)}
                            title="Eliminar de la base de datos"
                            className="p-1.5 text-slate-400 hover:text-rose-600 hover:bg-rose-50 rounded-lg transition-colors"
                          >
                            <Trash2 className="w-4 h-4" />
                          </button>
                        </div>
                      </td>
                    </tr>
                  );
                })
              )}
            </tbody>
          </table>
        </div>
        
        <div className="p-4 bg-slate-50 border-t border-slate-200 flex items-center justify-between text-xs text-slate-500">
          <span>Mostrando {filteredArticles.length} de {articles.length} artículos</span>
          <span className="font-mono">SQLite site.db (Tabla: Article)</span>
        </div>
      </div>

      {/* Modal de confirmación para eliminar */}
      {articleToDelete && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-xs">
          <div className="bg-white rounded-2xl p-6 max-w-md w-full shadow-2xl border border-slate-200">
            <div className="flex items-center gap-3 text-rose-600 mb-3">
              <div className="w-10 h-10 rounded-full bg-rose-50 flex items-center justify-center">
                <Trash2 className="w-5 h-5 text-rose-600" />
              </div>
              <h3 className="text-lg font-bold text-slate-900">¿Eliminar artículo?</h3>
            </div>
            
            <p className="text-xs sm:text-sm text-slate-600 mb-2">
              Estás a punto de eliminar permanentemente:
            </p>
            <p className="font-semibold text-slate-800 text-sm p-3 bg-slate-50 rounded-lg border border-slate-200 mb-6">
              "{articleToDelete.title}"
            </p>

            <div className="flex items-center justify-end gap-3">
              <button
                onClick={() => setArticleToDelete(null)}
                className="px-4 py-2 text-xs sm:text-sm font-medium text-slate-600 hover:bg-slate-100 rounded-lg transition-colors"
              >
                Cancelar
              </button>
              <button
                onClick={() => {
                  onDelete(articleToDelete.id);
                  setArticleToDelete(null);
                }}
                className="px-4 py-2 text-xs sm:text-sm font-semibold text-white bg-rose-600 hover:bg-rose-700 rounded-lg transition-colors"
              >
                Sí, Eliminar de SQLite
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
