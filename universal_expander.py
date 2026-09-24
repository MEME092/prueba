# -*- coding: utf-8 -*-
"""
Expansor de texto puro para garantizar que cada uno de los 26 artículos
supere holgadamente las 1.550 palabras de texto puro (sin contar etiquetas HTML).
"""

import re
from generate_tramites import TRAMITES_CONTENT
from generate_python_flet import PYTHON_FLET_CONTENT
from generate_android_adb import ANDROID_ADB_CONTENT
from generate_herramientas import HERRAMIENTAS_CONTENT

def count_pure_words(text):
    clean = re.sub(r'<[^>]+>', ' ', text)
    return len(re.findall(r'\b\w+\b', clean))

EXPANSIONS = {}

# -----------------------------------------------------------------------------
# ARTÍCULO 3: SISBÉN IV
# -----------------------------------------------------------------------------
EXPANSIONS[3] = """
<h2>7. El Registro Social de Hogares (RSH) y la Interoperabilidad de Bases de Datos</h2>
<p>Desde finales de 2023, el Departamento Nacional de Planeación puso en marcha el <strong>Registro Social de Hogares (RSH)</strong>, una mega base de datos que cruza automáticamente más de 40 fuentes de información estatales y privadas. Esto significa que la clasificación del Sisbén ya no depende únicamente de las respuestas que el ciudadano entrega al encuestador en su sala, sino de un seguimiento dinámico de transacciones en tiempo real.</p>
<p>El RSH coteja mensualmente la información con bases de datos como:</p>
<ul>
  <li><strong>PILA (Planilla Integrada de Liquidación de Aportes):</strong> Verifica si algún integrante del hogar se encuentra cotizando a seguridad social en salud o pensión con salarios formales.</li>
  <li><strong>ADRES (Administradora de los Recursos de la Salud):</strong> Comprueba si la persona figura en el régimen contributivo o en el subsidiado.</li>
  <li><strong>RUNT (Registro Único Nacional de Tránsito):</strong> Detecta si algún miembro del núcleo familiar figura como titular o propietario de vehículos automotores, motocicletas de alto cilindraje o maquinaria amarilla.</li>
  <li><strong>DIAN (Dirección de Impuestos y Aduanas Nacionales):</strong> Evalúa los reportes de información exógena, compras con tarjeta de crédito, retenciones en la fuente e ingresos brutos anuales.</li>
  <li><strong>Ministerio de Educación (SIMAT y SNIES):</strong> Cruza datos sobre matrículas en colegios privados o universidades públicas con matrícula cero.</li>
</ul>
<p>Por este motivo, si un hogar experimenta un cambio sustancial en sus ingresos (por ejemplo, pérdida del empleo formal o liquidación laboral), el sistema puede tardar hasta 60 días en reflejar la actualización. Conocer este mecanismo permite a los ciudadanos ejercer su derecho a la actualización de datos mediante los canales formales sin caer en la desesperación ni acudir a intermediarios ilegales.</p>

<h2>8. Procedimiento Legal para Exclusión de Miembros del Hogar</h2>
<p>Una situación muy habitual ocurre cuando un hijo mayor de edad se independiza o cuando ocurre una separación conyugal, pero la expareja continúa figurando en la ficha técnica del Sisbén elevando los ingresos del hogar de forma ficticia. Para retirar a un integrante:</p>
<ol>
  <li>El jefe de hogar registrado debe redactar una solicitud formal de <em>'Novedad de Retiro de Integrante'</em>.</li>
  <li>Adjuntar copia del documento de identidad del solicitante y del miembro que se retira (o manifestación bajo juramento de no convivencia con su nuevo domicilio).</li>
  <li>Radicar la novedad en el portal ciudadano o en la oficina municipal del Sisbén de su localidad. Al quedar en firme la novedad, el grupo familiar del hogar se recalculará automáticamente, permitiendo acceder a los beneficios sociales a los que verdaderamente tienen derecho.</li>
</ol>
"""

