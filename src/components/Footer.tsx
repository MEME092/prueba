import React from 'react';
import { CATEGORIES } from '../data/seedArticles';
import { Terminal, Shield, Heart } from 'lucide-react';

interface FooterProps {
  onSelectCategory: (slug: string) => void;
  onNavigateLegal: (page: 'about' | 'privacy' | 'cookies' | 'terms' | 'contact') => void;
}

export const Footer: React.FC<FooterProps> = ({
  onSelectCategory,
  onNavigateLegal
}) => {
  return (
    <footer className="bg-slate-900 text-slate-300 mt-20 border-t border-slate-800">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 py-14">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          
          {/* Columna 1: Identidad y Autor */}
          <div className="md:col-span-2 space-y-4">
            <div className="flex items-center gap-2.5">
              <div className="w-8 h-8 rounded-xl bg-indigo-600 text-white flex items-center justify-center font-bold shadow-md">
                <Terminal className="w-4 h-4" />
              </div>
              <span className="text-lg font-bold text-white tracking-tight">
                Tecnología para Gente Normal
              </span>
            </div>

            <p className="text-xs text-slate-400 max-w-md leading-relaxed">
              Publicación técnica independiente dedicada a guías prácticas de software, interfaces en Python y Flet, optimización de sistemas operativos y resolución de trámites digitales sin intermediarios. Editado por <strong>Andrés</strong>, estudiante de Ingeniería de Sistemas en la Universidad de la Costa (CUC), Barranquilla.
            </p>

            <div className="p-3.5 bg-slate-800/80 rounded-2xl border border-slate-700/60 text-xs space-y-1">
              <div className="flex items-center gap-1.5 text-emerald-400 font-semibold">
                <Shield className="w-3.5 h-3.5" />
                <span>Compromiso de Calidad Editorial</span>
              </div>
              <p className="text-[11px] text-slate-400 leading-normal">
                Cada tutorial publicado supera las 1.500 palabras y ha sido ejecutado paso a paso en hardware físico en nuestro laboratorio. No utilizamos contenido autogenerado.
              </p>
            </div>
          </div>

          {/* Columna 2: Categorías Principales */}
          <div>
            <h4 className="text-xs font-bold uppercase tracking-wider text-slate-100 mb-3">
              Temáticas
            </h4>
            <ul className="space-y-2 text-xs">
              {CATEGORIES.map((c) => (
                <li key={c.slug}>
                  <button
                    onClick={() => onSelectCategory(c.slug)}
                    className="text-slate-400 hover:text-white transition-colors text-left"
                  >
                    {c.name}
                  </button>
                </li>
              ))}
            </ul>
          </div>

          {/* Columna 3: Información Legal y Contacto */}
          <div>
            <h4 className="text-xs font-bold uppercase tracking-wider text-slate-100 mb-3">
              Legal & Autor
            </h4>
            <ul className="space-y-2 text-xs">
              <li>
                <button
                  onClick={() => onNavigateLegal('about')}
                  className="text-slate-400 hover:text-white transition-colors"
                >
                  Sobre el Autor (Andrés)
                </button>
              </li>
              <li>
                <button
                  onClick={() => onNavigateLegal('privacy')}
                  className="text-slate-400 hover:text-white transition-colors"
                >
                  Política de Privacidad
                </button>
              </li>
              <li>
                <button
                  onClick={() => onNavigateLegal('cookies')}
                  className="text-slate-400 hover:text-white transition-colors"
                >
                  Política de Cookies
                </button>
              </li>
              <li>
                <button
                  onClick={() => onNavigateLegal('terms')}
                  className="text-slate-400 hover:text-white transition-colors"
                >
                  Aviso Legal y Descargo Técnico
                </button>
              </li>
              <li>
                <button
                  onClick={() => onNavigateLegal('contact')}
                  className="text-slate-400 hover:text-white transition-colors"
                >
                  Contacto Directo
                </button>
              </li>
            </ul>
          </div>

        </div>

        {/* Barra Inferior */}
        <div className="mt-12 pt-6 border-t border-slate-800 flex flex-col sm:flex-row items-center justify-between text-xs text-slate-500 gap-4">
          <p>
            © {new Date().getFullYear()} Tecnología para Gente Normal. Diseñado y probado en Barranquilla, Colombia.
          </p>
          <div className="flex items-center gap-2 text-[11px]">
            <span>Hecho con dedicación para usuarios y estudiantes</span>
          </div>
        </div>
      </div>
    </footer>
  );
};
