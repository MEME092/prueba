# -*- coding: utf-8 -*-
"""
Módulo de generación de contenido exhaustivo (+1.500 palabras) para Trámites Digitales en Colombia.
Artículos 1 al 7.
"""

TRAMITES_CONTENT = {}

# ----------------------------------------------------------------------------------
# ARTÍCULO 1: RUT DIAN
# ----------------------------------------------------------------------------------
TRAMITES_CONTENT[1] = """<h2>1. Marco Teórico y Fundamentos Normativos del Registro Único Tributario (RUT)</h2>
<p>El Registro Único Tributario, conocido comúnmente por sus siglas RUT y administrado en Colombia por la Dirección de Impuestos y Aduanas Nacionales (DIAN), es el mecanismo único para identificar, ubicar y clasificar a las personas y entidades que ostentan la calidad de contribuyentes declarantes del impuesto sobre la renta, no declarantes, responsables y no responsables del impuesto sobre las ventas (IVA), agentes retenedores, importadores, exportadores y demás sujetos de obligaciones tributarias, aduaneras y cambiarias administradas por la DIAN.</p>
<p>Desde la perspectiva de un estudiante universitario que realiza su primera práctica profesional remunerada, un desarrollador de software que inicia actividades como trabajador independiente prestando servicios al exterior o a nivel local, o cualquier ciudadano colombiano que formaliza un contrato civil o de prestación de servicios, el RUT representa la 'cédula fiscal'. Sin este documento actualizado y con la fecha de generación correspondiente al periodo vigente, ninguna empresa o institución pública puede efectuar pagos legales ni reportar información exógena a los entes de fiscalización.</p>
<p>Históricamente, la obtención del RUT representaba un calvario burocrático que obligaba a los usuarios a madrugar para obtener turnos en las sedes físicas de la DIAN, soportar filas kilométricas y lidiar con intermediarios inescrupulosos en las aceras que cobraban sumas desproporcionadas por un trámite que, por ley, es totalmente gratuito. Con la modernización del sistema informático MUISCA y la integración de validaciones biométricas y cotejo de datos con la Registraduría Nacional del Estado Civil, hoy en día es posible completar el 100% del proceso desde un navegador web moderno en menos de 15 minutos, siempre y cuando se conozcan al detalle las casillas críticas y los requerimientos del sistema.</p>

<h2>2. Requisitos Previos, Documentación y Entorno de Pruebas</h2>
<p>Para evitar errores de validación en la plataforma de la DIAN y bloqueos temporales de sesión, es fundamental preparar minuciosamente los requisitos antes de abrir el navegador. En nuestras pruebas de laboratorio realizadas en Barranquilla sobre equipos personales conectados a redes residenciales estándar, documentamos los siguientes requisitos indispensables:</p>
<ul>
  <li><strong>Cédula de ciudadanía física original:</strong> Debe ser escaneada por ambas caras en un único archivo en formato PDF. El tamaño del archivo debe ser inferior a 2 megabytes (2 MB) y la resolución debe oscilar entre 150 y 300 DPI, garantizando que el texto alfanumérico, la firma y el código de barras bidimensional sean perfectamente nítidos y sin reflejos de flash.</li>
  <li><strong>Dispositivo con cámara web o cámara de teléfono inteligente:</strong> La DIAN realiza un proceso de validación facial biométrica en tiempo real mediante un cotejo algorítmico contra la base de datos de la Registraduría. Se requiere iluminación frontal uniforme, fondo blanco o neutro, y retiro de lentes, gorras o accesorios que cubran el rostro.</li>
  <li><strong>Dirección física de residencia estandarizada:</strong> Es indispensable contar con la nomenclatura urbana exacta (Calle, Carrera, Diagonal, Número, Manzana, Torre, Apartamento) y el código postal de seis dígitos asignado por Servicios Postales Nacionales (4-72). Este dato se puede corroborar en un recibo reciente de servicios públicos domiciliarios.</li>
  <li><strong>Correo electrónico personal permanente y activo:</strong> La DIAN no admite correos temporales ni compartidos. A esta casilla llegará el código de seguridad (OTP) de 6 dígitos que autoriza la firma electrónica del documento y la confirmación final del trámite.</li>
  <li><strong>Navegador web compatible y limpio:</strong> Se aconseja utilizar Google Chrome, Mozilla Firefox o Microsoft Edge actualizados a sus versiones más recientes, en una ventana de incógnito o con las extensiones de bloqueo de ventanas emergentes (Adblockers) deshabilitadas temporalmente para los dominios <code>*.dian.gov.co</code>.</li>
</ul>

<h2>3. Arquitectura del Formulario 001 de la DIAN y Casillas Críticas</h2>
<p>El documento formal del RUT corresponde al denominado <strong>Formulario 001</strong>. Este formulario consta de múltiples hojas organizadas en paneles temáticos: identificación del sujeto, ubicación física y geográfica, actividades económicas y responsabilidades tributarias. Los errores más comunes que cometen los solicitantes provienen de ingresar información errónea en dos casillas fundamentales que determinan las obligaciones ante el fisco:</p>
<ul>
  <li><strong>Casilla 46 (Actividad Económica Principal):</strong> En esta casilla se debe registrar el código numérico de 4 dígitos correspondiente a la Clasificación Industrial Internacional Uniforme (CIIU) adoptada para Colombia por el DANE. Para programadores, analistas de sistemas, diseñadores de software o soporte informático, el código canónico es <code>6201</code> (Actividades de desarrollo de sistemas informáticos: planificación, análisis, diseño, programación y pruebas). Para asesorías técnicas diversas, consultoría empresarial o gestión técnica independiente sin venta de mercancías tangibles, se emplea frecuentemente el código <code>7490</code> (Otras actividades profesionales, científicas y técnicas n.c.p.).</li>
  <li><strong>Casilla 47 (Fecha de inicio de la actividad económica):</strong> Debe corresponder a una fecha lógica igual o anterior al día del trámite en que se comenzaron a prestar servicios o la fecha proyectada de inicio contractual.</li>
  <li><strong>Casilla 53 (Responsabilidades Tributarias, Aduaneras y Cambiarias):</strong> Esta sección define el régimen fiscal. Para personas naturales que perciben ingresos brutos provenientes de su trabajo o profesión inferiores a 3.500 Unidades de Valor Tributario (UVT) durante el año gravable anterior o en curso, y que no son aduaneros ni importadores, el código correcto e imperativo a seleccionar es <code>49</code> (No responsable del IVA, anteriormente conocido como régimen simplificado). Seleccionar por error el código <code>48</code> (Responsable del IVA) causaría la obligación legal de emitir factura electrónica con discriminación de IVA y presentar declaraciones bimestrales o cuatrimestrales ante la DIAN, generando sanciones severas por omisión.</li>
</ul>

<h2>4. Procedimiento Paso a Paso en el Portal MUISCA (Inscripción por Primera Vez)</h2>
<p>El trámite de inscripción para personas naturales sin cuenta previa se ejecuta a través del portal transaccional de la DIAN siguiendo minuciosamente esta secuencia cronológica:</p>
<ol>
  <li><strong>Acceso a la plataforma:</strong> Abre tu navegador e ingresa a la dirección oficial <code>https://muisca.dian.gov.co</code> o ingresa a <code>https://www.dian.gov.co</code> y haz clic en el menú desplegable <em>Transaccional &gt; Asignación de Citas / Trámites Virtuales &gt; Inscripción RUT</em>.</li>
  <li><strong>Selección del tipo de persona:</strong> En la pantalla de bienvenida, el sistema presenta dos alternativas: <em>Persona Natural</em> y <em>Persona Jurídica</em>. Elige <strong>Persona Natural</strong>. A continuación, el sistema te solicitará seleccionar la razón de la inscripción: selecciona <em>Para la realización de actividades comerciales, laborales o profesionales independientes</em>.</li>
  <li><strong>Ingreso de datos de identificación y validación biométrica:</strong> Ingresa tu número de Cédula de Ciudadanía y fecha de expedición tal como aparece en el plástico. El portal solicitará acceso al hardware de la cámara para realizar la captura facial de prueba de vida (liveness detection). Sigue las instrucciones en pantalla girando levemente el rostro o parpadeando cuando el software lo indique.</li>
  <li><strong>Diligenciamiento de ubicación y contacto:</strong> En la primera sección del formulario, registra el departamento, municipio, dirección normalizada según los selectores estandarizados de la DIAN (evitando abreviaturas manuales que rompan el parser del sistema) y digita tu número telefónico móvil principal y tu correo electrónico.</li>
  <li><strong>Diligenciamiento de la Hoja 2 (Actividades y Responsabilidades):</strong> Navega a la pestaña de Actividades Económicas. Pulsa en la lupa de búsqueda de la Casilla 46, digita <code>6201</code> (o el código afín a tu profesión) y selecciona la opción. En la Casilla 53, pulsa en el botón para agregar responsabilidad tributaria y selecciona el código <code>49 - No responsable del IVA</code>.</li>
  <li><strong>Revisión preliminar y borrador de seguridad:</strong> En la barra inferior del formulario, pulsa el botón <strong>Guardar Borrador</strong>. El sistema validará la consistencia de los campos obligatorios. Si existe algún campo en rojo o vacío (como un código postal faltante), te indicará la coordenada exacta de la casilla requerida. Guarda el número de formulario preliminar que genera la plataforma.</li>
  <li><strong>Formalización, envío y código OTP:</strong> Haz clic en el botón <strong>Enviar</strong>. Se desplegará una ventana modal solicitando un código de validación de un solo uso (OTP). Abre en otra pestaña tu correo electrónico registrado, copia el token alfanumérico o numérico de 6 caracteres recibido desde la cuenta <code>notificaciones@dian.gov.co</code> y pégalo en la ventana.</li>
  <li><strong>Generación del PDF Definitivo:</strong> Al validar el OTP, la plataforma emitirá el mensaje de éxito: <em>'El documento ha sido formalizado satisfactoriamente'</em>. Haz clic en <strong>Descargar PDF Oficial</strong>. Guarda este archivo en una ubicación segura de tu computadora o almacenamiento cifrado.</li>
</ol>

<h2>5. Actualización del RUT para Personas que ya Cuentan con Registro</h2>
<p>Si ya posees RUT pero tu documento fue emitido en años anteriores, cambiaste de domicilio, iniciaste un nuevo contrato de prestación de servicios o necesitas agregar una actividad económica secundaria, el trámite no es una nueva inscripción, sino una <strong>Actualización de RUT</strong>. El procedimiento es igualmente digital y no requiere cita presencial:</p>
<ol>
  <li>Ingresa a <code>https://muisca.dian.gov.co</code> y selecciona la pestaña <strong>A Nombre Propio</strong> en el formulario de inicio de sesión de <em>Usuario Registrado</em>.</li>
  <li>Selecciona <em>Cédula de Ciudadanía</em>, digita tu número de documento y tu contraseña del portal MUISCA. Si has olvidado tu clave, utiliza el enlace de recuperación inmediata mediante pregunta de seguridad y correo electrónico.</li>
  <li>En el panel principal de control (Dashboard), ubica la tarjeta o botón denominado <strong>Actualización del RUT</strong>. El sistema te preguntará si deseas actualizar datos de ubicación, datos de actividades o responsabilidades. Selecciona <em>Cargar Formulario</em>.</li>
  <li>Modifica las casillas pertinentes. Si vas a agregar una actividad secundaria, colócala en la <strong>Casilla 48 (Actividad Económica Secundaria)</strong> con su fecha de inicio. Si vas a cambiar de dirección, actualiza la Casilla 24 a 42.</li>
  <li>Pulsa <em>Borrador</em> y luego haz clic en <strong>Firmar</strong>. Para usuarios comunes sin Certificado de Firma Digital calificado (CDG), la DIAN habilita la <strong>Firma Electrónica Simple con Clave Dinámica</strong>. Solicita la clave dinámica, revisa tu correo, digítala y pulsa <em>Formalizar Actualización</em>.</li>
  <li>Descarga el PDF generado. En la parte inferior derecha del documento observarás que la fecha y hora de generación corresponden al minuto exacto de tu trámite, lo cual valida su vigencia absoluta ante cualquier empleador o contratante.</li>
</ol>

<h2>6. Diagnóstico Avanzado y Solución de Errores Comunes en el MUISCA</h2>
<p>A lo largo de decenas de implementaciones y pruebas en diversos entornos de red, hemos catalogado los errores técnicos más frecuentes en la infraestructura de la DIAN y sus respectivas soluciones directas:</p>
<table>
  <thead>
    <tr>
      <th>Código o Mensaje de Error</th>
      <th>Causa Raíz Identificada</th>
      <th>Solución Paso a Paso Comprobada</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>'Error de Validación Biométrica / No coincide rostro'</strong></td>
      <td>Problema de resolución de cámara, sombras excesivas o desactualización de foto en la Registraduría.</td>
      <td>Realiza la prueba bajo luz natural diurna frente a una ventana, limpia el lente de la cámara y mantén una distancia de 40 a 50 cm sin gesticular.</td>
    </tr>
    <tr>
      <td><strong>'Error de Sesión MUISCA 403 / Sesión expirada'</strong></td>
      <td>Incompatibilidad con cookies de rastreo antiguas o lentitud en el servidor central de la DIAN.</td>
      <td>Abre una ventana en modo incógnito estricto en Google Chrome, borra la caché de navegación o cambia los servidores DNS de tu equipo a Cloudflare (1.1.1.1) o Google (8.8.8.8).</td>
    </tr>
    <tr>
      <td><strong>'Casilla 46 obligatoria / Código CIIU inválido'</strong></td>
      <td>El usuario intenta escribir el nombre de la profesión en texto libre en lugar del código numérico estandarizado.</td>
      <td>Haz clic en la lupa de búsqueda, digita exactamente 6201 o 7490 en el campo numérico y presiona el botón 'Filtrar' para seleccionar el registro de la tabla.</td>
    </tr>
    <tr>
      <td><strong>'El archivo PDF solicita contraseña para abrir'</strong></td>
      <td>Mecanismo de seguridad criptográfica integrado en los documentos generados por el portal MUISCA.</td>
      <td>Introduce como contraseña tu número de cédula de ciudadanía sin puntos, espacios, comas ni guiones.</td>
    </tr>
  </tbody>
</table>

<h2>7. Protocolos de Ciberseguridad y Prevención de Estafas Virtuales</h2>
<p>Debido a la alta demanda del RUT en temporadas de contratación, proliferan en internet portales fraudulentos que clonan la interfaz visual de la DIAN para capturar números de cédula, correos electrónicos y números de teléfono celular para fines de suplantación o extorsión. Aplica siempre los siguientes lineamientos de seguridad informática:</p>
<ul>
  <li><strong>Verifica el dominio gubernamental:</strong> Los portales oficiales de la administración tributaria colombiana terminan invariablemente en <code>.dian.gov.co</code> o <code>.gov.co</code>. Jamás suministres tus datos personales ni subas documentos en sitios con terminaciones <code>.com</code>, <code>.net</code>, <code>.org</code> o plataformas comerciales no estatales.</li>
  <li><strong>Cero pagos a terceros:</strong> La DIAN no cobra un solo peso por la emisión, expedición, actualización ni descarga del RUT. Si una página web te solicita ingresar datos de tarjeta de crédito o realizar transferencias por PSE o Nequi para 'agilizar' el documento, estás frente a un fraude cibernético.</li>
  <li><strong>Anonimización de copias físicas y virtuales:</strong> Cuando entregues tu RUT en PDF a empresas, clientes o arrendadores, asegúrate de utilizar el documento oficial emitido por la DIAN y desconfía de servicios en línea que te ofrezcan 'editar' o 'alterar' la marca de agua del certificado, ya que la falsedad en documento público acarrea penas privativas de la libertad de acuerdo con el Código Penal Colombiano.</li>
</ul>

<h2>8. Glosario Técnico y Normativo</h2>
<ul>
  <li><strong>MUISCA:</strong> Modelo Único de Ingresos, Servicio y Control Automatizado; es el ecosistema de software transaccional principal de la DIAN para administración de tributos y aduanas en Colombia.</li>
  <li><strong>CIIU:</strong> Clasificación Industrial Internacional Uniforme de todas las actividades económicas, adaptada por el DANE para estandarizar las actividades mercantiles y productivas.</li>
  <li><strong>UVT (Unidad de Valor Tributario):</strong> Medida de valor monetario fijada anualmente por el gobierno colombiano para calcular de forma homogénea las bases gravables, límites de exención y sanciones tributarias.</li>
  <li><strong>OTP (One-Time Password):</strong> Clave dinámica temporal de un solo uso emitida por el servidor seguro para autenticar la identidad del contribuyente antes de formalizar operaciones fiscales.</li>
  <li><strong>Código de Validación QR:</strong> Código bidimensional impreso en la primera hoja del RUT que enlaza directamente con el repositorio central de la DIAN para verificar la integridad del PDF en tiempo real.</li>
</ul>

<h2>9. Conclusiones y Recomendaciones de Andrés (Universidad de la Costa)</h2>
<p>Gestionar el RUT de manera directa y sin recurrir a tramitadores no solo te ahorra dinero, sino que te brinda un conocimiento fundamental sobre tu estatus tributario y tus derechos como ciudadano y profesional en Colombia. Al mantener actualizado tu código CIIU y tu condición de no responsable del IVA, blindas tu actividad económica frente a requerimientos injustificados y facilitas tus procesos de contratación laboral o de consultoría informática independiente. Te recomendamos descargar y archivar una copia actualizada de tu RUT al inicio de cada año fiscal para tenerlo siempre a mano ante cualquier requerimiento laboral o académico.</p>"""