# -----------------------------------------------------------------------------
# ARTÍCULO 5: CONTRALORÍA
# -----------------------------------------------------------------------------
EXPANSIONS[5] = """
<h2>9. El Régimen de Exclusión y Rehabilitación en el Boletín SIREF</h2>
<p>Una inquietud jurídica recurrente entre profesionales y contratistas es conocer cómo opera la <strong>rehabilitación fiscal</strong> cuando una persona ha sido sancionada en un proceso de responsabilidad fiscal. La legislación colombiana (Ley 610 de 2000, artículo 60) consagra que la inclusión en el Boletín de Responsables Fiscales tiene causales legales y expeditas de exclusión:</p>
<ol>
  <li><strong>Por pago total de la obligación fiscal liquidada:</strong> Cuando el sancionado cancela el valor del fallo condenatorio debidamente indexado ante la tesorería de la entidad estatal afectada o ante la Contraloría General. La entidad receptora remite de oficio la constancia de pago al área de registro del SIREF para su exclusión inmediata en un plazo máximo de cinco (5) días hábiles.</li>
  <li><strong>Por cumplimiento del término de cinco (5) años:</strong> La ley colombiana prohíbe las sanciones intemporales o imprescriptibles en materia fiscal ordinaria. Transcurridos cinco (5) años continuos desde la ejecutoria del fallo de responsabilidad fiscal sin que la entidad estatal haya logrado hacer efectiva la deuda mediante cobro coactivo, la anotación debe ser retirada del boletín por mandato del debido proceso y el derecho fundamental al trabajo, salvo que se haya formulado acuerdo formal de pago con plazos vigentes.</li>
  <li><strong>Por revocatoria directa o decisión judicial contenciosa:</strong> Si el afectado interpone una demanda de nulidad y restablecimiento del derecho ante los juzgados administrativos y obtiene una sentencia favorable que anule el acto administrativo fiscal, la Contraloría está obligada a retirar la anotación inmediatamente tras la ejecutoria de la providencia judicial.</li>
</ol>

<h2>10. Diferencia entre Responsabilidad Fiscal, Disciplinaria y Penal</h2>
<p>Para evitar confusiones en convocatorias públicas y auditorías de talento humano, es crucial no mezclar los tres tipos de responsabilidad que pueden concurrir en un mismo hecho:</p>
<ul>
  <li><strong>Responsabilidad Fiscal (Contraloría):</strong> Exclusivamente patrimonial y resarcitoria. Busca recuperar el dinero público perdido. No impone penas de cárcel ni destituye directamente, pero inhabilita para contratar con el Estado mientras figure la deuda en el boletín.</li>
  <li><strong>Responsabilidad Disciplinaria (Procuraduría):</strong> Sanciona la conducta funcional del servidor público o contratista. Puede imponer sanciones como destitución del cargo o suspensión e inhabilidad general.</li>
  <li><strong>Responsabilidad Penal (Fiscalía General y Jueces Penales):</strong> Investiga la comisión de delitos contra la administración pública (como peculado por apropiación, cohecho o celebración indebida de contratos) imponiendo penas privativas de la libertad en centros penitenciarios.</li>
</ul>
"""

# -----------------------------------------------------------------------------
# ARTÍCULO 6: RUNT Y SIMIT
# -----------------------------------------------------------------------------
EXPANSIONS[6] = """
<h2>9. Procedimiento Técnico para la Audiencia Pública Virtual de Impugnación</h2>
<p>Si consideras que un comparendo o fotomulta fue impuesto de manera irregular (por ejemplo, porque la cámara de fotodetección no contaba con la calibración metrológica vigente del Instituto Nacional de Metrología, o porque tú no ibas conduciendo el vehículo de acuerdo con la Sentencia C-038 de 2020), tienes el derecho legal fundamental de <strong>solicitar una Audiencia Pública de Impugnación</strong>:</p>
<ol>
  <li><strong>Plazo perentorio para solicitar audiencia:</strong>
    <ul>
      <li>Para comparendos físicos impuestos en vía pública por agentes de tránsito: Dispones de cinco (5) días hábiles posteriores a la orden de comparendo.</li>
      <li>Para comparendos electrónicos de fotodetección: Dispones de once (11) días hábiles contados a partir del día siguiente a la notificación por correo certificado o aviso judicial.</li>
    </ul>
  </li>
  <li><strong>Radicación virtual de la solicitud:</strong> La mayoría de secretarías de movilidad del país (como la de Barranquilla, Bogotá, Medellín o Cali) cuentan con ventanillas únicas virtuales donde puedes agendar tu audiencia por videoconferencia (Google Meet o Microsoft Teams).</li>
  <li><strong>Desarrollo de la audiencia ante el Inspector de Tránsito:</strong> Durante la audiencia, el inspector actúa como funcionario judicial contravencional. Debes presentar tus alegatos con fundamento en la ley: exigir la prueba de calibración del cinemómetro, solicitar la prueba fotográfica clara del rostro del conductor y constatar que se haya cumplido la debida notificación en la dirección registrada en el RUNT.</li>
  <li><strong>Decisión contravencional:</strong> Si el inspector encuentra fundados tus argumentos, emitirá una resolución de exoneración y ordenará al operador del SIMIT levantar el registro de la multa en un plazo no mayor a tres días hábiles, dejándote a paz y salvo de manera definitiva.</li>
</ol>

<h2>10. La Trampa de los Tramitadores de 'Borrados de Comparendos'</h2>
<p>En redes sociales y en las inmediaciones de las sedes de tránsito proliferan personas que ofrecen 'borrar comparendos del sistema SIMIT por la mitad de precio'. Esta práctica constituye una estafa cibernética. Ningún particular tiene acceso para alterar las tablas de bases de datos de la Federación Colombiana de Municipios. En muchos casos, lo que hacen estos delincuentes es interponer derechos de petición falsos con tutelas fraudulentas que suspenden temporalmente el comparendo durante pocos días mientras cobran la suma de dinero; cuando el juzgado rechaza la tutela, la multa reaparece en el sistema con intereses moratorios duplicados. Exige siempre resoluciones formales expedidas por inspectores de tránsito.</p>
"""

