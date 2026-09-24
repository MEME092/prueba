import React, { useState, useEffect } from 'react';
import { Cookie, ShieldCheck, Check, ExternalLink } from 'lucide-react';

interface CookieBannerProps {
  onOpenCookiesPolicy: () => void;
}

export const CookieBanner: React.FC<CookieBannerProps> = ({ onOpenCookiesPolicy }) => {
  // Cada vez que el usuario entra al portal (nueva visita / recarga), debe aceptar las cookies
  const [accepted, setAccepted] = useState(false);
  const [showNotification, setShowNotification] = useState(false);
  const [consentType, setConsentType] = useState<'all' | 'essential' | null>(null);

  useEffect(() => {
    // Al entrar al sitio, siempre se exige la confirmación activa del usuario
    setAccepted(false);
  }, []);

  const handleAccept = (type: 'all' | 'essential') => {
    setConsentType(type);
    setAccepted(true);
    setShowNotification(true);

    // Ocultar notificación tras 3.5 segundos
    setTimeout(() => {
      setShowNotification(false);
    }, 3500);
  };

  return (
    <>
      {/* Notificación flotante de confirmación tras aceptar */}
      {showNotification && (
        <div className="fixed bottom-5 right-5 z-50 bg-emerald-900/95 text-emerald-100 px-4 py-3 rounded-2xl shadow-xl border border-emerald-700/80 flex items-center gap-2.5 text-xs font-semibold backdrop-blur-md transition-all animate-fade-in">
          <Check className="w-4 h-4 text-emerald-400" />
          <span>
            {consentType === 'all'
              ? '✓ Preferencias aceptadas: Todas las cookies habilitadas.'
              : '✓ Preferencias aceptadas: Solo cookies técnicas esenciales habilitadas.'}
          </span>
        </div>
      )}

      {/* Banner / Modal exigido cada vez que se entra al portal */}
      {!accepted && (
        <aside
          aria-label="Consentimiento obligatorio de cookies"
          className="fixed bottom-0 inset-x-0 sm:bottom-6 sm:right-6 sm:left-auto sm:max-w-xl z-50 p-4 sm:p-0"
        >
          <div className="bg-slate-900/98 text-slate-100 p-5 sm:p-6 rounded-3xl shadow-2xl border border-indigo-500/40 backdrop-blur-xl ring-1 ring-white/10 space-y-4">
            <div className="flex items-start gap-3.5">
              <div className="p-3 rounded-2xl bg-indigo-600/30 text-indigo-400 shrink-0 mt-0.5 border border-indigo-500/30">
                <Cookie className="w-6 h-6 animate-pulse" />
              </div>
              <div className="space-y-1.5 flex-1">
                <div className="flex items-center gap-2">
                  <h3 className="text-sm font-bold text-white tracking-tight">
                    Aviso de Cookies
                  </h3>
                  <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">
                    Obligatorio al entrar
                  </span>
                </div>
                <p className="text-xs text-slate-300 leading-relaxed">
                  En <strong>Tecnología para Gente Normal</strong> utilizamos cookies técnicas esenciales y analíticas para recordar preferencias y garantizar el correcto funcionamiento del portal según la Ley 1581.
                </p>
              </div>
            </div>

            {/* Opciones y botones de aceptación */}
            <div className="pt-2 border-t border-slate-800/80 flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3">
              <button
                type="button"
                onClick={onOpenCookiesPolicy}
                className="text-[11px] text-indigo-300 hover:text-indigo-200 underline font-semibold inline-flex items-center gap-1 justify-center sm:justify-start"
              >
                <span>Leer Política de Cookies</span>
                <ExternalLink className="w-3 h-3" />
              </button>

              <div className="flex flex-wrap items-center gap-2">
                <button
                  type="button"
                  onClick={() => handleAccept('essential')}
                  className="flex-1 sm:flex-none px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-xl text-xs font-semibold transition-all border border-slate-700"
                >
                  Solo necesarias
                </button>
                <button
                  type="button"
                  onClick={() => handleAccept('all')}
                  className="flex-1 sm:flex-none px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white rounded-xl text-xs font-bold transition-all shadow-md shadow-indigo-600/30 flex items-center justify-center gap-1.5"
                >
                  <ShieldCheck className="w-3.5 h-3.5" />
                  <span>Aceptar todas</span>
                </button>
              </div>
            </div>
          </div>
        </aside>
      )}
    </>
  );
};
