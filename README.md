
# 🚀 Flask API Template

Plantilla base para construir APIs RESTful en Python usando Flask y Swagger (via Flask-RESTX). Ideal para proyectos modulares y escalables, con soporte para configuración por entorno y documentación automática de endpoints.

---

## 📦 Características

- 📂 Estructura modular por rutas
- 📑 Swagger UI integrado con Flask-RESTX
- 🔐 Configuración con variables de entorno
- 📧 Ejemplo de servicio de envío de emails
- ✅ Listo para escalar con nuevos módulos

---

## 🧱 Estructura del Proyecto

```
flask-api-template/
├── app.py                 # Punto de entrada de la app
├── config.py              # Configuraciones generales
├── routes/
│   └── email.py           # Ejemplo de ruta (envío de email)
├── .env                   # Variables de entorno (opcional)
├── requirements.txt       # Dependencias
└── README.md              # Este archivo
```

---

## 🚀 Primeros pasos

### 1. Clonar el repositorio

```bash
git clone https://github.com/JeanFlores10/flask-api-template.git
cd flask-api-template
```

### 2. Crear un entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Crear archivo `.env` con tus credenciales

```env
EMAIL_USER=tu_email@gmail.com
EMAIL_PASS=tu_contraseña_de_aplicación
```

> ⚠️ Requiere una contraseña de aplicación si usas Gmail con 2FA.

---

## ▶️ Ejecutar la aplicación

```bash
python app.py
```

La API estará disponible en:

```
http://localhost:5000/
```

Y la documentación interactiva Swagger UI en:

```
http://localhost:5000/
```

---

## 🔁 Crear un nuevo endpoint

1. Crea un nuevo archivo en `routes/`, por ejemplo `routes/usuarios.py`.
2. Define un nuevo `Namespace` y recursos allí.
3. En `app.py`, importa y registra el nuevo namespace:

```python
from routes.usuarios import api as usuarios_ns
api.add_namespace(usuarios_ns, path="/usuarios")
```

---

## 🌐 Despliegue

Puedes desplegar esta plantilla en cualquier servicio que soporte Python/Flask, como:

- [Render](https://render.com/)
- [Railway](https://railway.app/)
- [Heroku](https://www.heroku.com/) *(requiere `Procfile` y `gunicorn`)*

---

## 💡 Reutilizar como plantilla

Este repositorio está marcado como **template**, por lo que puedes crear nuevos proyectos desde él:

1. Haz clic en el botón verde `Use this template`.
2. Asigna un nombre al nuevo repo.
3. ¡Listo! Tendrás tu propia API lista para modificar y escalar.

---

## 📬 Créditos

Este proyecto fue generado por [JeanFlores10](https://github.com/JeanFlores10) como base para servicios Flask con Swagger.

---

## 🛠️ Requisitos

- Python 3.8+
- pip

---

## 📝 Licencia

Este proyecto está bajo la licencia MIT. Eres libre de usarlo, modificarlo y distribuirlo.
