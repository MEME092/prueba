# -*- coding: utf-8 -*-
"""
Módulo de generación de contenido exhaustivo (+1.500 palabras) para Python & Flet.
Artículos 8 al 13.
"""

PYTHON_FLET_CONTENT = {}

PYTHON_FLET_CONTENT[8] = """<h2>1. Introducción al Ecosistema de Flet y su Filosofía de Desarrollo</h2>
<p>El desarrollo de software multiplataforma ha experimentado una profunda evolución en la última década. Tradicionalmente, los ingenieros debían mantener bases de código separadas escritas en lenguajes distintos para satisfacer a usuarios de escritorio en Windows, macOS o Linux, y a usuarios móviles en Android e iOS. Si bien frameworks como Flutter revolucionaron este paradigma al permitir unificar el renderizado gráfico mediante el motor Skia / Impeller, exigían aprender Dart, un lenguaje con menor adopción en el ecosistema científico y de datos.</p>
<p>Aquí es donde irrumpe <strong>Flet</strong> (creado por Feodor Fitsner). Flet es un framework reactivo que construye un puente bidireccional de alto rendimiento entre la elegancia y versatilidad de <strong>Python</strong> y la potencia gráfica del motor de <strong>Flutter</strong>. En lugar de compilar Python directamente a código nativo de máquina, la aplicación Python se comunica mediante sockets locales y protocolos binarios de serialización JSON con un cliente Flutter en segundo plano, logrando interfaces que se ejecutan a 60 fotogramas por segundo con soporte nativo para animaciones, temas dinámicos y componentes de Material Design 3 sin requerir una sola línea de Dart o JavaScript.</p>
<p>Para estudiantes de ingeniería de sistemas y desarrolladores independientes, Flet representa la navaja suiza perfecta: permite crear desde herramientas de administración interna y dashboards analíticos hasta completas aplicaciones empresariales con persistencia de datos local garantizada.</p>

<h2>2. El Problema del Código Espagueti y la Necesidad de un Patrón Arquitectónico</h2>
<p>La inmensa mayoría de los tutoriales introductorios de Flet cometen un error pedagógico grave: colocan toda la lógica de negocio, las sentencias SQL y la creación de widgets visuales dentro de una única función gigante <code>def main(page: ft.Page):</code>. A este antipatrón se le conoce en la industria como 'Código Espagueti' o arquitectura de 'Smart UI'.</p>
<p>Cuando la aplicación crece más allá de 500 líneas de código, este esquema colapsa:</p>
<ul>
  <li>Modificar una columna en la base de datos obliga a editar decenas de componentes de interfaz.</li>
  <li>Es imposible escribir pruebas unitarias automatizadas (unit tests) sin levantar toda la ventana gráfica.</li>
  <li>Las operaciones bloqueantes de entrada y salida (I/O) congelan el hilo principal de la interfaz de usuario (UI Thread), degradando la experiencia del usuario.</li>
</ul>
<p>Para construir software mantenible y escalable, implementaremos el patrón de arquitectura desacoplada <strong>MVC (Modelo - Vista - Controlador)</strong> complementado con el patrón <strong>Repository</strong> para la persistencia transaccional en SQLite.</p>

<h2>3. Diseño de la Base de Datos SQLite y Principios ACID</h2>
<p>SQLite es el motor de base de datos relacional más embebido y probado del planeta. A diferencia de clientes-servidores como PostgreSQL o MySQL, SQLite almacena toda la estructura tabular y los índices en un único archivo físico en disco (<code>app_database.db</code>). En aplicaciones de escritorio y móviles, ofrece velocidad de microsegundos y pleno cumplimiento de los principios ACID (Atomicidad, Consistencia, Aislamiento y Durabilidad).</p>
<p>En entornos multihilo como Flet, debemos gestionar cuidadosamente la concurrencia: SQLite permite múltiples lectores simultáneos mediante el modo WAL (Write-Ahead Logging), pero bloquea la base de datos durante operaciones de escritura concurrentes. Por ello, diseñaremos una capa de conexión que encapsule las transacciones mediante manejadores de contexto (<code>with sqlite3.connect(...) as conn:</code>).</p>

<h2>4. Estructura de Directorios del Proyecto Profesional</h2>
<p>Organizamos el proyecto siguiendo la separación estricta de responsabilidades:</p>
<pre><code>mi_proyecto_flet/
├── app_database.db
├── main.py
├── config.py
├── models/
│   ├── __init__.py
│   └── task_model.py
├── repositories/
│   ├── __init__.py
│   └── task_repository.py
├── controllers/
│   ├── __init__.py
│   └── task_controller.py
└── views/
    ├── __init__.py
    ├── components/
    │   └── task_card.py
    └── task_view.py</code></pre>

<h2>5. Implementación del Patrón Repository con SQLite</h2>
<p>Comenzamos definiendo el Modelo de Datos utilizando la librería nativa <code>dataclasses</code> de Python para garantizar tipado estricto:</p>
<pre><code>from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Task:
    id: Optional[int]
    title: str
    description: str
    is_completed: bool
    created_at: str = datetime.now().isoformat()
</code></pre>
<p>A continuación, construimos la clase <code>TaskRepository</code> encargada exclusivamente de ejecutar las consultas SQL mediante sentencias parametrizadas seguras para prevenir ataques de inyección SQL (SQL Injection):</p>
<pre><code>import sqlite3
from typing import List, Optional
from models.task_model import Task

class TaskRepository:
    def __init__(self, db_path: str = "app_database.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    is_completed BOOLEAN NOT NULL CHECK (is_completed IN (0, 1)),
                    created_at TEXT NOT NULL
                )
            ''')
            conn.commit()

    def get_all(self) -> List[Task]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, title, description, is_completed, created_at FROM tasks ORDER BY id DESC")
            rows = cursor.fetchall()
            return [Task(id=r[0], title=r[1], description=r[2], is_completed=bool(r[3]), created_at=r[4]) for r in rows]

    def create(self, task: Task) -> int:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO tasks (title, description, is_completed, created_at) VALUES (?, ?, ?, ?)",
                (task.title, task.description, int(task.is_completed), task.created_at)
            )
            conn.commit()
            return cursor.lastrowid

    def update_status(self, task_id: int, is_completed: bool):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE tasks SET is_completed = ? WHERE id = ?", (int(is_completed), task_id))
            conn.commit()

    def delete(self, task_id: int):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            conn.commit()
</code></pre>

<h2>6. Creación de la Capa de Control y Gestión de Eventos</h2>
<p>El Controlador conecta la Vista con el Repositorio, desacoplando los componentes visuales de la base de datos física:</p>
<pre><code>from typing import List, Callable
from models.task_model import Task
from repositories.task_repository import TaskRepository

class TaskController:
    def __init__(self, repository: TaskRepository):
        self.repository = repository
        self.listeners: List[Callable] = []

    def register_listener(self, listener: Callable):
        self.listeners.append(listener)

    def notify_changes(self):
        for listener in self.listeners:
            listener()

    def load_tasks(self) -> List[Task]:
        return self.repository.get_all()

    def add_new_task(self, title: str, description: str):
        if not title.strip():
            raise ValueError("El título de la tarea no puede estar vacío.")
        new_task = Task(id=None, title=title.strip(), description=description.strip(), is_completed=False)
        self.repository.create(new_task)
        self.notify_changes()

    def toggle_task(self, task_id: int, current_status: bool):
        self.repository.update_status(task_id, not current_status)
        self.notify_changes()

    def remove_task(self, task_id: int):
        self.repository.delete(task_id)
        self.notify_changes()
</code></pre>

<h2>7. Construcción de la Vista Reactiva con Flet</h2>
<p>La vista solo se encarga de pintar widgets y despachar eventos al controlador. Observe cómo cada tarjeta de tarea reacciona limpiamente a los cambios de estado:</p>
<pre><code>import flet as ft
from controllers.task_controller import TaskController

class TaskView(ft.Container):
    def __init__(self, controller: TaskController, page: ft.Page):
        super().__init__()
        self.controller = controller
        self.page = page
        self.controller.register_listener(self.refresh_ui)

        self.txt_title = ft.TextField(label="Título de la tarea", expand=True)
        self.txt_desc = ft.TextField(label="Descripción detallada", expand=True)
        self.btn_add = ft.ElevatedButton("Guardar Tarea", icon=ft.Icons.ADD, on_click=self._on_add_clicked)
        self.tasks_column = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True, spacing=10)

        self.content = ft.Column(
            expand=True,
            controls=[
                ft.Text("Gestor de Tareas de Laboratorio", size=24, weight=ft.FontWeight.BOLD),
                ft.Row([self.txt_title, self.btn_add]),
                self.txt_desc,
                ft.Divider(),
                self.tasks_column
            ]
        )
        self.refresh_ui()

    def _on_add_clicked(self, e):
        try:
            self.controller.add_new_task(self.txt_title.value, self.txt_desc.value)
            self.txt_title.value = ""
            self.txt_desc.value = ""
            self.page.snack_bar = ft.SnackBar(ft.Text("Tarea registrada exitosamente en SQLite"))
            self.page.snack_bar.open = True
            self.page.update()
        except ValueError as err:
            self.page.snack_bar = ft.SnackBar(ft.Text(str(err)), bgcolor=ft.Colors.RED_700)
            self.page.snack_bar.open = True
            self.page.update()

    def refresh_ui(self):
        self.tasks_column.controls.clear()
        tasks = self.controller.load_tasks()
        for t in tasks:
            card = ft.Card(
                content=ft.Container(
                    padding=10,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Checkbox(
                                label=t.title,
                                value=t.is_completed,
                                on_change=lambda e, task_id=t.id, status=t.is_completed: self.controller.toggle_task(task_id, status)
                            ),
                            ft.IconButton(
                                icon=ft.Icons.DELETE_OUTLINE,
                                icon_color=ft.Colors.RED_400,
                                on_click=lambda e, task_id=t.id: self.controller.remove_task(task_id)
                            )
                        ]
                    )
                )
            )
            self.tasks_column.controls.append(card)
        self.page.update()
</code></pre>

<h2>8. Configuración del Punto de Entrada y Pruebas en Hardware Real</h2>
<p>Finalmente, configuramos <code>main.py</code> para inicializar la aplicación con tema adaptativo:</p>
<pre><code>import flet as ft
from repositories.task_repository import TaskRepository
from controllers.task_controller import TaskController
from views.task_view import TaskView

def main(page: ft.Page):
    page.title = "Sistema de Gestión Técnica CUC"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 900
    page.window.height = 700
    page.window.min_width = 500
    page.window.min_height = 400

    repo = TaskRepository("app_database.db")
    controller = TaskController(repo)
    view = TaskView(controller, page)

    page.add(view)

if __name__ == "__main__":
    ft.app(target=main)
</code></pre>

<h2>9. Matriz de Diagnóstico y Errores Habituales en Flet</h2>
<table>
  <thead>
    <tr>
      <th>Error en Consola</th>
      <th>Causa Técnica</th>
      <th>Solución Paso a Paso</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>sqlite3.OperationalError: database is locked</code></td>
      <td>Conexiones huérfanas abiertas sin cerrar en múltiples hilos asíncronos.</td>
      <td>Usar siempre el context manager <code>with sqlite3.connect()</code> y habilitar el modo <code>PRAGMA journal_mode=WAL;</code>.</td>
    </tr>
    <tr>
      <td><code>AssertionError: Control is already added to another parent</code></td>
      <td>Intento de agregar la misma instancia de un control a dos contenedores distintos.</td>
      <td>Instanciar nuevos controles o clonar la definición antes de agregarlos al árbol visual de Flet.</td>
    </tr>
    <tr>
      <td><code>RuntimeError: Event loop is closed</code></td>
      <td>Llamadas a <code>page.update()</code> desde un hilo secundario sin sincronización adecuada.</td>
      <td>Utilizar <code>page.run_task(...)</code> para despachar tareas asíncronas seguras hacia el bucle de eventos.</td>
    </tr>
  </tbody>
</table>

<h2>10. Conclusiones del Autor (Andrés - Universidad de la Costa)</h2>
<p>La combinación de Python, Flet y SQLite ofrece un equilibrio inigualable entre velocidad de desarrollo y rendimiento nativo. Al estructurar tus aplicaciones mediante patrones sólidos como MVC y Repository, garantizas que tus proyectos de aula o soluciones para clientes reales puedan evolucionar sin reescrituras traumáticas. Te animamos a clonar esta arquitectura y utilizarla como base para tus proyectos universitarios y de software libre.</p>"""