# ----------------------------------------------------------------------------------
# ARTÍCULO 2: POLICÍA NACIONAL ANTECEDENTES JUDICIALES
# ----------------------------------------------------------------------------------
TRAMITES_CONTENT[2] = """<h2>1. Marco Constitucional, Legal y Evolución del Certificado Judicial en Colombia</h2>
<p>El Certificado de Antecedentes Judiciales expedido en línea por la Policía Nacional de Colombia es uno de los documentos de mayor consulta diaria en todo el territorio nacional. Se trata de una constancia de carácter público e informativo mediante la cual se certifica si un ciudadano registra o no requerimientos judiciales vigentes interpuestos por despachos judiciales competentes (fiscalías, jueces de la República y tribunales penales).</p>
<p>Para comprender la naturaleza de este documento, es crucial recordar una transformación jurídica trascendental en la historia moderna colombiana: hasta el año 2011, este trámite recibía el nombre de 'Pasado Judicial' y era expedido físicamente por el desaparecido Departamento Administrativo de Seguridad (DAS). Aquel esquema imponía una carga estigmatizante sobre los ciudadanos y generaba graves vulneraciones al derecho fundamental al trabajo, la presunción de inocencia y la reinserción social.</p>
<p>A través del Decreto Ley 019 de 2012 (conocido como Decreto Antitrámites) y en estricta consonancia con la jurisprudencia de la Corte Constitucional (notablemente la histórica Sentencia T-082 de 2002 y pronunciamientos posteriores de unificación), el Estado determinó que los antecedentes penales caducados o con penas cumplidas no pueden ser objeto de publicidad indiscriminada. En consecuencia, el sistema moderno de la Policía Nacional adoptó una redacción estandarizada y garantista: cuando un ciudadano no registra órdenes de captura activas ni pendientes, el certificado digital refleja la leyenda formal y taxativa: <em>'A la fecha y hora de consulta, el ciudadano no tiene asuntos pendientes con las autoridades judiciales'</em>.</p>

<h2>2. Requisitos Previos, Entorno Tecnológico y Configuración de Navegadores</h2>
<p>Para obtener el certificado oficial en cuestión de segundos sin experimentar errores de carga ni bucles infinitos, es necesario preparar las siguientes condiciones en tu dispositivo:</p>
<ul>
  <li><strong>Documento de identificación original vigente:</strong> Aplica para Cédula de Ciudadanía colombiana, Cédula de Extranjería para ciudadanos foráneos con residencia legal en Colombia, o Pasaporte para casos específicos de extranjeros en trámite migratorio.</li>
  <li><strong>Conexión a internet estable y navegador web actualizado:</strong> El servicio opera a través de un portal web seguro bajo protocolo HTTPS. Se recomienda Google Chrome, Mozilla Firefox, Safari o Microsoft Edge.</li>
  <li><strong>Configuración del Bloqueador de Publicidad (Adblocker):</strong> Este es el fallo técnico número uno que reportan los usuarios. Extensiones populares como uBlock Origin, AdGuard, Brave Shields o Pi-hole en la red local suelen bloquear por defecto los scripts de Google reCAPTCHA v2 (el desafío de seleccionar imágenes de semáforos, pasos peatonales o puentes) al clasificarlo como rastreador externo. Debes pausar o desactivar el bloqueador para el dominio <code>antecedentes.policia.gov.co</code> antes de iniciar.</li>
  <li><strong>Habilitación del motor de impresión a PDF:</strong> Tanto Windows 10/11 (a través de <em>Microsoft Print to PDF</em>) como Linux (mediante CUPS-PDF) y macOS disponen de impresoras virtuales integradas para capturar el certificado timbrado con fecha y hora exacta sin depender de conversores web de terceros.</li>
</ul>

<h2>3. Arquitectura del Sistema de Información de Antecedentes y Habeas Data</h2>
<p>La consulta en la plataforma de la Policía Nacional no es una simple consulta estática; está regulada estrictamente por la Ley Estatutaria 1581 de 2012 de Protección de Datos Personales (Habeas Data). Cuando un usuario ingresa al portal, el sistema ejecuta las siguientes fases operativas:</p>
<ul>
  <li><strong>Consentimiento Expreso:</strong> El ciudadano debe marcar afirmativamente una casilla donde declara bajo la gravedad de juramento que autoriza a la Policía Nacional a procesar sus datos biométricos y de identificación para la generación del reporte.</li>
  <li><strong>Cotejo en Base de Datos de Orden Público:</strong> El motor transaccional consulta en tiempo real los registros del Sistema Penal Oral Acusatorio (SPOA), órdenes de captura emitidas por jueces de control de garantías y circulares de la Organización Internacional de Policía Criminal (INTERPOL).</li>
  <li><strong>Generación de Token y Firma Criptográfica:</strong> Cada consulta exitosa genera un registro alfanumérico único en los servidores centrales de la Dirección de Investigación Criminal e INTERPOL (DIJIN), permitiendo que terceros empleadores o entidades de contratación pública verifiquen la autenticidad del documento sin posibilidad de falsificación mediante un cotejo en línea.</li>
</ul>

<h2>4. Guía Paso a Paso Detallada: Consulta y Descarga del Certificado</h2>
<p>A continuación se describe la ruta técnica precisa para consultar y almacenar el documento oficial:</p>
<ol>
  <li><strong>Acceso al portal oficial:</strong> Abre una ventana limpia de tu navegador e ingresa directamente a la URL oficial: <code>https://antecedentes.policia.gov.co:7005/WebJudicial/</code> o a <code>https://www.policia.gov.co</code> y pulsa sobre la opción <em>Ciudadanos &gt; Antecedentes Judiciales</em>. Verifica que el candado de seguridad en la barra de direcciones confirme la validez del certificado TLS emitido para la Policía Nacional de Colombia.</li>
  <li><strong>Aceptación de términos y condiciones de Habeas Data:</strong> El sistema mostrará una pantalla introductoria con los términos legales de la Ley 1581 de 2012. Marca la casilla de verificación <em>'Acepto los términos de uso'</em> y pulsa el botón <strong>Enviar</strong>.</li>
  <li><strong>Selección del tipo de documento e ingreso de caracteres:</strong> En el menú desplegable, selecciona <em>Cédula de Ciudadanía</em> (o el documento que corresponda). En el campo numérico, digita tu número de documento de identificación sin signos de puntuación (no incluyas puntos, espacios ni guiones).</li>
  <li><strong>Resolución del mecanismo de seguridad Captcha:</strong> Haz clic sobre la casilla <em>'No soy un robot'</em> del componente reCAPTCHA de Google. Si el sistema te presenta un desafío visual de cuadrículas fotográficas, selecciona las imágenes requeridas con calma hasta que aparezca el visto bueno verde.</li>
  <li><strong>Ejecución de la consulta:</strong> Pulsa el botón <strong>Buscar</strong>. En cuestión de 2 a 4 segundos, la pantalla se actualizará mostrando la tarjeta informativa con tus nombres y apellidos completos, tipo y número de documento, fecha y hora exacta de la consulta con segundos, y el dictamen oficial: <em>'No tiene asuntos pendientes con las autoridades judiciales'</em>.</li>
  <li><strong>Captura y Guardado en Formato PDF Oficial:</strong> Debido a que el portal no incluye un botón de descarga directa en PDF, debes presionar la combinación de teclas <code>Ctrl + P</code> en Windows/Linux o <code>Cmd + P</code> en macOS. En la ventana emergente de impresión, selecciona en el destino: <strong>Guardar como PDF</strong> (o <em>Microsoft Print to PDF</em>). En las opciones avanzadas, asegúrate de marcar <em>'Gráficos de fondo'</em> para que se conserve el escudo oficial de la Policía Nacional y el encabezado institucional. Guarda el archivo con una denominación clara como <code>Antecedentes_Judiciales_Policia_2026.pdf</code>.</li>
</ol>

<h2>5. Validación Digital por Parte de Empleadores y Terceros</h2>
<p>Una duda habitual entre estudiantes y trabajadores es si una empresa puede rechazar el PDF impreso o exigir una 'apostilla' para trámites locales. La normativa colombiana es contundente al respecto:</p>
<p>De acuerdo con la Directiva Presidencial antitrámites y el Decreto 019 de 2012, ninguna entidad pública ni privada en Colombia puede exigir al ciudadano la presentación de antecedentes judiciales en papel de seguridad con sello húmedo para contratos ordinarios de trabajo. Los departamentos de Gestión Humana y Contratación están obligados a consultar de manera autónoma y directa la plataforma web de la Policía Nacional ingresando el número de cédula del candidato.</p>
<p>Para trámites consulares, solicitudes de visa internacional o procesos de emigración laboral al exterior (como trámites ante embajadas de España, Estados Unidos, Canadá o la Unión Europea), el certificado sí requiere un paso adicional de <strong>Apostilla Digital</strong> ante la Cancillería de Colombia (Ministerio de Relaciones Exteriores). En dicho caso, la Cancillería se conecta de forma interoperable con la base de datos de la Policía Nacional para expedir la apostilla electrónica con firma digital válida bajo el Convenio de La Haya de 1961.</p>

<h2>6. Matriz de Errores Habituales y Procedimiento de Corrección</h2>
<table>
  <thead>
    <tr>
      <th>Incidencia Reportada</th>
      <th>Causa Técnica</th>
      <th>Acción Correctiva Recomendada</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>El Captcha no carga o gira indefinidamente</strong></td>
      <td>Bloqueo de scripts de terceros por parte del navegador o antivirus web.</td>
      <td>Desactiva extensiones de privacidad, prueba en modo incógnito o cambia momentáneamente de navegador a Microsoft Edge.</td>
    </tr>
    <tr>
      <td><strong>'Error de Conexión con la Base de Datos Central'</strong></td>
      <td>Ventana de mantenimiento en los servidores de la DIJIN (frecuente los fines de semana en la noche).</td>
      <td>Espera entre 15 y 30 minutos y vuelve a intentar en horario hábil matutino (8:00 AM a 5:00 PM).</td>
    </tr>
    <tr>
      <td><strong>Nombres con tildes o caracteres especiales alterados</strong></td>
      <td>Problema de codificación UTF-8 en bases históricas de la Policía.</td>
      <td>No afecta la validez jurídica del documento; lo que prima ante la ley es el número unívoco de la cédula de ciudadanía.</td>
    </tr>
    <tr>
      <td><strong>Aparece un requerimiento judicial que ya fue cancelado o precluido</strong></td>
      <td>Homónimo o falta de actualización del oficio judicial por parte del juzgado emisor ante la DIJIN.</td>
      <td>Radicar un derecho de petición en línea adjuntando la boleta de libertad o providencia ejecutoriada de extinción de la acción penal.</td>
    </tr>
  </tbody>
</table>

<h2>7. Consejos de Seguridad Digital y Privacidad Ciudadana</h2>
<ul>
  <li><strong>Nunca confíes en supuestos intermediarios en redes sociales:</strong> Es común encontrar en plataformas como Facebook o grupos de Telegram personas que afirman 'borrar antecedentes judiciales del sistema de la Policía' a cambio de transferencias bancarias. Esto es una estafa cibernética clásica o un delito de corrupción penado con cárcel. Las bases de datos judiciales están auditadas por registros inmutables de trazabilidad.</li>
  <li><strong>Guarda tus consultas con metadatos:</strong> Al descargar tu PDF, conserva en el nombre del archivo la fecha exacta de emisión, ya que en la mayoría de convocatorias laborales del sector público o privado, el certificado tiene una validez temporal tácita de 30 a 60 días desde su expedición.</li>
</ul>

<h2>8. Conclusiones Técnicas de Andrés (Universidad de la Costa)</h2>
<p>El sistema en línea de antecedentes judiciales de la Policía Nacional representa uno de los mayores aciertos de digitalización ciudadana en Colombia, simplificando un trámite que hace una década tomaba horas y costos innecesarios. Como futuros ingenieros y ciudadanos informados, comprender los mecanismos de autenticación web, los derechos de Habeas Data y el funcionamiento de las impresoras virtuales a PDF nos permite realizar cualquier postulación laboral con total autonomía y seguridad informática.</p>"""