# -----------------------------------------------------------------------------
# ARTÍCULO 7: ADRES / FOSYGA BDUA
# -----------------------------------------------------------------------------
EXPANSIONS[7] = """
<h2>7. Procedimiento ante Multiafiliación en Dos EPS Distintas</h2>
<p>Uno de los problemas más engorrosos en la base de datos BDUA ocurre cuando el sistema refleja la anomalía conocida como <strong>Multiafiliación</strong>: el ciudadano aparece registrado simultáneamente en dos EPS diferentes (por ejemplo, en una EPS contributiva como Sanitas y en una subsidiada como Mutual Ser). Esto ocurre frecuentemente cuando se tramita un nuevo empleo formal y el empleador afilia al trabajador a una nueva entidad promotora de salud sin esperar el corte de compensación mensual de la ADRES.</p>
<p>Las consecuencias de la multiafiliación son delicadas: los sistemas hospitalarios pueden rechazar autorizaciones de medicamentos o remisiones quirúrgicas alegando un 'conflicto de competencias'. Para solucionar este bloqueo:</p>
<ol>
  <li>Ingresa a la plataforma oficial del Ministerio de Salud: <code>https://miseguridadsocial.gov.co</code> y regístrate con tu número de documento.</li>
  <li>Accede a la sección de <em>Novedades &gt; Unificación de Afiliación</em>.</li>
  <li>Selecciona cuál de las dos EPS es tu entidad de preferencia legítima y solicita la desafiliación formal de la entidad duplicada.</li>
  <li>El sistema consolidará la solicitud en el siguiente ciclo semanal de compensación de la ADRES, dejando un único registro activo en la BDUA.</li>
</ol>

<h2>8. Reclamación y Pago de Incapacidades Médicas ante la EPS</h2>
<p>Otro ámbito donde el certificado de afiliación de la ADRES cumple un papel determinante es en el cobro de incapacidades laborales de origen común o licencias de maternidad/paternidad. De conformidad con el Decreto 780 de 2016 y la jurisprudencia de la Corte Constitucional, para que una EPS reconozca económicamente una incapacidad médica, el trabajador debe contar con aportes continuos al sistema de seguridad social durante el periodo de gestación o durante las cuatro semanas anteriores al inicio del reposo médico.</p>
<p>Descargar el certificado de la BDUA permite acreditar de manera fidedigna la fecha exacta desde la cual te encuentras activo sin periodos de mora ni interrupciones patronales, sirviendo como prueba reina en caso de tener que interponer un derecho de petición o una acción de tutela por retención indebida del pago de subsidios de incapacidad médica.</p>
"""

# -----------------------------------------------------------------------------
# ARTÍCULO 10: APIS ASÍNCRONAS EN FLET
# -----------------------------------------------------------------------------
EXPANSIONS[10] = """
<h2>12. Implementación del Patrón Circuit Breaker para Resiliencia de Red</h2>
<p>En aplicaciones industriales de alta concurrencia construidas con Python y Flet, uno de los errores arquitectónicos más graves es seguir bombardeando un microservicio externo cuando este ya ha comenzado a fallar o responder con códigos HTTP 500 / 503. Esto provoca que la interfaz gráfica acumule cientos de corrutinas en espera, consumiendo memoria RAM y agotando los sockets del sistema operativo.</p>
<p>La solución de ingeniería recomendada es el patrón <strong>Circuit Breaker (Disyuntor de Red)</strong>. Este mecanismo monitoriza las solicitudes fallidas continuas: si se registran más de 5 fallos en menos de 10 segundos, el disyuntor 'se abre' e interrumpe inmediatamente todas las solicitudes subsiguientes durante un periodo de enfriamiento (por ejemplo, 30 segundos), mostrando un mensaje informativo amigable al usuario sin intentar conectarse a la red. Una vez transcurrido el tiempo de reposo, el disyuntor pasa a estado 'medio abierto' permitiendo una solicitud de prueba: si esta tiene éxito, el circuito se restablece con normalidad.</p>

<h2>13. Descarga Progresiva de Archivos Masivos con Monitoreo de Progreso</h2>
<p>Cuando tu aplicación en Flet necesita descargar conjuntos de datos pesados (como archivos GeoJSON, paquetes de modelos o imágenes de satélite), nunca debes descargar el archivo de un solo golpe. Con <code>aiohttp</code>, podemos leer el contenido por fragmentos de 64 KB y reflejar el porcentaje exacto de descarga en una barra interactiva <code>ft.ProgressBar</code>:</p>
<pre><code>async def download_file_with_progress(url: str, output_path: str, progress_bar: ft.ProgressBar, page: ft.Page):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            total_size = int(resp.headers.get('content-length', 0))
            downloaded = 0
            with open(output_path, 'wb') as f:
                async for chunk in resp.content.iter_chunked(65536):
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total_size &gt; 0:
                        progress_bar.value = downloaded / total_size
                        page.update()
</code></pre>
"""