PYTHON_FLET_CONTENT[9] = """<h2>1. La Importancia Crítica de la Seguridad Criptográfica en Aplicaciones Locales</h2>
<p>Uno de los errores más peligrosos y desafortunadamente comunes cometidos por desarrolladores novatos es almacenar contraseñas en texto plano o recurrir a algoritmos de hashing obsoletos y vulnerables como MD5 o SHA-1. En el contexto de aplicaciones de escritorio y móviles desarrolladas con Python y Flet, la base de datos SQLite reside físicamente en el dispositivo del usuario o en el almacenamiento interno del sistema operativo. Si un atacante tiene acceso físico al equipo o un malware extrae el archivo <code>.db</code>, cualquier contraseña no protegida adecuadamente queda expuesta de inmediato.</p>
<p>Para implementar un sistema de autenticación de nivel profesional, debemos utilizar funciones de derivación de claves criptográficamente lentas y robustas, diseñadas específicamente para resistir ataques de fuerza bruta y ataques basados en tablas arcoíris (Rainbow Tables) acelerados por tarjetas gráficas (GPU). En esta guía exhaustiva aprenderás a implementar el estándar de la industria <strong>bcrypt</strong> con generación dinámica de salpicaduras aleatorias (Salt) de factor de costo ajustable, integrándolo de manera fluida con SQLite y los mecanismos de almacenamiento seguro de sesiones de Flet.</p>

<h2>2. Fundamentos Matemáticos y Operativos del Algoritmo bcrypt</h2>
<p>Diseñado por Niels Provos y David Mazières en 1999 para el sistema operativo OpenBSD, bcrypt se basa en el cifrador por bloques <em>Blowfish</em> en su variante <em>Eksblowfish</em> (Exact Key Setup Blowfish). Lo que hace a bcrypt invulnerable ante ataques tradicionales es su característica de <strong>función de costo adaptable (Work Factor / Rounds)</strong>:</p>
<ul>
  <li><strong>La Sal (Salt):</strong> Es una cadena pseudoaleatoria de 16 bytes (codificada en 22 caracteres base64) generada por el sistema operativo mediante fuentes de entropía seguras (<code>/dev/urandom</code> en Linux/macOS o <code>CryptGenRandom</code> en Windows). La sal se combina con la contraseña antes del hashing, garantizando que dos usuarios con la misma contraseña tengan hashes completamente diferentes.</li>
  <li><strong>El Factor de Costo (Work Factor):</strong> Define el número de iteraciones exponenciales de la función de cifrado (2 elevado al costo). Por ejemplo, un factor de costo de 12 significa que el algoritmo ejecuta 4.096 iteraciones. Esto impone una penalización de cómputo calculada: mientras que para un usuario legítimo verificar una contraseña toma 250 milisegundos (imperceptible al hacer clic en 'Ingresar'), para un atacante que intente probar miles de millones de combinaciones por segundo el ataque se vuelve matemáticamente inviable.</li>
</ul>

<h2>3. Diseño del Esquema de Usuarios y Transacciones en SQLite</h2>
<p>Creamos una tabla de usuarios que almacena el hash completo generado por bcrypt (el cual incluye internamente el identificador de algoritmo <code>$2b$</code>, el factor de costo y la sal concatenada):</p>
<pre><code>CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP
);
</code></pre>

<h2>4. Implementación del Servicio de Seguridad Criptográfica</h2>
<p>Instalamos la librería oficial de bcrypt mediante <code>pip install bcrypt</code>. A continuación, construimos el módulo <code>security_service.py</code>:</p>
<pre><code>import bcrypt
from typing import Tuple

class SecurityService:
    @staticmethod
    def hash_password(plain_password: str, cost_rounds: int = 12) -> str:
        '''Genera un hash bcrypt seguro con sal aleatoria.'''
        if not plain_password or len(plain_password) < 8:
            raise ValueError("La contraseña debe contener un mínimo de 8 caracteres.")
        
        # Convertir contraseña a bytes en UTF-8
        password_bytes = plain_password.encode('utf-8')
        # Generar sal con factor de costo configurable
        salt = bcrypt.gensalt(rounds=cost_rounds)
        # Calcular el hash
        hashed_bytes = bcrypt.hashpw(password_bytes, salt)
        return hashed_bytes.decode('utf-8')

    @staticmethod
    def verify_password(plain_password: str, stored_hash: str) -> bool:
        '''Verifica en tiempo constante si la contraseña coincide con el hash almacenado.'''
        try:
            password_bytes = plain_password.encode('utf-8')
            hash_bytes = stored_hash.encode('utf-8')
            return bcrypt.checkpw(password_bytes, hash_bytes)
        except Exception:
            return False
</code></pre>

<h2>5. Repositorio de Usuarios con Manejo de Excepciones de Integridad</h2>
<p>El repositorio encapsula las operaciones de persistencia, capturando violaciones de unicidad cuando un nombre de usuario o correo electrónico ya existe:</p>
<pre><code>import sqlite3
from typing import Optional, Dict

class UserRepository:
    def __init__(self, db_path: str = "auth_demo.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    role TEXT NOT NULL DEFAULT 'user',
                    created_at TEXT NOT NULL
                )
            ''')
            conn.commit()

    def register_user(self, username: str, email: str, password_hash: str) -> bool:
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO users (username, email, password_hash, created_at) VALUES (?, ?, ?, datetime('now'))",
                    (username.lower().strip(), email.lower().strip(), password_hash)
                )
                conn.commit()
                return True
        except sqlite3.IntegrityError:
            return False

    def find_by_username(self, username: str) -> Optional[Dict]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, username, email, password_hash, role FROM users WHERE username = ? OR email = ?",
                (username.lower().strip(), username.lower().strip())
            )
            row = cursor.fetchone()
            if row:
                return {
                    "id": row[0],
                    "username": row[1],
                    "email": row[2],
                    "password_hash": row[3],
                    "role": row[4]
                }
            return None
</code></pre>

<h2>6. Persistencia de Sesión con Flet `client_storage`</h2>
<p>Uno de los retos clave en aplicaciones cliente es mantener la sesión activa cuando el usuario cierra y reabre la ventana. Flet proporciona la API <code>page.client_storage</code>, la cual almacena pares clave-valor cifrados en el almacén de configuración del sistema operativo (Windows Credential Locker / SharedPreferences en Android / Keychain en macOS).</p>
<pre><code># Guardar token o sesión tras login exitoso
page.client_storage.set("auth_session", {
    "user_id": user_data["id"],
    "username": user_data["username"],
    "role": user_data["role"]
})

# Leer sesión al arrancar la app
session = page.client_storage.get("auth_session")
if session:
    # Cargar directamente la vista principal
    show_dashboard(session["username"])
</code></pre>

<h2>7. Construcción de la Interfaz Gráfica de Login y Registro</h2>
<p>Diseñamos un formulario interactivo con validación de campos, animación de carga y mensajes de alerta mediante <code>ft.SnackBar</code>:</p>
<pre><code>import flet as ft
from security_service import SecurityService
from user_repository import UserRepository

class LoginApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.repo = UserRepository()
        self.page.title = "Acceso Seguro al Laboratorio CUC"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        # Controles de UI
        self.txt_username = ft.TextField(label="Usuario o Correo", width=340, prefix_icon=ft.Icons.PERSON)
        self.txt_password = ft.TextField(label="Contraseña", width=340, password=True, can_reveal_password=True, prefix_icon=ft.Icons.LOCK)
        self.prg_loader = ft.ProgressRing(visible=False, width=20, height=20)
        self.btn_login = ft.ElevatedButton("Iniciar Sesión", width=340, on_click=self._handle_login)
        self.btn_register = ft.TextButton("¿No tienes cuenta? Regístrate aquí", on_click=self._show_register_dialog)

        # Contenedor central tipo tarjeta flotante
        self.card = ft.Card(
            elevation=5,
            content=ft.Container(
                padding=35,
                content=ft.Column(
                    width=340,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(ft.Icons.SECURITY, size=50, color=ft.Colors.INDIGO_600),
                        ft.Text("Portal de Autenticación", size=20, weight=ft.FontWeight.BOLD),
                        ft.Text("Ingeniería de Sistemas - CUC", size=12, color=ft.Colors.GREY_600),
                        ft.Divider(height=25),
                        self.txt_username,
                        self.txt_password,
                        ft.Container(height=10),
                        ft.Row([self.btn_login, self.prg_loader], alignment=ft.MainAxisAlignment.CENTER),
                        self.btn_register
                    ]
                )
            )
        )
        self.page.add(self.card)

    def _handle_login(self, e):
        username = self.txt_username.value
        password = self.txt_password.value
        if not username or not password:
            self._notify("Por favor complete todos los campos obligatorios.", is_error=True)
            return

        self.prg_loader.visible = True
        self.btn_login.disabled = True
        self.page.update()

        # Buscar usuario en SQLite
        user = self.repo.find_by_username(username)
        if user and SecurityService.verify_password(password, user["password_hash"]):
            self.page.client_storage.set("auth_session", {"user_id": user["id"], "username": user["username"]})
            self._notify(f"¡Bienvenido de nuevo, {user['username']}!", is_error=False)
            self._show_dashboard(user["username"])
        else:
            self._notify("Credenciales inválidas. Compruebe su usuario o clave.", is_error=True)

        self.prg_loader.visible = False
        self.btn_login.disabled = False
        self.page.update()

    def _notify(self, message: str, is_error: bool = False):
        self.page.snack_bar = ft.SnackBar(
            ft.Text(message),
            bgcolor=ft.Colors.RED_700 if is_error else ft.Colors.GREEN_700
        )
        self.page.snack_bar.open = True
        self.page.update()

    def _show_dashboard(self, username: str):
        self.page.clean()
        self.page.add(
            ft.Column([
                ft.Text(f"Panel Principal de Ingeniería - Sesión: {username}", size=24, weight=ft.FontWeight.BOLD),
                ft.Text("Acceso autenticado mediante hash criptográfico bcrypt y base de datos SQLite.", size=14),
                ft.ElevatedButton("Cerrar Sesión", on_click=self._handle_logout)
            ])
        )

    def _handle_logout(self, e):
        self.page.client_storage.remove("auth_session")
        self.page.clean()
        self.page.add(self.card)

    def _show_register_dialog(self, e):
        # Diálogo modal para registrar nuevo usuario
        reg_user = ft.TextField(label="Nombre de Usuario")
        reg_email = ft.TextField(label="Correo Institucional")
        reg_pass = ft.TextField(label="Contraseña (mínimo 8 caracteres)", password=True, can_reveal_password=True)

        def do_register(ev):
            try:
                hashed = SecurityService.hash_password(reg_pass.value)
                success = self.repo.register_user(reg_user.value, reg_email.value, hashed)
                if success:
                    dlg.open = False
                    self._notify("Usuario registrado exitosamente. Ya puede iniciar sesión.")
                else:
                    self._notify("El nombre de usuario o correo ya se encuentra registrado.", is_error=True)
            except ValueError as err:
                self._notify(str(err), is_error=True)

        dlg = ft.AlertDialog(
            title=ft.Text("Registro de Nuevo Usuario"),
            content=ft.Column([reg_user, reg_email, reg_pass], tight=True),
            actions=[ft.TextButton("Cancelar", on_click=lambda ev: setattr(dlg, 'open', False) or self.page.update()),
                     ft.ElevatedButton("Crear Cuenta", on_click=do_register)]
        )
        self.page.dialog = dlg
        dlg.open = True
        self.page.update()
</code></pre>

<h2>8. Medidas de Blindaje contra Ataques de Fuerza Bruta y DoS</h2>
<p>Debido a que bcrypt es intencionalmente intensivo en CPU, un atacante automatizado podría saturar los núcleos de tu máquina enviando peticiones de autenticación masivas continuas. Para mitigar esta amenaza, recomendamos implementar:</p>
<ul>
  <li><strong>Límite de Intentos Fallidos (Rate Limiting):</strong> Llevar un contador de intentos fallidos por dirección IP o por identificador de usuario. Si se registran más de cinco intentos erróneos consecutivos en menos de diez minutos, bloquear temporalmente el formulario durante 15 minutos.</li>
  <li><strong>Despacho Asíncrono de Cómputo:</strong> Ejecutar la verificación de bcrypt fuera del hilo de renderizado utilizando el executor de hilos de Python (<code>asyncio.to_thread</code> o <code>concurrent.futures.ThreadPoolExecutor</code>) para que la interfaz gráfica nunca experimente tirones o congelamiento mientras se calcula la función criptográfica.</li>
</ul>

<h2>9. Conclusiones y Recomendaciones de Andrés (Universidad de la Costa)</h2>
<p>La seguridad no es un accesorio opcional que se añade al final de un proyecto; debe ser un pilar fundamental concebido desde la primera línea de código. Implementar bcrypt con un factor de costo adecuado y persistencia protegida en SQLite eleva cualquier desarrollo en Python Flet a estándares profesionales de ciberseguridad, asegurando la privacidad de las credenciales de tus usuarios en cualquier entorno operativo.</p>"""

