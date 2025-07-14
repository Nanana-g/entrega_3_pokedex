# Entrega del proyecto 3

Estudiantes:
Ariana Víquez
María Moroney
Robson Calvo

# Pokedex Web App

## Descripción


Como el api creado por el profe, esta app usa la PokeAPI, para buscar por nombre o ID, y guardar pokemones favoritos en una base de datos local usando FastAPI y SQLite.

---

## Requisitos
- Python== 3.12 (o superior)
- fastapi==0.104.1
- uvicorn==0.24.0
- sqlalchemy==2.0.23
- pydantic==2.5.0
- requests==2.31.0


---

## Instalación

1. **Clonar el repo y entrar a la carpeta del proyecto:**

   ```bash
   git clone <URL_DEL_REPO>
   cd entrega_3_pokedex

2. **Crear y activar un entorno virtual:**

python -m venv .venv
# En Windows PowerShell:
.\.venv\Scripts\Activate
# En CMD:
.\.venv\Scripts\activate.bat
# En Bash:
source .venv/bin/activate


3. **Instala las dependencias:**

pip install -r requirements.txt


## 
Cómo ejecutar la aplicación
1. **Levanta el backend (API con FastAPI)**
Desde la carpeta backend:


cd backend
python -m uvicorn main:app --reload
Esto iniciará el backend en http://localhost:8000.

Puedes ver la documentación interactiva de la API en http://localhost:8000/docs.

2. **Levanta el frontend (servidor local)**
En otra terminal, desde la carpeta frontend:

cd frontend
python -m http.server 8080
Esto iniciará el frontend en http://localhost:8080.

3. **Abre la aplicación en tu navegador**
Ve a http://localhost:8080 para usar la app.
El backend debe estar corriendo para que la app funcione correctamente.


**Estructura del proyecto**
entrega_3_pokedex/
│
├── backend/
│   ├── main.py
│   ├── modelo.py
│   ├── esquema.py
│   └── database/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── requirements.txt
└── README.md


¿Qué puedes hacer con la app?
Buscar y ver Pokémon usando la PokeAPI.
Guardar tus Pokémon favoritos en una base de datos local.
Ver y diferenciar tus favoritos de los datos externos.

Notas
Si tienes problemas de CORS, asegúrate de servir el frontend con python -m http.server.
Si tienes dudas sobre cómo activar el entorno virtual, revisa la sección de instalación.