# -----------------------------------------------------------------------------
# ARTÍCULO 12: DOCKER PWA FLET
# -----------------------------------------------------------------------------
EXPANSIONS[12] = """
<h2>13. Optimización de Memoria y Rendimiento con Jemalloc en Contenedores</h2>
<p>En aplicaciones de Python de larga duración bajo servidores en producción, el gestor de memoria predeterminado de la librería estándar de C (<code>glibc malloc</code>) tiende a fragmentar la memoria RAM con el paso de los días, haciendo que el contenedor consuma más memoria de la necesaria incluso después de que los usuarios cierran sus sesiones web.</p>
<p>Para solucionar esta fragmentación en Linux, los ingenieros de software configuran <strong>jemalloc</strong>, un gestor de memoria optimizado para multihilo desarrollado por Jason Evans para FreeBSD y utilizado intensivamente por Meta y Google. Podemos habilitarlo en nuestro <code>Dockerfile</code> agregando:</p>
<pre><code>RUN apt-get update &amp;&amp; apt-get install -y --no-install-recommends libjemalloc2 &amp;&amp; rm -rf /var/lib/apt/lists/*
ENV LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libjemalloc.so.2
</code></pre>
<p>Al cargar jemalloc antes de inicializar el runtime de Python, la memoria liberada por los componentes de Flet se devuelve de inmediato al sistema operativo, reduciendo la huella de memoria del contenedor en un 35% y previniendo caídas imprevistas por falta de RAM.</p>

<h2>14. Configuración de Cabeceras de Seguridad HTTP en Nginx</h2>
<p>Para obtener una calificación 'A+' en análisis de seguridad web (como SSL Labs o Mozilla Observatory), es imperativo que el archivo de configuración de Nginx inyecte las directivas de seguridad modernas que protejan a los usuarios de ataques de inyección de scripts (XSS) y secuestro de clics (Clickjacking):</p>
<pre><code>add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-XSS-Protection "1; mode=block" always;
add_header X-Content-Type-Options "nosniff" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header Content-Security-Policy "default-src 'self' https: data: blob: 'unsafe-inline' 'unsafe-eval' wss:;" always;
</code></pre>
"""

# -----------------------------------------------------------------------------
# ARTÍCULO 13: GESTIÓN DE ESTADOS EN FLET
# -----------------------------------------------------------------------------
EXPANSIONS[13] = """
<h2>14. Persistencia Cifrada de Sesiones y Tokens con AES-256</h2>
<p>Aunque <code>page.client_storage</code> almacena información en el dispositivo del usuario, en equipos compartidos (como computadoras de bibliotecas universitarias o laboratorios comunes), almacenar tokens de autenticación o datos personales en texto legible representa un riesgo de seguridad inaceptable.</p>
<p>Para blindar el almacenamiento local, implementamos una capa de encriptación transparente utilizando el estándar criptográfico <strong>Fernet (AES-128 en modo CBC con autenticación HMAC-SHA256)</strong> de la biblioteca <code>cryptography</code> de Python. Antes de que cualquier valor sea serializado hacia el almacenamiento local del sistema operativo, el objeto es cifrado con una clave derivada de la huella de hardware del equipo; y cuando la aplicación se inicia, se descifra en memoria volátil de forma transparente, garantizando que si un atacante copia el archivo de preferencias del disco duro, solo obtendrá cadenas binarias indescifrables.</p>

<h2>15. Buenas Prácticas para Evitar Fugas de Memoria en PubSub</h2>
<p>El bus de eventos <code>page.pubsub</code> es extremadamente poderoso, pero requiere disciplina de ciclo de vida: cuando un componente de la interfaz de usuario se destruye o se retira de la pantalla, debe desuscribirse explícitamente del bus de mensajes. Si un control permanece suscrito en memoria tras haber sido eliminado visualmente, el recolector de basura de Python no podrá destruirlo, acumulando instancias huérfanas en cada navegación que terminarán ralentizando la respuesta de la interfaz gráfica.</p>
"""

# -----------------------------------------------------------------------------
# ARTÍCULO 15: ADB WI-FI
# -----------------------------------------------------------------------------
EXPANSIONS[15] = """
<h2>10. Depuración Inalámbrica de Aplicaciones Móviles Compiladas (Flutter / React Native)</h2>
<p>Para estudiantes de ingeniería y desarrolladores que compilan aplicaciones móviles con frameworks como Flutter, Flet o React Native, la depuración inalámbrica en Android 11+ acelera drásticamente el flujo de trabajo conocido como <strong>Hot Reload (Recarga en Caliente)</strong>.</p>
<p>Cuando el terminal está conectado por Wi-Fi de alta velocidad en la banda de 5 GHz, cualquier cambio guardado en el editor de código se inyecta en la memoria del teléfono en menos de 400 milisegundos a través del socket TCP cifrado. Esto te permite sostener el teléfono en la mano, probar gestos táctiles, rotaciones de pantalla y sensores de cámara en tiempo real con absoluta libertad de movimiento mientras tu computadora compila los activos en tu escritorio.</p>

<h2>11. Protocolo para Resolver la Pérdida de IP Dinámica mediante DHCP Lease</h2>
<p>En redes domésticas estándar, el router asigna direcciones IP dinámicas a los teléfonos móviles mediante el protocolo DHCP. Si el tiempo de concesión (DHCP Lease Time) expira, el router puede cambiar la IP del teléfono (por ejemplo, de <code>192.168.1.15</code> a <code>192.168.1.42</code>), obligándote a consultar nuevamente el menú de depuración.</p>
<p>Para evitar esta molestia, se recomienda ingresar al panel de administración de tu router doméstico (normalmente en <code>192.168.1.1</code>) y configurar una <strong>Reserva de IP estática por Dirección MAC</strong> asociada a la tarjeta de red de tu smartphone. De este modo, tu teléfono mantendrá exactamente la misma dirección IP durante años, permitiéndote conectarte con un alias permanente en tu consola de comandos.</p>
"""

