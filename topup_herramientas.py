# -*- coding: utf-8 -*-
"""
Top-up para artículos 20 a 26 para que TODOS superen estrictamente las 1.550 palabras.
"""

EXTRA_20 = r"""
<h2>12. Desactivación de Seguridad Basada en Virtualización (VBS) en Equipos Modestos</h2>
<p>En procesadores de gama de entrada o media (como Core i3/i5 o Ryzen 3/5 de generaciones anteriores), una de las funciones de Windows 11 que más penaliza el rendimiento en compilación de código y emuladores es la <strong>Seguridad basada en virtualización (VBS)</strong> y la <strong>Integridad de memoria (HVCI / Core Isolation)</strong>. Esta característica ejecuta el kernel de Windows dentro de un contenedor seguro aislado, lo cual es excelente para defensa contra malware corporativo, pero impone una degradación de rendimiento de entre el 8% y el 15% en operaciones de CPU intensivas.</p>
<p>Si utilizas tu equipo para desarrollo universitario y deseas exprimir cada ciclo de reloj disponible, puedes abrir la aplicación <em>Seguridad de Windows &gt; Seguridad del dispositivo &gt; Detalles de aislamiento del núcleo</em> y desactivar la casilla <strong>Integridad de memoria</strong>. Tras reiniciar el equipo, notarás una respuesta mucho más ágil en compiladores de C++, intérpretes de Python y emuladores móviles de Android.</p>
"""

EXTRA_21 = r"""
<h2>11. Inicialización de Systemd y Gestión de Daemons en Segundo Plano</h2>
<p>En versiones anteriores de WSL, una de las mayores limitaciones era la ausencia de <strong>systemd</strong> como sistema de inicialización PID 1, lo cual obligaba a iniciar servicios como PostgreSQL, MySQL o Nginx mediante comandos arcaicos de <code>service start</code> o scripts manuales en <code>.bashrc</code>.</p>
<p>En Ubuntu 24.04 LTS bajo Windows 11, systemd viene completamente integrado y activado. Puedes verificarlo ejecutando <code>systemctl status</code>. Ahora puedes habilitar demonios para que se inicien automáticamente al abrir la terminal (por ejemplo, <code>sudo systemctl enable docker</code> o <code>sudo systemctl enable postgresql</code>), replicando con una fidelidad del 100% el comportamiento de un servidor productivo en la nube.</p>
<p>Además, al configurar el modo de red en espejo (<code>networkingMode=mirrored</code> en <code>.wslconfig</code>), cualquier servidor web que levantes en Ubuntu en el puerto 8000 o 3000 estará accesible de inmediato en Windows escribiendo simplemente <code>http://localhost:8000</code> en Chrome, sin necesidad de averiguar la IP virtual interna de Hyper-V ni configurar complejas reglas de reenvío de puertos.</p>
"""

EXTRA_22 = r"""
<h2>10. Automatización de Calidad con Git Hooks y Pre-commit</h2>
<p>En entornos de desarrollo profesionales, subir código mal formateado o con errores de sintaxis al repositorio remoto es una falta de rigor inadmisible. Para automatizar la auditoría de calidad antes de que un commit sea consolidado, Git dispone del sistema de <strong>Hooks (Ganchos de ciclo de vida)</strong> en la carpeta <code>.git/hooks/</code>.</p>
<p>Podemos instalar la herramienta de software libre <code>pre-commit</code> mediante <code>pip install pre-commit</code> y definir en la raíz del proyecto un archivo <code>.pre-commit-config.yaml</code>:</p>
<pre><code>repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.3.0
    hooks:
      - id: ruff
        args: [ --fix ]
      - id: ruff-format
</code></pre>
<p>Al ejecutar <code>pre-commit install</code>, cada vez que intentes realizar un <code>git commit</code>, Git ejecutará automáticamente el linter y formateador Ruff. Si encuentra algún error de importación o violación de estilo, rechazará el commit y corregirá los archivos automáticamente, garantizando que el historial del repositorio compartido permanezca siempre con calidad de producción.</p>
"""