PYTHON_FLET_CONTENT[10] = """<h2>1. Programación Concurrente y el Desafío del Bloqueo en Aplicaciones de Interfaz Gráfica</h2>
<p>En el desarrollo de software moderno, prácticamente cualquier aplicación debe interoperar con servicios en la nube: microservicios empresariales, pasarelas de pago, bases de datos remotas o APIs públicas del clima, divisas y datos abiertos de gobiernos. Sin embargo, en los entornos gráficos (GUI), la comunicación a través de redes introduce un desafío crítico: la <strong>latencia de red</strong>.</p>
<p>Cuando un programa ejecuta una solicitud HTTP síncrona tradicional utilizando librerías como <code>requests</code> o <code>urllib</code>, el hilo de ejecución se detiene por completo mientras espera la respuesta del servidor remoto (frecuentemente entre 200 milisegundos y varios segundos). Si esta llamada se realiza en el hilo principal de la interfaz de usuario de Flet, la ventana se congela por completo: las animaciones se detienen, los botones no responden al clic y el sistema operativo puede marcar la aplicación como 'No responde'.</p>
<p>Para resolver este problema de raíz, es imprescindible dominar el paradigma asíncrono no bloqueante mediante <strong>asyncio</strong> y la librería de alto rendimiento <strong>aiohttp</strong>, integrándola armoniosamente con el ciclo de vida reactivo de Flet.</p>

<h2>2. Comparativa Técnica: `requests` vs `aiohttp` en Arquitecturas Reactivas</h2>
<table>
  <thead>
    <tr>
      <th>Característica de Diseño</th>
      <th>Librería Clásica `requests`</th>
      <th>Librería Asíncrona `aiohttp`</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Modelo de Entrada/Salida</strong></td>
      <td>Bloqueante síncrono (I/O Blocking).</td>
      <td>No bloqueante basado en eventos (Event-Loop Async I/O).</td>
    </tr>
    <tr>
      <td><strong>Rendimiento bajo Concurrencia</strong></td>
      <td>Requiere crear un hilo del SO por cada petición (alto consumo de memoria).</td>
      <td>Gestiona miles de peticiones simultáneas sobre un único hilo mediante corrutinas.</td>
    </tr>
    <tr>
      <td><strong>Integración con Flet Async</strong></td>
      <td>Requiere encapsulamiento manual en <code>threading.Thread</code>.</td>
      <td>Nativa directa con <code>async def main(page: ft.Page):</code>.</td>
    </tr>
    <tr>
      <td><strong>Soporte para WebSockets y Streaming</strong></td>
      <td>Limitado y engorroso.</td>
      <td>Soporte nativo completo bidireccional.</td>
    </tr>
  </tbody>
</table>

<h2>3. Configuración del Entorno y Manejo de Sesiones HTTP Persistentes</h2>
<p>Para comenzar, instalamos la librería ejecutando en nuestra terminal: <code>pip install aiohttp</code>. En aplicaciones profesionales nunca debemos abrir y cerrar una nueva sesión TCP en cada llamada individual. La creación de handshakes TLS/SSL consume recursos innecesarios. Lo correcto es reutilizar un objeto <strong>ClientSession</strong> persistente a lo largo de toda la vida útil de la aplicación:</p>
<pre><code>import aiohttp
import asyncio
from typing import Optional, Dict, Any

class ApiService:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session: Optional[aiohttp.ClientSession] = None

    async def get_session(self) -> aiohttp.ClientSession:
        if self.session is None or self.session.closed:
            timeout = aiohttp.ClientTimeout(total=10, connect=3)
            self.session = aiohttp.ClientSession(timeout=timeout)
        return self.session

    async def close(self):
        if self.session and not self.session.closed:
            await self.session.close()
</code></pre>

<h2>4. Implementación de Peticiones Seguras con Manejo de Errores y Timeouts</h2>
<p>Añadimos métodos tipados para realizar consultas GET y envíos POST con reintentos y captura de fallos de red:</p>
<pre><code>    async def fetch_data(self, endpoint: str) -> Dict[str, Any]:
        session = await self.get_session()
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    raise aiohttp.ClientResponseError(
                        request_info=response.request_info,
                        history=response.history,
                        status=response.status,
                        message=f"Error HTTP del servidor: Código {response.status}"
                    )
        except asyncio.TimeoutError:
            raise TimeoutError("El servidor remoto tardó demasiado en responder (Timeout).")
        except aiohttp.ClientConnectorError:
            raise ConnectionError("No fue posible establecer conexión con el host. Verifique su red.")
</code></pre>

<h2>5. Construcción de una Interfaz Reactiva con Indicadores de Carga en Tiempo Real</h2>
<p>Diseñamos una vista en Flet que consulta una API REST pública mostrando un componente <code>ft.ProgressRing</code> mientras se descargan los datos:</p>
<pre><code>import flet as ft
import asyncio
from api_service import ApiService

async def main(page: ft.Page):
    page.title = "Consumo Asíncrono de APIs en Tiempo Real"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 30

    api = ApiService("https://jsonplaceholder.typicode.com")

    txt_search = ft.TextField(label="Filtrar por nombre o título", expand=True)
    loader = ft.ProgressRing(visible=False)
    results_list = ft.ListView(expand=True, spacing=10, padding=20)

    async def load_posts(e=None):
        loader.visible = True
        btn_refresh.disabled = True
        results_list.controls.clear()
        page.update()

        try:
            posts = await api.fetch_data("/posts")
            query = txt_search.value.lower() if txt_search.value else ""

            filtered_posts = [
                p for p in posts 
                if query in p["title"].lower() or query in p["body"].lower()
            ][:15]

            for post in filtered_posts:
                card = ft.Card(
                    elevation=2,
                    content=ft.Container(
                        padding=15,
                        content=ft.Column([
                            ft.Text(f"Post #{post['id']}: {post['title'].capitalize()}", weight=ft.FontWeight.BOLD, size=15),
                            ft.Text(post['body'], color=ft.Colors.GREY_700, size=12)
                        ])
                    )
                )
                results_list.controls.append(card)

            page.snack_bar = ft.SnackBar(ft.Text(f"Se cargaron {len(filtered_posts)} registros en tiempo real."))
            page.snack_bar.open = True

        except Exception as err:
            page.snack_bar = ft.SnackBar(ft.Text(str(err)), bgcolor=ft.Colors.RED_700)
            page.snack_bar.open = True

        finally:
            loader.visible = False
            btn_refresh.disabled = False
            page.update()

    btn_refresh = ft.ElevatedButton("Consultar API", icon=ft.Icons.CLOUD_DOWNLOAD, on_click=load_posts)
    txt_search.on_submit = load_posts

    page.add(
        ft.Column(
            expand=True,
            controls=[
                ft.Text("Monitor de Microservicios Asíncronos", size=22, weight=ft.FontWeight.BOLD),
                ft.Text("Demostración de I/O no bloqueante con aiohttp y Flet en Barranquilla.", size=12, color=ft.Colors.GREY_600),
                ft.Row([txt_search, btn_refresh, loader]),
                ft.Divider(),
                results_list
            ]
        )
    )

    await load_posts()

if __name__ == "__main__":
    ft.app(target=main)
</code></pre>

<h2>6. Autenticación con Tokens JWT y Rotación de Headers Bearer</h2>
<p>En arquitecturas empresariales seguras, los endpoints de la API están protegidos por tokens de autenticación JSON Web Tokens (JWT). Para integrar esta funcionalidad sin ensuciar la lógica de negocio, extendemos <code>ApiService</code> con un interceptor que inyecta automáticamente el encabezado <code>Authorization: Bearer &lt;token&gt;</code>:</p>
<pre><code>class AuthenticatedApiService(ApiService):
    def __init__(self, base_url: str):
        super().__init__(base_url)
        self.jwt_token: Optional[str] = None

    def set_auth_token(self, token: str):
        self.jwt_token = token

    async def get_session(self) -> aiohttp.ClientSession:
        session = await super().get_session()
        if self.jwt_token:
            session.headers["Authorization"] = f"Bearer {self.jwt_token}"
        return session
</code></pre>

<h2>7. Caché en Memoria con Política TTL (Time-To-Live)</h2>
<p>Para reducir el consumo de ancho de banda y evitar penalizaciones por exceder límites de tasa de peticiones (Rate Limiting), implementamos un sistema de caché asíncrono con expiración temporal:</p>
<pre><code>import time

class CacheEntry:
    def __init__(self, data: Any, ttl_seconds: int = 60):
        self.data = data
        self.expires_at = time.time() + ttl_seconds

    def is_valid(self) -> bool:
        return time.time() &lt; self.expires_at

class CachedApiService(ApiService):
    def __init__(self, base_url: str):
        super().__init__(base_url)
        self._cache: Dict[str, CacheEntry] = {}

    async def fetch_cached(self, endpoint: str, ttl: int = 60) -> Dict[str, Any]:
        if endpoint in self._cache and self._cache[endpoint].is_valid():
            return self._cache[endpoint].data

        data = await self.fetch_data(endpoint)
        self._cache[endpoint] = CacheEntry(data, ttl)
        return data
</code></pre>

<h2>8. Streaming Asíncrono de Respuestas Masivas</h2>
<p>Cuando consumimos archivos de gran tamaño (como exports CSV de miles de filas o imágenes de sensores), leer toda la respuesta en memoria mediante <code>response.read()</code> puede provocar errores de desbordamiento de memoria RAM (OOM). La solución elegante es consumir la respuesta en flujos de bloques (chunks):</p>
<pre><code>async def stream_download(self, endpoint: str, local_filepath: str, progress_callback=None):
    session = await self.get_session()
    url = f"{self.base_url}/{endpoint.lstrip('/')}"
    async with session.get(url) as resp:
        resp.raise_for_status()
        total_size = int(resp.headers.get('content-length', 0))
        downloaded = 0
        with open(local_filepath, 'wb') as fd:
            async for chunk in resp.content.iter_chunked(65536): # 64 KB por bloque
                fd.write(chunk)
                downloaded += len(chunk)
                if progress_callback and total_size &gt; 0:
                    progress_callback(downloaded / total_size)
</code></pre>

<h2>9. Patrón de Tareas de Fondo y Polling Asíncrono Periódico</h2>
<p>En muchos escenarios industriales (como telemetría de sensores IoT, monitoreo de transacciones financieras o sincronización de chats), la aplicación requiere consultar la API de forma periódica cada 10 o 30 segundos sin intervención manual. Con Flet y asyncio, esto se logra mediante una tarea de fondo (Background Task):</p>
<pre><code>async def background_polling_worker(api: ApiService, page: ft.Page, status_label: ft.Text):
    while True:
        try:
            status_data = await api.fetch_data("/health_check")
            status_label.value = f"Estado del Servidor: {status_data.get('status', 'OK')} • Ping: 42ms"
            status_label.color = ft.Colors.GREEN_600
        except Exception:
            status_label.value = "Estado del Servidor: Desconectado o Inaccesible"
            status_label.color = ft.Colors.RED_600
        page.update()
        await asyncio.sleep(15)
</code></pre>

<h2>10. Matriz de Errores Comunes y Pruebas de Resiliencia</h2>
<table>
  <thead>
    <tr>
      <th>Comportamiento Anómalo</th>
      <th>Causa Raíz</th>
      <th>Estrategia de Mitigación</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>ClientOSError: Can not write request body for [url]</code></td>
      <td>La conexión TCP fue cerrada abruptamente por el cortafuegos o proxy intermedio.</td>
      <td>Implementar política de reintentos exponenciales con jitter (biblioteca <code>tenacity</code> o bucle try/except manual).</td>
    </tr>
    <tr>
      <td>La interfaz se queda colgada a pesar de usar corrutinas</td>
      <td>Se mezcló una llamada síncrona dentro de la función async (ejemplo: <code>time.sleep()</code> o <code>requests.get()</code>).</td>
      <td>Reemplazar estrictamente <code>time.sleep</code> por <code>await asyncio.sleep</code> y usar siempre <code>aiohttp</code> para I/O.</td>
    </tr>
    <tr>
      <td>Fuga de descriptores de sockets (Socket Leaks)</td>
      <td>No cerrar la sesión de aiohttp cuando la ventana del usuario se destruye.</td>
      <td>Vincular el método <code>api.close()</code> al evento de desconexión <code>page.on_disconnect</code>.</td>
    </tr>
  </tbody>
</table>

<h2>11. Conclusiones y Valoración de Andrés (Universidad de la Costa)</h2>
<p>Dominar la programación asíncrona con aiohttp y Flet transforma radicalmente la calidad de tus aplicaciones. Tus usuarios percibirán una interfaz fluida, con respuestas inmediatas y sin congelamientos repentinos, incluso bajo redes inestables o servidores distantes. Este estándar de ingeniería es fundamental para cualquier estudiante que aspire a crear software moderno de clase mundial.</p>"""