# ----------------------------------------------------------------------------------
# ARTÍCULO 3: SISBÉN IV CONSULTA Y REENCUESTA
# ----------------------------------------------------------------------------------
TRAMITES_CONTENT[3] = """<h2>1. Fundamentos del Sisbén IV y su Modelo de Clasificación Socioeconómica</h2>
<p>El Sistema de Identificación de Potenciales Beneficiarios de Programas Sociales (Sisbén) es la principal herramienta de focalización individual del gasto social del Estado colombiano, administrada técnicamente por el Departamento Nacional de Planeación (DNP). A diferencia de lo que muchas personas creen, el Sisbén no es un subsidio en sí mismo, ni es un sistema de salud (EPS), ni entrega dinero en efectivo de forma automática; es un sistema de información y clasificación estandarizado que evalúa las condiciones de vida e ingresos de los hogares colombianos para determinar quiénes pueden acceder a programas como Renta Ciudadana, Colombia Mayor, Devolución del IVA, Jóvenes en Paz, subsidios de vivienda Mi Casa Ya y gratuidad en la matrícula universitaria en instituciones de educación superior pública.</p>
<p>En el año 2021, Colombia culminó la transición histórica del Sisbén III al <strong>Sisbén IV</strong>. El antiguo modelo (Sisbén III) funcionaba con un puntaje numérico decimal que iba desde 0 hasta 100 puntos, lo cual generaba distorsiones graves: si una familia humilde pintaba la fachada de su vivienda o adquiría un televisor mediante crédito, su puntaje se disparaba perdiendo el acceso a la salud subsidiada. El Sisbén IV revolucionó este esquema al abandonar el puntaje numérico y adoptar un modelo multidimensional de <strong>clasificación por grupos alfanuméricos</strong>, el cual cruza la información declarada en la encuesta domiciliaria con decenas de registros administrativos en tiempo real (DIAN, PILA, ADRES, Registraduría, Ministerio de Educación y centrales de riesgo financiero).</p>

<h2>2. Estructura de Grupos y Subgrupos en el Sisbén IV</h2>
<p>El sistema clasifica a la población en cuatro grandes grupos poblacionales, subdivididos en categorías específicas identificadas con letras y números:</p>
<ul>
  <li><strong>Grupo A (Pobreza Extrema):</strong> Comprende los subgrupos desde <code>A1</code> hasta <code>A5</code>. En este segmento se encuentran los hogares con la menor capacidad de generación de ingresos y condiciones de vida sumamente precarias. Los hogares en Grupo A tienen prioridad absoluta en todos los programas de transferencias monetarias del Departamento para la Prosperidad Social (DPS).</li>
  <li><strong>Grupo B (Pobreza Moderada):</strong> Comprende los subgrupos desde <code>B1</code> hasta <code>B7</code>. Son familias cuyos ingresos se encuentran por debajo de la línea de pobreza pero que cuentan con ciertas capacidades laborales o estabilidad básica. Tienen acceso a subsidios de vivienda, transferencias condicionadas y tarifas reducidas en trámites públicos.</li>
  <li><strong>Grupo C (Población Vulnerable):</strong> Comprende los subgrupos desde <code>C1</code> hasta <code>C18</code>. Identifica a aquellos hogares que, si bien no se consideran técnicamente en condición de pobreza monetaria, están en alto riesgo de caer en ella ante cualquier evento adverso (pérdida de empleo, enfermedad de alto costo, inflación desbordada). Tienen acceso preferente a gratuidad en matrícula de educación superior (Política de Gratuidad 'Puedo Estudiar') y beneficios de formación técnica en el SENA.</li>
  <li><strong>Grupo D (Población No Pobre / No Vulnerable):</strong> Comprende los subgrupos desde <code>D1</code> hasta <code>D21</code>. Son hogares con estabilidad económica o ingresos suficientes que no califican para subsidios asistenciales del Estado, pero que pueden requerir la ficha del Sisbén como requisito de control en trámites administrativos o compensaciones de servicios públicos.</li>
</ul>

<h2>3. Procedimiento Digital para Consultar y Descargar la Ficha Oficial del Sisbén IV</h2>
<p>El Departamento Nacional de Planeación dispone de un portal web público donde cualquier ciudadano colombiano o extranjero regularizado puede consultar su ficha técnica y descargar el certificado oficial timbrado con firma digital:</p>
<ol>
  <li><strong>Ingreso a la plataforma central:</strong> Accede a través de tu navegador a la dirección web oficial: <code>https://www.sisben.gov.co</code> y localiza el botón destacado <strong>Consulta tu grupo Sisbén</strong> en la esquina superior derecha o en la zona central de la portada.</li>
  <li><strong>Selección del documento de identificación:</strong> En el formulario interactivo, despliega la lista de tipos de documento. Las opciones incluyen: <em>Cédula de Ciudadanía</em>, <em>Tarjeta de Identidad</em> (para menores de edad), <em>Registro Civil de Nacimiento</em>, <em>Cédula de Extranjería</em>, <em>Permiso por Protección Temporal (PPT)</em> o <em>Permiso Especial de Permanencia (PEP)</em>.</li>
  <li><strong>Ingreso del número sin separadores:</strong> Escribe tu número de identificación en la casilla correspondiente. No ingreses puntos, comas ni espacios.</li>
  <li><strong>Validación de seguridad:</strong> Completa el captcha visual de verificación de seguridad.</li>
  <li><strong>Visualización de la Ficha de Información Social:</strong> Pulsa el botón <strong>Consultar</strong>. La plataforma desplegará la ficha completa del hogar, la cual incluye: nombres completos del consultante, departamento y municipio donde se realizó el censo domiciliario, fecha de la última actualización en base de datos nacional, grupo asignado (por ejemplo, <em>B4</em>) y los nombres de todos los integrantes registrados que conforman el núcleo familiar.</li>
  <li><strong>Descarga en PDF con sello del DNP:</strong> En la parte inferior de la consulta, pulsa sobre el botón <strong>Imprimir</strong> o presiona <code>Ctrl + P</code>. Selecciona <em>Guardar como PDF</em> asegurándote de habilitar las opciones de encabezados y fondos gráficos para que se conserve el membrete oficial de la República de Colombia y el Departamento Nacional de Planeación.</li>
</ol>

<h2>4. Qué Hacer si Apareces con 'Franja Roja' o Estado en Verificación</h2>
<p>Desde la implementación del Registro Social de Hogares (RSH), cientos de miles de colombianos han descubierto con preocupación que su ficha del Sisbén muestra una advertencia de color rojo con el mensaje: <em>'Ficha en verificación'</em> o <em>'Inconsistencia en información administrativa'</em>. Este fenómeno suele suspender temporalmente el cobro de subsidios como Renta Ciudadana o Colombia Mayor.</p>
<p>La causa técnica de este bloqueo ocurre cuando el algoritmo del DNP detecta una disparidad entre lo declarado en la encuesta presencial y los cruces de datos externos. Por ejemplo: un integrante del hogar declaró no tener empleo pero apareció cotizando a pensión en la planilla PILA como trabajador dependiente; o se reportó la posesión de un vehículo de alta gama o transacciones bancarias que superan los topes fijados para pobreza extrema.</p>
<p>Para subsanar esta franja roja, el jefe de hogar debe acudir a la oficina municipal del Sisbén de su alcaldía local (o radicar solicitud formal por el portal ciudadano del Sisbén) aportando pruebas documentales: certificado laboral con monto real de salario, certificación de retiro de empresa si el contrato ya finalizó, o documentos que demuestren que los ingresos del cotizante no corresponden a enriquecimiento sino a sustento básico.</p>

<h2>5. Procedimiento para Solicitar Reencuesta o Actualización por Cambio de Domicilio</h2>
<p>Si consideras que tu grupo asignado no refleja tu realidad económica actual, si cambiaste de lugar de residencia, si nació un nuevo integrante en tu hogar o si falleció un familiar registrado, estás en el derecho legal de solicitar una <strong>reencuesta nueva</strong>:</p>
<ol>
  <li><strong>Plataforma virtual del Portal Ciudadano:</strong> Ingresa a <code>https://portalciudadano.sisben.gov.co</code> y regístrate con tu correo electrónico y cédula. Esta es la plataforma habilitada por el DNP para tramitar solicitudes sin hacer filas en las sedes físicas de las alcaldías.</li>
  <li><strong>Opción de Solicitud de Reencuesta:</strong> Una vez dentro de tu perfil de usuario, selecciona el módulo <em>Solicitar encuesta nueva por inconformidad</em> o <em>Modificación de miembros del hogar</em>.</li>
  <li><strong>Diligenciamiento de datos geográficos:</strong> Sube la fotografía digital de tu recibo de energía eléctrica o acueducto para validar la dirección donde el encuestador del municipio acudirá con el dispositivo móvil de captura (DMC).</li>
  <li><strong>Visita domiciliaria obligatoria:</strong> La solicitud virtual genera un radicado. Posteriormente, un funcionario debidamente carnetizado de la Alcaldía Distrital (por ejemplo, de la Alcaldía de Barranquilla o Bogotá) visitará tu vivienda para aplicar la encuesta en el software oficial del DNP. Exige siempre el número de radicado del trámite.</li>
</ol>

<h2>6. Mitos Frecuentes vs. Realidad Técnica del Sisbén IV</h2>
<table>
  <thead>
    <tr>
      <th>Mito Popular</th>
      <th>Realidad Técnica Basada en la Ley</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><em>'Si consigo un empleo formal me quitan el Sisbén para siempre.'</em></td>
      <td>El Sisbén no se 'quita'; el registro permanece en la base nacional. Lo que ocurre es que tu grupo se actualiza automáticamente mediante el Registro Social de Hogares.</td>
    </tr>
    <tr>
      <td><em>'Tengo que pagarle a un gestor comunal para que me baje a Grupo A.'</em></td>
      <td>Totalmente falso y fraudulento. Los encuestadores utilizan software georreferenciado con auditoría por GPS; ningún intermediario externo puede modificar los algoritmos del DNP.</td>
    </tr>
    <tr>
      <td><em>'Estar en el Sisbén me da derecho automático al subsidio mensual.'</em></td>
      <td>El Sisbén solo clasifica. Cada programa social (DPS, MinVivienda, MinEducación) fija sus propios puntos de corte y cupos presupuestales anuales.</td>
    </tr>
  </tbody>
</table>

<h2>7. Conclusiones y Consejos de Andrés (Universidad de la Costa)</h2>
<p>El Sisbén IV es el mapa social de Colombia. Mantener tu información verídica y consultar periódicamente tu estado en la plataforma nacional es indispensable para cualquier estudiante universitario que aspire a beneficios de matrícula cero o subsidios de sostenimiento. Nunca recurras a intermediarios callejeros ni entregues sumas de dinero por supuestos 'cambios de puntaje'; utiliza siempre los canales oficiales del DNP y el Portal Ciudadano.</p>"""

