import React, { useState } from 'react';
import { Article } from './types';
import { INITIAL_ARTICLES, CATEGORIES } from './data/seedArticles';
import { Navbar } from './components/Navbar';
import { Footer } from './components/Footer';
import { ArticleCard } from './components/ArticleCard';
import { ArticleDetail } from './components/ArticleDetail';
import { AdminPanel } from './components/AdminPanel';
import { AdminEditArticle } from './components/AdminEditArticle';
import { AdminNewArticle } from './components/AdminNewArticle';
import { ProductionCenter } from './components/ProductionCenter';
import { LegalPages } from './components/LegalPages';
import { CookieBanner } from './components/CookieBanner';
import { 
  ShieldCheck, 
  Terminal, 
  Search, 
  CheckCircle2, 
  BookOpen,
  ChevronLeft,
  ChevronRight
} from 'lucide-react';

const ARTICLES_PER_PAGE = 9;

export default function App() {
  const [articles, setArticles] = useState<Article[]>(INITIAL_ARTICLES);
  const [currentView, setCurrentView] = useState<
    'home' | 'article-detail' | 'admin' | 'admin-edit' | 'admin-new' | 'production' | 'legal'
  >('home');
  const [selectedArticle, setSelectedArticle] = useState<Article | null>(null);
  const [editingArticle, setEditingArticle] = useState<Article | null>(null);
  const [selectedCategory, setSelectedCategory] = useState<string>('all');
  const [legalPage, setLegalPage] = useState<'about' | 'privacy' | 'cookies' | 'terms' | 'contact'>('about');
  const [searchQuery, setSearchQuery] = useState('');
  const [currentPage, setCurrentPage] = useState<number>(1);

  // Artículos filtrados para la vista pública
  const publishedArticles = articles.filter(a => a.status === 'Publicado');

  const filteredArticles = publishedArticles.filter(art => {
    const matchesCategory = selectedCategory === 'all' || art.category_slug === selectedCategory;
    const matchesSearch = art.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
                          art.excerpt.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesCategory && matchesSearch;
  });

  const totalPages = Math.max(1, Math.ceil(filteredArticles.length / ARTICLES_PER_PAGE));
  const paginatedArticles = filteredArticles.slice(
    (currentPage - 1) * ARTICLES_PER_PAGE,
    currentPage * ARTICLES_PER_PAGE
  );

  const handlePageChange = (page: number) => {
    setCurrentPage(page);
    const element = document.getElementById('articles-grid-top');
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    } else {
      window.scrollTo({ top: 350, behavior: 'smooth' });
    }
  };

  // Manejo de acciones del CMS Admin
  const handleEditClick = (article: Article) => {
    setEditingArticle(article);
    setCurrentView('admin-edit');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleSaveEdit = (updatedArticle: Article) => {
    setArticles(prev => prev.map(a => a.id === updatedArticle.id ? updatedArticle : a));
    if (selectedArticle && selectedArticle.id === updatedArticle.id) {
      setSelectedArticle(updatedArticle);
    }
    setEditingArticle(null);
    setCurrentView('admin');
  };

  const handleDeleteArticle = (id: number) => {
    setArticles(prev => prev.filter(a => a.id !== id));
  };

  const handleCreateArticle = (newArtData: Omit<Article, 'id'>) => {
    const nextId = Math.max(...articles.map(a => a.id), 0) + 1;
    const newArt: Article = {
      id: nextId,
      ...newArtData
    };
    setArticles([newArt, ...articles]);
    setCurrentView('admin');
  };

  const handleViewArticle = (article: Article) => {
    setSelectedArticle(article);
    setCurrentView('article-detail');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleCategoryClick = (slug: string) => {
    setSelectedCategory(slug);
    setCurrentView('home');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleOpenLegal = (page: 'about' | 'privacy' | 'cookies' | 'terms' | 'contact') => {
    setLegalPage(page);
    setCurrentView('legal');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <div className="min-h-screen flex flex-col bg-slate-50 text-slate-900 font-sans selection:bg-indigo-500 selection:text-white">
      
      {/* Navbar Superior Limpio y Profesional */}
      <Navbar
        currentView={currentView}
        onNavigateHome={() => {
          setSelectedCategory('all');
          setCurrentView('home');
        }}
        onSelectCategory={handleCategoryClick}
        selectedCategory={selectedCategory}
        onNavigateLegal={handleOpenLegal}
      />

      {/* Contenido Principal según la vista activa */}
      <main className="flex-1">
        {currentView === 'home' && (
          <div>
            {/* HERO SECTION DE ALTO VALOR TÉCNICO */}
            <section className="relative overflow-hidden bg-gradient-to-b from-white via-indigo-50/20 to-slate-50 border-b border-slate-200/80 pt-12 pb-14">
              <div className="max-w-7xl mx-auto px-4 sm:px-6">
                
                {/* Badge de Autor Verificado */}
                <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full text-xs font-semibold bg-indigo-50 border border-indigo-200 text-indigo-700 mb-6 shadow-xs">
                  <ShieldCheck className="w-4 h-4 text-emerald-600" />
                  <span>Por Andrés • Estudiante de Ingeniería de Sistemas (CUC Barranquilla)</span>
                </div>

                <div className="max-w-3xl">
                  <h1 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-slate-900 tracking-tight leading-tight mb-4">
                    Tutoriales técnicos reales para resolver problemas del día a día.
                  </h1>
                  <p className="text-base sm:text-lg text-slate-600 leading-relaxed mb-6 font-normal">
                    Sin rodeos ni explicaciones inútiles. Guías completas paso a paso de trámites digitales, programación práctica en <strong>Python & Flet</strong>, optimización avanzada de Android y herramientas verificadas en laboratorio con más de 1.500 palabras por artículo.
                  </p>

                  {/* Buscador de artículos */}
                  <div className="relative max-w-lg mb-4">
                    <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-3.5" />
                    <input
                      type="text"
                      placeholder="Buscar tutorial (ej. RUT, Flet, ADB, Windows 11)..."
                      value={searchQuery}
                      onChange={(e) => setSearchQuery(e.target.value)}
                      className="w-full pl-10 pr-4 py-2.5 text-sm bg-white border border-slate-300 rounded-xl shadow-xs focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
                    />
                    {searchQuery && (
                      <button
                        onClick={() => setSearchQuery('')}
                        className="absolute right-3 top-3 text-xs text-slate-400 hover:text-slate-600"
                      >
                        Limpiar
                      </button>
                    )}
                  </div>
                </div>

                {/* Filtros de Categoría */}
                <div className="flex flex-wrap items-center gap-2 mt-6 pt-4 border-t border-slate-200/60">
                  <span className="text-xs font-bold uppercase tracking-wider text-slate-400 mr-2">Filtrar:</span>
                  <button
                    onClick={() => {
                      setSelectedCategory('all');
                      setCurrentPage(1);
                    }}
                    className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold transition-all ${
                      selectedCategory === 'all'
                        ? 'bg-slate-900 text-white shadow-xs'
                        : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-100'
                    }`}
                  >
                    Todos ({publishedArticles.length})
                  </button>
                  {CATEGORIES.map((c) => {
                    const count = publishedArticles.filter(a => a.category_slug === c.slug).length;
                    return (
                      <button
                        key={c.slug}
                        onClick={() => {
                          setSelectedCategory(c.slug);
                          setCurrentPage(1);
                        }}
                        className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold transition-all ${
                          selectedCategory === c.slug
                            ? 'bg-indigo-600 text-white shadow-xs'
                            : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-100'
                        }`}
                      >
                        {c.name} ({count})
                      </button>
                    );
                  })}
                </div>

              </div>
            </section>

            {/* SECCIÓN PRINCIPAL: ARTÍCULOS DESTACADOS Y GRILLA */}
            <div id="articles-grid-top" className="max-w-7xl mx-auto px-4 sm:px-6 py-10">
              
              {/* Título de Sección */}
              <div className="flex items-center justify-between mb-8 pb-3 border-b border-slate-200">
                <div>
                  <h2 className="text-2xl font-bold text-slate-900 tracking-tight">
                    {selectedCategory === 'all' 
                      ? 'Últimos Tutoriales Publicados' 
                      : CATEGORIES.find(c => c.slug === selectedCategory)?.name}
                  </h2>
                  <p className="text-xs text-slate-500 mt-0.5">
                    {selectedCategory === 'all'
                      ? 'Guías extensas paso a paso probadas en laboratorio'
                      : CATEGORIES.find(c => c.slug === selectedCategory)?.description}
                  </p>
                </div>

                <span className="text-xs font-semibold text-slate-500 bg-slate-100 px-2.5 py-1 rounded-md">
                  {filteredArticles.length} guías disponibles
                </span>
              </div>

              {/* Grilla de Artículos */}
              {filteredArticles.length === 0 ? (
                <div className="text-center py-16 bg-white rounded-2xl border border-slate-200 p-8">
                  <Terminal className="w-12 h-12 text-slate-300 mx-auto mb-3" />
                  <h3 className="text-lg font-bold text-slate-700">No encontramos resultados para tu búsqueda</h3>
                  <p className="text-xs text-slate-500 mt-1 max-w-sm mx-auto">
                    Intenta cambiar la categoría o prueba buscando términos como "RUT", "Flet", "ADB" o "Windows".
                  </p>
                  <button
                    onClick={() => { setSelectedCategory('all'); setSearchQuery(''); setCurrentPage(1); }}
                    className="mt-4 px-4 py-2 text-xs font-semibold text-indigo-600 bg-indigo-50 rounded-lg hover:bg-indigo-100"
                  >
                    Restablecer filtros
                  </button>
                </div>
              ) : (
                <>
                  <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 sm:gap-8">
                    {paginatedArticles.map((article, idx) => (
                      <ArticleCard
                        key={article.id}
                        article={article}
                        onSelect={handleViewArticle}
                        featured={idx === 0 && selectedCategory === 'all' && !searchQuery && currentPage === 1}
                      />
                    ))}
                  </div>

                  {/* Paginación */}
                  {totalPages > 1 && (
                    <div className="mt-12 flex flex-col sm:flex-row items-center justify-between gap-4 border-t border-slate-200 pt-6">
                      <div className="text-xs text-slate-500 font-medium">
                        Mostrando <span className="font-semibold text-slate-700">{(currentPage - 1) * ARTICLES_PER_PAGE + 1}</span> - <span className="font-semibold text-slate-700">{Math.min(currentPage * ARTICLES_PER_PAGE, filteredArticles.length)}</span> de <span className="font-semibold text-slate-700">{filteredArticles.length}</span> tutoriales
                      </div>

                      <div className="flex items-center gap-1.5">
                        <button
                          onClick={() => handlePageChange(currentPage - 1)}
                          disabled={currentPage === 1}
                          className="px-3 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-1 border border-slate-200 bg-white text-slate-700 hover:bg-slate-50 disabled:opacity-40 disabled:cursor-not-allowed transition-all"
                          aria-label="Página anterior"
                        >
                          <ChevronLeft className="w-3.5 h-3.5" />
                          <span>Anterior</span>
                        </button>

                        {Array.from({ length: totalPages }, (_, i) => i + 1).map((pageNum) => (
                          <button
                            key={pageNum}
                            onClick={() => handlePageChange(pageNum)}
                            className={`w-8 h-8 rounded-lg text-xs font-bold transition-all ${
                              currentPage === pageNum
                                ? 'bg-indigo-600 text-white shadow-xs'
                                : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-50'
                            }`}
                          >
                            {pageNum}
                          </button>
                        ))}

                        <button
                          onClick={() => handlePageChange(currentPage + 1)}
                          disabled={currentPage === totalPages}
                          className="px-3 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-1 border border-slate-200 bg-white text-slate-700 hover:bg-slate-50 disabled:opacity-40 disabled:cursor-not-allowed transition-all"
                          aria-label="Página siguiente"
                        >
                          <span>Siguiente</span>
                          <ChevronRight className="w-3.5 h-3.5" />
                        </button>
                      </div>
                    </div>
                  )}
                </>
              )}

              {/* Caja de Compromiso Editorial y Rigor */}
              <section className="mt-14 bg-white rounded-2xl p-6 sm:p-8 border border-slate-200 shadow-xs">
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6 items-center">
                  <div className="md:col-span-2 space-y-2">
                    <span className="text-xs font-bold uppercase tracking-wider text-indigo-600">
                      Rigor Editorial & Verificación
                    </span>
                    <h3 className="text-xl font-bold text-slate-900">
                      ¿Por qué confiar en Tecnología para Gente Normal?
                    </h3>
                    <p className="text-xs sm:text-sm text-slate-600 leading-relaxed">
                      Cada tutorial supera las 1.500 palabras de contenido técnico y es redactado tras ejecutar pruebas exhaustivas en hardware físico en nuestro laboratorio en Barranquilla por Andrés, estudiante de Ingeniería de Sistemas en la Universidad de la Costa (CUC). No publicamos traducciones automáticas ni artículos de relleno sintético.
                    </p>
                  </div>

                  <div className="p-4 bg-slate-50 rounded-xl border border-slate-200 space-y-2 text-xs">
                    <div className="flex items-center gap-2 text-emerald-700 font-semibold">
                      <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
                      <span>Artículos completos (+1.500 palabras)</span>
                    </div>
                    <div className="flex items-center gap-2 text-emerald-700 font-semibold">
                      <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
                      <span>Comandos y código probado en vivo</span>
                    </div>
                    <div className="flex items-center gap-2 text-emerald-700 font-semibold">
                      <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
                      <span>Sello "💡 Probado por nosotros" con métricas</span>
                    </div>
                  </div>
                </div>
              </section>

            </div>
          </div>
        )}

        {currentView === 'article-detail' && selectedArticle && (
          <ArticleDetail
            article={selectedArticle}
            onBack={() => setCurrentView('home')}
            onCategorySelect={(slug) => {
              setSelectedCategory(slug);
              setCurrentView('home');
            }}
            onOpenAuthorProfile={() => handleOpenLegal('about')}
          />
        )}

        {currentView === 'admin' && (
          <AdminPanel
            articles={articles}
            onEdit={handleEditClick}
            onDelete={handleDeleteArticle}
            onView={handleViewArticle}
            onCreateNew={() => setCurrentView('admin-new')}
            onOpenProductionCenter={() => setCurrentView('production')}
            onGoToHome={() => setCurrentView('home')}
          />
        )}

        {currentView === 'admin-edit' && editingArticle && (
          <AdminEditArticle
            article={editingArticle}
            onSave={handleSaveEdit}
            onCancel={() => setCurrentView('admin')}
          />
        )}

        {currentView === 'admin-new' && (
          <AdminNewArticle
            onSave={handleCreateArticle}
            onCancel={() => setCurrentView('admin')}
          />
        )}

        {currentView === 'production' && (
          <ProductionCenter />
        )}

        {currentView === 'legal' && (
          <LegalPages
            pageType={legalPage}
            onBack={() => setCurrentView('home')}
          />
        )}
      </main>

      {/* Banner de Consentimiento de Cookies (Discreto y no invasivo) */}
      <CookieBanner onOpenCookiesPolicy={() => handleOpenLegal('cookies')} />

      {/* Footer Público */}
      <Footer
        onSelectCategory={handleCategoryClick}
        onNavigateLegal={handleOpenLegal}
      />

    </div>
  );
}