PYTHON_FLET_CONTENT[11] = """<h2>1. La Relevancia de los Reportes Ejecutivos en el Software Empresarial</h2>
<p>En el mundo profesional y corporativo, una aplicación de software no está verdaderamente completa si no le permite al usuario exportar sus datos para compartirlos con la gerencia, contadores o clientes externos. Ya sea para emitir una orden de compra, un certificado académico, una factura de servicios profesionales o un consolidado de inventarios, dos formatos dominan de manera indiscutible la industria:</p>
<ul>
  <li><strong>El formato PDF (Portable Document Format):</strong> Es el estándar universal para documentos inmutables, diseñados para impresión física o visualización idéntica en cualquier pantalla. Requiere diseño vectorial exacto, membretes corporativos, paginación automática y márgenes milimétricos.</li>
  <li><strong>El formato Excel (.xlsx):</strong> Es el estándar para análisis de datos tabulares, auditorías contables y procesamiento numérico. Los usuarios esperan celdas formateadas con estilos de moneda, encabezados coloridos, filtros automáticos y fórmulas activas.</li>
</ul>
<p>En esta guía práctica integraremos las librerías líderes del ecosistema Python —<strong>ReportLab</strong> para la síntesis vectorial de PDFs y <strong>openpyxl</strong> para la manipulación avanzada de hojas de cálculo— directamente dentro de una interfaz reactiva construida en Flet utilizando el diálogo nativo de selección de archivos del sistema operativo (<code>ft.FilePicker</code>).</p>

<h2>2. Generación Vectorial de PDFs con ReportLab (Platypus Flowables)</h2>
<p>Muchos tutoriales cometen el error de usar primitivas de bajo nivel dibujando coordenadas absolutas (<code>canvas.drawString(x, y, text)</code>). Este enfoque es frágil: si el texto es un poco más largo de lo previsto, se desborda de la página sin saltar de línea automáticamente.</p>
<p>La forma profesional de programar en ReportLab es mediante <strong>PLATYPUS (Page Layout and Typography Using Scripts)</strong>. Platypus utiliza un paradigma de flujo dinámico (Flowables) donde los elementos (párrafos, tablas, imágenes, saltos de página) fluyen de forma adaptativa respetando márgenes y calculando los saltos de hoja de forma matemática:</p>
<pre><code>from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from typing import List, Dict

class PdfReportGenerator:
    @staticmethod
    def build_financial_report(output_filename: str, records: List[Dict]):
        doc = SimpleDocTemplate(
            output_filename,
            pagesize=letter,
            rightMargin=54,
            leftMargin=54,
            topMargin=54,
            bottomMargin=54
        )
        
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            name='ReportTitle',
            parent=styles['Heading1'],
            fontSize=18,
            leading=22,
            textColor=colors.HexColor("#1e293b"),
            spaceAfter=15
        )
        
        elements = []
        elements.append(Paragraph("Informe Consolidado de Laboratorio CUC", title_style))
        elements.append(Paragraph("Generado por el Módulo de Automatización en Barranquilla.", styles['Normal']))
        elements.append(Spacer(1, 20))
        
        table_data = [["ID", "Descripción del Módulo", "Estado de Pruebas", "Costo Estimado"]]
        for r in records:
            table_data.append([
                str(r["id"]),
                r["name"],
                r["status"],
                f"${r['cost']:,.2f}"
            ])
            
        t = Table(table_data, colWidths=[40, 240, 110, 110])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#4f46e5")),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('ALIGN', (3, 1), (3, -1), 'RIGHT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#f8fafc")),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#f1f5f9")])
        ]))
        
        elements.append(t)
        doc.build(elements)
</code></pre>

<h2>3. Gráficos Estadísticos Vectoriales Embebidos en ReportLab</h2>
<p>Para añadir valor analítico a los documentos PDF, ReportLab incluye un motor de gráficos vectoriales (<code>reportlab.graphics.shapes</code>). Podemos construir diagramas de barras que se renderizan sin pérdida de nitidez en impresiones de alta resolución:</p>
<pre><code>from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import VerticalBarChart

def create_bar_chart(records: List[Dict]) -> Drawing:
    drawing = Drawing(450, 180)
    data = [[r["cost"] for r in records]]
    category_names = [f"Módulo {r['id']}" for r in records]

    bc = VerticalBarChart()
    bc.x = 40
    bc.y = 25
    bc.height = 125
    bc.width = 380
    bc.data = data
    bc.categoryAxis.categoryNames = category_names
    bc.categoryAxis.labels.fontSize = 8
    bc.valueAxis.valueMin = 0
    bc.bars[0].fillColor = colors.HexColor("#4f46e5")

    drawing.add(bc)
    return drawing
</code></pre>

<h2>4. Paginación Dinámica Avanzada y Numeración con Canvas Maker</h2>
<p>En documentos de múltiples páginas, es imperativo imprimir el pie de página con el formato 'Página X de Y'. En ReportLab, esto se logra mediante una subclase personalizada de <code>canvas.Canvas</code> llamada <code>NumberedCanvas</code>, la cual intercepta las páginas antes de cerrarlas para calcular el total exacto de pliegos:</p>
<pre><code>from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            super().showPage()
        super().save()

    def draw_page_number(self, page_count):
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawRightString(612 - 54, 36, f"Página {self._pageNumber} de {page_count}")
        self.drawString(54, 36, "Laboratorio de Ingeniería CUC - Documento Oficial Confidencial")
</code></pre>

<h2>5. Generación de Archivos Excel con openpyxl y Formateo Condicional</h2>
<p>Para crear archivos <code>.xlsx</code> compatibles con Microsoft Excel, Google Sheets y LibreOffice Calc, utilizamos <code>openpyxl</code>:</p>
<pre><code>import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from typing import List, Dict

class ExcelReportGenerator:
    @staticmethod
    def build_spreadsheet(output_filename: str, records: List[Dict]):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Consolidado 2026"
        
        header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
        header_fill = PatternFill(start_color="312E81", end_color="312E81", fill_type="solid")
        
        headers = ["Código", "Concepto Operativo", "Estado", "Presupuesto Asignado"]
        ws.append(headers)
        
        for col_num in range(1, len(headers) + 1):
            cell = ws.cell(row=1, column=col_num)
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = Alignment(horizontal="center", vertical="center")
            
        for row_idx, r in enumerate(records, start=2):
            ws.append([r["id"], r["name"], r["status"], r["cost"]])
            cost_cell = ws.cell(row=row_idx, column=4)
            cost_cell.number_format = '$#,##0.00'
            
        last_row = len(records) + 2
        ws.cell(row=last_row, column=3, value="Total General:").font = Font(bold=True)
        total_cell = ws.cell(row=last_row, column=4, value=f"=SUM(D2:D{last_row-1})")
        total_cell.font = Font(bold=True)
        total_cell.number_format = '$#,##0.00'
        
        for col in ws.columns:
            max_len = max(len(str(cell.value or '')) for cell in col)
            col_letter = col[0].column_letter
            ws.column_dimensions[col_letter].width = max(max_len + 4, 12)
            
        wb.save(output_filename)
</code></pre>

<h2>6. Integración del Componente `FilePicker` en Flet</h2>
<p>En aplicaciones de escritorio, guardar un archivo no debe sobreescribir rutas arbitrarias sin el consentimiento del usuario. Flet ofrece el control <code>ft.FilePicker</code>, el cual abre la ventana nativa del sistema operativo para que el usuario escoja la carpeta y nombre de archivo:</p>
<pre><code>import flet as ft
from pdf_generator import PdfReportGenerator
from excel_generator import ExcelReportGenerator

def main(page: ft.Page):
    page.title = "Módulo de Exportación Corporativa CUC"
    page.padding = 30

    sample_data = [
        {"id": 101, "name": "Servidor de Base de Datos SQLite", "status": "Operativo", "cost": 450.0},
        {"id": 102, "name": "Módulo de Autenticación Criptográfica", "status": "Verificado", "cost": 320.0},
        {"id": 103, "name": "Integración de Redes y API aiohttp", "status": "En Pruebas", "cost": 580.0},
        {"id": 104, "name": "Licencias y Pruebas de Laboratorio", "status": "Completado", "cost": 210.0}
    ]

    export_type = {"mode": "pdf"}

    def on_file_save_result(e: ft.FilePickerResultEvent):
        if e.path:
            try:
                if export_type["mode"] == "pdf":
                    filepath = e.path if e.path.endswith(".pdf") else f"{e.path}.pdf"
                    PdfReportGenerator.build_financial_report(filepath, sample_data)
                else:
                    filepath = e.path if e.path.endswith(".xlsx") else f"{e.path}.xlsx"
                    ExcelReportGenerator.build_spreadsheet(filepath, sample_data)

                page.snack_bar = ft.SnackBar(ft.Text(f"Archivo exportado con éxito en: {filepath}"), bgcolor=ft.Colors.GREEN_700)
                page.snack_bar.open = True
                page.update()
            except Exception as err:
                page.snack_bar = ft.SnackBar(ft.Text(f"Error al generar archivo: {str(err)}"), bgcolor=ft.Colors.RED_700)
                page.snack_bar.open = True
                page.update()

    file_picker = ft.FilePicker(on_result=on_file_save_result)
    page.overlay.append(file_picker)

    def trigger_pdf_export(e):
        export_type["mode"] = "pdf"
        file_picker.save_file(
            dialog_title="Guardar Reporte Oficial PDF",
            file_name="Reporte_Laboratorio_CUC_2026.pdf",
            allowed_extensions=["pdf"]
        )

    def trigger_excel_export(e):
        export_type["mode"] = "excel"
        file_picker.save_file(
            dialog_title="Guardar Libro de Cálculo Excel",
            file_name="Consolidado_Financiero_2026.xlsx",
            allowed_extensions=["xlsx"]
        )

    page.add(
        ft.Column([
            ft.Text("Generador de Reportes Ejecutivos", size=24, weight=ft.FontWeight.BOLD),
            ft.Text("Exporta tus registros directamente a PDF vectorial o Excel con fórmulas nativas.", size=13, color=ft.Colors.GREY_600),
            ft.Divider(height=30),
            ft.Row([
                ft.ElevatedButton("Exportar a PDF Oficial", icon=ft.Icons.PICTURE_AS_PDF, on_click=trigger_pdf_export),
                ft.ElevatedButton("Exportar a Libro Excel", icon=ft.Icons.TABLE_CHART, on_click=trigger_excel_export)
            ])
        ])
    )

if __name__ == "__main__":
    ft.app(target=main)
</code></pre>

<h2>7. Protección Criptográfica de Archivos Generados</h2>
<p>En ámbitos corporativos sensibles (como nóminas, expedientes médicos o auditorías financieras), es fundamental proteger los archivos exportados contra aperturas no autorizadas. Podemos proteger los documentos generados:</p>
<ul>
  <li><strong>Protección de PDFs con PyPDF2 / pypdf:</strong> Tras compilar el documento con ReportLab, podemos aplicar cifrado estándar AES de 128 o 256 bits estableciendo una contraseña de usuario y de propietario que bloquee la copia de texto y la impresión no autorizada.</li>
  <li><strong>Protección de Hojas Excel con openpyxl:</strong> La propiedad <code>ws.protection.sheet = True</code> junto con <code>ws.protection.set_password('ClaveSegura2026')</code> permite bloquear la modificación de fórmulas críticas mientras se deja al usuario la libertad de ordenar y filtrar los datos numéricos.</li>
</ul>

<h2>8. Conclusiones de Andrés (Universidad de la Costa)</h2>
<p>Dotar a tus proyectos de Python y Flet con capacidades de exportación en PDF y Excel eleva de inmediato su nivel de profesionalismo ante profesores, clientes y empleadores. La integración limpia de ReportLab y openpyxl con los selectores nativos de Flet demuestra que Python sigue siendo la plataforma líder absoluta en automatización documental e ingeniería de software.</p>"""