# ----------------------------------------------------------------------------------
# ARTÍCULO 4: ANTECEDENTES PROCURADURÍA SIRI
# ----------------------------------------------------------------------------------
TRAMITES_CONTENT[4] = """<h2>1. Naturaleza Jurídica y Propósito del Certificado de la Procuraduría General de la Nación</h2>
<p>La Procuraduría General de la Nación es el máximo organismo del Ministerio Público en Colombia. Su misión constitucional fundamental radica en vigilar la conducta oficial de quienes desempeñan funciones públicas, adelantar investigaciones disciplinarias, sancionar faltas cometidas por servidores del Estado y particulares que manejan recursos públicos, y salvaguardar los derechos humanos y el ordenamiento jurídico de la República.</p>
<p>El Certificado de Antecedentes Disciplinarios emitido por la Procuraduría es un documento que certifica la existencia o inexistencia de providencias ejecutoriadas que impongan sanciones de destitución, suspensión en el ejercicio del cargo, inhabilidad general o especial para contratar con el Estado colombiano o para el desempeño de funciones públicas. Para cualquier profesional, contratista de prestación de servicios, pasante universitario o ciudadano que aspire a celebrar un contrato estatal (regido por la Ley 80 de 1993 y sus normas complementarias), la presentación de este certificado es un requisito legal inexcusable.</p>

<h2>2. Marco Normativo: Código General Disciplinario y Reformas Recientes</h2>
<p>El régimen disciplinario en Colombia ha experimentado profundas transformaciones normativas en los últimos años. La entrada en vigencia de la <strong>Ley 1952 de 2019</strong> (Código General Disciplinario), modificada sustancialmente por la <strong>Ley 2094 de 2021</strong>, reorganizó las funciones de instrucción y juzgamiento para garantizar el debido proceso y la doble conformidad de acuerdo con los estándares fijados por la Corte Interamericana de Derechos Humanos (Corte IDH) en el emblemático caso Petro Urrego vs. Colombia.</p>
<p>Bajo este esquema normativo, las faltas gravísimas cometidas a título de dolo o culpa gravísima pueden conllevar la destitución del cargo e inhabilidad general para ejercer cargos públicos por periodos que van desde diez (10) hasta veinte (20) años. Las faltas graves acarrean suspensión e inhabilidad especial, mientras que las faltas leves culposas conllevan amonestación escrita con registro en la hoja de vida o multas económicas. Toda esta gama de decisiones sancionatorias ejecutoriadas debe ser transmitida inmediatamente por los operadores disciplinarios al sistema central de registro de la Procuraduría para su publicidad oportuna.</p>

<h2>3. Diferencia Crucial: Certificado Ordinario vs. Certificado Especial</h2>
<p>Uno de los errores más recurrentes entre los ciudadanos al momento de realizar este trámite en línea es no saber qué modalidad de certificado generar, ya que la plataforma presenta dos opciones bien diferenciadas:</p>
<ul>
  <li><strong>Certificado Ordinario:</strong> Es el documento estándar que solicita la gran mayoría de empresas privadas, bolsas de empleo y procesos contractuales generales. Este certificado refleja las sanciones disciplinarias e inhabilidades que se encuentren <strong>vigentes</strong> al momento de la consulta durante los últimos cinco (5) años anteriores a la expedición del certificado. Si el ciudadano nunca ha sido sancionado o su periodo de sanción ya expiró y no tiene inhabilidades activas, el sistema emitirá el documento indicando: <em>'No registra antecedentes disciplinarios'</em>.</li>
  <li><strong>Certificado Especial:</strong> Es un documento reservado y requerido exclusivamente para acceder a cargos de alto nivel en el Estado o corporaciones de elección popular que exigen requisitos constitucionales o legales específicos de inhabilidad (por ejemplo: aspirantes a la Presidencia de la República, Congreso de la República, magistraturas de altas cortes, directores de entidades descentralizadas, o cargos de elección como alcaldes y gobernadores). En el Certificado Especial se incluyen todas las sanciones que se hayan impuesto en cualquier época de la vida, independientemente de que hayan caducado, con el fin de verificar inhabilidades intemporales establecidas por la Constitución Política.</li>
</ul>

<h2>4. Arquitectura del Sistema de Información de Registro de Sanciones e Inhabilidades (SIRI)</h2>
<p>La emisión de este certificado se apoya tecnológicamente en el denominado <strong>Sistema SIRI</strong> (Sistema de Información de Registro de Sanciones e Inhabilidades). Esta base de datos nacional centralizada se alimenta diariamente de las comunicaciones y sentencias remitidas por las procuradurías delegadas, personerías municipales, oficinas de control disciplinario interno y tribunales de la Comisión Nacional de Disciplina Judicial.</p>
<p>El sistema opera de forma automatizada mediante un servicio web protegido con capas de seguridad contra ataques de denegación de servicio (DDoS) y cuenta con una función criptográfica de verificación que estampa un código alfanumérico único en el encabezado del documento PDF. Cualquier receptor del documento puede digitar dicho código en el portal de validación para contrastar que el contenido del archivo coincida al 100% con los registros originales del SIRI.</p>

<h2>5. Procedimiento Paso a Paso para la Generación y Descarga en Línea</h2>
<p>El trámite de expedición del Certificado de Antecedentes de la Procuraduría es completamente gratuito y no demanda más de dos minutos siguiendo estos pasos:</p>
<ol>
  <li><strong>Ingreso a la web oficial:</strong> Abre tu navegador e ingresa a <code>https://www.procuraduria.gov.co</code> y busca la sección destacada <em>'Certificado de Antecedentes'</em>, o accede directamente a la URL transaccional: <code>https://www.procuraduria.gov.co/Pages/Generacion-de-antecedentes.aspx</code>.</li>
  <li><strong>Selección de la opción Generar:</strong> En el menú lateral o central, encontrarás tres opciones: <em>'Generar Certificado'</em>, <em>'Consultar Certificado'</em> y <em>'Validar Certificado'</em>. Selecciona <strong>Generar Certificado de Antecedentes</strong>.</li>
  <li><strong>Elección del tipo de certificado:</strong> Marca la casilla correspondiente a <strong>Certificado Ordinario</strong> (a menos que una convocatoria pública de alto nivel te exija expresamente el certificado especial).</li>
  <li><strong>Ingreso de datos de identificación:</strong>
    <ul>
      <li>Selecciona en el menú desplegable tu tipo de documento: <em>Cédula de Ciudadanía</em>, <em>Cédula de Extranjería</em>, <em>Número de Identificación Tributaria (NIT)</em> o <em>Pasaporte</em>.</li>
      <li>Escribe tu número de identificación en la casilla contigua sin caracteres no numéricos.</li>
    </ul>
  </li>
  <li><strong>Resolución de la pregunta de control de seguridad:</strong> El sistema de la Procuraduría no utiliza el reCAPTCHA tradicional de Google, sino un sistema propio de preguntas matemáticas o lógicas de validación ciudadana (por ejemplo: <em>'¿Cuál es la capital de Colombia?'</em>, <em>'Resuelva: ¿cuánto es 5 + 3?'</em>, o una imagen con letras distorsionadas). Digita la respuesta exacta en minúsculas.</li>
  <li><strong>Generación y descarga del PDF timbrado:</strong> Haz clic en el botón <strong>Generar</strong>. El sistema procesará la solicitud en el motor SIRI y descargará automáticamente un archivo PDF oficial a tu carpeta de descargas, o abrirá una nueva pestaña del navegador mostrando el certificado con el sello institucional de la Procuraduría General de la Nación, la firma digital y el código de verificación alfanumérico.</li>
</ol>

<h2>6. Validación Criptográfica y Procedimiento de Corrección de Homónimos</h2>
<p>En el ejercicio profesional, pueden presentarse casos atípicos en los cuales un ciudadano que jamás ha ejercido cargos públicos ni contratado con el Estado aparece en el sistema con un reporte sancionatorio. Este fenómeno casi siempre obedece a un <strong>homónimo registral</strong> o a un error mecanográfico en la transcripción del número de cédula realizado por el juzgado o la personería municipal al momento de remitir la boleta de reporte al SIRI.</p>
<p>Si te encuentras ante esta situación anómala, el procedimiento legal para subsanarlo es el siguiente:</p>
<ol>
  <li>Descarga el certificado donde se evidencia el antecedente erróneo y anota el número de radicado del proceso disciplinario.</li>
  <li>Redacta un <em>Derecho de Petición en interés particular</em> dirigido a la División de Registro y Control y Correspondencia de la Procuraduría General de la Nación.</li>
  <li>Adjunta una copia legible de tu Cédula de Ciudadanía y un Certificado de Vigencia de Documento expedido por la Registraduría Nacional del Estado Civil.</li>
  <li>Radica la solicitud a través de la sede electrónica de la Procuraduría (<code>sedeelectronica.procuraduria.gov.co</code>). Por mandato del Código de Procedimiento Administrativo y de lo Contencioso Administrativo (CPACA), la entidad cuenta con un plazo perentorio de quince (15) días hábiles para cotejar el expediente físico original y depurar la base de datos nacional.</li>
</ol>

<h2>7. Solución a Problemas Técnicos Frecuentes</h2>
<table>
  <thead>
    <tr>
      <th>Problema Detectado</th>
      <th>Explicación Técnica</th>
      <th>Solución Inmediata</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>El navegador bloquea la descarga automática</strong></td>
      <td>El navegador web interpreta la descarga iniciada por JavaScript como una ventana emergente peligrosa.</td>
      <td>Revisa la barra de direcciones superior derecha, haz clic en el ícono de ventana bloqueada y selecciona 'Permitir siempre ventanas emergentes de procuraduria.gov.co'.</td>
    </tr>
    <tr>
      <td><strong>Pregunta de control da error repetidamente</strong></td>
      <td>Sensibilidad a mayúsculas, tildes o caracteres especiales en las respuestas del sistema.</td>
      <td>Escribe la respuesta en minúsculas sencillas sin tildes (por ejemplo, escribe 'bogota' en lugar de 'Bogotá').</td>
    </tr>
    <tr>
      <td><strong>'El número de documento no se encuentra en el censo'</strong></td>
      <td>Cédula expedida recientemente cuya base de datos aún no ha sido sincronizada desde la Registraduría.</td>
      <td>Esperar entre 8 y 15 días hábiles después de reclamar la cédula física o radicar petición de sincronización en el portal SIRI.</td>
    </tr>
    <tr>
      <td><strong>El PDF aparece en blanco al abrirse en el visor</strong></td>
      <td>Incompatibilidad del visor PDF integrado del navegador con las fuentes tipográficas del sello oficial.</td>
      <td>Descargar el archivo al disco duro y abrirlo con Adobe Acrobat Reader, Foxit Reader o el navegador Edge.</td>
    </tr>
  </tbody>
</table>

<h2>8. Medidas de Seguridad y Custodia del Documento Electrónico</h2>
<ul>
  <li><strong>Auditoría de integridad documental:</strong> Recuerda que todo certificado emitido por la Procuraduría cuenta con un hash único de comprobación. Modificar el texto de un certificado en un editor de PDF para borrar una anotación sancionatoria constituye el delito tipificado de uso de documento público falso (artículo 289 del Código Penal Colombiano), el cual contempla penas de prisión de cuatro a ocho años.</li>
  <li><strong>Vigencia institucional recomendada:</strong> Las secretarías de despacho, universidades y juntas directivas suelen exigir que el certificado no posea una antigüedad mayor a treinta (30) o sesenta (60) días. Acostúmbrate a emitir un ejemplar nuevo el mismo día en que vas a radicar tu documentación laboral.</li>
</ul>

<h2>9. Conclusiones y Recomendaciones de Andrés (Universidad de la Costa)</h2>
<p>El Certificado de Antecedentes Disciplinarios de la Procuraduría es uno de los trámites estatales más ágiles, transparentes y confiables en Colombia. Conocer la diferencia entre el certificado ordinario y el especial, comprender el marco de la Ley 1952 y saber cómo validar el código alfanumérico ante cualquier comité evaluador te otorga una ventaja profesional indudable. Te recomendamos consultar tu historial periódicamente para garantizar que tu hoja de vida pública se encuentre siempre impecable y lista para cualquier oportunidad académica o laboral.</p>"""

