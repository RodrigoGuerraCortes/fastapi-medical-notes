# 🩺 FastAPI Medical Notes — Patient CRUD Example

This project is a **FastAPI + SQLAlchemy + PostgreSQL** template demonstrating a clean and modular architecture for building medical microservices.  
It currently implements a complete **CRUD** for managing patients, with full test coverage using **pytest** and **SQLite in-memory** testing.

---

## 🚀 Features

- ⚡ FastAPI-based REST API  
- 🧩 SQLAlchemy ORM with PostgreSQL support  
- ✅ Pydantic schemas for data validation  
- 🐳 Dockerized environment (API + DB)  
- 🧪 Automated tests with pytest  
- 🧠 SQLite in-memory testing environment  
- 🔄 Dependency overrides for isolated testing  

---

## 🧱 Project Structure

```
app/
├── crud/
│   └── patient_crud.py
├── models/
│   └── patient_model.py
├── routers/
│   └── patient_router.py
├── schemas/
│   └── patient_schema.py
├── tests/
│   ├── conftest.py
│   └── test_patients_api.py
├── database.py
└── main.py
```

---

## ⚙️ Run with Docker

```bash
docker compose up --build -d
```

This will start two containers:

| Service | Description |
|----------|--------------|
| 🐘 `postgres-db-go-rest-template` | PostgreSQL 15 database |
| 🚀 `fastapi-medical-notes` | FastAPI API running on port **8002** |

Access the API docs:  
👉 [http://localhost:8002/docs](http://localhost:8002/docs)

---

## 🧪 Run Tests

To execute the full test suite inside the FastAPI container:

```bash
docker compose exec -e PYTHONPATH=/app fastapi pytest -v --disable-warnings
```

All CRUD tests (create, read, update, delete) run using an **in-memory SQLite database** to ensure isolation.

---

## 🧰 Example Endpoints

| Method | Endpoint | Description |
|---------|-----------|-------------|
| `GET` | `/patients/` | List all patients |
| `GET` | `/patients/{id}` | Get a patient by ID |
| `POST` | `/patients/` | Create a new patient |
| `PUT` | `/patients/{id}` | Update an existing patient |
| `DELETE` | `/patients/{id}` | Delete a patient |

---

## 🧑‍💻 Technologies

- Python 3.12  
- FastAPI  
- SQLAlchemy ORM  
- PostgreSQL / SQLite  
- Pytest  
- Docker & Docker Compose  

---

## 📄 License

MIT License © Rodrigo Guerra

---

# 🇪🇸 FastAPI Medical Notes — Ejemplo de CRUD de Pacientes

Este proyecto es una plantilla **FastAPI + SQLAlchemy + PostgreSQL**, diseñada para construir microservicios médicos con arquitectura modular y limpia.  
Actualmente implementa un **CRUD completo de pacientes**, con cobertura de pruebas usando **pytest** y **SQLite en memoria**.

---

## 🚀 Características

- API REST con FastAPI  
- ORM SQLAlchemy con PostgreSQL  
- Validaciones con Pydantic  
- Entorno Dockerizado (API + Base de datos)  
- Pruebas automatizadas con pytest  
- Base de datos SQLite en memoria para testing  
- Dependencias sobrescritas para pruebas aisladas  

---

## 🧱 Estructura del Proyecto

```
app/
├── crud/
│   └── patient_crud.py
├── models/
│   └── patient_model.py
├── routers/
│   └── patient_router.py
├── schemas/
│   └── patient_schema.py
├── tests/
│   ├── conftest.py
│   └── test_patients_api.py
├── database.py
└── main.py
```

---

## ⚙️ Ejecutar con Docker

```bash
docker compose up --build -d
```

Se levantarán los servicios:
- 🐘 `postgres-db-go-rest-template` — Contenedor PostgreSQL 15  
- 🚀 `fastapi-medical-notes` — Servicio FastAPI en el puerto **8002**

Accede a la documentación interactiva:  
👉 [http://localhost:8002/docs](http://localhost:8002/docs)

---

## 🧪 Ejecutar Tests

Ejecuta la suite completa dentro del contenedor FastAPI:

```bash
docker compose exec -e PYTHONPATH=/app fastapi pytest -v --disable-warnings
```

Todos los tests de CRUD (crear, leer, actualizar, eliminar) se ejecutan usando SQLite en memoria.

---

## 🧰 Endpoints Disponibles

| Método | Endpoint | Descripción |
|---------|-----------|-------------|
| `GET` | `/patients/` | Lista todos los pacientes |
| `GET` | `/patients/{id}` | Obtiene un paciente por ID |
| `POST` | `/patients/` | Crea un nuevo paciente |
| `PUT` | `/patients/{id}` | Actualiza un paciente existente |
| `DELETE` | `/patients/{id}` | Elimina un paciente |

---

## 🧑‍💻 Tecnologías

- Python 3.12  
- FastAPI  
- SQLAlchemy ORM  
- PostgreSQL / SQLite  
- Pytest  
- Docker & Docker Compose  

---

## 📄 Licencia

MIT License © Rodrigo Guerra