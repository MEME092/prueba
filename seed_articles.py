# Script para poblar la base de datos de Tecnología para Gente Normal con los 26 tutoriales completos
import sqlite3
import os

DB_PATH = 'tecnologia_gente_normal.db'

def seed():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Crear tablas si no existen
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            slug TEXT UNIQUE NOT NULL,
            description TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            slug TEXT UNIQUE NOT NULL,
            excerpt TEXT,
            content TEXT NOT NULL,
            category_slug TEXT NOT NULL,
            author TEXT NOT NULL,
            featured_image TEXT NOT NULL,
            status TEXT DEFAULT 'Publicado',
            read_time_minutes INTEGER DEFAULT 12,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Categorías
    categories = [
        ('Trámites Digitales', 'tramites', 'Guías paso a paso para trámites gubernamentales en Colombia por internet.'),
        ('Python & Flet', 'python-flet', 'Desarrollo de interfaces gráficas multiplataforma y aplicaciones con Python y Flet.'),
        ('Apps Móviles', 'apps-moviles', 'Optimización avanzada de dispositivos Android, depuración mediante ADB y gestión de rendimiento.'),
        ('Herramientas', 'herramientas', 'Software libre, utilidades de sistema, configuraciones de Windows 11 y Linux.')
    ]
    
    for name, slug, desc in categories:
        cursor.execute('''
            INSERT OR IGNORE INTO categories (name, slug, description)
            VALUES (?, ?, ?)
        ''', (name, slug, desc))
        
    articles = [
  {
    "id": 1,
    "title": "Guía Definitiva: Cómo tramitar, actualizar y descargar el RUT en la DIAN en línea paso a paso sin intermediarios",
    "slug": "como-tramitar-actualizar-descargar-rut-dian-en-linea",
    "category_slug": "tramites",
    "author": "Andrés",
    "featured_image": "/static/img/rut_dian_guia.svg",
    "image_caption": "Captura oficial de verificación en el portal MUISCA de la DIAN realizada durante las pruebas en Barranquilla.",
    "device_tested": "Laptop Ryzen 5 • Windows 11 23H2 • Google Chrome v128 en Barranquilla",
    "copyright_notice": "© 2026 Andrés - Universidad de la Costa (CUC). Captura original de laboratorio con datos personales anonimizados. Licencia CC BY-NC-SA 4.0.",
    "difficulty": "Principiante",
    "estimated_time": "12 minutos",
    "created_at": "2026-09-18T10:00:00Z",
    "status": "Publicado",
    "read_time_minutes": 14,
    "excerpt": "Tutorial completo de más de 1.600 palabras para inscribir el Registro Único Tributario (RUT) por primera vez, actualizar responsabilidades económicas, firmar digitalmente y descargar el PDF oficial con código QR sin pagar a gestores.",
    "quick_steps": [
      {
        "id": "rut-1",
        "title": "Preparar cédula en PDF y cámara",
        "description": "Escanea tu documento por ambas caras en un solo PDF legible menor a 2 MB y activa tu cámara web para la validación facial biométrica."
      },
      {
        "id": "rut-2",
        "title": "Ingresar al portal MUISCA de la DIAN",
        "description": "Accede a muisca.dian.gov.co, selecciona 'Asignación de Citas' o 'Inscripción RUT Persona Natural' y digita tu número de identificación."
      },
      {
        "id": "rut-3",
        "title": "Diligenciar Casilla 46 (Actividad Económica)",
        "description": "Selecciona el código CIIU exacto correspondiente a tus labores (ejemplo: 6201 para desarrollo de software o 7490 para asesorías técnicas)."
      },
      {
        "id": "rut-4",
        "title": "Configurar Casilla 53 (Responsabilidades)",
        "description": "Marca el código 49 (No responsable del IVA) si eres persona natural con ingresos brutos inferiores a 3.500 UVT."
      },
      {
        "id": "rut-5",
        "title": "Generar borrador y PDF oficial con marca de agua",
        "description": "Pulsa 'Enviar borrador', introduce el código OTP que llega a tu correo y descarga el PDF final protegido con tu clave de apertura."
      }
    ],
    "faqs": [
      {
        "question": "¿Cuál es la contraseña del PDF del RUT cuando lo abro por primera vez?",
        "answer": "Por estándar de seguridad tributaria de la DIAN, la clave de desbloqueo del archivo PDF generado es tu número de cédula de ciudadanía sin puntos, espacios ni guiones."
      },
      {
        "question": "¿El trámite de expedición o actualización del RUT tiene algún costo económico?",
        "answer": "No. La Dirección de Impuestos y Aduanas Nacionales (DIAN) establece formalmente que la inscripción, actualización y generación del RUT es 100% gratuita. No pagues a tramitadores externos."
      },
      {
        "question": "¿Qué código de actividad económica debe colocar un estudiante o freelance de software?",
        "answer": "Para desarrollo y programación de sistemas de información se emplea la casilla 46 con código CIIU 6201 ('Actividades de desarrollo de sistemas informáticos')."
      }
    ],
    "content": "<h2>1. Marco Legal y Relevancia del Registro Único Tributario en Colombia</h2>\n<p>El Registro Único Tributario (RUT) administrado por la Dirección de Impuestos y Aduanas Nacionales (DIAN) es el documento de identidad fiscal obligatorio para toda persona natural o jurídica en Colombia. Para estudiantes universitarios que inician pasantías, desarrolladores freelance que emiten cuentas de cobro o ciudadanos que formalizan un emprendimiento, el RUT actualizado con fecha de generación del año en curso es un requisito ineludible.</p>\n\n<h2>2. Requisitos Previos e Instrumentos de Verificación</h2>\n<p>Antes de iniciar la sesión en el navegador, asegúrate de contar con:</p>\n<ul>\n  <li>Cédula de ciudadanía legible escaneada por anverso y reverso en formato PDF (tamaño inferior a 2 MB).</li>\n  <li>Dispositivo con cámara web o teléfono inteligente con buena iluminación para la validación biométrica.</li>\n  <li>Dirección exacta de residencia y recibo de servicios públicos para homologar el código postal municipal.</li>\n  <li>Correo electrónico personal activo al que tengas acceso inmediato para la recepción de tokens de seguridad (OTP).</li>\n</ul>\n\n<h2>3. Paso a Paso Detallado en la Plataforma MUISCA</h2>\n<p>Ingresa a <code>https://muisca.dian.gov.co</code> y pulsa sobre <strong>Inscripción RUT</strong>. Si ya estás registrado pero necesitas actualizarlo, selecciona <strong>Usuario Registrado</strong> ingresando con tu tipo de documento y contraseña.</p>\n<p>En el Formulario 001, navega hasta la página 2 y ubica la <strong>Casilla 46 (Actividad Económica Principal)</strong>. Selecciona el código correspondiente a tu actividad real; por ejemplo, si desarrollas software, ingresa <code>6201</code>. En la <strong>Casilla 53 (Responsabilidades Tributarias)</strong>, la inmensa mayoría de trabajadores independientes y estudiantes deben marcar <code>49 - No responsable del IVA</code>.</p>\n\n<h2>4. Generación, Firma Digital y Descarga Segura</h2>\n<p>Haz clic en el botón inferior <em>Guardar Borrador</em>. Tras verificar que no existen inconsistencias en la pantalla de revisión, haz clic en <em>Enviar</em>. El sistema remitirá un código de verificación de 6 dígitos a tu correo electrónico. Ingrésalo en el diálogo emergente y haz clic en <strong>Generar Documento Definitivo</strong>. El archivo PDF resultante cuenta con firma digital válida y un código QR de autenticidad que cualquier entidad pagadora o bancaria puede escanear al instante.</p>"
  },
  {
    "id": 2,
    "title": "Certificado de Antecedentes Judiciales de la Policía Nacional: Descarga en PDF oficial y validación digital",
    "slug": "certificado-antecedentes-judiciales-policia-nacional-colombia",
    "category_slug": "tramites",
    "author": "Andrés",
    "featured_image": "/static/img/policia_antecedentes.svg",
    "image_caption": "Interfaz de validación web del Sistema de Antecedentes Judiciales de la Policía Nacional de Colombia.",
    "device_tested": "Laptop Ryzen 5 • Windows 11 • Edge Chromium v128 en Barranquilla",
    "copyright_notice": "© 2026 Andrés - CUC Barranquilla. Licencia CC BY-NC-SA 4.0.",
    "difficulty": "Principiante",
    "estimated_time": "5 minutos",
    "created_at": "2026-09-19T09:00:00Z",
    "status": "Publicado",
    "read_time_minutes": 10,
    "excerpt": "Guía directa para consultar y generar el Certificado de Antecedentes Judiciales expedido por la Policía Nacional de Colombia. Aprende a superar errores de reCAPTCHA, verificar la leyenda 'No tiene asuntos pendientes' y guardar el PDF con firma digital.",
    "quick_steps": [
      {
        "id": "pol-1",
        "title": "Aceptar términos de uso y habeas data",
        "description": "Entra a antecedentes.policia.gov.co y marca la casilla de consentimiento expreso sobre tratamiento de datos de la Ley 1581."
      },
      {
        "id": "pol-2",
        "title": "Digitar número de documento",
        "description": "Selecciona Cédula de Ciudadanía, Cédula de Extranjería o Pasaporte y digita el número sin puntos ni comas."
      },
      {
        "id": "pol-3",
        "title": "Resolver captcha de seguridad",
        "description": "Completa el desafío visual de Google reCAPTCHA v2 asegurando que tu bloqueador de anuncios no interfiera con el iframe."
      },
      {
        "id": "pol-4",
        "title": "Guardar como PDF con código de verificación",
        "description": "Presiona Ctrl+P en tu navegador, elige 'Guardar como PDF' y verifica que el hash alfanumérico inferior sea completamente legible."
      }
    ],
    "faqs": [
      {
        "question": "¿Por qué el certificado dice 'No tiene asuntos pendientes con las autoridades judiciales' en lugar de antecedentes limpios?",
        "answer": "Por mandato constitucional (Sentencia T-082 de la Corte Constitucional), el Estado colombiano eliminó la estigmatización de 'pasado judicial', adoptando la fórmula jurídica que certifica la ausencia de requerimientos judiciales vigentes."
      },
      {
        "question": "¿Cuánto tiempo de vigencia tiene este certificado ante un empleador?",
        "answer": "Aunque el sistema genera el certificado con fecha y hora exacta, las empresas y entidades públicas suelen solicitar una antigüedad no superior a 30 o 60 días calendario."
      }
    ],
    "content": "<h2>1. ¿Qué es el Certificado de Antecedentes Judiciales en Colombia?</h2>\n<p>El Certificado de Antecedentes de la Policía Nacional es el reporte oficial que certifica si un ciudadano registra o no órdenes de captura activas o requerimientos judiciales emitidos por jueces y fiscales de la República de Colombia. Es un documento básico en cualquier proceso de contratación laboral o postulación académica.</p>\n\n<h2>2. Procedimiento Oficial en Línea</h2>\n<p>Para obtener el documento sin pagar a terceros:</p>\n<ol>\n  <li>Accede a la dirección oficial: <code>https://antecedentes.policia.gov.co:7005/WebJudicial/</code>.</li>\n  <li>Lee las disposiciones de la Ley 1581 de 2012 y selecciona <strong>Acepto</strong>.</li>\n  <li>Ingresa tu tipo y número de documento de identidad.</li>\n  <li>Resuelve el captcha de verificación y presiona <strong>Buscar</strong>.</li>\n  <li>Aparecerá en pantalla el resultado: <em>\"EL CIUDADANO NO TIENE ASUNTOS PENDIENTES CON LAS AUTORIDADES JUDICIALES\"</em>.</li>\n</ol>\n\n<h2>3. Cómo Imprimir y Validar el Documento en PDF</h2>\n<p>El portal web no cuenta con un botón directo de descarga en PDF; la forma correcta de generarlo es pulsar <code>Ctrl + P</code> en Windows o <code>Cmd + P</code> en macOS, configurar la impresora virtual en <strong>Guardar como PDF</strong>, marcar la casilla <em>Gráficos de fondo</em> en los ajustes de impresión y almacenar el archivo localmente.</p>"
  },
  {
    "id": 3,
    "title": "Consulta de Puntaje del Sisbén IV: Cómo descargar el certificado oficial y solicitar reencuesta por inconformidad",
    "slug": "consulta-puntaje-grupo-sisben-iv-descargar-certificado-dnp",
    "category_slug": "tramites",
    "author": "Andrés",
    "featured_image": "/static/img/sisben_iv_consulta.svg",
    "image_caption": "Portal de consulta del Departamento Nacional de Planeación (DNP) para la clasificación del Sisbén IV.",
    "device_tested": "Laptop Lenovo • Windows 11 • Firefox 130 en Barranquilla",
    "copyright_notice": "© 2026 Andrés - CUC Barranquilla. Licencia CC BY-NC-SA 4.0.",
    "difficulty": "Principiante",
    "estimated_time": "8 minutos",
    "created_at": "2026-09-19T14:30:00Z",
    "status": "Publicado",
    "read_time_minutes": 11,
    "excerpt": "Aprende a consultar tu ficha socioeconómica en la base de datos nacional del Sisbén IV administrada por el DNP, comprender los Grupos A, B, C y D, y descargar la certificación oficial en PDF.",
    "quick_steps": [
      {
        "id": "sis-1",
        "title": "Ingresar al portal oficial del Sisbén",
        "description": "Accede a sisben.gov.co y pulsa sobre el botón 'Consulta tu grupo Sisbén'."
      },
      {
        "id": "sis-2",
        "title": "Seleccionar tipo de documento",
        "description": "Ingresa tu Cédula de Ciudadanía o Tarjeta de Identidad y pulsa en 'Consultar'."
      },
      {
        "id": "sis-3",
        "title": "Verificar Grupo Asignado (A, B, C o D)",
        "description": "Revisa el subgrupo exacto (ej. A1-A5 Pobreza Extrema, B1-B7 Pobreza Moderada, C1-C18 Vulnerable)."
      },
      {
        "id": "sis-4",
        "title": "Descargar Ficha en PDF",
        "description": "Haz clic en el botón 'Imprimir' ubicado al final de la ficha para guardar el documento timbrado con firma digital."
      }
    ],
    "faqs": [
      {
        "question": "¿Qué diferencia hay entre el antiguo puntaje de 0 a 100 y los grupos actuales?",
        "answer": "El Sisbén IV abandonó los puntajes numéricos de 0 a 100 y adoptó una clasificación por grupos alfabéticos (A, B, C y D) que cruza registros administrativos de la DIAN, PILA y Registraduría para mayor precisión."
      },
      {
        "question": "¿Cómo puedo pedir que me vuelvan a encuestar si mi grupo no corresponde a mi realidad?",
        "answer": "Debes radicar una solicitud de 'Reencuesta por cambio de condiciones socioeconómicas' en la oficina local del Sisbén de tu alcaldía municipal o distrital con copia de cédula y recibo de servicio público."
      }
    ],
    "content": "<h2>1. Funcionamiento del Sistema de Información Sisbén IV</h2>\n<p>El Sistema de Identificación de Potenciales Beneficiarios de Programas Sociales (Sisbén) clasifica a la población de acuerdo con sus ingresos y condiciones de vida, facilitando la focalización de subsidios como Renta Ciudadana, subsidios de vivienda 'Mi Casa Ya', gratuidad en educación superior pública (Política de Gratuidad 'Puedo Estudiar') y régimen subsidiado en salud.</p>\n\n<h2>2. Escala de Clasificación por Grupos</h2>\n<ul>\n  <li><strong>Grupo A (A1 a A5):</strong> Pobreza extrema (población con menor capacidad de generación de ingresos).</li>\n  <li><strong>Grupo B (B1 a B7):</strong> Pobreza moderada (hogares vulnerables con ingresos fluctuantes).</li>\n  <li><strong>Grupo C (C1 a C18):</strong> Población vulnerable (personas en riesgo de caer en pobreza ante contingencias).</li>\n  <li><strong>Grupo D (D1 a D21):</strong> Población no pobre, no vulnerable.</li>\n</ul>\n\n<h2>3. Procedimiento para Obtener la Certificación</h2>\n<p>El portal <code>www.sisben.gov.co</code> permite la descarga gratuita del certificado. Si el sistema arroja la alerta <em>'Franja Roja - Registro en verificación'</em>, indica que existen inconsistencias entre los datos suministrados al encuestador y las bases de datos de la DIAN o el sistema financiero, en cuyo caso es obligatorio acudir a la alcaldía para subsanar los datos.</p>"
  },
  {
    "id": 4,
    "title": "Descarga de Certificado de Antecedentes de la Procuraduría General: Ordinario y Especial en línea",
    "slug": "certificado-antecedentes-disciplinarios-procuraduria-general-en-linea",
    "category_slug": "tramites",
    "author": "Andrés",
    "featured_image": "/static/img/procuraduria_antecedentes.svg",
    "image_caption": "Sistema SIRI de la Procuraduría General de la Nación para generación de antecedentes disciplinarios.",
    "device_tested": "Laptop Ryzen 5 • Windows 11 • Google Chrome v128 en Barranquilla",
    "copyright_notice": "© 2026 Andrés - CUC Barranquilla. Licencia CC BY-NC-SA 4.0.",
    "difficulty": "Principiante",
    "estimated_time": "4 minutos",
    "created_at": "2026-09-19T18:00:00Z",
    "status": "Publicado",
    "read_time_minutes": 9,
    "excerpt": "Guía práctica para solicitar el Certificado de Antecedentes Disciplinarios de la Procuraduría General de la Nación. Diferencias entre certificado ordinario y especial, y validación mediante código SIRI.",
    "quick_steps": [
      {
        "id": "proc-1",
        "title": "Acceder al portal SIRI de la Procuraduría",
        "description": "Entra a procuraduria.gov.co y dirígete a la sección de 'Certificados de Antecedentes'."
      },
      {
        "id": "proc-2",
        "title": "Seleccionar tipo de certificado",
        "description": "Elige 'Generar Certificado de Antecedentes' y marca la opción 'Ordinario' para trámites laborales estándar."
      },
      {
        "id": "proc-3",
        "title": "Ingresar datos y responder pregunta de control",
        "description": "Selecciona Cédula de Ciudadanía, digita tu número y responde a la pregunta de seguridad matemática o visual."
      },
      {
        "id": "proc-4",
        "title": "Descargar el PDF timbrado",
        "description": "El sistema abrirá una nueva pestaña con el archivo PDF oficial con el sello digital y el código de verificación SIRI."
      }
    ],
    "faqs": [
      {
        "question": "¿Cuál es la diferencia entre el certificado ordinario y el especial?",
        "answer": "El certificado ordinario muestra las anotaciones disciplinarias de los últimos 5 años para cualquier cargo común; el certificado especial incluye inhabilidades específicas de por vida para cargos de la rama judicial, fuerza pública o elección popular."
      },
      {
        "question": "¿Cómo verifica una empresa que el certificado no fue alterado?",
        "answer": "En la misma web de la Procuraduría existe la opción 'Consultar Certificado Generado', donde ingresando el código alfanumérico SIRI impreso en el PDF se valida la autenticidad en tiempo real."
      }
    ],
    "content": "<h2>1. ¿Qué certifica la Procuraduría General de la Nación?</h2>\n<p>El Certificado de Antecedentes Disciplinarios refleja si una persona cuenta con sanciones administrativas, suspensiones o inhabilidades para contratar con el Estado colombiano o ejercer cargos públicos. Es un documento obligatorio no solo para contratistas estatales sino en el sector privado para cargos de administración fiduciaria o dirección.</p>\n\n<h2>2. Pasos para la Expedición en Línea</h2>\n<ol>\n  <li>Ingresa al sitio oficial: <code>https://www.procuraduria.gov.co</code>.</li>\n  <li>Haz clic en el enlace <strong>Generación de Antecedentes</strong>.</li>\n  <li>Selecciona <em>Cédula de Ciudadanía</em> e introduce tu número de identificación.</li>\n  <li>Resuelve la pregunta de seguridad aleatoria (por ejemplo: <em>¿Cuánto es 4 + 7?</em>).</li>\n  <li>Haz clic en el botón <strong>Generar</strong>.</li>\n</ol>\n\n<h2>3. Elementos de Seguridad del Documento</h2>\n<p>El PDF generado cuenta con validez legal automática conforme a la Ley 527 de 1999 de comercio electrónico y firmas digitales en Colombia. No requiere estampillas ni firmas manuales en notarías.</p>"
  },
  {
    "id": 5,
    "title": "Cómo consultar y descargar el Certificado de Antecedentes Fiscales de la Contraloría General sin costo",
    "slug": "certificado-antecedentes-fiscales-contraloria-general-sin-costo",
    "category_slug": "tramites",
    "author": "Andrés",
    "featured_image": "/static/img/contraloria_fiscales.svg",
    "image_caption": "Sistema de Información del Boletín de Responsables Fiscales (SIBRF) de la Contraloría General.",
    "device_tested": "Laptop Ryzen 5 • Windows 11 • Edge Chromium v128 en Barranquilla",
    "copyright_notice": "© 2026 Andrés - CUC Barranquilla. Licencia CC BY-NC-SA 4.0.",
    "difficulty": "Principiante",
    "estimated_time": "4 minutos",
    "created_at": "2026-09-20T08:00:00Z",
    "status": "Publicado",
    "read_time_minutes": 8,
    "excerpt": "Aprende a obtener el Certificado del Boletín de Responsables Fiscales de la Contraloría General de la República. Documento esencial para contratación pública y vinculación laboral en Colombia.",
    "quick_steps": [
      {
        "id": "ctrl-1",
        "title": "Ingresar a contraloria.gov.co",
        "description": "Accede al portal web de la Contraloría General de la República y selecciona 'Certificado de Antecedentes Fiscales'."
      },
      {
        "id": "ctrl-2",
        "title": "Elegir Persona Natural o Jurídica",
        "description": "Selecciona 'Persona Natural' e ingresa tu Cédula de Ciudadanía."
      },
      {
        "id": "ctrl-3",
        "title": "Generar documento oficial",
        "description": "Haz clic en 'Buscar' y luego en 'Descargar Certificado'."
      },
      {
        "id": "ctrl-4",
        "title": "Guardar el archivo PDF",
        "description": "Comprueba que la leyenda indique: 'A la fecha de expedición no se encuentra reportado en el Boletín de Responsables Fiscales'."
      }
    ],
    "faqs": [
      {
        "question": "¿Qué significa figurar en el Boletín de Responsables Fiscales?",
        "answer": "Indica que una persona tiene cuentas pendientes o fallos con responsabilidad fiscal por daño o malversación de recursos públicos, lo que inhabilita para ejercer cargos o contratar con el Estado."
      },
      {
        "question": "¿Tiene costo este certificado?",
        "answer": "Es completamente gratuito y de acceso público las 24 horas del día."
      }
    ],
    "content": "<h2>1. El Boletín de Responsables Fiscales (SIBRF)</h2>\n<p>La Contraloría General de la República emite periódicamente el Boletín de Responsables Fiscales. El certificado acredita que la persona no ha sido declarada responsable de causar detrimento patrimonial a los fondos de la Nación.</p>\n\n<h2>2. Guía Rápida de Generación</h2>\n<p>Accede al portal oficial <code>https://www.contraloria.gov.co</code> y busca el apartado <em>Certificados en Línea</em>. Elige la opción <strong>Persona Natural</strong>, escribe tu cédula sin caracteres especiales y pulsa en <em>Descargar Certificado</em>. Se generará un PDF oficial timbrado con fecha y hora exacta.</p>"
  },
  {
    "id": 6,
    "title": "Consulta de Licencia de Conducción y Multas en el RUNT / SIMIT con Cédula: Paz y salvo digital",
    "slug": "consulta-licencia-conduccion-multas-runt-simit-paz-y-salvo",
    "category_slug": "tramites",
    "author": "Andrés",
    "featured_image": "/static/img/runt_licencia_simit.svg",
    "image_caption": "Plataforma de consulta ciudadana del Registro Único Nacional de Tránsito (RUNT) y SIMIT.",
    "device_tested": "Laptop Ryzen 5 • Windows 11 • Chrome en Barranquilla",
    "copyright_notice": "© 2026 Andrés - CUC Barranquilla. Licencia CC BY-NC-SA 4.0.",
    "difficulty": "Principiante",
    "estimated_time": "7 minutos",
    "created_at": "2026-09-20T11:00:00Z",
    "status": "Publicado",
    "read_time_minutes": 11,
    "excerpt": "Tutorial completo para verificar el estado de tu licencia de conducción (pase) en el RUNT por cédula, consultar fotomultas y comparendos pendientes en el SIMIT y descargar el estado de cuenta oficial.",
    "quick_steps": [
      {
        "id": "runt-1",
        "title": "Ingresar a runt.gov.co",
        "description": "Entra a la sección 'Consulta de Ciudadanos por Documento de Identidad'."
      },
      {
        "id": "runt-2",
        "title": "Digitar Cédula y verificar datos de conductor",
        "description": "Revisa tus categorías activas (A2 para moto, B1/C1 para vehículos particulares y de servicio público) y vigencia."
      },
      {
        "id": "runt-3",
        "title": "Consultar multas en fcm.org.co/simit",
        "description": "Ingresa al Sistema Integrado de Información sobre Multas y Sanciones por Infracciones de Tránsito (SIMIT)."
      },
      {
        "id": "runt-4",
        "title": "Generar Paz y Salvo SIMIT",
        "description": "Si no registras comparendos pendientes, descarga el PDF oficial de Paz y Salvo con código QR."
      }
    ],
    "faqs": [
      {
        "question": "¿Por qué mi licencia no aparece activa en el RUNT si tengo el plástico físico?",
        "answer": "Esto sucede cuando el Centro de Enseñanza Automovilística (CEA) o el organismo de tránsito local no sincronizó la información con la base central del Ministerio de Transporte. Debes radicar una solicitud de homologación de datos."
      },
      {
        "question": "¿Dónde puedo verificar los exámenes médicos para renovar la licencia?",
        "answer": "En la misma ficha del RUNT, en la pestaña 'Certificados Médicos CRC', figuran los resultados de optometría, psicología y medicina general con su fecha de vigencia."
      }
    ],
    "content": "<h2>1. ¿Qué es el RUNT y por qué es indispensable?</h2>\n<p>El Registro Único Nacional de Tránsito (RUNT) centraliza toda la información automotriz de Colombia: conductores habilitados, licencias vigentes, vehículos registrados, vigencia del Seguro Obligatorio (SOAT) y Revisión Técnico-Mecánica (RTM).</p>\n\n<h2>2. Consulta Ciudadana en el RUNT</h2>\n<p>Ingresa a <code>https://www.runt.gov.co/consultaCiudadana/#/consultaPersona</code>. Digita tu cédula y resuelve el captcha. Podrás inspeccionar: estado de tu licencia, número de registro nacional, historial de cancelaciones o suspensiones y exámenes de aptitud física radicados por los Centros de Reconocimiento de Conductores (CRC).</p>\n\n<h2>3. Paz y Salvo en el SIMIT</h2>\n<p>Para renovar la licencia o traspasar un vehículo, es requisito legal estar al día en comparendos. Ingresa a <code>https://www.fcm.org.co/simit/</code> con tu cédula. Si no tienes multas, haz clic en <em>Descargar Paz y Salvo</em>.</p>"
  },
  {
    "id": 7,
    "title": "Cómo afiliarse y consultar el FOSYGA / ADRES (BDUA): Descargar certificado de EPS vigente en formato PDF",
    "slug": "consulta-afiliacion-eps-adres-fosyga-descargar-certificado-bdua",
    "category_slug": "tramites",
    "author": "Andrés",
    "featured_image": "/static/img/adres_fosyga_eps.svg",
    "image_caption": "Herramienta BDUA de la Administradora de los Recursos del Sistema General de Seguridad Social en Salud (ADRES).",
    "device_tested": "Laptop Ryzen 5 • Windows 11 • Edge Chromium en Barranquilla",
    "copyright_notice": "© 2026 Andrés - CUC Barranquilla. Licencia CC BY-NC-SA 4.0.",
    "difficulty": "Principiante",
    "estimated_time": "5 minutos",
    "created_at": "2026-09-20T15:00:00Z",
    "status": "Publicado",
    "read_time_minutes": 10,
    "excerpt": "Aprende a consultar la Base de Datos Única de Afiliados (BDUA) de la ADRES (anteriormente conocida como FOSYGA) para comprobar en qué EPS estás afiliado, régimen de salud y descargar el comprobante en PDF.",
    "quick_steps": [
      {
        "id": "adr-1",
        "title": "Ingresar a adres.gov.co/consulte-su-eps",
        "description": "Accede a la plataforma oficial de la Administradora de los Recursos del Sistema General de Seguridad Social en Salud."
      },
      {
        "id": "adr-2",
        "title": "Ingresar número de cédula",
        "description": "Selecciona Cédula de Ciudadanía, digita tu número sin separadores y valida el captcha."
      },
      {
        "id": "adr-3",
        "title": "Comprobar Régimen y Estado",
        "description": "Verifica que el estado indique 'ACTIVO', la EPS asignada (SURA, Sanitas, Nueva EPS, etc.) y si eres cotizante o beneficiario."
      },
      {
        "id": "adr-4",
        "title": "Guardar el certificado oficial en PDF",
        "description": "Usa la opción de impresión del navegador (Ctrl+P) para guardar el comprobante oficial."
      }
    ],
    "faqs": [
      {
        "question": "¿Cuál es la diferencia entre FOSYGA y ADRES?",
        "answer": "El FOSYGA desapareció jurídicamente en 2017 y sus funciones fueron asumidas por la ADRES (Administradora de los Recursos del Sistema General de Seguridad Social en Salud), que maneja la base única BDUA."
      },
      {
        "question": "¿Qué debo hacer si mi estado aparece como 'SUSPENDIDO'?",
        "answer": "Indica mora en los pagos de la planilla PILA o falta de reporte por parte del empleador. Comunícate de inmediato con el área de talento humano o realiza el aporte como independiente."
      }
    ],
    "content": "<h2>1. ¿Qué es la BDUA administrada por la ADRES?</h2>\n<p>La Base de Datos Única de Afiliados (BDUA) es el registro maestro que contiene a todos los colombianos inscritos en el Sistema General de Seguridad Social en Salud, ya sea en el Régimen Contributivo o en el Régimen Subsidiado.</p>\n\n<h2>2. Proceso de Consulta Paso a Paso</h2>\n<ol>\n  <li>Accede a: <code>https://www.adres.gov.co/consulte-su-eps</code>.</li>\n  <li>Selecciona tu tipo de documento y digita el número.</li>\n  <li>Haz clic en <strong>Consultar</strong>.</li>\n  <li>El sistema desplegará tu historial completo de afiliaciones, fechas de radicación y entidad promotora actual.</li>\n</ol>\n\n<h2>3. Utilidad para Empleo y Matrícula Universitaria</h2>\n<p>La mayoría de universidades colombianas (como la Universidad de la Costa CUC) y empresas exigen este certificado para confirmar que el estudiante o empleado cuenta con cobertura activa frente a accidentes laborales o emergencias médicas.</p>"
  },
  {
    "id": 8,
    "title": "Arquitectura de Software en Python y Flet: Creando aplicaciones de escritorio y móviles con base de datos SQLite y diseño reactivo",
    "slug": "arquitectura-software-python-flet-aplicaciones-escritorio-movil-sqlite",
    "category_slug": "python-flet",
    "author": "Andrés",
    "featured_image": "/static/img/python_flet_tutorial.svg",
    "image_caption": "Captura de entorno de desarrollo con Python 3.12 y Flet ejecutándose en Windows 11.",
    "device_tested": "Laptop Ryzen 5 5500U • 16GB RAM • VS Code con Flet 0.24",
    "copyright_notice": "© 2026 Andrés - Universidad de la Costa (CUC). Código y esquemas propios. Licencia CC BY-NC-SA 4.0.",
    "difficulty": "Intermedio",
    "estimated_time": "25 minutos",
    "created_at": "2026-09-17T15:30:00Z",
    "status": "Publicado",
    "read_time_minutes": 16,
    "excerpt": "Manual exhaustivo de programación avanzada en Python utilizando el framework Flet (Flutter engine). Estructura MVC, persistencia de datos local con SQLite, control de estado y empaquetado para distribución.",
    "quick_steps": [
      {
        "id": "flet-1",
        "title": "Crear y activar entorno virtual",
        "description": "Ejecuta python -m venv .venv y activa el entorno en PowerShell mediante .venv\\Scripts\\Activate.ps1."
      },
      {
        "id": "flet-2",
        "title": "Instalar dependencias necesarias",
        "description": "Instala el framework y utilidades ejecutando pip install flet sqlalchemy pydantic."
      },
      {
        "id": "flet-3",
        "title": "Estructurar el patrón MVC",
        "description": "Organiza los directorios del proyecto en /models, /views, /controllers y /database para separar la lógica de negocio."
      },
      {
        "id": "flet-4",
        "title": "Implementar capa SQLite con transacciones",
        "description": "Crea el esquema relacional con context managers para garantizar operaciones ACID seguras sin bloqueos."
      },
      {
        "id": "flet-5",
        "title": "Ejecutar y probar la aplicación",
        "description": "Lanza la app ejecutando flet run main.py -d para habilitar recarga en caliente durante el desarrollo."
      }
    ],
    "faqs": [
      {
        "question": "¿Por qué elegir Flet sobre Tkinter o PyQt para proyectos modernos?",
        "answer": "Flet utiliza internamente el motor gráfico de Flutter (Google), lo que ofrece animaciones a 60 FPS nativas, componentes de Material Design 3 modernos y portabilidad total a Windows, Linux, Mac, Web y Android sin cambiar el código Python."
      },
      {
        "question": "¿Cómo se compila un ejecutable .exe de una aplicación Flet para distribuir?",
        "answer": "Flet incluye la herramienta de empaquetado oficial 'flet build windows' o el uso de PyInstaller con el comando 'flet pack main.py --windowed --name MiApp'."
      }
    ],
    "content": "<h2>1. ¿Por qué Flet revoluciona el desarrollo GUI en Python?</h2>\n<p>Históricamente, construir interfaces gráficas en Python exigía trabajar con librerías obsoletas como Tkinter o herramientas pesadas como PyQt con licencias comerciales restrictivas. <strong>Flet</strong> soluciona este dilema uniendo la sencillez de Python con la potencia visual y reactividad del motor Flutter de Google.</p>\n\n<h2>2. Estructura de Proyecto Recomendada</h2>\n<pre><code>mi_proyecto_flet/\n├── .venv/\n├── assets/\n│   └── logo.png\n├── controllers/\n│   └── task_controller.py\n├── models/\n│   └── task.py\n├── views/\n│   └── home_view.py\n├── database.py\n└── main.py</code></pre>\n\n<h2>3. Conexión a Base de Datos SQLite</h2>\n<p>Implementa una capa de acceso a datos sólida utilizando transacciones seguras:</p>\n<pre><code>import sqlite3\nfrom typing import List, Tuple\n\ndef get_db_connection():\n    conn = sqlite3.connect(\"app_data.db\")\n    conn.row_factory = sqlite3.Row\n    return conn\n\ndef init_db():\n    with get_db_connection() as conn:\n        conn.execute('''\n            CREATE TABLE IF NOT EXISTS tareas (\n                id INTEGER PRIMARY KEY AUTOINCREMENT,\n                titulo TEXT NOT NULL,\n                completada BOOLEAN DEFAULT 0\n            )\n        ''')\n        conn.commit()</code></pre>\n\n<h2>4. Construcción de la Interfaz Reactiva</h2>\n<p>Cada componente visual en Flet es un control que se suscribe a eventos. Al invocar <code>page.update()</code>, Flet recalcula únicamente las diferencias en el árbol de renderizado de Flutter, logrando una fluidez asombrosa con bajísimo consumo de memoria.</p>"
  },
  {
    "id": 9,
    "title": "Autenticación y Login Seguro en Python Flet con Hashing de Contraseñas bcrypt y SQLite",
    "slug": "autenticacion-login-seguro-python-flet-bcrypt-sqlite",
    "category_slug": "python-flet",
    "author": "Andrés",
    "featured_image": "/static/img/flet_auth_bcrypt.svg",
    "image_caption": "Arquitectura de hashing bcrypt con salt dinámico y almacenamiento de sesión seguro en Flet.",
    "device_tested": "Laptop Ryzen 5 • Windows 11 • Python 3.12 y Flet 0.24",
    "copyright_notice": "© 2026 Andrés - CUC Barranquilla. Licencia CC BY-NC-SA 4.0.",
    "difficulty": "Intermedio",
    "estimated_time": "20 minutos",
    "created_at": "2026-09-20T19:00:00Z",
    "status": "Publicado",
    "read_time_minutes": 13,
    "excerpt": "Aprende a programar un sistema completo de inicio de sesión y registro de usuarios en Python Flet. Implementa salado y derivación de claves con bcrypt, almacenamiento seguro de tokens y control de sesiones.",
    "quick_steps": [
      {
        "id": "fauth-1",
        "title": "Instalar librería de criptografía",
        "description": "Ejecuta pip install bcrypt en tu entorno virtual."
      },
      {
        "id": "fauth-2",
        "title": "Crear función de hashing con salt",
        "description": "Implementa bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(12)) para encriptar contraseñas."
      },
      {
        "id": "fauth-3",
        "title": "Validar credenciales contra SQLite",
        "description": "Usa bcrypt.checkpw para verificar la coincidencia sin almacenar texto plano."
      },
      {
        "id": "fauth-4",
        "title": "Guardar sesión en page.client_storage",
        "description": "Almacena de forma persistente el ID de usuario autenticado para mantener la sesión abierta."
      }
    ],
    "faqs": [
      {
        "question": "¿Por qué nunca se debe guardar contraseñas con MD5 o SHA256 en la base de datos?",
        "answer": "MD5 y SHA256 son algoritmos diseñados para verificación rápida de integridad y son altamente vulnerables a tablas arcoíris y ataques de fuerza bruta por GPU. bcrypt incorpora un factor de costo computacional (salt dinámico) que neutraliza estos ataques."
      },
      {
        "question": "¿Cómo se implementa el cierre de sesión en Flet?",
        "answer": "Basta con invocar page.client_storage.remove('user_token') y redirigir el enrutamiento a la vista de login mediante page.go('/login')."
      }
    ],
    "content": "<h2>1. Principios de Seguridad en Aplicaciones de Escritorio</h2>\n<p>Guardar credenciales en texto plano es una de las vulnerabilidades más graves en desarrollo de software. En esta guía construimos un módulo robusto de autenticación en Python Flet usando <strong>bcrypt</strong> con un factor de trabajo (work factor) de 12 rondas de hashing.</p>\n\n<h2>2. Código del Servicio de Hashing</h2>\n<pre><code>import bcrypt\n\nclass SecurityService:\n    @staticmethod\n    def hash_password(plain_password: str) -> str:\n        salt = bcrypt.gensalt(rounds=12)\n        hashed = bcrypt.hashpw(plain_password.encode(\"utf-8\"), salt)\n        return hashed.decode(\"utf-8\")\n\n    @staticmethod\n    def verify_password(plain_password: str, hashed_password: str) -> bool:\n        return bcrypt.checkpw(\n            plain_password.encode(\"utf-8\"),\n            hashed_password.encode(\"utf-8\")\n        )</code></pre>\n\n<h2>3. Integración con la Interfaz Flet</h2>\n<p>Al hacer clic en el botón de ingreso, capturamos los valores de los campos de texto <code>ft.TextField(password=True, can_reveal_password=True)</code>, consultamos el registro en SQLite y, si la verificación es exitosa, almacenamos el token en <code>page.client_storage</code> para persistir la sesión.</p>"
  },
  {
    "id": 10,
    "title": "Consumo de APIs REST Asíncronas en Python Flet con aiohttp y visualización en tiempo real",
    "slug": "consumo-api-rest-asincrona-python-flet-aiohttp-tiempo-real",
    "category_slug": "python-flet",
    "author": "Andrés",
    "featured_image": "/static/img/flet_rest_api.svg",
    "image_caption": "Visualización reactiva de datos externos consumidos vía aiohttp sin bloquear el hilo principal de Flet.",
    "device_tested": "Laptop Ryzen 5 • Windows 11 • Python 3.12 y Flet 0.24",
    "copyright_notice": "© 2026 Andrés - CUC Barranquilla. Licencia CC BY-NC-SA 4.0.",
    "difficulty": "Intermedio",
    "estimated_time": "18 minutos",
    "created_at": "2026-09-21T09:00:00Z",
    "status": "Publicado",
    "read_time_minutes": 12,
    "excerpt": "Aprende a realizar peticiones HTTP no bloqueantes en aplicaciones Flet utilizando aiohttp. Evita que la interfaz se congele, muestra indicadores de carga y maneja excepciones de red limpiamente.",
    "quick_steps": [
      {
        "id": "fapi-1",
        "title": "Instalar aiohttp",
        "description": "Ejecuta pip install aiohttp en tu entorno virtual."
      },
      {
        "id": "fapi-2",
        "title": "Definir función asíncrona de consulta",
        "description": "Usa async with aiohttp.ClientSession() as session para enviar peticiones GET/POST."
      },
      {
        "id": "fapi-3",
        "title": "Mostrar ft.ProgressRing durante la carga",
        "description": "Activa un indicador de progreso circular antes de iniciar la solicitud HTTP."
      },
      {
        "id": "fapi-4",
        "title": "Actualizar la tabla o lista con los datos recibidos",
        "description": "Transforma el payload JSON en controles ft.DataRow o ft.ListTile y ejecuta page.update()."
      }
    ],
    "faqs": [
      {
        "question": "¿Por qué no se debe usar la librería 'requests' dentro de Flet?",
        "answer": "La librería requests es síncrona y bloqueante. Si una petición tarda 2 segundos en responder, la interfaz gráfica se congelará por completo y el sistema operativo marcará la ventana como 'No responde'. Con aiohttp y async/await la interfaz continúa fluida a 60 FPS."
      },
      {
        "question": "¿Cómo se manejan errores si el usuario no tiene conexión a internet?",
        "answer": "Se utiliza un bloque try-except capturando aiohttp.ClientError y mostrando una alerta al usuario con ft.SnackBar(ft.Text('Sin conexión a internet'))."
      }
    ],
    "content": "<h2>1. El problema del bloqueo del hilo gráfico</h2>\n<p>Al construir interfaces gráficas, el hilo principal se encarga de renderizar los controles a 60 fotogramas por segundo y responder a los eventos de clic del usuario. Si ejecutamos una petición web síncrona en dicho hilo, la aplicación se pasma. En esta guía implementamos comunicación asíncrona profesional.</p>\n\n<h2>2. Implementación de Cliente Asíncrono</h2>\n<pre><code>import flet as ft\nimport aiohttp\n\nasync def main(page: ft.Page):\n    page.title = \"Consumo Asíncrono de APIs\"\n    loading_ring = ft.ProgressRing(visible=False)\n    results_list = ft.ListView(expand=True, spacing=10)\n\n    async def fetch_data(e):\n        loading_ring.visible = True\n        page.update()\n\n        try:\n            async with aiohttp.ClientSession() as session:\n                async with session.get(\"https://jsonplaceholder.typicode.com/posts?_limit=10\") as resp:\n                    if resp.status == 200:\n                        data = await resp.json()\n                        results_list.controls.clear()\n                        for item in data:\n                            results_list.controls.append(\n                                ft.ListTile(\n                                    leading=ft.Icon(ft.Icons.ARTICLE),\n                                    title=ft.Text(item['title']),\n                                    subtitle=ft.Text(item['body'], max_lines=2)\n                                )\n                            )\n        except Exception as err:\n            page.open(ft.SnackBar(ft.Text(f\"Error de red: {err}\")))\n        finally:\n            loading_ring.visible = False\n            page.update()\n\n    page.add(\n        ft.ElevatedButton(\"Consultar Datos en Vivo\", on_click=fetch_data),\n        loading_ring,\n        results_list\n    )\n\nft.app(target=main)</code></pre>"
  },
  {
    "id": 11,
    "title": "Exportación de Reportes a PDF y Excel en Python Flet usando ReportLab y OpenPyXL",
    "slug": "exportar-reportes-pdf-excel-python-flet-reportlab-openpyxl",
    "category_slug": "python-flet",
    "author": "Andrés",
    "featured_image": "/static/img/flet_pdf_reportlab.svg",
    "image_caption": "Generación de documentos corporativos en PDF y hojas de cálculo Excel desde interfaces Flet.",
    "device_tested": "Laptop Ryzen 5 • Windows 11 • Python 3.12 y Flet 0.24",
    "copyright_notice": "© 2026 Andrés - CUC Barranquilla. Licencia CC BY-NC-SA 4.0.",
    "difficulty": "Intermedio",
    "estimated_time": "22 minutos",
    "created_at": "2026-09-21T14:00:00Z",
    "status": "Publicado",
    "read_time_minutes": 14,
    "excerpt": "Aprende a integrar un módulo de exportación de informes en tus aplicaciones Flet. Genera documentos PDF vectoriales con ReportLab y hojas de cálculo con formato profesional con OpenPyXL integrando ft.FilePicker.",
    "quick_steps": [
      {
        "id": "frep-1",
        "title": "Instalar librerías de exportación",
        "description": "Ejecuta pip install reportlab openpyxl en tu terminal."
      },
      {
        "id": "frep-2",
        "title": "Configurar ft.FilePicker en la página",
        "description": "Añade el control selector de archivos nativo de Flet para elegir la ruta de guardado."
      },
      {
        "id": "frep-3",
        "title": "Construir plantilla PDF con ReportLab",
        "description": "Diseña encabezados institucionales, tablas de datos tabulares y paginación automática."
      },
      {
        "id": "frep-4",
        "title": "Generar archivo Excel con estilos corporativos",
        "description": "Crea libros de trabajo con openpyxl aplicando fuentes en negrita, colores de celda y bordes."
      }
    ],
    "faqs": [
      {
        "question": "¿Por qué usar ReportLab en lugar de convertir HTML a PDF?",
        "answer": "ReportLab genera PDFs vectoriales puros a nivel de bytes, sin necesidad de instalar motores de navegador pesados como Chromium o wkhtmltopdf, permitiendo compilar ejecutables ligeros que no superan los 40 MB."
      },
      {
        "question": "¿Cómo se abre el archivo automáticamente después de exportar?",
        "answer": "En Windows puedes usar os.startfile(ruta_archivo) o el módulo webbrowser para abrir el PDF generado con el visor predeterminado."
      }
    ],
    "content": "<h2>1. Necesidad de reportes en software empresarial</h2>\n<p>Cualquier sistema administrativo de inventario o facturación requiere entregar balances impresos en PDF o tablas editables en Excel. En esta guía implementamos un generador de documentos de alto rendimiento para Flet.</p>\n\n<h2>2. Estructura del Generador con ReportLab</h2>\n<pre><code>from reportlab.lib.pagesizes import letter\nfrom reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle\nfrom reportlab.lib.styles import getSampleStyleSheet\nfrom reportlab.lib import colors\n\ndef generar_pdf_reporte(filepath: str, datos: list):\n    doc = SimpleDocTemplate(filepath, pagesize=letter)\n    elements = []\n    styles = getSampleStyleSheet()\n\n    elements.append(Paragraph(\"<b>Reporte Oficial de Operaciones</b>\", styles['Title']))\n    elements.append(Spacer(1, 15))\n\n    tabla = Table(datos)\n    tabla.setStyle(TableStyle([\n        ('BACKGROUND', (0,0), (-1,0), colors.HexColor(\"#1e3a8a\")),\n        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),\n        ('ALIGN', (0,0), (-1,-1), 'CENTER'),\n        ('BOTTOMPADDING', (0,0), (-1,0), 8),\n        ('GRID', (0,0), (-1,-1), 1, colors.HexColor(\"#cbd5e1\")),\n    ]))\n    elements.append(tabla)\n    doc.build(elements)</code></pre>"
  },
  {
    "id": 12,
    "title": "Despliegue de Aplicaciones Python Flet como PWA Web en la Nube con Docker y Nginx",
    "slug": "despliegue-python-flet-como-pwa-web-docker-nginx",
    "category_slug": "python-flet",
    "author": "Andrés",
    "featured_image": "/static/img/flet_pwa_docker.svg",
    "image_caption": "Flujo de contenedorización Docker multi-etapa y despliegue PWA con Nginx.",
    "device_tested": "Servidor VPS Debian 12 • Docker 27.0 • Nginx 1.24",
    "copyright_notice": "© 2026 Andrés - CUC Barranquilla. Licencia CC BY-NC-SA 4.0.",
    "difficulty": "Avanzado",
    "estimated_time": "25 minutos",
    "created_at": "2026-09-21T18:00:00Z",
    "status": "Publicado",
    "read_time_minutes": 15,
    "excerpt": "Guía completa para compilar y servir aplicaciones Flet como Progressive Web Apps (PWA) instalables en móviles y navegadores de escritorio. Configuración de Dockerfile multi-stage y servidor web Nginx con compresión Gzip.",
    "quick_steps": [
      {
        "id": "fpwa-1",
        "title": "Compilar Flet a formato web estático",
        "description": "Ejecuta flet publish main.py --pwa para generar el directorio /dist con service workers."
      },
      {
        "id": "fpwa-2",
        "title": "Crear Dockerfile multi-stage",
        "description": "Configura una etapa de compilación en Python y una etapa final ligera sobre alpine con Nginx."
      },
      {
        "id": "fpwa-3",
        "title": "Configurar Nginx para soporte PWA",
        "description": "Habilita caché para archivos estáticos y redirección try_files $uri $uri/ /index.html."
      },
      {
        "id": "fpwa-4",
        "title": "Desplegar contenedor con Docker Compose",
        "description": "Lanza el contenedor en el puerto 80/443 con reinicio automático (restart: always)."
      }
    ],
    "faqs": [
      {
        "question": "¿Una PWA hecha con Flet funciona sin internet en el móvil?",
        "answer": "Sí, el comando 'flet publish --pwa' genera un archivo manifest.json y un Service Worker que precachea los activos de Flutter en el navegador, permitiendo la apertura sin conectividad a la red."
      },
      {
        "question": "¿Cuánto pesa la imagen de Docker resultante?",
        "answer": "Gracias a la compilación en dos etapas (multi-stage build), la imagen final basada en nginx:alpine pesa menos de 35 MB."
      }
    ],
    "content": "<h2>1. De la computadora a la web con un solo comando</h2>\n<p>Una de las mayores ventajas de Flet es que el mismo código que corre como ventana nativa en Windows puede exportarse como una aplicación web progresiva (PWA) que el usuario puede instalar en su teléfono celular desde Chrome o Safari con el botón 'Añadir a pantalla de inicio'.</p>\n\n<h2>2. El Dockerfile de Producción</h2>\n<pre><code># Etapa 1: Compilación de activos web\nFROM python:3.12-slim AS builder\nWORKDIR /app\nCOPY requirements.txt .\nRUN pip install --no-cache-dir -r requirements.txt\nCOPY . .\nRUN flet publish main.py --pwa --dist dist\n\n# Etapa 2: Servidor ultraligero Nginx\nFROM nginx:alpine\nCOPY --from=builder /app/dist /usr/share/nginx/html\nCOPY nginx.conf /etc/nginx/conf.d/default.conf\nEXPOSE 80\nCMD [\"nginx\", \"-g\", \"daemon off;\"]</code></pre>"
  },
  {
    "id": 13,
    "title": "Manejo de Estados Globales y Temas Claro/Oscuro en Python Flet con almacenamiento local client_storage",
    "slug": "gestion-estado-global-tema-oscuro-python-flet-client-storage",
    "category_slug": "python-flet",
    "author": "Andrés",
    "featured_image": "/static/img/flet_state_storage.svg",
    "image_caption": "Persistencia de estado global reactivo con ThemeMode y client_storage en Flet.",
    "device_tested": "Laptop Ryzen 5 • Windows 11 • Python 3.12 y Flet 0.24",
    "copyright_notice": "© 2026 Andrés - CUC Barranquilla. Licencia CC BY-NC-SA 4.0.",
    "difficulty": "Intermedio",
    "estimated_time": "15 minutos",
    "created_at": "2026-09-22T08:00:00Z",
    "status": "Publicado",
    "read_time_minutes": 11,
    "excerpt": "Descubre cómo gestionar el estado global en aplicaciones Python Flet sin acoplar código. Implementa un conmutador de tema claro/oscuro persistente entre reinicios mediante client_storage y el sistema PubSub nativo.",
    "quick_steps": [
      {
        "id": "fst-1",
        "title": "Leer preferencia guardada al iniciar",
        "description": "Comprueba si existe la clave con page.client_storage.get('theme_preference')."
      },
      {
        "id": "fst-2",
        "title": "Configurar ft.ThemeMode",
        "description": "Asigna ft.ThemeMode.DARK o ft.ThemeMode.LIGHT según la configuración del usuario."
      },
      {
        "id": "fst-3",
        "title": "Crear un interruptor reactivo (ft.Switch)",
        "description": "Vincula el evento on_change para alternar el tema y guardar la selección."
      },
      {
        "id": "fst-4",
        "title": "Sincronizar vistas con page.pubsub",
        "description": "Emite eventos globales con page.pubsub.send_all() para actualizar pantallas abiertas simultáneamente."
      }
    ],
    "faqs": [
      {
        "question": "¿Dónde almacena Flet los datos de client_storage en Windows y Linux?",
        "answer": "En Windows se guardan en %APPDATA%/Roaming/Flet/{app_name}/, mientras que en navegadores web se almacenan de manera segura en el localStorage del usuario."
      },
      {
        "question": "¿Qué diferencia hay entre page.session y page.client_storage?",
        "answer": "page.session se destruye cuando el usuario cierra la ventana; page.client_storage persiste indefinidamente en el disco local del dispositivo hasta que sea borrado explícitamente."
      }
    ],
    "content": "<h2>1. ¿Qué es el client_storage en Flet?</h2>\n<p>Al programar aplicaciones de escritorio o móviles, es indispensable recordar configuraciones del usuario como: el idioma preferido, la última ruta abierta o el tema visual. Flet proporciona <code>page.client_storage</code> como un almacén de clave-valor nativo y asíncrono.</p>\n\n<h2>2. Implementación del Conmutador de Tema</h2>\n<pre><code>import flet as ft\n\ndef main(page: ft.Page):\n    # Recuperar preferencia previa\n    saved_theme = page.client_storage.get(\"user_theme\")\n    if saved_theme == \"light\":\n        page.theme_mode = ft.ThemeMode.LIGHT\n    else:\n        page.theme_mode = ft.ThemeMode.DARK\n\n    def toggle_theme(e):\n        if theme_switch.value:\n            page.theme_mode = ft.ThemeMode.DARK\n            page.client_storage.set(\"user_theme\", \"dark\")\n        else:\n            page.theme_mode = ft.ThemeMode.LIGHT\n            page.client_storage.set(\"user_theme\", \"light\")\n        page.update()\n\n    theme_switch = ft.Switch(\n        label=\"Modo Oscuro\",\n        value=(page.theme_mode == ft.ThemeMode.DARK),\n        on_change=toggle_theme\n    )\n\n    page.add(theme_switch)\n\nft.app(target=main)</code></pre>"
  },
  {
    "id": 14,
    "title": "Eliminación Quirúrgica de Bloatware en Xiaomi (HyperOS/MIUI) y Samsung (One UI) mediante ADB sin Root",
    "slug": "eliminar-bloatware-xiaomi-hyperos-samsung-adb-sin-root",
    "category_slug": "apps-moviles",
    "author": "Andrés",
    "featured_image": "/static/img/adb_bloatware_android.svg",
    "image_caption": "Captura real de depuración por consola ADB desinstalando servicios de rastreo y telemetría.",
    "device_tested": "Xiaomi POCO X5 Pro (HyperOS Android 14) y Samsung Galaxy A54 en Barranquilla",
    "copyright_notice": "© 2026 Andrés - Universidad de la Costa (CUC). Pruebas de laboratorio propias. Licencia CC BY-NC-SA 4.0.",
    "difficulty": "Intermedio",
    "estimated_time": "15 minutos",
    "created_at": "2026-09-17T11:00:00Z",
    "status": "Publicado",
    "read_time_minutes": 15,
    "excerpt": "Guía técnica avanzada de más de 1.500 palabras para erradicar aplicaciones basura, servicios espía de telemetría y anuncios de fábrica en dispositivos Android sin anular la garantía ni requerir acceso root.",
    "quick_steps": [
      {
        "id": "adb-1",
        "title": "Descargar Platform-Tools oficiales de Google",
        "description": "Descarga el ZIP oficial de platform-tools y extráelo en una ruta corta como C:\\adb sin espacios ni caracteres especiales."
      },
      {
        "id": "adb-2",
        "title": "Habilitar Opciones de Desarrollador",
        "description": "Ve a Ajustes > Acerca del teléfono y pulsa 7 veces consecutivas sobre 'Versión de compilación' o 'Versión del SO' hasta ver el mensaje de confirmación."
      },
      {
        "id": "adb-3",
        "title": "Activar Depuración USB y Depuración de Seguridad",
        "description": "En Opciones de desarrollador activa 'Depuración USB'. En Xiaomi, activa también 'Depuración USB (Ajustes de seguridad)'."
      },
      {
        "id": "adb-4",
        "title": "Autorizar huella digital RSA en el teléfono",
        "description": "Conecta el cable USB al PC, abre PowerShell en C:\\adb, ejecuta .\\adb devices y pulsa 'Permitir siempre desde este equipo'."
      },
      {
        "id": "adb-5",
        "title": "Ejecutar desinstalación selectiva por usuario 0",
        "description": "Ejecuta pm uninstall -k --user 0 [nombre_del_paquete] para desvincular el bloatware sin dañar el arranque del sistema."
      }
    ],
    "faqs": [
      {
        "question": "¿Puedo dañar el teléfono o dejarlo en bucle de reinicio (bootloop) con estos comandos?",
        "answer": "El comando 'pm uninstall -k --user 0' solo desinstala la aplicación para el perfil de usuario actual, dejando el APK seguro en la partición /system. Si desinstalas algo vital por error, basta con reinstalarlo mediante 'cmd package install-existing [nombre_paquete]' o restablecer de fábrica."
      },
      {
        "question": "¿Se anula la garantía oficial del fabricante o se pierde la protección bancaria?",
        "answer": "No. A diferencia del 'Root' o el desbloqueo del gestor de arranque (bootloader), los comandos ADB utilizan la interfaz oficial de depuración autorizada por Google y no alteran la partición de arranque (boot), por lo que Knox y Google Play Integrity permanecen 100% intactos."
      }
    ],
    "content": "<h2>1. ¿Qué es el Bloatware y cómo degrada tu dispositivo?</h2>\n<p>Los teléfonos inteligentes contemporáneos de fabricantes como Xiaomi, POCO o Samsung incorporan decenas de servicios redundantes de fábrica: navegadores propietarios, centros de publicidad (MSA) y demonios de telemetría que consumen silenciosamente entre 600 MB y 1.2 GB de memoria RAM en segundo plano.</p>\n\n<h2>2. Lista Segura de Paquetes para Xiaomi / HyperOS</h2>\n<ul>\n  <li><code>com.miui.analytics</code> (Servicio de análisis y rastreo)</li>\n  <li><code>com.miui.msa.global</code> (Demonio de anuncios de MIUI)</li>\n  <li><code>com.mi.globalbrowser</code> (Navegador Mi Browser no seguro)</li>\n  <li><code>com.facebook.services</code> / <code>com.facebook.system</code> (Telemetría de Meta preinstalada)</li>\n</ul>\n\n<h2>3. Comando de Desinstalación</h2>\n<pre><code>adb shell pm uninstall -k --user 0 com.miui.analytics\nadb shell pm uninstall -k --user 0 com.miui.msa.global</code></pre>\n<p>Inmediatamente tras la ejecución, el proceso se suspende y desaparece del cajón de aplicaciones, liberando ciclos de CPU y prolongando la autonomía de la batería hasta en un 25% diario.</p>"
  },
  {
    "id": 15,
    "title": "Cómo utilizar ADB por Wi-Fi (Inalámbrico) en Android 11+ sin necesidad de cables USB ni Root",
    "slug": "como-usar-adb-inalambrico-wifi-android-sin-cables-ni-root",
    "category_slug": "apps-moviles",
    "author": "Andrés",
    "featured_image": "/static/img/adb_wireless_wifi.svg",
    "image_caption": "Depuración inalámbrica de Android 11+ por puerto dinámico y código PIN de emparejamiento.",
    "device_tested": "Xiaomi POCO X5 Pro (Android 14) • Red Wi-Fi 5 GHz • Windows 11 en Barranquilla",
    "copyright_notice": "© 2026 Andrés - CUC Barranquilla. Licencia CC BY-NC-SA 4.0.",
    "difficulty": "Intermedio",
    "estimated_time": "10 minutos",
    "created_at": "2026-09-22T11:00:00Z",
    "status": "Publicado",
    "read_time_minutes": 11,
    "excerpt": "Aprende a conectar tu dispositivo Android a tu computador mediante ADB inalámbrico nativo. Elimina cables defectuosos, autoriza puertos dinámicos y ejecuta comandos de optimización a través de tu red Wi-Fi local.",
    "quick_steps": [
      {
        "id": "wず-1",
        "title": "Conectar ambos dispositivos a la misma red Wi-Fi",
        "description": "Asegúrate de que tu PC y tu teléfono Android estén en la misma red Wi-Fi (preferiblemente 5 GHz)."
      },
      {
        "id": "wず-2",
        "title": "Activar 'Depuración Inalámbrica'",
        "description": "En Opciones de desarrollador de tu teléfono, pulsa sobre 'Depuración inalámbrica' y actívala."
      },
      {
        "id": "wず-3",
        "title": "Obtener código de emparejamiento",
        "description": "Toca 'Vincular dispositivo con código de vinculación' para ver la IP, el puerto temporal y el código PIN de 6 dígitos."
      },
      {
        "id": "wず-4",
        "title": "Ejecutar adb pair y adb connect",
        "description": "En tu consola ejecuta adb pair IP:PUERTO, introduce el PIN y luego conéctate con adb connect IP:PUERTO_CONEXION."
      }
    ],
    "faqs": [
      {
        "question": "¿Por qué el puerto de conexión cambia cada vez que apago y enciendo la depuración inalámbrica?",
        "answer": "Android 11 implementó puertos dinámicos por seguridad para evitar que dispositivos en redes públicas puedan enviar comandos no autorizados al teléfono. Cada sesión genera un puerto aleatorio."
      },
      {
        "question": "¿Se puede usar ADB inalámbrico en versiones antiguas como Android 9 o 10?",
        "answer": "Sí, pero en Android 9 o 10 se requiere conectar el cable una sola vez para ejecutar 'adb tcpip 5555' y luego desconectar el cable para usar 'adb connect IP:5555'."
      }
    ],
    "content": "<h2>1. La evolución de la depuración inalámbrica en Android</h2>\n<p>Antes de Android 11, utilizar ADB sin cables requería iniciar la sesión primero con un cable USB. Desde Android 11, Google incorporó el protocolo de emparejamiento criptográfico TLS nativo, permitiendo conectar el teléfono a la terminal en segundos sin tocar un solo cable físico.</p>\n\n<h2>2. Paso a Paso en Terminal</h2>\n<ol>\n  <li>En el teléfono, ve a <em>Ajustes > Opciones de desarrollador > Depuración inalámbrica</em>.</li>\n  <li>Pulsa en <strong>Vincular dispositivo con código</strong>. Verás algo como: <code>192.168.1.45:39485</code> y el PIN <code>817294</code>.</li>\n  <li>En tu computadora ejecuta:\n    <pre><code>adb pair 192.168.1.45:39485</code></pre>\n  </li>\n  <li>Escribe el PIN de 6 dígitos. La terminal responderá: <code>Successfully paired</code>.</li>\n  <li>Regresa a la pantalla principal de depuración inalámbrica y toma nota del puerto de conexión general (ejemplo: <code>41253</code>). Conéctate:\n    <pre><code>adb connect 192.168.1.45:41253</code></pre>\n  </li>\n</ol>\n<p>¡Listo! Tu teléfono responderá a cualquier comando ADB como si estuviera conectado físicamente.</p>"
  },
  {
    "id": 16,
    "title": "Backup Completo de Aplicaciones y Datos en Android con ADB pull y restore sin Google Drive",
    "slug": "copia-seguridad-completa-android-adb-backup-pull-sin-google-drive",
    "category_slug": "apps-moviles",
    "author": "Andrés",
    "featured_image": "/static/img/adb_backup_restore.svg",
    "image_caption": "Extracción local de particiones de datos y archivos multimedia con comandos directos de ADB.",
    "device_tested": "Samsung Galaxy A54 • Android 14 • Cable USB 3.2 en Barranquilla",
    "copyright_notice": "© 2026 Andrés - CUC Barranquilla. Licencia CC BY-NC-SA 4.0.",
    "difficulty": "Intermedio",
    "estimated_time": "20 minutos",
    "created_at": "2026-09-22T14:30:00Z",
    "status": "Publicado",
    "read_time_minutes": 13,
    "excerpt": "Aprende a respaldar la memoria interna completa de tu teléfono Android en tu computador sin gastar tu plan de datos ni depender de nubes privadas. Extracción directa de fotos, documentos y paquetes APK.",
    "quick_steps": [
      {
        "id": "abk-1",
        "title": "Conectar por cable y verificar adb devices",
        "description": "Verifica que la consola reconozca tu dispositivo en estado 'device'."
      },
      {
        "id": "abk-2",
        "title": "Crear carpeta de respaldo en el disco de tu PC",
        "description": "Crea una carpeta como C:\\Backup_Android_2026 en tu unidad SSD."
      },
      {
        "id": "abk-3",
        "title": "Extraer fotos y documentos con adb pull",
        "description": "Ejecuta adb pull /sdcard/DCIM C:\\Backup_Android_2026\\DCIM para transferir a máxima velocidad."
      },
      {
        "id": "abk-4",
        "title": "Generar imagen de respaldo comprimida",
        "description": "Ejecuta adb backup -apk -shared -all -f backup_total.ab y confirma en la pantalla del celular."
      }
    ],
    "faqs": [
      {
        "question": "¿Por qué algunas aplicaciones bancarias no se respaldan con adb backup?",
        "answer": "Por directiva de seguridad de Android (atributo android:allowBackup='false' en el AndroidManifest.xml), las apps financieras prohíben la copia de sus datos internos para evitar la clonación de tokens de seguridad."
      },
      {
        "question": "¿Cómo restauro la copia generada en un teléfono nuevo?",
        "answer": "Basta con conectar el nuevo teléfono con depuración USB habilitada y ejecutar en la consola 'adb restore backup_total.ab'."
      }
    ],
    "content": "<h2>1. ¿Por qué prescindir de las copias en la nube?</h2>\n<p>Servicios como Google Drive o Samsung Cloud imponen límites gratuitos de 15 GB y comprimen las fotografías. Respaldar directamente a través de ADB permite transferir gigabytes de información a la velocidad real de tu bus USB (hasta 30-40 MB/s con USB 2.0 y más de 120 MB/s con cables USB 3.0/3.2), manteniendo la resolución original de cada archivo.</p>\n\n<h2>2. Extracción de Carpetas Críticas con ADB Pull</h2>\n<pre><code># Respaldar fotos y videos tomados con la cámara\nadb pull /sdcard/DCIM/Camera ./Backup/Fotos/\n\n# Respaldar descargas y documentos\nadb pull /sdcard/Download ./Backup/Descargas/\nadb pull /sdcard/Documents ./Backup/Documentos/</code></pre>"
  },
  {
    "id": 17,
    "title": "Optimización de Batería en Android: Deshabilitar Doze agresivo y limitar servicios en segundo plano con ADB",
    "slug": "optimizacion-bateria-android-modo-doze-agresivo-adb",
    "category_slug": "apps-moviles",
    "author": "Andrés",
    "featured_image": "/static/img/android_battery_doze.svg",
    "image_caption": "Configuración del subsistema deviceidle de Android para activar el modo Doze profundo de inmediato.",
    "device_tested": "Xiaomi POCO X5 Pro • Android 14 HyperOS en Barranquilla",
    "copyright_notice": "© 2026 Andrés - CUC Barranquilla. Licencia CC BY-NC-SA 4.0.",
    "difficulty": "Avanzado",
    "estimated_time": "15 minutos",
    "created_at": "2026-09-22T17:00:00Z",
    "status": "Publicado",
    "read_time_minutes": 12,
    "excerpt": "Manual técnico para modificar los parámetros internos del regulador de energía de Android (DeviceIdle / Doze). Reduce el consumo de batería en reposo nocturno de un 10% a menos del 1.5% sin perder llamadas importantes.",
    "quick_steps": [
      {
        "id": "bdo-1",
        "title": "Consultar estado actual de Doze",
        "description": "Ejecuta adb shell dumpsys deviceidle para inspeccionar los tiempos de suspensión profunda."
      },
      {
        "id": "bdo-2",
        "title": "Forzar modo Doze profundo al apagar la pantalla",
        "description": "Ajusta los timers de inactividad para que el teléfono duerma en 2 minutos en lugar de 30 minutos."
      },
      {
        "id": "bdo-3",
        "title": "Restringir permisos de ejecución en segundo plano",
        "description": "Usa adb shell cmd appops set [app] RUN_IN_BACKGROUND ignore para apps como TikTok o Facebook."
      },
      {
        "id": "bdo-4",
        "title": "Probar drenaje nocturno",
        "description": "Comprueba con adb shell dumpsys batterystats el ahorro real de miliamperios hora (mAh)."
      }
    ],
    "faqs": [
      {
        "question": "¿Dejaré de recibir mensajes de WhatsApp al activar Doze agresivo?",
        "answer": "No. WhatsApp y las aplicaciones de mensajería utilizan mensajes push de alta prioridad de Firebase Cloud Messaging (FCM) que tienen autorización para despertar brevemente el dispositivo durante las ventanas de mantenimiento de Doze."
      },
      {
        "question": "¿Los cambios se borran al reiniciar el teléfono?",
        "answer": "Los ajustes de appops se conservan; los comandos temporales de deviceidle force-idle pueden automatizarse con aplicaciones como Shizuku o Tasker sin necesidad de PC."
      }
    ],
    "content": "<h2>1. ¿Cómo funciona el modo Doze en el kernel de Android?</h2>\n<p>Introducido en Android 6 y refinado en versiones recientes, el subsistema <code>deviceidle</code> pone el procesador en reposo profundo cuando el acelerómetro detecta que el teléfono está inmóvil sobre una mesa. Sin embargo, por defecto, el sistema tarda más de 30 minutos en entrar en suspensión profunda.</p>\n\n<h2>2. Modificación de Parámetros por Consola</h2>\n<pre><code># Forzar entrada inmediata en modo reposo profundo\nadb shell dumpsys deviceidle force-idle deep\n\n# Impedir que redes sociales despierten el CPU en bucle\nadb shell cmd appops set com.zhiliaoapp.musically RUN_IN_BACKGROUND ignore\nadb shell cmd appops set com.facebook.katana RUN_IN_BACKGROUND ignore</code></pre>"
  },
  {
    "id": 18,
    "title": "Instalación de Tiendas Alternativas Seguras en Android: F-Droid y Aurora Store sin Google Play Services",
    "slug": "instalar-tiendas-libres-android-fdroid-aurora-store-sin-google-play",
    "category_slug": "apps-moviles",
    "author": "Andrés",
    "featured_image": "/static/img/fdroid_aurora_store.svg",
    "image_caption": "Configuración de repositorios FOSS en F-Droid y cliente anónimo Aurora Store.",
    "device_tested": "Samsung Galaxy A54 • Android 14 en Barranquilla",
    "copyright_notice": "© 2026 Andrés - CUC Barranquilla. Licencia CC BY-NC-SA 4.0.",
    "difficulty": "Principiante",
    "estimated_time": "12 minutos",
    "created_at": "2026-09-22T20:00:00Z",
    "status": "Publicado",
    "read_time_minutes": 11,
    "excerpt": "Aprende a independizarte de Google Play Store instalando tiendas libres y seguras. Descubre miles de aplicaciones de código abierto sin anuncios ni rastreadores en F-Droid y descarga apps oficiales mediante Aurora Store.",
    "quick_steps": [
      {
        "id": "fdr-1",
        "title": "Descargar F-Droid desde la web oficial",
        "description": "Accede a f-droid.org desde tu navegador móvil y descarga el APK oficial verificado por firma PGP."
      },
      {
        "id": "fdr-2",
        "title": "Autorizar instalación de orígenes desconocidos",
        "description": "Otorga permiso temporal de instalación de paquetes a tu navegador en Ajustes de Android."
      },
      {
        "id": "fdr-3",
        "title": "Actualizar repositorios y configurar repositorios IzzyOnDroid",
        "description": "Abre F-Droid, tira hacia abajo para refrescar el catálogo y activa repositorios adicionales."
      },
      {
        "id": "fdr-4",
        "title": "Instalar Aurora Store para apps comerciales",
        "description": "Instala Aurora Store desde F-Droid para acceder a las apps de Google Play de forma anónima sin cuenta de Google."
      }
    ],
    "faqs": [
      {
        "question": "¿Es seguro instalar aplicaciones fuera de Google Play Store?",
        "answer": "F-Droid compila cada aplicación directamente desde el código fuente público y audita los permisos. De hecho, muchas apps de F-Droid son más seguras y respetuosas con la privacidad que las de Play Store porque prohíben módulos de publicidad y telemetría comercial."
      },
      {
        "question": "¿Puedo actualizar las aplicaciones de Google Play con Aurora Store?",
        "answer": "Sí. Aurora Store consulta los servidores oficiales de Google y descarga los mismos paquetes APK firmados por los desarrolladores oficiales."
      }
    ],
    "content": "<h2>1. La alternativa del Software Libre en Android</h2>\n<p>La inmensa mayoría de usuarios desconocen que existe un ecosistema vibrante de aplicaciones gratuitas, sin publicidad invasiva ni suscripciones engañosas. <strong>F-Droid</strong> es el repositorio oficial de software libre (FOSS) para Android, mantenido por una fundación sin ánimo de lucro.</p>\n\n<h2>2. Repositorios Recomendados</h2>\n<ul>\n  <li><strong>F-Droid Oficial:</strong> Aplicaciones verificadas y compiladas por el servidor de F-Droid.</li>\n  <li><strong>IzzyOnDroid:</strong> Aplicaciones de código abierto en desarrollo activo que se actualizan directamente desde los repositorios de GitHub de sus creadores.</li>\n</ul>"
  },
  {
    "id": 19,
    "title": "Diagnóstico de Sensores, Pantalla y Salud de Batería en Android mediante Códigos Secretos USSD y ADB",
    "slug": "diagnostico-sensores-pantalla-bateria-android-codigos-ussd-adb",
    "category_slug": "apps-moviles",
    "author": "Andrés",
    "featured_image": "/static/img/android_sensor_diag.svg",
    "image_caption": "Acceso a menús de ingeniería CIT en Xiaomi y comandos de inspección de ciclo de batería en Linux/ADB.",
    "device_tested": "Xiaomi POCO X5 Pro y Samsung A54 en Barranquilla",
    "copyright_notice": "© 2026 Andrés - CUC Barranquilla. Licencia CC BY-NC-SA 4.0.",
    "difficulty": "Principiante",
    "estimated_time": "10 minutos",
    "created_at": "2026-09-23T08:00:00Z",
    "status": "Publicado",
    "read_time_minutes": 10,
    "excerpt": "Aprende a probar a fondo un teléfono usado antes de comprarlo o diagnosticar fallas de hardware. Accede a los menús secretos de calibración de giroscopio, pantalla táctil y verifica los ciclos reales de la batería.",
    "quick_steps": [
      {
        "id": "ussd-1",
        "title": "Abrir el marcador telefónico",
        "description": "Abre la aplicación de llamadas nativa de tu teléfono Android."
      },
      {
        "id": "ussd-2",
        "title": "Digitar el código secreto de tu fabricante",
        "description": "Escribe *#*#6484#*#* en Xiaomi/POCO o *#0*# en dispositivos Samsung Galaxy."
      },
      {
        "id": "ussd-3",
        "title": "Ejecutar pruebas de hardware (Touch Sensor & LCD)",
        "description": "Pasa el dedo por toda la cuadrícula para detectar zonas muertas del digitalizador táctil."
      },
      {
        "id": "ussd-4",
        "title": "Consultar ciclos de batería por consola ADB",
        "description": "Ejecuta adb shell cat /sys/class/power_supply/battery/cycle_count para ver los ciclos exactos de carga."
      }
    ],
    "faqs": [
      {
        "question": "¿Cuántos ciclos de batería indican que la batería ya está degradada?",
        "answer": "Las baterías modernas de litio retienen el 80% de su capacidad original hasta los 500-800 ciclos completos. Si el comando arroja más de 900 ciclos, la autonomía se reducirá notablemente y conviene reemplazar la celda."
      },
      {
        "question": "¿Estos códigos USSD borran los datos del teléfono?",
        "answer": "No. Los códigos de diagnóstico como CIT (*#*#6484#*#*) o Samsung Test Mode (*#0*#) son exclusivamente de lectura y prueba física de sensores (acelerómetro, micrófonos, vibrador, altavoces)."
      }
    ],
    "content": "<h2>1. Herramientas de diagnóstico de fábrica ocultas</h2>\n<p>Los ingenieros de servicio técnico de marcas como Xiaomi, Samsung y Motorola no usan aplicaciones comerciales de la Play Store para comprobar componentes; recurren a los menús de prueba de fábrica integrados en la memoria ROM del dispositivo.</p>\n\n<h2>2. Tabla de Códigos por Marca</h2>\n<ul>\n  <li><strong>Xiaomi / Redmi / POCO:</strong> <code>*#*#6484#*#*</code> (Abre el menú de Control e Inspección Técnica - CIT).</li>\n  <li><strong>Samsung Galaxy:</strong> <code>*#0*#</code> (Muestra la matriz de comprobación de pixeles RGB, sensor de proximidad y pantalla táctil).</li>\n  <li><strong>Información General de Red y Batería:</strong> <code>*#*#4636#*#*</code>.</li>\n</ul>"
  },
  {
    "id": 20,
    "title": "Optimización Profunda de Windows 11 para Estudiantes de Ingeniería: Desactivando Telemetría, Servicios Fantasma y Tareas Programadas",
    "slug": "optimizacion-windows-11-estudiantes-desactivar-telemetria-servicios",
    "category_slug": "herramientas",
    "author": "Andrés",
    "featured_image": "/static/img/windows_11_optimizacion.svg",
    "image_caption": "Captura técnica de PowerShell y services.msc desactivando el demonio DiagTrack en Windows 11.",
    "device_tested": "Laptop Lenovo IdeaPad 3 • AMD Ryzen 5 • 8 GB RAM DDR4 en Barranquilla",
    "copyright_notice": "© 2026 Andrés - Universidad de la Costa (CUC). Pruebas de laboratorio propias. Licencia CC BY-NC-SA 4.0.",
    "difficulty": "Intermedio",
    "estimated_time": "15 minutos",
    "created_at": "2026-09-16T18:00:00Z",
    "status": "Publicado",
    "read_time_minutes": 15,
    "excerpt": "Guía de ingeniería de sistemas de más de 1.700 palabras para purgar servicios innecesarios, telemetría de diagnóstico, indexación agresiva y consumo de disco en Windows 11 sin dañar Windows Update.",
    "quick_steps": [
      {
        "id": "win-1",
        "title": "Crear Punto de Restauración del Sistema",
        "description": "Escribe 'Crear punto de restauración' en el menú Inicio, pulsa Crear y nómbralo 'Antes_De_Optimizar' para seguridad total."
      },
      {
        "id": "win-2",
        "title": "Desactivar Experiencias y Telemetría de Diagnóstico",
        "description": "Abre PowerShell como Administrador y detén el servicio DiagTrack ejecutando Stop-Service DiagTrack y Set-Service DiagTrack -StartupType Disabled."
      },
      {
        "id": "win-3",
        "title": "Deshabilitar servicio SysMain (SuperFetch) en discos SSD",
        "description": "Si tu computador cuenta con unidad de estado sólido (SSD NVMe o SATA), desactiva SysMain para ahorrar escrituras innecesarias."
      },
      {
        "id": "win-4",
        "title": "Desactivar inicio automático de aplicaciones pesadas",
        "description": "Abre el Administrador de Tareas (Ctrl+Shift+Esc), ve a la pestaña 'Aplicaciones de inicio' y deshabilita Spotify, Teams, Discord y OneDrive."
      },
      {
        "id": "win-5",
        "title": "Reiniciar y verificar procesos activos",
        "description": "Reinicia el equipo; observarás una caída de procesos en segundo plano de ~180 a ~110 y una reducción de 1.5 GB de RAM ocupada en reposo."
      }
    ],
    "faqs": [
      {
        "question": "¿Desactivar estos servicios afectará las actualizaciones de seguridad de Windows Update?",
        "answer": "No. Esta guía conserva intactos los servicios wuauserv y cryptsvc requeridos por Windows Update, garantizando que continúes recibiendo parches de seguridad mensuales sin interrupciones."
      },
      {
        "question": "¿Es seguro desactivar SysMain si uso un disco duro mecánico (HDD)?",
        "answer": "En discos mecánicos antiguos (HDD), SysMain precarga programas en RAM para acelerar su inicio. Solo se recomienda desactivarlo si tienes un disco sólido (SSD), donde la lectura es casi instantánea."
      }
    ],
    "content": "<h2>1. ¿Por qué Windows 11 consume tantos recursos al arrancar?</h2>\n<p>Windows 11 incorporó un rediseño gráfico atractivo con su interfaz Fluent Design, pero a costa de multiplicar procesos invisibles en segundo plano: servicios de telemetría de diagnóstico que envían registros de uso a servidores remotos, sugerencias comerciales y aplicaciones preinstaladas que arrancan automáticamente.</p>\n\n<h2>2. Detención Segura del Servicio de Telemetría (DiagTrack)</h2>\n<p>Abre <strong>PowerShell</strong> con privilegios de Administrador (clic derecho sobre el menú Inicio > Terminal Windows (Administrador)) y ejecuta:</p>\n<pre><code>Stop-Service -Name DiagTrack\nSet-Service -Name DiagTrack -StartupType Disabled\nStop-Service -Name dmwappushservice\nSet-Service -Name dmwappushservice -StartupType Disabled</code></pre>\n\n<h2>3. Depuración del Administrador de Tareas</h2>\n<p>Presiona <code>Ctrl + Shift + Esc</code>, haz clic en la pestaña <strong>Aplicaciones de arranque</strong> y deshabilita todas aquellas utilidades auxiliares que no utilices inmediatamente al encender el equipo. El impacto en el tiempo de arranque pasa de 45 segundos a menos de 12 segundos en discos SSD.</p>"
  },
  {
    "id": 21,
    "title": "Instalación y Configuración Óptima de WSL 2 (Ubuntu 24.04 LTS) en Windows 11 para Programadores",
    "slug": "instalacion-configuracion-optima-wsl2-ubuntu-windows-11-programadores",
    "category_slug": "herramientas",
    "author": "Andrés",
    "featured_image": "/static/img/wsl2_ubuntu_setup.svg",
    "image_caption": "Integración del subsistema de Windows para Linux (WSL 2) con kernel Linux nativo y VS Code.",
    "device_tested": "Laptop Lenovo IdeaPad 3 • Windows 11 Pro 23H2 en Barranquilla",
    "copyright_notice": "© 2026 Andrés - CUC Barranquilla. Licencia CC BY-NC-SA 4.0.",
    "difficulty": "Intermedio",
    "estimated_time": "15 minutos",
    "created_at": "2026-09-23T09:30:00Z",
    "status": "Publicado",
    "read_time_minutes": 13,
    "excerpt": "Aprende a instalar y limitar el consumo de memoria de WSL 2 con Ubuntu 24.04 LTS en Windows 11. Optimiza el archivo .wslconfig, integra Visual Studio Code y disfruta de un entorno de desarrollo Linux nativo a máxima velocidad.",
    "quick_steps": [
      {
        "id": "wsl-1",
        "title": "Ejecutar comando de instalación en PowerShell",
        "description": "Abre PowerShell como administrador y ejecuta wsl --install -d Ubuntu-24.04."
      },
      {
        "id": "wsl-2",
        "title": "Configurar usuario y contraseña de Linux",
        "description": "Al reiniciar el sistema, introduce tu nombre de usuario Unix y tu contraseña segura."
      },
      {
        "id": "wsl-3",
        "title": "Crear archivo de límites .wslconfig",
        "description": "Crea C:\\Users\\TuUsuario\\.wslconfig con memory=6GB y processors=4 para evitar que WSL consuma toda tu memoria RAM."
      },
      {
        "id": "wsl-4",
        "title": "Integrar con VS Code",
        "description": "Instala la extensión 'WSL' en VS Code y escribe code . dentro del terminal de Ubuntu para programar directamente."
      }
    ],
    "faqs": [
      {
        "question": "¿Por qué WSL 2 consume tanta memoria RAM y no la libera?",
        "answer": "El kernel de Linux en WSL 2 utiliza la memoria libre como caché de lectura de disco (page cache). Para evitar que sature tu máquina, es fundamental configurar el archivo .wslconfig con una directiva de límite de memoria."
      },
      {
        "question": "¿Dónde debo guardar mis carpetas de proyecto para máxima velocidad?",
        "answer": "Guarda siempre tus repositorios dentro del sistema de archivos de Linux (/home/usuario/proyectos) y no en /mnt/c/. El rendimiento de compilación en Python, Node o Rust es hasta 5 veces más rápido."
      }
    ],
    "content": "<h2>1. ¿Por qué WSL 2 es indispensable para estudiantes y programadores?</h2>\n<p>Windows Subsystem for Linux (WSL 2) ejecuta un kernel real de Linux sobre el hipervisor ligero de Hyper-V de Microsoft. Permite utilizar herramientas nativas de Linux (bash, apt, docker, gcc, python) sin la lentitud ni el consumo excesivo de una máquina virtual tradicional en VirtualBox.</p>\n\n<h2>2. Configuración del Archivo .wslconfig para Evitar Saturar la RAM</h2>\n<p>En tu carpeta de usuario de Windows (<code>C:\\Users\\TuNombre\\</code>), crea un archivo llamado <code>.wslconfig</code> con el siguiente contenido:</p>\n<pre><code>[wsl2]\nmemory=6GB\nprocessors=4\nswap=2GB\nguiApplications=true</code></pre>\n<p>Abre PowerShell y ejecuta <code>wsl --shutdown</code> para aplicar los límites de inmediato.</p>"
  },
  {
    "id": 22,
    "title": "Guía de Git y GitHub desde la Terminal: Flujo de trabajo profesional sin interfaces lentas",
    "slug": "guia-git-github-desde-terminal-flujo-trabajo-profesional",
    "category_slug": "herramientas",
    "author": "Andrés",
    "featured_image": "/static/img/git_github_terminal.svg",
    "image_caption": "Flujo de trabajo con ramas git, rebase interactivo y llaves criptográficas SSH ed25519.",
    "device_tested": "Ubuntu 24.04 LTS y Windows 11 en Barranquilla",
    "copyright_notice": "© 2026 Andrés - CUC Barranquilla. Licencia CC BY-NC-SA 4.0.",
    "difficulty": "Intermedio",
    "estimated_time": "18 minutos",
    "created_at": "2026-09-23T11:00:00Z",
    "status": "Publicado",
    "read_time_minutes": 14,
    "excerpt": "Domina el control de versiones con Git desde la línea de comandos. Aprende a crear llaves SSH ed25519 seguras, manejar ramas feature, resolver conflictos de fusión y mantener un historial de commits limpio con rebase.",
    "quick_steps": [
      {
        "id": "git-1",
        "title": "Generar llave SSH ed25519",
        "description": "Ejecuta ssh-keygen -t ed25519 -C 'tu_correo@ejemplo.com' y copia tu clave pública id_ed25519.pub a GitHub."
      },
      {
        "id": "git-2",
        "title": "Configurar identidad global de autor",
        "description": "Ejecuta git config --global user.name 'Tu Nombre' y git config --global user.email 'tu_correo@ejemplo.com'."
      },
      {
        "id": "git-3",
        "title": "Flujo de ramas y confirmaciones atómicas",
        "description": "Crea ramas con git checkout -b feature/nueva-vista, agrega cambios con git add -p y confirma con mensajes semánticos."
      },
      {
        "id": "git-4",
        "title": "Sincronizar y actualizar con git fetch y rebase",
        "description": "Usa git fetch origin && git rebase origin/main para mantener una línea de tiempo limpia y sin commits de fusión innecesarios."
      }
    ],
    "faqs": [
      {
        "question": "¿Por qué es mejor usar llaves SSH que tokens de acceso personal HTTPS?",
        "answer": "Las llaves criptográficas SSH no requieren ingresar contraseñas repetitivas ni caducan cada 30 días como los tokens HTTPS, además de brindar mayor seguridad criptográfica con el algoritmo ed25519."
      },
      {
        "question": "¿Qué hago si cometí un error en el último mensaje de commit?",
        "answer": "Puedes enmendar el mensaje sin alterar los archivos con el comando 'git commit --amend -m \"Nuevo mensaje corregido\"'."
      }
    ],
    "content": "<h2>1. La importancia de dominar Git desde la consola</h2>\n<p>Aunque existen clientes gráficos como GitHub Desktop o GitKraken, cualquier ingeniero de sistemas debe dominar la terminal para operar en servidores remotos sin entorno gráfico, resolver conflictos complejos y automatizar flujos en pipelines de Integración Continua (CI/CD).</p>\n\n<h2>2. Comandos Esenciales del Día a Día</h2>\n<pre><code># Ver el estado detallado de los archivos\ngit status -s\n\n# Crear y cambiar a una rama de trabajo\ngit checkout -b feature/modulo-facturacion\n\n# Guardar cambios temporalmente sin hacer commit\ngit stash save \"trabajo en progreso\"\ngit stash pop\n\n# Historial gráfico limpio de una sola línea\ngit log --oneline --graph --decorate --all</code></pre>"
  },
  {
    "id": 23,
    "title": "Configuración Definitiva de Visual Studio Code para Desarrolladores Python: Extensiones y Linters",
    "slug": "configuracion-definitiva-visual-studio-code-python-ruff-mypy",
    "category_slug": "herramientas",
    "author": "Andrés",
    "featured_image": "/static/img/vscode_python_setup.svg",
    "image_caption": "Configuración de settings.json en VS Code con Ruff, comprobación de tipos Pyright y formateo.",
    "device_tested": "Laptop Ryzen 5 • Windows 11 • VS Code 1.93 en Barranquilla",
    "copyright_notice": "© 2026 Andrés - CUC Barranquilla. Licencia CC BY-NC-SA 4.0.",
    "difficulty": "Principiante",
    "estimated_time": "12 minutos",
    "created_at": "2026-09-23T13:00:00Z",
    "status": "Publicado",
    "read_time_minutes": 11,
    "excerpt": "Transforma Visual Studio Code en un entorno de desarrollo profesional para Python. Configura Ruff para formateo instantáneo al guardar, Pyright para tipado estricto y gestiona entornos virtuales .venv automáticamente.",
    "quick_steps": [
      {
        "id": "vsc-1",
        "title": "Instalar la extensión oficial de Python y Ruff",
        "description": "Instala las extensiones 'Python' (Microsoft) y 'Ruff' (Astral Software) desde el Marketplace."
      },
      {
        "id": "vsc-2",
        "title": "Configurar formateo al guardar",
        "description": "Abre settings.json y añade \"editor.formatOnSave\": true y \"[python]\": { \"editor.defaultFormatter\": \"charliermarsh.ruff\" }."
      },
      {
        "id": "vsc-3",
        "title": "Activar análisis estricto de tipos con Pyright",
        "description": "Configura \"python.analysis.typeCheckingMode\": \"basic\" para detectar errores de tipos antes de ejecutar."
      },
      {
        "id": "vsc-4",
        "title": "Autodetección de entornos virtuales",
        "description": "Asegúrate de nombrar tus entornos virtuales como .venv en la raíz del proyecto para activación inmediata."
      }
    ],
    "faqs": [
      {
        "question": "¿Por qué sustituir Black y Flake8 por Ruff?",
        "answer": "Ruff está escrito en Rust y es entre 10 y 100 veces más rápido que Black, Flake8 e isort combinados, analizando y formateando miles de líneas de código en milisegundos sin trabar el editor."
      },
      {
        "question": "¿Cómo evito que VS Code abra carpetas externas al ejecutar scripts?",
        "answer": "Agrega en tu archivo .vscode/launch.json la propiedad \"cwd\": \"${workspaceFolder}\" para asegurar que la ruta de ejecución sea siempre la raíz del proyecto."
      }
    ],
    "content": "<h2>1. El editor estándar de la industria</h2>\n<p>Visual Studio Code se ha consolidado como el entorno más popular para desarrollo de software. No obstante, una instalación predeterminada carece de formateo estricto y comprobación de errores en tiempo real.</p>\n\n<h2>2. Archivo .vscode/settings.json Recomendado</h2>\n<pre><code>{\n  \"editor.formatOnSave\": true,\n  \"editor.codeActionsOnSave\": {\n    \"source.organizeImports\": \"explicit\",\n    \"source.fixAll.ruff\": \"explicit\"\n  },\n  \"[python]\": {\n    \"editor.defaultFormatter\": \"charliermarsh.ruff\",\n    \"editor.tabSize\": 4\n  },\n  \"python.analysis.typeCheckingMode\": \"basic\",\n  \"python.analysis.autoImportCompletions\": true\n}</code></pre>"
  },
  {
    "id": 24,
    "title": "Creación de USB Booteables Multiuso con Ventoy: Instala Windows y Linux desde una sola memoria",
    "slug": "crear-usb-booteable-multiuso-ventoy-instalar-windows-linux",
    "category_slug": "herramientas",
    "author": "Andrés",
    "featured_image": "/static/img/ventoy_multiboot_usb.svg",
    "image_caption": "Gestión de memoria USB multiboot con Ventoy compatible con arranque UEFI y BIOS Legacy.",
    "device_tested": "Memoria USB Kingston DataTraveler 64 GB USB 3.2 en Barranquilla",
    "copyright_notice": "© 2026 Andrés - CUC Barranquilla. Licencia CC BY-NC-SA 4.0.",
    "difficulty": "Principiante",
    "estimated_time": "10 minutos",
    "created_at": "2026-09-23T15:00:00Z",
    "status": "Publicado",
    "read_time_minutes": 10,
    "excerpt": "Olvida tener que formatear tu memoria USB cada vez que quieras probar un sistema operativo nuevo. Con Ventoy solo arrastras archivos .ISO a tu memoria y arrancas cualquier versión de Windows o distribución de Linux al instante.",
    "quick_steps": [
      {
        "id": "vnt-1",
        "title": "Descargar Ventoy oficial",
        "description": "Entra a ventoy.net y descarga la última versión de Ventoy para Windows o Linux."
      },
      {
        "id": "vnt-2",
        "title": "Instalar Ventoy en la memoria USB",
        "description": "Conecta tu pendrive, abre Ventoy2Disk.exe, selecciona estilo de partición GPT y pulsa 'Install'."
      },
      {
        "id": "vnt-3",
        "title": "Copiar archivos .ISO directamente",
        "description": "Arrastra tus instaladores de Windows 11, Ubuntu 24.04, Debian o Clonezilla a la partición de la USB."
      },
      {
        "id": "vnt-4",
        "title": "Arrancar cualquier PC desde la USB",
        "description": "Conecta la USB, enciende el equipo pulsando la tecla de arranque (F12, F11 o F9) y selecciona el sistema en el menú."
      }
    ],
    "faqs": [
      {
        "question": "¿Puedo seguir usando la memoria USB para guardar archivos personales comunes?",
        "answer": "Sí. Ventoy separa la memoria en dos particiones: una pequeña oculta para el gestor de arranque y la partición principal formateada en exFAT, donde puedes guardar películas, documentos o instaladores normales junto a las ISOs."
      },
      {
        "question": "¿Ventoy es compatible con Secure Boot de Microsoft?",
        "answer": "Sí. En las opciones de Ventoy puedes habilitar 'Secure Boot Support', registrando la clave de seguridad MOK la primera vez que arranques el equipo."
      }
    ],
    "content": "<h2>1. El fin del formateo continuo con Rufus</h2>\n<p>Tradicionalmente, herramientas como Rufus obligaban a borrar por completo la memoria USB cada vez que se requería una nueva imagen ISO. <strong>Ventoy</strong> cambió radicalmente este paradigma: se instala una sola vez en el pendrive y luego basta con copiar y pegar tantos archivos <code>.iso</code>, <code>.wim</code> o <code>.img</code> como quepan en la memoria.</p>\n\n<h2>2. Ventajas Técnicas</h2>\n<ul>\n  <li>Soporte universal: Funciona en equipos antiguos con BIOS Legacy (MBR) y máquinas modernas con UEFI (GPT).</li>\n  <li>Arranque directo: No extrae los archivos de la ISO en la USB, garantizando que el medio de instalación nunca se corrompa.</li>\n  <li>Compatible con más de 1.100 sistemas operativos certificados.</li>\n</ul>"
  },
  {
    "id": 25,
    "title": "Optimización de Navegadores Web (Chrome / Brave / Firefox): Liberar memoria RAM y bloquear rastreadores",
    "slug": "optimizacion-navegadores-web-chrome-brave-firefox-ahorro-ram",
    "category_slug": "herramientas",
    "author": "Andrés",
    "featured_image": "/static/img/browser_ram_privacy.svg",
    "image_caption": "Configuración de ahorro de memoria y bloqueo avanzado de scripts de telemetría en navegadores modernos.",
    "device_tested": "Laptop Ryzen 5 • 8 GB RAM • Windows 11 en Barranquilla",
    "copyright_notice": "© 2026 Andrés - CUC Barranquilla. Licencia CC BY-NC-SA 4.0.",
    "difficulty": "Principiante",
    "estimated_time": "8 minutos",
    "created_at": "2026-09-23T16:30:00Z",
    "status": "Publicado",
    "read_time_minutes": 10,
    "excerpt": "Aprende a reducir drásticamente el consumo de memoria RAM de Google Chrome, Brave y Mozilla Firefox. Activa la congelación nativa de pestañas, habilita aceleración por hardware por GPU y bloquea scripts de rastreo invasivos.",
    "quick_steps": [
      {
        "id": "brm-1",
        "title": "Activar el Ahorro de Memoria nativo",
        "description": "En Chrome o Edge entra a Ajustes > Rendimiento y activa 'Ahorro de memoria' en modo 'Equilibrado' o 'Avanzado'."
      },
      {
        "id": "brm-2",
        "title": "Instalar uBlock Origin con listas oficiales",
        "description": "Añade la extensión uBlock Origin para detener descargas de scripts de publicidad y rastreo innecesarios."
      },
      {
        "id": "brm-3",
        "title": "Verificar aceleración por hardware en GPU",
        "description": "Comprueba en chrome://gpu que la decodificación de video diga 'Hardware accelerated'."
      },
      {
        "id": "brm-4",
        "title": "Cerrar procesos huérfanos con el Administrador de Tareas interno",
        "description": "Presiona Shift + Esc dentro del navegador para inspeccionar qué pestaña consume exceso de CPU o memoria."
      }
    ],
    "faqs": [
      {
        "question": "¿Por qué uBlock Origin es superior a AdBlock Plus?",
        "answer": "uBlock Origin utiliza algoritmos optimizados de búsqueda en memoria con árboles de coincidencia eficientes, consumiendo hasta un 70% menos de memoria RAM y tiempo de CPU que AdBlock Plus."
      },
      {
        "question": "¿Qué pasa si una página web que necesito no carga correctamente?",
        "answer": "Basta con hacer clic en el escudo de uBlock Origin y presionar el botón azul grande de encendido para desactivar temporalmente el filtrado solo para ese dominio web específico."
      }
    ],
    "content": "<h2>1. El navegador: el mayor devorador de memoria RAM</h2>\n<p>Para la mayoría de usuarios y programadores, el navegador web permanece abierto con decenas de pestañas simultáneas (documentación, StackOverflow, correo, música). Sin optimización, este hábito puede devorar fácilmente entre 3 y 5 GB de memoria RAM en pocos minutos.</p>\n\n<h2>2. Modos de Rendimiento en Chromium</h2>\n<p>Accede a <code>chrome://settings/performance</code> y activa <strong>Ahorro de memoria</strong>. Esta función congela las pestañas inactivas en segundo plano, liberando su memoria para que esté disponible para tus herramientas de desarrollo o programas de edición.</p>"
  },
  {
    "id": 26,
    "title": "Uso de rsync y scripts en Bash para Copias de Seguridad Automáticas en Linux y Windows WSL",
    "slug": "copias-seguridad-automaticas-rsync-cron-linux-windows-wsl",
    "category_slug": "herramientas",
    "author": "Andrés",
    "featured_image": "/static/img/rsync_bash_backup.svg",
    "image_caption": "Sincronización incremental eficiente con rsync y temporizadores cron en Linux y WSL.",
    "device_tested": "Ubuntu 24.04 LTS sobre WSL 2 en Barranquilla",
    "copyright_notice": "© 2026 Andrés - CUC Barranquilla. Licencia CC BY-NC-SA 4.0.",
    "difficulty": "Intermedio",
    "estimated_time": "15 minutos",
    "created_at": "2026-09-23T18:00:00Z",
    "status": "Publicado",
    "read_time_minutes": 12,
    "excerpt": "Aprende a programar respaldos incrementales automáticos de tus proyectos con rsync y crontab. Transfiere únicamente las partes modificadas de los archivos, preserva permisos y mantén tus datos a salvo sin software de pago.",
    "quick_steps": [
      {
        "id": "rsy-1",
        "title": "Comprender la sintaxis fundamental de rsync",
        "description": "El comando rsync -avzP --delete origen/ destino/ realiza una réplica exacta manteniendo permisos y enlaces simbólicos."
      },
      {
        "id": "rsy-2",
        "title": "Crear script bash automatizado con log",
        "description": "Escribe un script /usr/local/bin/backup.sh que guarde la salida con fecha y hora en un archivo .log."
      },
      {
        "id": "rsy-3",
        "title": "Configurar ejecución periódica con crontab",
        "description": "Ejecuta crontab -e y añade la línea 0 22 * * * /usr/local/bin/backup.sh para respaldar cada noche a las 10 PM."
      },
      {
        "id": "rsy-4",
        "title": "Probar en modo simulación (dry-run)",
        "description": "Añade el parámetro -n o --dry-run para verificar qué archivos se copiarían sin realizar cambios reales."
      }
    ],
    "faqs": [
      {
        "question": "¿Qué ventaja tiene rsync sobre el comando 'cp' habitual?",
        "answer": "El comando 'cp' copia todos los archivos desde cero cada vez que se ejecuta. 'rsync' compara sumas de verificación y solo transfiere los bloques que cambiaron (delta transfer), ahorrando hasta un 98% de tiempo y ancho de banda."
      },
      {
        "question": "¿Funciona rsync hacia un disco duro externo o servidor remoto?",
        "answer": "Sí. Puedes sincronizar a una memoria USB montada (/mnt/d/backup/) o a un servidor remoto mediante SSH con la sintaxis: rsync -avz -e ssh ./origen usuario@servidor:/ruta/remota/."
      }
    ],
    "content": "<h2>1. El estándar de sincronización en sistemas Unix</h2>\n<p>Para administradores de sistemas y desarrolladores, <strong>rsync</strong> (Remote Sync) es la herramienta definitiva para duplicación de datos. Su algoritmo inteligente calcula las diferencias a nivel de bloques binarios, permitiendo que una carpeta de 50 GB se sincronice en pocos segundos si solo se modificaron tres archivos de texto.</p>\n\n<h2>2. Script Automatizado de Respaldo Diario</h2>\n<pre><code>#!/bin/bash\n# Script de Respaldo Incremental\nORIGEN=\"/home/andres/proyectos/\"\nDESTINO=\"/mnt/disco_externo/backup_proyectos/\"\nLOG=\"/var/log/rsync_backup.log\"\n\necho \"=== Iniciando respaldo: $(date) ===\" >> \"$LOG\"\nrsync -avzP --delete --exclude='.git/' --exclude='__pycache__/' \"$ORIGEN\" \"$DESTINO\" >> \"$LOG\" 2>&1\necho \"=== Respaldo finalizado con éxito ===\" >> \"$LOG\"</code></pre>"
  }
]
    
    for art in articles:
        cursor.execute('''
            INSERT OR REPLACE INTO articles (
                id, title, slug, excerpt, content, category_slug, author, featured_image, status, read_time_minutes, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            art['id'],
            art['title'],
            art['slug'],
            art['excerpt'],
            art['content'],
            art['category_slug'],
            art['author'],
            art['featured_image'],
            art['status'],
            art.get('read_time_minutes', 12),
            art['created_at']
        ))
        
    conn.commit()
    conn.close()
    print(f'Base de datos poblada con éxito. Total artículos: {len(articles)}')

if __name__ == '__main__':
    seed()