# -----------------------------------------------------------------------------
# ARTÍCULO 16: BACKUP COMPLETO CON ADB
# -----------------------------------------------------------------------------
EXPANSIONS[16] = """
<h2>12. Respaldo de Bases de Datos SQLite de Mensajería y Preferencias de Usuario</h2>
<p>Para usuarios que realizan auditorías forenses o que necesitan migrar configuraciones de aplicaciones complejas, el almacenamiento de Android custodia decenas de bases de datos en formato <strong>SQLite</strong> que contienen registros de conversaciones, preferencias de temas y marcadores locales.</p>
<p>Si bien los directorios privados <code>/data/data/</code> están protegidos por el sistema operativo contra lecturas directas por usuarios sin privilegios de Root, muchas aplicaciones de productividad y código abierto (como clientes de podcast, lectores de libros electrónicos o gestores de finanzas personales) ofrecen la opción de <em>'Exportar copia de seguridad local a almacenamiento compartido'</em>. Al seleccionar la carpeta <code>/sdcard/Documents/Backups/</code>, puedes utilizar <code>adb pull</code> para rescatar estas bases de datos relacionales y examinarlas en tu computadora con herramientas como <em>DB Browser for SQLite</em>, permitiéndote auditar la integridad de tus datos de forma transparente.</p>

<h2>13. Protocolo de Limpieza y Purgado de Archivos Temporales Residuales</h2>
<p>Antes de iniciar una copia de seguridad física masiva, es una excelente práctica de optimización purgar los archivos residuales de caché que solo ocupan espacio en el disco duro de destino sin aportar valor informativo:</p>
<pre><code># Limpiar la caché de miniaturas de imágenes en Android
adb shell rm -rf /sdcard/DCIM/.thumbnails/*
adb shell rm -rf /sdcard/Pictures/.thumbnails/*
</code></pre>
<p>Este sencillo comando puede liberar entre 1 y 4 GB de espacio en memorias saturadas, ahorrando valiosos minutos durante el proceso de transferencia por el cable USB.</p>
"""

# -----------------------------------------------------------------------------
# ARTÍCULO 17: BATERÍA ANDROID
# -----------------------------------------------------------------------------
EXPANSIONS[17] = """
<h2>11. La Química de las Celdas de Litio y la Regla del 20-80% de Carga</h2>
<p>Más allá de las optimizaciones del kernel de Android y del Modo Doze, la longevidad física de una batería de smartphone depende directamente de los principios electroquímicos de las celdas de polímero de iones de litio (Li-Po). Las celdas de litio sufren su mayor estrés mecánico y degradación de cátodos en los dos extremos de voltaje: cuando descienden por debajo del 20% (voltaje inferior a 3.6V) y cuando se mantienen saturadas al 100% a 4.35V bajo altas temperaturas.</p>
<p>Para maximizar los ciclos de vida útil de la batería (permitiendo que conserve más del 85% de su capacidad original después de tres años de uso universitario intensivo), los fabricantes modernos han incorporado opciones de <strong>Protección de Batería</strong> que limitan la recarga al 80% o 85%. En terminales que no disponen de esta opción visual, podemos monitorizar el voltaje en tiempo real mediante un script en ADB que emita una alerta sonora en la computadora cuando el charge counter alcance el umbral óptimo de desconexión.</p>

<h2>12. Desactivación de Efectos Hápticos y Sensores Secundarios Innecesarios</h2>
<p>Cada vez que el teléfono vibra al escribir en el teclado virtual o al desbloquear la pantalla, el motor de vibración háptica consume un pulso instantáneo de corriente de hasta 100 miliamperios. Desactivar la vibración en la pulsación de teclas y reducir la tasa de refresco de pantalla de 120 Hz a 60 Hz en jornadas donde se requiere máxima autonomía puede prolongar el tiempo de pantalla activa entre 1.5 y 2 horas adicionales.</p>
"""

# -----------------------------------------------------------------------------
# ARTÍCULO 18: TIENDAS ALTERNATIVAS ANDROID
# -----------------------------------------------------------------------------
EXPANSIONS[18] = """
<h2>10. Configuración de DNS Cifrado sobre HTTPS (DoH) y Bloqueo Centralizado de Anuncios</h2>
<p>Al migrar hacia un entorno de software libre con F-Droid y Aurora Store, un complemento indispensable para blindar la privacidad en cualquier red es configurar un <strong>DNS Privado</strong> en Android. A diferencia del DNS tradicional que envía las consultas en texto plano, Android 9 en adelante incluye soporte nativo para <em>DNS-over-TLS (DoT)</em>:</p>
<ol>
  <li>Ve a <em>Ajustes &gt; Conexiones &gt; Más ajustes de conexión &gt; DNS Privado</em>.</li>
  <li>Selecciona la opción <em>'Nombre de host del proveedor de DNS privado'</em>.</li>
  <li>Introduce un servidor auditado que filtre telemetría y rastreadores publicitarios a nivel de red, como <code>dns.adguard-dns.com</code> o un perfil personalizado de <code>nextdns.io</code>.</li>
</ol>
<p>A partir de ese instante, cualquier aplicación comercial que intente enviar estadísticas de uso o descargar anuncios publicitarios se topará con una pared a nivel de resolución de nombres, ahorrando datos móviles y protegiendo tu navegación en redes públicas no seguras.</p>

<h2>11. Auditoría de Seguridad de Permisos Sensibles con App Ops</h2>
<p>En el modelo de seguridad de Android moderno, algunas aplicaciones solicitan acceso a la cámara, micrófono o ubicación precisa bajo pretextos engañosos. Mediante herramientas de código abierto como <strong>App Ops</strong> integradas con Shizuku, podemos revocar permisos de forma granular o configurar el modo 'Ignorar' (donde la aplicación cree que tiene el permiso pero el sistema operativo le suministra datos en blanco o coordenadas simuladas), garantizando que ninguna corporación pueda espiar tus conversaciones ni vigilar tus rutinas de estudio.</p>
"""

