import React from 'react';
import { Terminal, Shield } from 'lucide-react';

interface NavbarProps {
  onNavigateHome: () => void;
}

export const Navbar: React.FC<NavbarProps> = ({
  onNavigateHome
}) => {
  return (
    <header className="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200/80 shadow-xs">
      <div className="max-w-7xl mx-auto px-4 sm:px-6">
        <div className="flex items-center justify-between h-16">
          
          {/* Logo y Nombre del Blog */}
          <div 
            onClick={onNavigateHome}
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

        </div>
      </div>
    </header>
  );
};