EXTRA_23 = r"""
<h2>10. Gestión de Múltiples Versiones de Python con Pyenv</h2>
<p>En el transcurso de una carrera de ingeniería o en el trabajo con diferentes clientes, es habitual tener que trabajar en proyectos antiguos desarrollados en Python 3.9 junto con desarrollos modernos que aprovechan las optimizaciones de velocidad de Python 3.12 o 3.13. Instalar múltiples versiones del intérprete directamente sobre el sistema operativo suele generar conflictos graves en el PATH de Windows o Linux.</p>
<p>La solución estándar de la industria es utilizar <strong>pyenv</strong> (o <em>pyenv-win</em> en Windows). Pyenv permite descargar y compilar cualquier versión específica de Python en tu carpeta de usuario y alternar entre ellas con un simple comando de consola (<code>pyenv local 3.11.8</code>). Al abrir la carpeta del proyecto en VS Code, la extensión de Python reconocerá de inmediato el intérprete de pyenv seleccionado, garantizando compatibilidad absoluta de librerías y dependencias sin alterar la instalación global del sistema.</p>

<h2>11. Atajos de Teclado Productivos y Multi-Cursor para Edición Masiva</h2>
<p>Dominar los atajos de teclado en Visual Studio Code reduce en decenas de horas el tiempo necesario para programar y refactorizar código:</p>
<ul>
  <li><code>Alt + Clic</code> o <code>Ctrl + Alt + Flecha Arriba/Abajo</code>: Agrega múltiples cursores verticales, permitiendo editar 20 variables simultáneamente en diferentes líneas.</li>
  <li><code>Ctrl + D</code>: Selecciona la siguiente coincidencia de la palabra actual bajo el cursor para renombrado rápido en el archivo.</li>
  <li><code>Shift + Alt + Flecha Arriba/Abajo</code>: Duplica la línea actual instantáneamente sin usar Ctrl+C / Ctrl+V.</li>
  <li><code>Ctrl + Shift + O</code>: Abre la paleta de símbolos del archivo actual, permitiendo saltar a cualquier clase, método o función escribiendo las primeras letras del nombre.</li>
</ul>
"""

EXTRA_24 = r"""
<h2>9. Personalización Visual Completa con Temas GRUB2 en Alta Definición</h2>
<p>A diferencia de los instaladores USB tradicionales con interfaces de texto rudimentarias en modo DOS, el menú de arranque de Ventoy se basa en el gestor de arranque <strong>GRUB2</strong>. Esto permite personalizar por completo la apariencia gráfica de la pantalla de bienvenida:</p>
<ol>
  <li>Descarga un tema compatible con GRUB2 (por ejemplo, desde <em>gnome-look.org</em> en la categoría GRUB Themes).</li>
  <li>Descomprime la carpeta del tema dentro de <code>/ventoy/theme/</code> en la partición principal de tu memoria USB.</li>
  <li>En el archivo <code>ventoy.json</code>, configura la ruta del archivo de estilo tipográfico y la resolución de pantalla nativa (por ejemplo: <code>1920x1080</code>):
    <pre><code>{
  "theme": {
    "file": "/ventoy/theme/elegance/theme.txt",
    "gfxmode": "1920x1080"
  }
}
</code></pre>
  </li>
</ol>
<p>Al encender la computadora, Ventoy se desplegará con un elegante fondo institucional, logotipos vectoriales de cada distribución reconocida automáticamente (el logo de Windows para instaladores de Microsoft, el pingüino de Tux para Linux y el camaleón para openSUSE) y tipografías nítidas en alta definición.</p>

<h2>10. Instalaciones Desatendidas Automatizadas con XML y Kickstart</h2>
<p>Para administradores de sistemas que deben formatear e instalar Windows o Linux en aulas completas de computadoras, Ventoy soporta <strong>instalaciones desatendidas (Unattended Installation)</strong>. Mediante una plantilla XML (<code>autounattend.xml</code>) vinculada en <code>ventoy.json</code>, el instalador de Windows se encarga automáticamente de particionar el disco duro, crear la cuenta de usuario local predeterminada, configurar la zona horaria de Colombia e instalar controladores sin que el técnico tenga que pulsar un solo botón durante el proceso de bienvenida.</p>
"""

EXTRA_25 = r"""
<h2>10. Contenedores Multicuenta en Firefox para Separar Trabajo y Estudio</h2>
<p>Uno de los mayores dolores de cabeza para estudiantes y profesionales que manejan múltiples correos electrónicos de Google, plataformas académicas de Moodle y cuentas de clientes es tener que abrir ventanas de incógnito o navegadores secundarios para no mezclar sesiones.</p>
<p>Mozilla Firefox soluciona esto de raíz con su función nativa de <strong>Contenedores Multicuenta (Firefox Multi-Account Containers)</strong>. Esta tecnología aísla las cookies, la memoria local de almacenamiento y las sesiones de autenticación en pestañas codificadas por colores (por ejemplo: <em>Contenedor Azul para Universidad CUC</em>, <em>Contenedor Naranja para Trabajo Freelance</em> y <em>Contenedor Verde para Finanzas Personales</em>). Puedes tener abierta simultáneamente la misma página con tres usuarios diferentes en pestañas contiguas dentro de una sola ventana, ahorrando gigabytes de memoria RAM frente al uso de múltiples navegadores pesados.</p>

<h2>11. Auditoría de Extensiones Vampiro y Limpieza de Caché de Renderizado</h2>
<p>Con el paso de los meses, navegadores como Chrome acumulan gigabytes de archivos temporales en <code>Service Worker/CacheStorage</code> y extensiones que inyectan scripts en cada página web abierta. Realizar un mantenimiento trimestral eliminando extensiones innecesarias y borrando la caché de sombreadores de la GPU (GPU Shader Cache) restaura la fluidez de respuesta del navegador a su velocidad de primer día.</p>
"""