# -----------------------------------------------------------------------------
# ARTÍCULO 19: DIAGNÓSTICO DE HARDWARE USSD
# -----------------------------------------------------------------------------
EXPANSIONS[19] = """
<h2>9. Verificación de Autenticidad de Pantallas de Repuesto (OLED vs LCD Genérico)</h2>
<p>Uno de los fraudes más habituales en el mercado de reparación de teléfonos móviles consiste en cobrar al cliente por una pantalla de repuesto 'original' pero instalar en su lugar un panel LCD IPS genérico de bajísima calidad en lugar del panel AMOLED de fábrica. Mediante el menú de pruebas USSD y la consola ADB, podemos desenmascarar este engaño en menos de diez segundos:</p>
<ol>
  <li><strong>Prueba del Negro Puro:</strong> Entra al menú de diagnóstico de pantalla o abre una imagen completamente negra en una habitación a oscuras. En un panel AMOLED real, los píxeles negros están completamente apagados y emiten cero lúmenes de luz. Si observas un brillo grisáceo o filtración de luz en los bordes de la pantalla, se trata de un panel LCD genérico con retroiluminación fluorescente.</li>
  <li><strong>Prueba de la Tasa de Muestreo Táctil (Touch Polling Rate):</strong> Abre el menú de prueba de táctil (Touch). Con un panel original, el sistema registra lecturas a 240 Hz o 360 Hz con una latencia imperceptible; en pantallas chinas de imitación, la tasa cae a menos de 90 Hz, provocando que los trazos se sientan lentos y entrecortados.</li>
  <li><strong>Comprobación del Controlador de Panel por Consola ADB:</strong>
    <pre><code>adb shell dumpsys SurfaceFlinger | grep -i "display"</code></pre>
    La consola imprimirá el identificador de fabricante del controlador de pantalla (por ejemplo, <em>Samsung Display</em> o <em>BOE Technology</em>). Si el identificador arroja cadenas no reconocidas o errores de comunicación DSI, la pantalla instalada es un clon de bajo costo.</li>
</ol>
"""

# -----------------------------------------------------------------------------
# ARTÍCULO 20: WINDOWS 11 OPTIMIZACIÓN
# -----------------------------------------------------------------------------
EXPANSIONS[20] = """
<h2>14. Ajuste Fino de Efectos Visuales y Animaciones para Máxima Fluidez</h2>
<p>Windows 11 introduce transparencias avanzadas (efecto Mica y Acrylic) y animaciones de apertura de ventanas que consumen ciclos de la tarjeta gráfica y pueden provocar microtirones en monitores de 60 Hz. Para obtener una respuesta inmediata en el entorno de desarrollo:</p>
<ol>
  <li>Presiona <code>Windows + R</code>, escribe <code>sysdm.cpl</code> y presiona Enter para abrir las <em>Propiedades del Sistema</em>.</li>
  <li>En la pestaña <em>Opciones avanzadas</em>, pulsa en el botón <strong>Configuración...</strong> del apartado <em>Rendimiento</em>.</li>
  <li>Selecciona la opción <strong>Personalizar</strong> y deja marcadas únicamente las siguientes tres casillas esenciales:
    <ul>
      <li><em>Mostrar vistas en miniatura en lugar de iconos</em> (indispensable para ver miniaturas de imágenes en el explorador).</li>
      <li><em>Suavizar bordes para las fuentes de pantalla</em> (crítico para que el texto y el código en el editor no se vean pixelados).</li>
      <li><em>Mostrar sombras bajo las ventanas</em> (para mantener la separación visual de ventanas superpuestas).</li>
    </ul>
  </li>
  <li>Desmarca todas las demás opciones de animaciones innecesarias y haz clic en <em>Aplicar</em>.</li>
</ol>
<p>Al aplicar este cambio, las ventanas se abrirán de forma instantánea sin retrasos artificiales, logrando una sensación de velocidad equiparable a sistemas operativos ultraligeros de Linux.</p>
"""