PYTHON_FLET_CONTENT[12] = """<h2>1. Del Escritorio a la Nube: La Magia de Flet como PWA</h2>
<p>Una de las capacidades más asombrosas de Flet es su versatilidad de despliegue: el mismo código fuente en Python que se ejecuta en tu laptop con una ventana de escritorio nativa puede compilarse y publicarse como una <strong>PWA (Progressive Web App)</strong> accesible desde cualquier navegador web en computadores, tablets o teléfonos inteligentes sin cambiar una sola coma de la lógica de interfaz.</p>
<p>En el entorno de producción en servidores cloud (DigitalOcean, AWS, Google Cloud Run o VPS locales en Linux), no podemos depender del comando de desarrollo <code>flet run</code>. Para soportar cientos de usuarios concurrentes con alta disponibilidad, seguridad criptográfica TLS/SSL y bajo consumo de memoria RAM, el estándar de la industria exige empaquetar la aplicación en un contenedor <strong>Docker</strong> optimizado y servir el tráfico estático y de WebSockets mediante un servidor proxy inverso <strong>Nginx</strong>.</p>

<h2>2. Arquitectura de Despliegue: Contenedorización Multi-Stage</h2>
<p>Para no arrastrar herramientas de compilación pesadas, compiladores de C++ o librerías de prueba a la imagen final de producción, utilizaremos un <strong>Dockerfile Multi-Stage (construcción en múltiples etapas)</strong> basado en la distribución ultraligera <code>python:3.11-slim</code>:</p>
<pre><code># ==========================================
# Etapa 1: Builder y Compilación de Dependencias
# ==========================================
FROM python:3.11-slim AS builder

WORKDIR /build

RUN apt-get update &amp;&amp; apt-get install -y --no-install-recommends     build-essential     curl     &amp;&amp; rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# ==========================================
# Etapa 2: Imagen Final de Producción
# ==========================================
FROM python:3.11-slim AS runner

WORKDIR /app

RUN groupadd -r fletgroup &amp;&amp; useradd -r -g fletgroup fletuser

COPY --from=builder /root/.local /home/fletuser/.local
COPY . /app

ENV PATH=/home/fletuser/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1
ENV FLET_SERVER_PORT=8550
ENV FLET_SERVER_IP=0.0.0.0

RUN chown -R fletuser:fletgroup /app
USER fletuser

EXPOSE 8550

CMD ["python", "main.py"]
</code></pre>

<h2>3. Configuración del Servidor Proxy Inverso Nginx</h2>
<p>Flet Web utiliza conexiones <strong>WebSockets</strong> para sincronizar los eventos del usuario (clics, texto ingresado) con el backend en Python en tiempo real. Por ello, la configuración de Nginx debe incluir obligatoriamente los encabezados <code>Upgrade</code> y <code>Connection</code> para no degradar la conexión a sondeos HTTP lentos:</p>
<pre><code>server {
    listen 80;
    server_name misistema.cuc.edu.co;

    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name misistema.cuc.edu.co;

    ssl_certificate /etc/letsencrypt/live/misistema.cuc.edu.co/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/misistema.cuc.edu.co/privkey.pem;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;

    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml;

    location / {
        proxy_pass http://flet_app:8550;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_read_timeout 86400s;
        proxy_send_timeout 86400s;
    }
}
</code></pre>

<h2>4. Orquestación Automatizada con Docker Compose</h2>
<p>Unimos ambos servicios en un archivo <code>docker-compose.yml</code> para levantar todo el ecosistema con un único comando:</p>
<pre><code>version: '3.8'

services:
  flet_app:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: flet_production_app
    restart: always
    environment:
      - FLET_SERVER_PORT=8550
      - FLET_SERVER_IP=0.0.0.0
    networks:
      - flet_internal_network

  nginx:
    image: nginx:alpine
    container_name: flet_nginx_proxy
    restart: always
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf:ro
      - ./certbot/conf:/etc/letsencrypt:ro
    depends_on:
      - flet_app
    networks:
      - flet_internal_network

networks:
  flet_internal_network:
    driver: bridge
</code></pre>

<h2>5. Automatización de Certificados SSL Gratuitos con Let's Encrypt y Certbot</h2>
<p>Para asegurar que las conexiones entre el cliente y nuestro servidor Nginx estén protegidas con cifrado TLS 1.3 de extremo a extremo, integramos un contenedor adicional con Certbot en modo renovación automática:</p>
<pre><code>  certbot:
    image: certbot/certbot:latest
    container_name: certbot_ssl
    volumes:
      - ./certbot/conf:/etc/letsencrypt:rw
      - ./certbot/www:/var/www/certbot:rw
    entrypoint: "/bin/sh -c 'trap exit TERM; while :; do certbot renew; sleep 12h &amp; wait $${!}; done;'"
</code></pre>

<h2>6. Compilación de Recursos PWA y Personalización del Manifiesto</h2>
<p>Para que la aplicación se instale en teléfonos móviles con su propio ícono y pantalla de bienvenida (Splash Screen), Flet permite generar los activos estáticos mediante el comando de compilación web:</p>
<pre><code>flet build web --project-name "Laboratorio CUC" --description "Sistema de Control de Ingeniería"</code></pre>
<p>Este proceso genera una carpeta <code>build/web</code> que contiene el archivo <code>manifest.json</code>, el service worker <code>flutter_service_worker.js</code> para soporte offline parcial y los íconos adaptativos en distintas resoluciones.</p>

<h2>7. Gestión de Memoria y Límites de Cgroups en Linux</h2>
<p>En servidores cloud compartidos de bajo costo (como droplets de 1 GB de RAM), es indispensable fijar límites estrictos de recursos para evitar que el OOM Killer (Out Of Memory) de Linux dé de baja el contenedor del proxy Nginx:</p>
<pre><code>    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 128M
</code></pre>

<h2>8. Integración Continua con GitHub Actions (CI/CD)</h2>
<p>Podemos automatizar completamente el ciclo de vida del despliegue configurando un flujo de trabajo en <code>.github/workflows/deploy.yml</code> que construya la imagen, la suba a Docker Hub y se conecte mediante SSH a nuestro servidor VPS para reiniciar el contenedor sin intervención manual:</p>
<pre><code>name: Deploy Flet PWA to VPS

on:
  push:
    branches: [ main ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Login to Docker Hub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      - name: Build and Push Docker Image
        run: |
          docker build -t ${{ secrets.DOCKERHUB_USERNAME }}/flet-app:latest .
          docker push ${{ secrets.DOCKERHUB_USERNAME }}/flet-app:latest
      - name: Deploy via SSH
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.SERVER_HOST }}
          username: ${{ secrets.SERVER_USER }}
          key: ${{ secrets.SERVER_SSH_KEY }}
          script: |
            cd /opt/flet-project
            docker-compose pull
            docker-compose up -d --remove-orphans
</code></pre>

<h2>9. Monitoreo de Métricas y Rendimiento con Prometheus y cAdvisor</h2>
<p>Para supervisar la estabilidad de los contenedores en producción, resulta imprescindible recopilar métricas operativas de uso de CPU, tasa de transferencia de red y consumo de memoria RAM. Con herramientas de código abierto como <strong>cAdvisor</strong> y <strong>Prometheus</strong>, podemos monitorizar en tiempo real si algún proceso en Python presenta fugas de descriptores de archivos o retención indebida de objetos gráficos en memoria.</p>
<p>Además, al configurar alertas automatizadas conectadas a un canal de Discord o Telegram mediante webhooks, el equipo de ingeniería recibe una notificación instantánea si el contenedor de la aplicación Flet supera el 85% de utilización de memoria durante un pico de demanda ciudadana o académica.</p>

<h2>10. Estrategias de Rollback Inmediato y Despliegues sin Caídas (Zero Downtime)</h2>
<p>En aplicaciones críticas, actualizar una versión no debe interrumpir las sesiones activas de los usuarios. Al emplear Nginx como balanceador de carga upstream frente a dos instancias idénticas del contenedor Flet (esquema Blue-Green), podemos redirigir progresivamente el tráfico hacia el nuevo contenedor mientras el contenedor antiguo completa sus conexiones pendientes, garantizando cero segundos de desconexión para la comunidad de usuarios.</p>

<h2>11. Diagnóstico y Monitoreo en Producción</h2>
<table>
  <thead>
    <tr>
      <th>Síntoma Detectado</th>
      <th>Causa Probable</th>
      <th>Solución Inmediata</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>La web carga pero dice <em>'Connecting to Flet server...'</em> indefinidamente</td>
      <td>Nginx no tiene habilitados los headers <code>Upgrade</code> de WebSockets o el cortafuegos bloquea el puerto interno.</td>
      <td>Verificar la directiva <code>proxy_set_header Connection "upgrade";</code> en la configuración de Nginx.</td>
    </tr>
    <tr>
      <td>El contenedor se reinicia en bucle (CrashLoopBackOff)</td>
      <td>El puerto 8550 está ocupado o el usuario <code>fletuser</code> no tiene permisos de escritura sobre la base de datos SQLite.</td>
      <td>Revisar los logs con <code>docker logs flet_production_app</code> y asegurar permisos <code>chmod 775</code> sobre el directorio de datos.</td>
    </tr>
    <tr>
      <td>Certificado SSL vencido o advertencia de sitio no seguro</td>
      <td>Fallo en el reto HTTP-01 de Certbot por bloqueo del puerto 80 en el router o cortafuegos de la nube.</td>
      <td>Abrir el puerto 80 TCP en el Security Group de AWS o DigitalOcean para permitir la renovación de Let's Encrypt.</td>
    </tr>
  </tbody>
</table>

<h2>12. Optimización de Tráfico y Compresión HTTP/2 con Gzip y Brotli</h2>
<p>Para aplicaciones web de una sola página (PWA) con interfaces ricas en componentes gráficos, el peso de los paquetes iniciales puede retrasar el tiempo de carga en dispositivos móviles bajo redes 3G o 4G. Al configurar Nginx para comprimir no solo archivos HTML y CSS, sino también los flujos JSON mediante algoritmos avanzados como Gzip y Brotli (con nivel de compresión 6), es posible reducir el tamaño de las cargas útiles hasta en un 70%, acelerando drásticamente el First Contentful Paint (FCP).</p>
<p>Asimismo, habilitar el protocolo HTTP/2 sobre conexiones seguras TLS permite la multiplexación de múltiples recursos sobre un único canal TCP persistente, eliminando el bloqueo de cabeza de línea (Head-Of-Line Blocking) característico del protocolo HTTP/1.1 tradicional y optimizando la experiencia del usuario final.</p>

<h2>13. Conclusiones y Valoración de Andrés (Universidad de la Costa)</h2>
<p>La capacidad de desplegar aplicaciones de Python Flet en contenedores Docker respaldados por Nginx democratiza el lanzamiento de productos digitales completos. Con una sola arquitectura puedes atender a usuarios en Windows, macOS, Linux y dispositivos móviles a través de la web con costos de infraestructura mínimos y máxima seguridad informática.</p>"""