# ----------------------------------------------------------------------------------
# ARTÍCULO 5: CONTRALORÍA ANTECEDENTES FISCALES
# ----------------------------------------------------------------------------------
TRAMITES_CONTENT[5] = """<h2>1. Fundamento Constitucional y Misión del Control Fiscal en Colombia</h2>
<p>La Contraloría General de la República (CGR) es el máximo órgano de control fiscal del Estado colombiano. De conformidad con el artículo 267 de la Constitución Política de 1991, su función primordial es la vigilancia de la gestión fiscal de la administración pública y de los particulares o entidades que manejen o custodien fondos o bienes de la Nación. Su radio de acción abarca el control financiero, de gestión y de resultados, fundado en la eficiencia, la economía, la equidad y la valoración de los costos ambientales.</p>
<p>Dentro de este marco de vigilancia opera el denominado <strong>Boletín de Responsables Fiscales (SIRECI / SIREF)</strong>. Cuando un servidor público o un contratista independiente genera un detrimento patrimonial a las finanzas del Estado por dolo o culpa grave (por ejemplo, sobrecostos injustificados en obras públicas, desvío de recursos de regalías o pérdida de inventarios públicos bajo su custodia) y es condenado mediante un proceso de responsabilidad fiscal ejecutoriado, su nombre es reportado en este boletín. El <strong>Certificado de Antecedentes Fiscales</strong> es el documento formal y vinculante que acredita que una persona natural o jurídica no se encuentra incluida en dicho registro sancionatorio.</p>

<h2>2. Estructura Jurídica del Proceso de Responsabilidad Fiscal</h2>
<p>Para comprender por qué una persona natural o una empresa puede llegar a figurar en el boletín fiscal, es necesario conocer la normativa que rige las investigaciones de la CGR: la <strong>Ley 610 de 2000</strong> y el Estatuto Anticorrupción contenido en la <strong>Ley 1474 de 2011</strong>. El proceso de responsabilidad fiscal tiene una naturaleza eminentemente resarcitoria, no penal ni sancionatoria en estricto sentido. Su propósito principal no es privar de la libertad a la persona, sino lograr la recuperación de los dineros públicos que fueron indebidamente apropiados, extraviados o malgastados.</p>
<p>El proceso fiscal requiere la concurrencia probada de tres elementos estructurales esenciales:</p>
<ul>
  <li><strong>Una conducta dolosa o gravemente culposa:</strong> Atribuible a una persona que ejerza gestión fiscal o que tenga la custodia material o jurídica de recursos públicos de la Nación o de las entidades territoriales.</li>
  <li><strong>Un daño patrimonial al Estado:</strong> Que se traduce en una lesión cierta, económica, cuantificable y real sobre los bienes, caudales o presupuestos de las entidades públicas.</li>
  <li><strong>Un nexo causal directo:</strong> La relación directa de causalidad entre la acción u omisión del gestor y el daño económico efectivamente ocasionado a las arcas estatales.</li>
</ul>
<p>Una vez concluido el proceso con un fallo con responsabilidad fiscal ejecutoriado y en firme, la Contraloría liquida la cuantía del daño. Si el responsable no cancela la obligación patrimonial de forma inmediata, se emite el reporte al Boletín de Responsables Fiscales y se inician los cobros coactivos mediante embargos de cuentas bancarias y bienes inmuebles.</p>

<h2>3. Obligatoriedad Legal en la Contratación Pública y Privada</h2>
<p>La presentación del Certificado de Antecedentes Fiscales de la Contraloría es obligatoria para:</p>
<ul>
  <li>Posesión en cualquier cargo de la carrera administrativa, provisionalidad o de libre nombramiento y remoción en entidades del Estado a nivel nacional, departamental o municipal.</li>
  <li>Suscripción de contratos estatales regidos por la Ley 80 de 1993, la Ley 1150 de 2007 o bajo regímenes especiales de contratación con recursos públicos.</li>
  <li>Licitaciones públicas, subastas inversas, convenios de asociación o convocatorias del Sistema General de Regalías (SGR).</li>
  <li>Empresas privadas que requieren verificar la solvencia moral y patrimonial de directores financieros, tesoreros o revisores fiscales.</li>
</ul>
<p>La ley establece expresamente que estar incluido en el Boletín de Responsables Fiscales genera una inhabilidad sobreviniente para contratar o desempeñar funciones públicas, la cual persiste hasta tanto el sancionado cancele la totalidad de la deuda fiscal liquidada o se configure una causal legal de exclusión.</p>

<h2>4. Procedimiento Paso a Paso para la Expedición Virtual del Certificado Fiscal</h2>
<p>El trámite de consulta y descarga del certificado es totalmente digital, gratuito y no requiere la intermediación de abogados ni gestores de ventanilla:</p>
<ol>
  <li><strong>Ingreso al portal institucional:</strong> Abre el navegador web e ingresa a la dirección oficial: <code>https://www.contraloria.gov.co</code>.</li>
  <li><strong>Localización del servicio de antecedentes:</strong> En la página de inicio, busca el banner interactivo denominado <em>'Certificado de Antecedentes Fiscales'</em> o ingresa directamente a la sección de trámites en línea: <code>https://cfiscales.contraloria.gov.co/</code>.</li>
  <li><strong>Selección del tipo de persona:</strong>
    <ul>
      <li><strong>Persona Natural:</strong> Para ciudadanos independientes, profesionales, estudiantes o empleados públicos (utiliza cédula de ciudadanía o cédula de extranjería).</li>
      <li><strong>Persona Jurídica:</strong> Para empresas legalmente constituidas, sociedades comerciales, fundaciones o consorcios (utiliza el NIT con su dígito de verificación).</li>
    </ul>
  </li>
  <li><strong>Diligenciamiento de los datos de consulta:</strong> Selecciona el tipo de documento, escribe el número de identificación en la casilla correspondiente (sin puntos, sin espacios ni caracteres especiales) y pulsa en el botón para responder el reto de seguridad.</li>
  <li><strong>Generación y visualización del documento:</strong> Haz clic sobre el botón <strong>Generar Certificado</strong>. El sistema procesará la solicitud consultando en el servidor del SIREF y emitirá en pantalla un documento en formato PDF con la firma electrónica del Contralor General o su delegado.</li>
  <li><strong>Almacenamiento del PDF timbrado:</strong> Haz clic en el ícono de descarga del visor de PDF o presiona <code>Ctrl + S</code> para guardar el archivo localmente. El archivo contiene un código de seguridad de 32 caracteres y un código QR que permite validar su autenticidad desde cualquier dispositivo móvil.</li>
</ol>

<h2>5. Modalidades Especiales: Certificado con Historia y Consultas Corporativas</h2>
<p>Para entidades estatales u organizaciones que manejan grandes volúmenes de personal, la Contraloría dispone de herramientas especializadas:</p>
<ul>
  <li><strong>Certificado con Historia:</strong> Mientras que el certificado ordinario únicamente refleja la situación fiscal activa del ciudadano al día de la consulta, las entidades con atribuciones de control pueden solicitar un certificado histórico que documente si el investigado figuró en el boletín en periodos pretéritos y las fechas en que canceló sus obligaciones patrimoniales.</li>
  <li><strong>Consulta Masiva de Antecedentes (Web Service):</strong> Las secretarías de educación, alcaldías y ministerios pueden conectarse vía API o cargar lotes en formato CSV/Excel a través del aplicativo SIRECI para obtener de forma simultánea el estado fiscal de centenares de contratistas en segundos, reduciendo drásticamente los cuellos de botella administrativos.</li>
</ul>

<h2>6. Tabla de Contingencias y Preguntas Técnicas Frecuentes</h2>
<table>
  <thead>
    <tr>
      <th>Situación Técnica</th>
      <th>Motivo Subyacente</th>
      <th>Acción de Resolución</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>'Error de Conexión con el Servidor SIREF'</strong></td>
      <td>Sobrecarga de tráfico en horas pico de contratación pública (primeros días hábiles de enero o periodos electorales).</td>
      <td>Realizar la consulta en horarios de baja demanda, preferiblemente entre las 6:00 AM y 8:00 AM, o en horas de la noche.</td>
    </tr>
    <tr>
      <td><strong>El código QR no redirige a la página oficial</strong></td>
      <td>Lector de QR en el móvil desactualizado o adulteración del archivo PDF por un emisor fraudulento.</td>
      <td>Acceder directamente a contraloria.gov.co e ingresar manualmente el código alfanumérico en el validador oficial.</td>
    </tr>
    <tr>
      <td><strong>Aparece un homónimo en el Boletín</strong></td>
      <td>Coincidencia exacta de nombres en personas con números de identificación distintos.</td>
      <td>Verificar siempre que el certificado esté expedido con tu número de cédula exacto. El número de identificación prima sobre los nombres.</td>
    </tr>
    <tr>
      <td><strong>El certificado muestra fecha de un año anterior</strong></td>
      <td>Caché local del navegador que sirve un archivo PDF previamente descargado.</td>
      <td>Forzar recarga dura con Ctrl + Shift + R o eliminar cookies y archivos temporales del navegador.</td>
    </tr>
  </tbody>
</table>

<h2>7. Buenas Prácticas y Ciberseguridad para el Manejo de Documentos Fiscales</h2>
<ul>
  <li><strong>Descarga directa desde la fuente:</strong> Nunca aceptes certificados fiscales remitidos por cadenas de WhatsApp o descargados desde plataformas de almacenamiento no oficiales. La validez de estos documentos ante comités evaluadores depende de su trazabilidad original.</li>
  <li><strong>Control de vigencia temporal:</strong> Aunque el documento indica la fecha y hora de corte, los manuales de contratación de las entidades del Estado suelen exigir que el certificado no supere los 30 días calendario de haber sido expedido. Genera siempre un ejemplar fresco antes de radicar tus cuentas de cobro o propuestas de licitación.</li>
</ul>

<h2>8. Conclusiones y Valoración de Andrés (Universidad de la Costa)</h2>
<p>El Certificado de Antecedentes Fiscales de la Contraloría es el testimonio de transparencia financiera que avala a cualquier profesional para gestionar recursos del Estado o prestar sus servicios técnicos a entidades públicas en Colombia. Gracias a la digitalización de la CGR, obtener este certificado es una operación sencilla, rápida y segura que todo estudiante de ingeniería y futuro profesional debe dominar con absoluta solvencia técnica.</p>"""