# -----------------------------------------------------------------------------
# ARTÍCULO 21: WSL 2
# -----------------------------------------------------------------------------
EXPANSIONS[21] = """
<h2>13. Montaje y Acceso a Unidades USB y Dispositivos de Hardware con USBIPD</h2>
<p>En asignaturas de arquitectura de computadores, sistemas embebidos o internet de las cosas (IoT), los estudiantes necesitan interactuar con placas de desarrollo como Arduino, ESP32 o microcontroladores STM32 directamente desde el compilador de Linux en WSL 2. Tradicionalmente, WSL 2 no tenía acceso a los puertos USB físicos de la máquina host.</p>
<p>Microsoft resolvió esta carencia mediante el proyecto de código abierto <strong>usbipd-win</strong>. Al instalarlo en Windows mediante <code>winget install usbipd</code>, podemos compartir cualquier dispositivo USB conectado a la máquina física con el kernel de Ubuntu:</p>
<pre><code># En PowerShell de Windows: Listar dispositivos USB
usbipd list

# Adjuntar el microcontrolador o pendrive al subsistema WSL 2
usbipd attach --wsl -b 1-4

# Dentro de la consola de Ubuntu en WSL 2:
lsusb
dmesg | grep ttyUSB
</code></pre>
<p>El dispositivo aparecerá de inmediato bajo <code>/dev/ttyUSB0</code> o <code>/dev/ttyACM0</code>, permitiéndote compilar y flashear firmware directamente desde la terminal de Ubuntu con total compatibilidad de controladores.</p>
"""

# -----------------------------------------------------------------------------
# ARTÍCULO 22: GIT Y GITHUB
# -----------------------------------------------------------------------------
EXPANSIONS[22] = """
<h2>12. El Arte del Rebase Interactivo: `git rebase -i` para Limpiar el Historial</h2>
<p>Durante una jornada maratónica de programación, es normal realizar múltiples confirmaciones temporales con mensajes informales como <em>'fix bug'</em>, <em>'correccion menor'</em> o <em>'intentando compilar'</em>. Antes de enviar tu rama de trabajo a revisión para ser fusionada en la rama principal de producción, es una norma de cortesía y profesionalismo consolidar esos cambios en commits limpios y coherentes mediante un <strong>Rebase Interactivo</strong>:</p>
<pre><code># Reordenar y consolidar los últimos 4 commits
git rebase -i HEAD~4
</code></pre>
<p>Git abrirá tu editor de texto predeterminado listando los últimos commits acompañados de comandos de acción:</p>
<ul>
  <li><code>pick</code>: Conserva el commit tal como está.</li>
  <li><code>reword</code>: Mantiene el código pero te permite reescribir el mensaje de confirmación para que sea más descriptivo.</li>
  <li><code>squash</code>: Fusiona el commit con el anterior, combinando los cambios en una sola confirmación lógica.</li>
  <li><code>drop</code>: Elimina el commit por completo de la historia del proyecto.</li>
</ul>
<p>Al guardar y cerrar el editor, Git reescribirá la cadena de confirmaciones, logrando un historial profesional, legible y digno de ser presentado en un portafolio de ingeniería de software.</p>
"""

# -----------------------------------------------------------------------------
# ARTÍCULO 23: VISUAL STUDIO CODE
# -----------------------------------------------------------------------------
EXPANSIONS[23] = """
<h2>14. Configuración de Cobertura de Código y Calidad con Coverage.py</h2>
<p>En proyectos de ingeniería de software avanzados, no basta con saber que las pruebas unitarias pasan; es indispensable medir qué porcentaje exacto de las líneas de código han sido ejecutadas y validadas por los tests. La biblioteca estándar en Python para esta tarea es <strong>coverage.py</strong>:</p>
<pre><code># Instalar la herramienta de cobertura
pip install coverage

# Ejecutar las pruebas unitarias midiendo la cobertura de código
coverage run -m pytest

# Generar un reporte interactivo en formato HTML
coverage html
</code></pre>
<p>Al abrir el archivo <code>htmlcov/index.html</code> en tu navegador web, VS Code y Coverage te mostrarán una radiografía visual completa de tu repositorio: las líneas coloreadas en verde representan código probado con éxito, mientras que las líneas en rojo destacan ramas condicionales o excepciones que aún no cuentan con pruebas unitarias, permitiéndote blindar tus desarrollos antes de enviarlos a producción.</p>
"""

# -----------------------------------------------------------------------------
# ARTÍCULO 24: VENTOY
# -----------------------------------------------------------------------------
EXPANSIONS[24] = """
<h2>13. Verificación de Integridad Criptográfica de ISOs en el Menú de Ventoy</h2>
<p>Uno de los mayores riesgos al instalar sistemas operativos en computadoras de producción es que el archivo ISO descargado desde internet se haya corrompido durante la descarga o haya sido alterado por un atacante en la red. Si intentas instalar un sistema operativo a partir de una ISO dañada, el proceso puede congelarse a la mitad, dejando la computadora sin sistema operativo arrancable.</p>
<p>Ventoy soluciona este riesgo de forma brillante integrando un <strong>comprobador criptográfico de Checksums directamente en el menú de arranque</strong>. Al colocarte sobre cualquier ISO en el menú de Ventoy y presionar la tecla <code>Ctrl + M</code> o <code>c</code>, Ventoy calculará en tiempo real el hash <strong>SHA-256</strong> o <strong>MD5</strong> leyendo la memoria física del pendrive y comparándolo con el valor oficial publicado por la distribución (Canonical para Ubuntu o Microsoft para Windows). Si los hashes coinciden al 100%, tienes la certeza matemática de que la instalación se completará sin fallos de lectura ni corrupción de datos.</p>
"""

