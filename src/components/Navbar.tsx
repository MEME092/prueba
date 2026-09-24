import React, { useState } from 'react';
import { CATEGORIES } from '../data/seedArticles';
import { Terminal, Shield, Menu, X, ChevronRight, User, Mail } from 'lucide-react';

interface NavbarProps {
  currentView: string;
  onNavigateHome: () => void;
  onSelectCategory: (slug: string) => void;
  selectedCategory: string;
  onNavigateLegal: (page: 'about' | 'privacy' | 'cookies' | 'terms' | 'contact') => void;
}

export const Navbar: React.FC<NavbarProps> = ({
  currentView,
  onNavigateHome,
  onSelectCategory,
  selectedCategory,
  onNavigateLegal
}) => {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  return (
    <header className="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200/80 shadow-xs">
      <div className="max-w-7xl mx-auto px-4 sm:px-6">
        <div className="flex items-center justify-between h-16">
          
          {/* Logo y Nombre del Blog */}
          <div 
            onClick={() => {
              onSelectCategory('all');
              onNavigateHome();
            }}
            className="flex items-center gap-3 cursor-pointer group"
          >
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-indigo-600 to-indigo-500 text-white flex items-center justify-center shadow-md group-hover:shadow-indigo-200 group-hover:scale-105 transition-all">
              <Terminal className="w-5 h-5 text-indigo-100" />
            </div>
            <div>
              <span className="font-extrabold text-base sm:text-lg text-slate-900 tracking-tight block leading-tight group-hover:text-indigo-600 transition-colors">
                Tecnología para Gente Normal
              </span>
              <span className="text-[11px] text-slate-500 flex items-center gap-1 font-medium">
                <Shield className="w-3 h-3 text-emerald-600 inline" />
                Por Andrés • CUC Barranquilla
              </span>
            </div>
          </div>

          {/* Menú Desktop Principal */}
          <nav className="hidden lg:flex items-center gap-1">
            <button
              onClick={() => {
                onSelectCategory('all');
                onNavigateHome();
              }}
              className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition-colors ${
                currentView === 'home' && selectedCategory === 'all'
                  ? 'bg-slate-900 text-white'
                  : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'
              }`}
            >
              Inicio
            </button>
            {CATEGORIES.map((cat) => (
              <button
                key={cat.slug}
                onClick={() => {
                  onSelectCategory(cat.slug);
                  onNavigateHome();
                }}
                className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition-colors ${
                  currentView === 'home' && selectedCategory === cat.slug
                    ? 'bg-indigo-600 text-white'
                    : 'text-slate-600 hover:text-indigo-600 hover:bg-slate-100'
                }`}
              >
                {cat.name}
              </button>
            ))}
            <button
              onClick={() => onNavigateLegal('about')}
              className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition-colors ${
                currentView === 'legal'
                  ? 'text-indigo-600 font-bold bg-indigo-50'
                  : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'
              }`}
            >
              Sobre el Autor
            </button>
            <button
              onClick={() => onNavigateLegal('contact')}
              className="px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition-colors"
            >
              Contacto
            </button>
          </nav>

          {/* Botón Móvil */}
          <div className="lg:hidden flex items-center gap-2">
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="p-2 text-slate-600 hover:text-slate-900 hover:bg-slate-100 rounded-lg"
              aria-label="Abrir menú"
            >
              {mobileMenuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
            </button>
          </div>

        </div>
      </div>

      {/* Menú Desplegable Móvil */}
      {mobileMenuOpen && (
        <div className="lg:hidden border-t border-slate-200 bg-white px-4 py-3 space-y-2 shadow-lg animate-fade-in">
          <div className="text-[11px] font-bold uppercase tracking-wider text-slate-400 px-2 py-1">
            Secciones
          </div>
          <button
            onClick={() => {
              onSelectCategory('all');
              onNavigateHome();
              setMobileMenuOpen(false);
            }}
            className="w-full text-left px-3 py-2 text-xs font-semibold rounded-lg hover:bg-slate-100 text-slate-700"
          >
            Todas las publicaciones
          </button>
          {CATEGORIES.map((cat) => (
            <button
              key={cat.slug}
              onClick={() => {
                onSelectCategory(cat.slug);
                onNavigateHome();
                setMobileMenuOpen(false);
              }}
              className="w-full text-left px-3 py-2 text-xs font-semibold rounded-lg hover:bg-slate-100 text-slate-700 flex items-center justify-between"
            >
              <span>{cat.name}</span>
              <ChevronRight className="w-3.5 h-3.5 text-slate-400" />
            </button>
          ))}
          <div className="pt-2 border-t border-slate-100 flex flex-col gap-1.5">
            <button
              onClick={() => {
                onNavigateLegal('about');
                setMobileMenuOpen(false);
              }}
              className="w-full text-left px-3 py-2 text-xs font-semibold rounded-lg hover:bg-slate-100 text-slate-700 flex items-center gap-2"
            >
              <User className="w-4 h-4 text-indigo-600" />
              <span>Sobre Andrés (Autor)</span>
            </button>
            <button
              onClick={() => {
                onNavigateLegal('contact');
                setMobileMenuOpen(false);
              }}
              className="w-full text-left px-3 py-2 text-xs font-semibold rounded-lg hover:bg-slate-100 text-slate-700 flex items-center gap-2"
            >
              <Mail className="w-4 h-4 text-indigo-600" />
              <span>Contacto Directo</span>
            </button>
          </div>
        </div>
      )}
    </header>
  );
};