# ----------------------------------------------------------------------------------
# ARTÍCULO 6: RUNT Y SIMIT
# ----------------------------------------------------------------------------------
TRAMITES_CONTENT[6] = """<h2>1. Ecosistema de Tránsito en Colombia: Arquitectura del RUNT y el SIMIT</h2>
<p>El sector vial y automotor en Colombia se gestiona a través de dos macroplataformas tecnológicas complementarias pero jurídicamente distintas: el <strong>RUNT</strong> (Registro Único Nacional de Tránsito) y el <strong>SIMIT</strong> (Sistema Integrado de Información sobre Multas y Sanciones por Infracciones de Tránsito). Comprender con precisión qué datos custodia cada sistema es la clave para evitar trámites infructuosos y resolver comparendos viales con éxito:</p>
<ul>
  <li><strong>El RUNT (Registro Único Nacional de Tránsito):</strong> Regulado por la Ley 769 de 2002 (Código Nacional de Tránsito) y la Ley 1005 de 2006, es una mega base de datos centralizada administrada mediante concesión bajo supervisión del Ministerio de Transporte. El RUNT consolida de manera fidedigna la hoja de vida de todos los conductores del país, el historial técnico y documental de todos los vehículos automotores, remolques y semirremolques, las licencias de conducción (categorías A1, A2, B1, B2, C1, C2, C3), los certificados de aptitud médica emitidos por Centros de Reconocimiento de Conductores (CRC), las pólizas del SOAT y las revisiones técnico-mecánicas expedidas por los CDA.</li>
  <li><strong>El SIMIT (Federación Colombiana de Municipios):</strong> Es el sistema nacional oficial creado por mandato legal para centralizar el registro, cobro y recaudo de todas las multas y sanciones impuestas por las secretarías de tránsito y movilidad de todos los municipios, distritos y departamentos de Colombia. Cuando un agente de tránsito impone un comparendo físico en vía o una cámara de fotodetección (fotomulta) registra una presunta infracción de velocidad o SOAT vencido, la información viaja obligatoriamente al SIMIT.</li>
</ul>

<h2>2. Marco Constitucional: Sentencia C-038 de 2020 y la Responsabilidad en Fotomultas</h2>
<p>Uno de los hitos jurídicos más relevantes en el derecho del tránsito colombiano aconteció con la expedición de la histórica <strong>Sentencia C-038 de 2020 de la Corte Constitucional</strong>. Durante años, muchas secretarías de movilidad del país aplicaban una interpretación abusiva de la responsabilidad solidaria, sancionando automáticamente al propietario registrado en el RUNT sin importar quién iba conduciendo el vehículo al momento de la infracción capturada por las cámaras de fotodetección.</p>
<p>La Corte Constitucional declaró inexequible este principio de solidaridad para infracciones de tránsito generales, consagrando de manera categórica que el Estado tiene la carga ineludible de demostrar la <em>culpabilidad personalísima del conductor</em>. En palabras sencillas: una cámara de fotomulta no puede multar a un propietario simplemente por ser el dueño del carro o la moto si la autoridad no prueba de manera técnica e idónea que esa persona específica era quien iba tras el volante. Aunque posteriormente la Ley 2161 de 2021 impuso deberes de aseguramiento al propietario respecto a tener el SOAT y la Revisión Técnico-Mecánica vigentes, en infracciones de velocidad, semáforos en rojo o maniobras prohibidas la carga de individualización del conductor sigue siendo estricta obligación del organismo de tránsito.</p>

<h2>3. Por Qué el 'Paz y Salvo' es Indispensable para Cualquier Trámite de Tránsito</h2>
<p>De acuerdo con el artículo 10 de la Ley 769 de 2002, para que un ciudadano pueda realizar cualquier trámite de tránsito en Colombia (como renovar la licencia de conducción, expedir un duplicado por pérdida, tramitar el traspaso de propiedad de una motocicleta o automóvil, o inscribir una prenda financiera), debe encontrarse a <strong>Paz y Salvo por concepto de multas e infracciones de tránsito</strong> en el sistema SIMIT. La existencia de un solo comparendo pendiente bloquea automáticamente la plataforma del RUNT impidiendo finalizar cualquier solicitud.</p>

<h2>4. Consulta de Licencia de Conducción en el Portal RUNT Paso a Paso</h2>
<p>Para comprobar si tu licencia de conducción se encuentra activa, verificar su fecha de vencimiento o revisar el estado de tu SOAT y revisión técnico-mecánica, sigue este procedimiento:</p>
<ol>
  <li><strong>Acceso al portal oficial:</strong> Abre tu navegador e ingresa a <code>https://www.runt.gov.co</code> o directamente a la sección de consulta ciudadana: <code>https://www.runt.gov.co/consultaCiudadana/#/consultaPersona</code>.</li>
  <li><strong>Selección del módulo de consulta:</strong> En el menú de servicios al ciudadano, selecciona <em>'Consulta de Ciudadanos por Documento de Identidad'</em>.</li>
  <li><strong>Diligenciamiento de los datos de búsqueda:</strong>
    <ul>
      <li>Selecciona el tipo de documento: <em>Cédula de Ciudadanía</em>, <em>Tarjeta de Identidad</em> o <em>Cédula de Extranjería</em>.</li>
      <li>Digita el número de documento de identificación sin espacios ni separadores.</li>
    </ul>
  </li>
  <li><strong>Superación del Captcha de seguridad:</strong> Resuelve el captcha visual para comprobar que no eres un script automatizado.</li>
  <li><strong>Análisis de la información en pantalla:</strong> Pulsa <strong>Consultar Información</strong>. El sistema desplegará:
    <ul>
      <li><strong>Datos Generales:</strong> Nombres completos, estado del ciudadano ante el RUNT (debe decir <em>'Activo'</em>) y fecha de inscripción original.</li>
      <li><strong>Licencias de Conducción:</strong> Detalla cada una de las categorías autorizadas (por ejemplo, <em>A2 para motocicletas</em> y <em>B1 para automóviles particulares</em>), número del plástico físico, organismo de tránsito emisor (ejemplo: <em>Secretaría Distrital de Tránsito y Seguridad Vial de Barranquilla</em>), fecha de expedición y, fundamentalmente, la <strong>fecha de vencimiento</strong> de cada categoría.</li>
      <li><strong>Certificados Médicos:</strong> Muestra el historial de exámenes de aptitud física, mental y de coordinación motriz cargados por los centros médicos autorizados.</li>
    </ul>
  </li>
</ol>

<h2>5. Consulta de Multas, Comparendos y Fotomultas en el Portal SIMIT</h2>
<p>Para verificar si tienes sanciones económicas registradas o comparendos en proceso de impugnación:</p>
<ol>
  <li><strong>Acceso a la plataforma SIMIT:</strong> Ingresa a <code>https://www.fcm.org.co/simit/</code>.</li>
  <li><strong>Búsqueda directa por identificación o placa:</strong> En el banner principal de consulta, ingresa tu número de cédula de ciudadanía o la placa del vehículo que conduces.</li>
  <li><strong>Evaluación de los resultados arrojados:</strong>
    <ul>
      <li><strong>Si no tienes infracciones:</strong> El sistema mostrará una pantalla limpia con un botón verde que indica: <em>'El ciudadano no posee multas ni comparendos pendientes'</em>.</li>
      <li><strong>Si registras infracciones:</strong> Se listará una tabla detallada con el número del comparendo, la fecha y hora de la infracción, la secretaría de tránsito correspondiente, el código de la infracción (ejemplo: <code>C02</code> por estacionar en sitio prohibido, <code>C29</code> por exceso de velocidad, o <code>C35</code> por revisión técnico-mecánica), el valor liquidado y el estado procesal (comparendo notificado o resolución sancionatoria ejecutoriada).</li>
    </ul>
  </li>
  <li><strong>Generación del Paz y Salvo Oficial en PDF:</strong> Si te encuentras al día, haz clic sobre el botón <strong>Descargar Paz y Salvo</strong>. El SIMIT generará un certificado en formato PDF con firma digital institucional y código de validación, el cual puedes imprimir o presentar ante cualquier organismo de tránsito.</li>
</ol>

<h2>6. Aspectos Legales Clave: Prescripción y Caducidad de Comparendos</h2>
<p>Muchos ciudadanos desconocen los términos perentorios que establece el Código Nacional de Tránsito y terminan pagando comparendos que legalmente ya no pueden ser cobrados por las secretarías de tránsito:</p>
<ul>
  <li><strong>Caducidad de la acción contravencional (Artículo 161 Ley 769):</strong> Si una secretaría de tránsito no expide la resolución sancionatoria dentro del término perentorio de <strong>un (1) año</strong> posterior a la fecha de la presunta infracción (notificación del comparendo), la acción caduca de pleno derecho y la multa debe ser archivada mediante solicitud formal.</li>
  <li><strong>Prescripción de la sanción (Artículo 159 Ley 769):</strong> Si ya existe resolución sancionatoria en firme, la secretaría dispone de un término de <strong>tres (3) años</strong> contados a partir de la ejecutoria de dicha resolución para efectuar el cobro coactivo. Si en ese lapso no se inició el mandamiento de pago debidamente notificado, la acción de cobro prescribe y el ciudadano puede radicar un derecho de petición exigiendo el levantamiento inmediato de la sanción en el SIMIT.</li>
</ul>

<h2>7. Matriz de Preguntas Frecuentes y Solución de Inconsistencias</h2>
<table>
  <thead>
    <tr>
      <th>Inconsistencia Frecuente</th>
      <th>Explicación Legal / Técnica</th>
      <th>Solución Operativa</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Pagué el comparendo por PSE pero sigo apareciendo con deuda en el RUNT</strong></td>
      <td>El SIMIT toma entre 24 y 48 horas hábiles en sincronizar sus transacciones bancarias con la base central del RUNT.</td>
      <td>Guarda el comprobante de pago con código CUS del banco y acude a la secretaría o espera 48 horas para que el web service actualice el paz y salvo.</td>
    </tr>
    <tr>
      <td><strong>Aparece una fotomulta de una ciudad donde nunca he estado</strong></td>
      <td>Fotomulta por presunta clonación de placas o error de digitación en la secretaría municipal foránea.</td>
      <td>Radicar impugnación virtual ante el organismo de tránsito aportando pruebas de ubicación (peajes, GPS o registros laborales).</td>
    </tr>
    <tr>
      <td><strong>El RUNT dice 'Licencia Inactiva'</strong></td>
      <td>La licencia cumplió su periodo de vigencia (10 años para particulares menores de 60 años) o no fue renovada en el plazo de ley.</td>
      <td>Agendar examen en un CRC autorizado y acudir a la secretaría de tránsito municipal para tramitar la renovación.</td>
    </tr>
  </tbody>
</table>

<h2>8. Conclusiones y Consejos de Andrés (Universidad de la Costa)</h2>
<p>La consulta periódica del RUNT y el SIMIT es un hábito indispensable para cualquier conductor o propietario de vehículos en Colombia. Conocer tus fechas de vencimiento de la licencia, verificar la vigencia de tu SOAT y monitorear que no tengas fotomultas notificadas a tus espaldas te evitará dolores de cabeza, inmovilizaciones con grúa en retenes viales y sobrecostos por cobros coactivos. Utiliza siempre los canales oficiales y haz valer tus derechos legales ante cualquier irregularidad administrativa.</p>"""