EXTRA_26 = r"""
<h2>11. Detección de Cambios en Tiempo Real con Inotifywait</h2>
<p>Aunque programar tareas periódicas con crontab a las 2:00 AM es excelente para respaldos nocturnos, en proyectos de código críticos donde un corte de energía imprevisto puede destruir el trabajo de la última hora, esperar a la noche es un riesgo inaceptable. En sistemas Linux y WSL 2, podemos combinar <code>rsync</code> con la herramienta de eventos del kernel <strong>inotifywait</strong>:</p>
<pre><code>#!/bin/bash
# Monitoreo continuo de eventos del sistema de archivos
inotifywait -m -r -e modify,create,delete /home/andres/proyectos | while read -r direct evento archivo; do
    echo "[*] Cambio detectado en $archivo ($evento). Sincronizando..."
    rsync -avq --delete /home/andres/proyectos/ /mnt/backup_local/proyectos/
done
</code></pre>
<p>Este script se ejecuta en segundo plano como un demonio silencioso: en el instante exacto en que guardas un archivo en VS Code o compilas una nueva versión, el kernel de Linux emite un evento y rsync transmite la modificación al disco de respaldo en menos de 100 milisegundos sin consumir CPU en reposo.</p>

<h2>12. Cifrado Asimétrico con GPG antes de la Sincronización Remota</h2>
<p>Si la copia de seguridad se va a almacenar en un servidor remoto de terceros o en una cuenta de almacenamiento compartida en la nube, es una buena práctica de ciberseguridad cifrar los archivos comprimidos mediante <strong>GPG (GNU Privacy Guard)</strong> utilizando cifrado simétrico AES-256 antes de la transferencia. De este modo, incluso si el servidor remoto sufriera una filtración de seguridad, tus códigos fuente, credenciales de bases de datos y documentos personales permanecerán matemáticamente impenetrables.</p>
"""

with open('generate_herramientas.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Insert the extra sections before the conclusion in each article
# Article 20
text = text.replace(
    r'<h2>11. Conclusiones y Recomendaciones de Andrés (Universidad de la Costa)</h2>',
    EXTRA_20 + '\n<h2>13. Conclusiones y Recomendaciones de Andrés (Universidad de la Costa)</h2>'
)

# Article 21
text = text.replace(
    r'<h2>10. Conclusiones y Consejos de Andrés (Universidad de la Costa)</h2>',
    EXTRA_21 + '\n<h2>12. Conclusiones y Consejos de Andrés (Universidad de la Costa)</h2>'
)

# Article 22
text = text.replace(
    r'<h2>9. Conclusiones y Consejos de Andrés (Universidad de la Costa)</h2>',
    EXTRA_22 + '\n<h2>11. Conclusiones y Consejos de Andrés (Universidad de la Costa)</h2>'
)

# Article 23
text = text.replace(
    r'<h2>9. Conclusiones y Recomendaciones de Andrés (Universidad de la Costa)</h2>',
    EXTRA_23 + '\n<h2>12. Conclusiones y Recomendaciones de Andrés (Universidad de la Costa)</h2>'
)

# Article 24
text = text.replace(
    r'<h2>8. Conclusiones y Valoración de Andrés (Universidad de la Costa)</h2>',
    EXTRA_24 + '\n<h2>11. Conclusiones y Valoración de Andrés (Universidad de la Costa)</h2>'
)

# Article 25
text = text.replace(
    r'<h2>9. Conclusiones y Recomendaciones de Andrés (Universidad de la Costa)</h2>',
    EXTRA_25 + '\n<h2>12. Conclusiones y Recomendaciones de Andrés (Universidad de la Costa)</h2>'
)

# Article 26
text = text.replace(
    r'<h2>10. Conclusiones y Recomendaciones de Andrés (Universidad de la Costa)</h2>',
    EXTRA_26 + '\n<h2>13. Conclusiones y Recomendaciones de Andrés (Universidad de la Costa)</h2>'
)

with open('generate_herramientas.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("generate_herramientas.py successfully expanded with rich extra sections!")
