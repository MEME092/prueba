# -*- coding: utf-8 -*-
with open('generate_herramientas.py', 'r', encoding='utf-8') as f:
    text = f.read()

EXTRA_23_B = r"""
<h2>12. Perfilado de Rendimiento de Código con cProfile y SnakeViz</h2>
<p>Cuando un algoritmo en Python tarda varios segundos en completarse y necesitas optimizar su tiempo de ejecución, adivinar qué función es el cuello de botella suele ser un error. VS Code permite integrar el generador de perfiles estándar de Python <code>cProfile</code> junto con el visualizador interactivo <strong>SnakeViz</strong>:</p>
<pre><code># Instalar el analizador gráfico de llamadas
pip install snakeviz

# Ejecutar el perfilado del script principal
python -m cProfile -o programa.prof main.py

# Visualizar el diagrama de rayos solares y llamadas en el navegador
snakeviz programa.prof
</code></pre>
<p>SnakeViz desplegará en tu navegador un diagrama visual interactivo que desglosa el número exacto de llamadas y el tiempo acumulado en microsegundos de cada función, permitiéndote identificar con precisión matemática qué bucle o consulta de base de datos requiere optimización algorítmica.</p>
"""

EXTRA_24_B = r"""
<h2>11. Soporte para Arranque por Red Local PXE e iPXE con Ventoy</h2>
<p>Para laboratorios universitarios o salas de cómputo donde no se desea conectar físicamente una memoria USB a cada computadora, Ventoy incluye el revolucionario plugin <strong>Ventoy Server (iPXE)</strong>. Al ejecutar el servidor Ventoy en una máquina conectada a la red de área local (LAN), cualquier computadora configurada para arrancar desde la tarjeta de red (Wake-on-LAN / Network Boot PXE) cargará el menú interactivo de Ventoy a través del cable Ethernet a velocidad Gigabit, permitiendo instalar sistemas operativos en simultáneo sobre decenas de terminales de forma automatizada y sin moverte de tu escritorio.</p>
"""

text = text.replace(
    r'<h2>12. Conclusiones y Recomendaciones de Andrés (Universidad de la Costa)</h2>',
    EXTRA_23_B + '\n<h2>13. Conclusiones y Recomendaciones de Andrés (Universidad de la Costa)</h2>',
    1 # Only first match for article 23
)

text = text.replace(
    r'<h2>11. Conclusiones y Valoración de Andrés (Universidad de la Costa)</h2>',
    EXTRA_24_B + '\n<h2>12. Conclusiones y Valoración de Andrés (Universidad de la Costa)</h2>',
    1 # Only first match for article 24
)

with open('generate_herramientas.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated articles 23 and 24!")