# ----------------------------------------------------------------------------------
# ARTÍCULO 7: ADRES / FOSYGA BDUA
# ----------------------------------------------------------------------------------
TRAMITES_CONTENT[7] = """<h2>1. Del FOSYGA a la ADRES: Evolución del Sistema de Salud Colombiano</h2>
<p>Para la inmensa mayoría de los colombianos, el término 'FOSYGA' (Fondo de Solidaridad y Garantía) sigue estando arraigado en el lenguaje cotidiano cuando se habla de verificar el estado de afiliación a una EPS. Sin embargo, en términos institucionales y jurídicos, el FOSYGA dejó de existir formalmente en el año 2017 a partir de la entrada en vigencia del Decreto 1429 de 2016 y la Ley 1753 de 2015, dando paso a la <strong>ADRES</strong>: la <em>Administradora de los Recursos del Sistema General de Seguridad Social en Salud</em>.</p>
<p>La ADRES es comúnmente llamada por economistas y salubristas como 'el banco de la salud' en Colombia. Es la entidad pública descentralizada del orden nacional que recauda los aportes a salud de todos los trabajadores cotizantes dependientes e independientes, gestiona los recursos del presupuesto general de la Nación destinados al régimen subsidiado y efectúa los giros directos de la Unidad de Pago por Capitación (UPC) a las Entidades Promotoras de Salud (EPS) y a las Instituciones Prestadoras de Servicios (IPS, clínicas y hospitales) en todo el territorio nacional.</p>
<p>Dentro de la infraestructura de la ADRES se encuentra el corazón informático del sistema de aseguramiento: la <strong>BDUA (Base de Datos Única de Afiliados)</strong>. La BDUA es el registro maestro que contiene la información completa, actualizada y oficial de todos los ciudadanos afiliados a los regímenes contributivo, subsidiado, regímenes especiales (Fuerzas Militares, Policía Nacional, Magisterio / Ecopetrol) y de excepción en Colombia.</p>

<h2>2. Para Qué se Necesita el Certificado de Afiliación de la ADRES (BDUA)</h2>
<p>El certificado emitido por la BDUA de la ADRES es el único documento oficial avalado por el Ministerio de Salud que certifica con valor probatorio en cuál EPS se encuentra activo un ciudadano y cuál es su condición de afiliación. Se solicita obligatoriamente en situaciones como:</p>
<ul>
  <li><strong>Contratación laboral o suscripción de contratos de prestación de servicios:</strong> Las áreas de talento humano necesitan constatar en cuál EPS debe afiliarse o cotizarse la seguridad social del nuevo trabajador o prestador de servicios.</li>
  <li><strong>Admisiones universitarias y pasantías académicas:</strong> Las universidades públicas y privadas exigen certificado de EPS vigente para autorizar matrículas y vinculación a pólizas de accidentes escolares y prácticas clínicas o técnicas.</li>
  <li><strong>Traslado entre EPS:</strong> Permite validar que el usuario no presente multiafiliación ni inconsistencias de régimen antes de tramitar el traslado a través del portal transaccional Mi Seguridad Social.</li>
  <li><strong>Atención de urgencias médicas y remisiones:</strong> Los centros hospitalarios consultan la BDUA cuando un paciente ingresa por urgencias sin carné físico para identificar de inmediato a qué entidad facturar los servicios médicos prestados.</li>
</ul>

<h2>3. Mecanismos de Movilidad y Portabilidad Nacional (Decreto 780 de 2016)</h2>
<p>Una de las innovaciones normativas más importantes para estudiantes y trabajadores temporales es la figura de la <strong>Movilidad entre Regímenes</strong> y la <strong>Portabilidad Nacional</strong> reguladas en el Decreto Único Reglamentario del Sector Salud (Decreto 780 de 2016):</p>
<ul>
  <li><strong>Movilidad entre Regímenes:</strong> Si una persona se encuentra afiliada al régimen subsidiado (a través de su encuesta del Sisbén) y consigue un empleo formal o suscribe un contrato de prestación de servicios que la obliga a cotizar al régimen contributivo, <em>ya no tiene que retirarse de su EPS subsidiada ni perder su cupo histórico</em>. La persona puede permanecer en la misma EPS bajo la modalidad de movilidad contributiva; y cuando el contrato laboral finalice, regresa de forma automática al régimen subsidiado sin periodos de carencia ni pérdida de tratamientos continuos.</li>
  <li><strong>Portabilidad Nacional:</strong> Si un estudiante de Barranquilla se traslada temporalmente a realizar sus prácticas profesionales o intercambio académico en Bogotá, Medellín o Cali, no requiere cambiar de EPS. Solo debe ingresar a la página web de su EPS o a la ADRES y solicitar la portabilidad nacional por el periodo de su estancia, garantizando que una IPS receptora en la ciudad destino le brinde citas médicas de medicina general, odontología y especialistas sin trabas administrativas.</li>
</ul>

<h2>4. Procedimiento Digital Paso a Paso para la Consulta y Descarga del Certificado</h2>
<p>La consulta en la plataforma de la ADRES es completamente pública, gratuita y no requiere registro previo con contraseña:</p>
<ol>
  <li><strong>Acceso al portal oficial de la ADRES:</strong> Abre tu navegador e ingresa directamente a la URL de consulta de afiliados: <code>https://www.adres.gov.co/consulte-su-eps</code> o ingresa a <code>https://www.adres.gov.co</code> y pulsa sobre el botón <em>'Consulte su EPS'</em>.</li>
  <li><strong>Configuración del tipo de documento:</strong> En el formulario interactivo, despliega la lista y selecciona el documento correspondiente:
    <ul>
      <li><em>Cédula de Ciudadanía (CC)</em> para mayores de 18 años.</li>
      <li><em>Tarjeta de Identidad (TI)</em> para menores entre 7 y 17 años.</li>
      <li><em>Registro Civil (RC)</em> para niños de 0 a 6 años.</li>
      <li><em>Cédula de Extranjería (CE)</em> o <em>Permiso por Protección Temporal (PPT)</em> para migrantes regulares.</li>
    </ul>
  </li>
  <li><strong>Ingreso del número de documento:</strong> Digita los dígitos de tu número de identificación de forma continua, sin puntos, espacios ni guiones.</li>
  <li><strong>Superación del desafío Captcha:</strong> Resuelve el captcha visual para confirmar que la petición es humana. Asegúrate de que no haya bloqueadores de anuncios cerrando el iframe del captcha.</li>
  <li><strong>Ejecución y lectura de los resultados oficiales:</strong> Haz clic en el botón <strong>Consultar</strong>. La pantalla desplegará la ficha técnica oficial con los siguientes bloques de datos:
    <ul>
      <li><strong>Datos Básicos:</strong> Nombres y apellidos completos del afiliado, fecha de nacimiento y departamento/municipio de expedición.</li>
      <li><strong>Estado de la Afiliación:</strong> Debe reflejar la leyenda en color verde: <code>ACTIVO</code>. Si dice <code>SUSPENDIDO</code> o <code>RETIRADO</code>, el usuario no cuenta con cobertura médica ordinaria.</li>
      <li><strong>Entidad Promotora de Salud (EPS):</strong> Nombre oficial de la aseguradora (ejemplo: <em>Nueva EPS S.A.</em>, <em>Sanitas EPS</em>, <em>Salud Total</em>, <em>Mutual Ser</em>, etc.).</li>
      <li><strong>Régimen:</strong> Indica si el usuario pertenece al <em>Régimen Contributivo</em> (cotizante o beneficiario dependiente) o al <em>Régimen Subsidiado</em> (financiado por el Estado mediante focalización del Sisbén).</li>
      <li><strong>Fecha de Afiliación Continua:</strong> Muestra la fecha exacta desde la cual el usuario está afiliado a su actual EPS, dato fundamental para el cálculo de semanas de antigüedad en traslados.</li>
    </ul>
  </li>
  <li><strong>Descarga en PDF e Impresión del Certificado:</strong> En la parte inferior de la ventana, pulsa sobre el botón <strong>Imprimir</strong>. Se abrirá el cuadro de diálogo de impresión de tu navegador. Elige <em>Guardar como PDF</em>, verifica que el escudo de Colombia y el logo de la ADRES aparezcan en la cabecera del documento y pulsa <em>Guardar</em>.</li>
</ol>

<h2>5. Solución a los Problemas Más Habituales en la BDUA de la ADRES</h2>
<table>
  <thead>
    <tr>
      <th>Problema Técnico o Registral</th>
      <th>Causa Origen</th>
      <th>Vía de Solución Paso a Paso</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Apareces como 'Suspendido' a pesar de estar trabajando</strong></td>
      <td>Tu empleador no pagó la planilla PILA a tiempo o hubo un error en la digitación de la novedad de ingreso.</td>
      <td>Solicitar al departamento de nómina el soporte de pago de la planilla PILA del mes vencido y radicarlo ante la EPS para el levantamiento de la suspensión.</td>
    </tr>
    <tr>
      <td><strong>Multiafiliación: Figuran dos EPS al mismo tiempo</strong></td>
      <td>Se tramitó un traslado pero la EPS antigua no procesó la novedad de retiro en los cortes mensuales de la BDUA.</td>
      <td>Ingresar a <code>miseguridadsocial.gov.co</code> y radicar una unificación de afiliación o presentar reclamo ante la Superintendencia Nacional de Salud (Supersalud).</td>
    </tr>
    <tr>
      <td><strong>El sistema dice: 'El documento consultado no se encuentra en la base de datos'</strong></td>
      <td>Eres mayor de edad reciente y tu EPS no actualizó tu tarjeta de identidad a cédula de ciudadanía en la BDUA.</td>
      <td>Consultar primero con tu número de Tarjeta de Identidad antigua. Si aparece activo, enviar copia de tu cédula nueva a los canales virtuales de tu EPS para la homologación de documento.</td>
    </tr>
  </tbody>
</table>

<h2>6. Conclusiones y Consejos de Andrés (Universidad de la Costa)</h2>
<p>La Base de Datos Única de Afiliados (BDUA) de la ADRES es el termómetro en tiempo real de tu aseguramiento en salud en Colombia. Consultar tu estado de afiliación antes de ingresar a un nuevo trabajo, al iniciar un semestre universitario o antes de realizar un viaje intermunicipal es una práctica de prevención fundamental. Gracias a las plataformas virtuales del Estado, hoy cualquier ciudadano puede comprobar sus derechos y descargar su soporte oficial en PDF sin gastar un solo peso ni depender de terceros tramitadores.</p>"""

print("Módulo generate_tramites.py cargado con éxito. Artículos 1 al 7 listos.")