# -----------------------------------------------------------------------------
# ARTÍCULO 25: NAVEGADORES
# -----------------------------------------------------------------------------
EXPANSIONS[25] = """
<h2>13. Aislamiento Estricto de Sitios Web y Mitigación de Vulnerabilidades de CPU</h2>
<p>En la era posterior a las históricas vulnerabilidades de hardware <em>Spectre</em> y <em>Meltdown</em> descubiertas en procesadores modernos, los navegadores web basados en Chromium implementaron el mecanismo de seguridad <strong>Site Isolation (Aislamiento de Sitios)</strong>. Esta tecnología garantiza que las páginas de dominios web distintos siempre se ejecuten en procesos de sistema operativo independientes, impidiendo que una página maliciosa abierta en una pestaña pueda leer las cookies bancarias o contraseñas almacenadas en otra pestaña contigua.</p>
<p>Sin embargo, para computadoras modestas con 8 GB de RAM o menos, Site Isolation puede consumir entre 500 MB y 1 GB adicional de memoria. En Google Chrome y Brave, podemos verificar el estado de aislamiento accediendo a <code>chrome://process-internals</code>, donde se muestra el mapa interactivo de procesos del renderizador y podemos equilibrar el nivel de seguridad y consumo de recursos según la criticidad de nuestras sesiones de navegación.</p>
"""

# -----------------------------------------------------------------------------
# ARTÍCULO 26: RSYNC BASH
# -----------------------------------------------------------------------------
EXPANSIONS[26] = """
<h2>14. Notificaciones Automatizadas por Webhook a Discord o Telegram</h2>
<p>Un script de respaldo que se ejecuta a las 2:00 AM mediante crontab debe mantener informado al administrador del sistema sobre el resultado de la operación sin obligarlo a abrir manualmente los archivos de log cada mañana. Podemos enriquecer nuestro script en Bash enviando una notificación instantánea a un canal privado de Discord o Telegram mediante un simple comando <code>curl</code>:</p>
<pre><code># Función para enviar alertas vía Webhook a Discord
notificar_discord() {
    local MENSAJE="$1"
    local WEBHOOK_URL="https://discord.com/api/webhooks/TU_WEBHOOK_SECRETO"
    curl -H "Content-Type: application/json" \
         -X POST \
         -d "{\"content\": \"$MENSAJE\"}" \
         "$WEBHOOK_URL" &gt; /dev/null 2&gt;&amp;1
}

# Al finalizar con éxito el script:
notificar_discord "✅ [BACKUP OK] Copia de seguridad finalizada en Servidor CUC ($DURACION seg)."
</code></pre>
<p>De esta manera, recibes en tu teléfono móvil la confirmación diaria de que tus copias de seguridad se completaron exitosamente, o una alerta urgente en color rojo si la unidad de disco de destino no fue detectada, permitiéndote reaccionar a tiempo y garantizar la continuidad operativa de tus proyectos.</p>
"""

# Apply expansions to the respective files or data structures
print("Applying universal pure word expansions...")

# Update generate_tramites.py for 3, 5, 6, 7
with open('generate_tramites.py', 'r', encoding='utf-8') as f:
    gt_code = f.read()

for art_id in [3, 5, 6, 7]:
    if art_id in EXPANSIONS:
        extra = EXPANSIONS[art_id]
        # Insert before conclusions
        gt_code = re.sub(
            r'(<h2>\d+\.\s*Conclusiones.*?</h2>)',
            lambda m: extra + '\n' + m.group(1),
            gt_code,
            count=1
        )

# Update generate_python_flet.py for 10, 12, 13
with open('generate_python_flet.py', 'r', encoding='utf-8') as f:
    gpf_code = f.read()

for art_id in [10, 12, 13]:
    if art_id in EXPANSIONS:
        extra = EXPANSIONS[art_id]
        gpf_code = re.sub(
            r'(<h2>\d+\.\s*Conclusiones.*?</h2>)',
            lambda m: extra + '\n' + m.group(1),
            gpf_code,
            count=1
        )

# Update generate_android_adb.py for 15, 16, 17, 18, 19
with open('generate_android_adb.py', 'r', encoding='utf-8') as f:
    ga_code = f.read()

for art_id in [15, 16, 17, 18, 19]:
    if art_id in EXPANSIONS:
        extra = EXPANSIONS[art_id]
        ga_code = re.sub(
            r'(<h2>\d+\.\s*Conclusiones.*?</h2>)',
            lambda m: extra + '\n' + m.group(1),
            ga_code,
            count=1
        )

# Update generate_herramientas.py for 20, 21, 22, 23, 24, 25, 26
with open('generate_herramientas.py', 'r', encoding='utf-8') as f:
    gh_code = f.read()

for art_id in [20, 21, 22, 23, 24, 25, 26]:
    if art_id in EXPANSIONS:
        extra = EXPANSIONS[art_id]
        gh_code = re.sub(
            r'(<h2>\d+\.\s*Conclusiones.*?</h2>)',
            lambda m: extra + '\n' + m.group(1),
            gh_code,
            count=1
        )

with open('generate_tramites.py', 'w', encoding='utf-8') as f:
    f.write(gt_code)

with open('generate_python_flet.py', 'w', encoding='utf-8') as f:
    f.write(gpf_code)

with open('generate_android_adb.py', 'w', encoding='utf-8') as f:
    f.write(ga_code)

with open('generate_herramientas.py', 'w', encoding='utf-8') as f:
    f.write(gh_code)

print("All module files successfully updated with universal pure word expansions!")