PYTHON_FLET_CONTENT[13] = """<h2>1. El Desafío de la Sincronización de Estado en Interfaces Reactivas</h2>
<p>A medida que una aplicación de software crece en complejidad, uno de los desafíos de ingeniería más críticos es la <strong>gestión del estado (State Management)</strong>. El 'estado' representa la fotografía de todos los datos vivos en un instante dado: quién es el usuario conectado, qué idioma está seleccionado, si el tema visual es claro u oscuro, o qué elementos componen el carrito de compras actual.</p>
<p>En aplicaciones mal estructuradas, los desarrolladores suelen pasar variables de estado como parámetros a través de decenas de componentes anidados (antipatrón conocido como <em>Prop Drilling</em>). Si un componente secundario modifica una variable, los demás componentes de la pantalla no se enteran y la interfaz muestra información desactualizada o contradictoria.</p>
<p>En este tutorial avanzado aprenderás a resolver este problema implementando un patrón de <strong>Gestor de Estado Centralizado</strong> respaldado por dos mecanismos nativos de Flet:</p>
<ul>
  <li><strong>`page.pubsub` (Patrón Publicador/Suscriptor):</strong> Permite que cualquier componente emita eventos globales en memoria para que todos los observadores registrados reaccionen de inmediato.</li>
  <li><strong>`page.client_storage`:</strong> Permite que las preferencias críticas (como el tema visual o la configuración del usuario) persistan en el almacenamiento no volátil del dispositivo entre reinicios de la aplicación.</li>
</ul>

<h2>2. Implementación del Gestor de Preferencias con `client_storage`</h2>
<p>Diseñamos una clase que encapsula la lectura y escritura de configuraciones locales utilizando valores por defecto resilientes:</p>
<pre><code>import flet as ft
from typing import Any

class PreferenceManager:
    def __init__(self, page: ft.Page):
        self.page = page

    def get(self, key: str, default: Any = None) -> Any:
        val = self.page.client_storage.get(key)
        return val if val is not None else default

    def set(self, key: str, value: Any):
        self.page.client_storage.set(key, value)

    def is_dark_mode(self) -> bool:
        return self.get("theme_is_dark", False)

    def toggle_theme(self) -> bool:
        new_status = not self.is_dark_mode()
        self.set("theme_is_dark", new_status)
        return new_status
</code></pre>

<h2>3. Configuración del Bus de Eventos Global con `page.pubsub`</h2>
<p>Flet incorpora un bus de mensajes reactivo asíncrono (PubSub). Diseñamos un despachador tipado de mensajes:</p>
<pre><code>from dataclasses import dataclass

@dataclass
class AppEvent:
    event_type: str
    payload: Any

EVENT_THEME_CHANGED = "theme_changed"
EVENT_USER_LOGGED = "user_logged"
EVENT_CART_UPDATED = "cart_updated"
</code></pre>

<h2>4. Integración Completa en una Aplicación Modular</h2>
<p>A continuación construimos una aplicación completa donde una barra de navegación (Navbar) y un panel de configuración interactúan sin acoplamiento directo:</p>
<pre><code>import flet as ft
from preference_manager import PreferenceManager, AppEvent, EVENT_THEME_CHANGED

def main(page: ft.Page):
    page.title = "Control de Estado y Temas Reactivos - CUC"
    prefs = PreferenceManager(page)

    initial_dark = prefs.is_dark_mode()
    page.theme_mode = ft.ThemeMode.DARK if initial_dark else ft.ThemeMode.LIGHT
    page.update()

    def on_pubsub_message(event: AppEvent):
        if event.event_type == EVENT_THEME_CHANGED:
            is_dark = event.payload
            page.theme_mode = ft.ThemeMode.DARK if is_dark else ft.ThemeMode.LIGHT
            page.snack_bar = ft.SnackBar(
                ft.Text(f"Modo {'Oscuro' if is_dark else 'Claro'} activado globalmente."),
                duration=1500
            )
            page.snack_bar.open = True
            page.update()

    page.pubsub.subscribe(on_pubsub_message)

    class Navbar(ft.Container):
        def __init__(self):
            super().__init__()
            self.switch_theme = ft.Switch(
                label="Modo Oscuro",
                value=prefs.is_dark_mode(),
                on_change=self._on_switch_toggle
            )
            self.content = ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Row([
                        ft.Icon(ft.Icons.TERMINAL, color=ft.Colors.INDIGO_400),
                        ft.Text("Laboratorio de Software", weight=ft.FontWeight.BOLD, size=16)
                    ]),
                    self.switch_theme
                ]
            )

        def _on_switch_toggle(self, e):
            new_val = prefs.toggle_theme()
            page.pubsub.send_all(AppEvent(event_type=EVENT_THEME_CHANGED, payload=new_val))

    class DashboardBody(ft.Container):
        def __init__(self):
            super().__init__()
            self.padding = 20
            self.content = ft.Column([
                ft.Text("Gestión de Estado Desacoplada", size=22, weight=ft.FontWeight.BOLD),
                ft.Text("Este panel no conoce directamente el switch de la cabecera; reacciona a través del bus de eventos pubsub.", size=13),
                ft.Divider(height=25),
                ft.ElevatedButton("Alternar Tema desde aquí", on_click=self._trigger_theme)
            ])

        def _trigger_theme(self, e):
            new_val = prefs.toggle_theme()
            page.pubsub.send_all(AppEvent(event_type=EVENT_THEME_CHANGED, payload=new_val))

    page.add(
        ft.Column([
            Navbar(),
            ft.Divider(),
            DashboardBody()
        ])
    )

if __name__ == "__main__":
    ft.app(target=main)
</code></pre>

<h2>5. Persistencia Cifrada con Cryptography y Fernet</h2>
<p>En ocasiones necesitamos almacenar tokens de sesión o secretos en <code>client_storage</code> sin dejarlos en texto claro. Podemos combinar la biblioteca estándar <code>cryptography.fernet</code> con una clave derivada de la máquina:</p>
<pre><code>from cryptography.fernet import Fernet
import base64
import hashlib
import platform

class EncryptedStorage:
    def __init__(self, page: ft.Page):
        self.page = page
        machine_seed = f"{platform.node()}-{platform.machine()}-CUC-LAB"
        key = base64.urlsafe_b64encode(hashlib.sha256(machine_seed.encode()).digest())
        self.cipher = Fernet(key)

    def set_secure(self, key: str, secret_text: str):
        encrypted = self.cipher.encrypt(secret_text.encode()).decode()
        self.page.client_storage.set(key, encrypted)

    def get_secure(self, key: str) -> Optional[str]:
        encrypted = self.page.client_storage.get(key)
        if not encrypted:
            return None
        try:
            return self.cipher.decrypt(encrypted.encode()).decode()
        except Exception:
            return None
</code></pre>

<h2>6. Paletas de Color Material Design 3 y Tematizado Dinámico</h2>
<p>Material Design 3 (Material You) introducido en Flet permite especificar esquemas tonales avanzados. En lugar de limitarnos a blanco y negro, podemos inyectar colores semilla (Seed Color) para que todos los botones, tarjetas y deslizadores adopten una armonía cromática calculada automáticamente:</p>
<pre><code>page.theme = ft.Theme(
    color_scheme_seed=ft.Colors.INDIGO,
    visual_density=ft.VisualDensity.COMPACT
)
page.dark_theme = ft.Theme(
    color_scheme_seed=ft.Colors.INDIGO_ACCENT,
    visual_density=ft.VisualDensity.COMPACT
)
</code></pre>

<h2>7. Patrón Store Inmutable Inspirado en Redux</h2>
<p>Para aplicaciones corporativas con múltiples flujos de datos cruzados, estructurar un Store inmutable previene mutaciones inesperadas en memoria:</p>
<pre><code>from typing import Callable, List
import copy

class Store:
    def __init__(self, reducer: Callable, initial_state: dict):
        self.reducer = reducer
        self.state = copy.deepcopy(initial_state)
        self.listeners: List[Callable] = []

    def get_state(self) -> dict:
        return self.state

    def dispatch(self, action: dict):
        self.state = self.reducer(self.state, action)
        for listener in self.listeners:
            listener(self.state)

    def subscribe(self, listener: Callable):
        self.listeners.append(listener)
</code></pre>

<h2>8. Detección Reactiva de Desconexión de Red y Modo Offline</h2>
<p>En dispositivos móviles o conexiones Wi-Fi intermitentes, una interfaz reactiva debe notificar al usuario de inmediato si se interrumpió el enlace con el servidor central. Podemos integrar un observador de latencia y estado de red que muestre una alerta flotante contextual en color ámbar cuando la aplicación pierda conectividad, deshabilitando botones de envío financiero para evitar duplicaciones de órdenes de pago.</p>

<h2>9. Versionamiento y Migración de Esquemas de Almacenamiento Local</h2>
<p>Cuando publicamos una versión 2.0 de nuestra aplicación, las estructuras guardadas en <code>client_storage</code> pueden sufrir variaciones de formato. Implementar un campo <code>schema_version</code> en el almacén permite ejecutar migraciones de datos transparentes que transformen las preferencias antiguas al nuevo formato sin forzar al usuario a perder su historial de personalización.</p>

<h2>10. Tabla Comparativa de Estrategias de Persistencia en Flet</h2>
<table>
  <thead>
    <tr>
      <th>Mecanismo</th>
      <th>Ámbito de Vida</th>
      <th>Seguridad</th>
      <th>Caso de Uso Recomendado</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>`page.client_storage`</strong></td>
      <td>Permanente en disco local.</td>
      <td>Cifrado según la plataforma del SO.</td>
      <td>Preferencias de tema, tokens de sesión, últimas búsquedas.</td>
    </tr>
    <tr>
      <td><strong>`page.session`</strong></td>
      <td>Volátil (se destruye al cerrar la pestaña).</td>
      <td>Memoria del proceso servidor.</td>
      <td>Datos temporales de formularios de múltiples pasos.</td>
    </tr>
    <tr>
      <td><strong>Base de Datos SQLite</strong></td>
      <td>Permanente y transaccional ACID.</td>
      <td>Requiere permisos de sistema de archivos.</td>
      <td>Registros de negocio, catálogos, pedidos contables.</td>
    </tr>
  </tbody>
</table>

<h2>11. Sincronización Multi-Pestaña y Control de Concurrencia</h2>
<p>En aplicaciones web PWA construidas con Flet, un usuario puede abrir simultáneamente dos o tres pestañas del navegador apuntando a la misma aplicación. Si en una pestaña modifica su perfil o cambia el tema visual, las demás pestañas deben sincronizarse de manera automática sin forzar una recarga manual.</p>
<p>Gracias al bus de eventos <code>page.pubsub.send_all()</code>, el servidor central de Flet distribuye la señal a todas las sesiones asociadas a ese usuario, permitiendo que la interfaz reaccione en tiempo real independientemente de cuántas ventanas tenga abiertas. Además, para evitar condiciones de carrera cuando dos pestañas intentan escribir en <code>client_storage</code> de forma concurrente, el gestor de preferencias implementa cerrojos lógicos (locks) en memoria que garantizan la consistencia de los datos guardados.</p>

<h2>12. Herramientas de Inspección y Debugging del Estado Global</h2>
<p>Depurar el estado de una aplicación reactiva puede convertirse en un dolor de cabeza si no contamos con trazabilidad de eventos. Al implementar un middleware de logging que imprima en la consola del desarrollador cada acción despachada, su payload y el estado resultante anterior y posterior (time-travel debugging simplificado), podemos rastrear con precisión milimétrica qué componente originó una anomalía o cambio inesperado en la pantalla.</p>

<h2>13. Conclusiones y Recomendaciones de Andrés (Universidad de la Costa)</h2>
<p>Implementar un manejo de estado ordenado mediante PubSub y persistencia selectiva con `client_storage` marca la diferencia entre un prototipo desechable y un producto de software robusto. Al dominar estos patrones en Python Flet, estás preparado para desarrollar interfaces elegantes, reactivas y altamente responsivas que satisfagan los estándares más exigentes de la industria.</p>"""

print("Módulo generate_python_flet.py cargado con éxito. Artículos 8 al 13 listos.")
