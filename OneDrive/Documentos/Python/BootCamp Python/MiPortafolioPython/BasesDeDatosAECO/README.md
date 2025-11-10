# Modelado y Gestión de Base de Datos Relacional - Portafolio AECO

Este proyecto implementa una base de datos relacional y sistema CRUD web para la gestión de clientes, proyectos y diagnósticos energéticos en el sector arquitectura, ingeniería y construcción (AECO). Refleja un enfoque estratégico para digitalizar procesos y potenciar la eficiencia de organizaciones AECO mediante soluciones tecnológicas.

---

## Índice

1. [Estructura principal](#estructura-principal)
2. [Propósito profesional](#propósito-profesional)
3. [Instalación y ejecución (Django)](#instalación-y-ejecución-django)
4. [Ejecución de consultas SQL](#ejecución-de-consultas-sql)
5. [Diagrama Entidad-Relación](#diagrama-entidad-relación)
6. [Autor](#autor)

---

## Estructura principal

- **Clientes:** Registro de datos relevantes (nombre, contacto, dirección).
- **Proyectos:** Descripción, fechas y vinculación de proyectos con los clientes correspondientes.
- **Diagnósticos:** Resultados y observaciones de evaluaciones energéticas asociadas a cada proyecto.

---

## Propósito profesional

Como arquitecto y emprendedor, el dominio en bases de datos y la normalización de información son claves para construir soluciones digitales escalables y confiables. Este repositorio demuestra mi capacidad para articular proyectos reales integrando gestión de datos, automatización y reporting.

---

## Instalación y ejecución (Django)

1. Clona el repositorio o descarga el proyecto.
2. Crea un entorno virtual en la raíz:
    ```
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```
3. Instala las dependencias:
    ```
    pip install -r requirements.txt
    ```
4. Realiza migraciones de la base de datos:
    ```
    python manage.py migrate
    ```
5. Crea un usuario admin:
    ```
    python manage.py createsuperuser
    ```
6. Ejecuta el servidor de desarrollo:
    ```
    python manage.py runserver
    ```
7. Accede a:
    - Página de inicio: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    - Listado de proyectos: [http://127.0.0.1:8000/proyectos/](http://127.0.0.1:8000/proyectos/)
    - Crear proyecto: [http://127.0.0.1:8000/proyectos/nuevo/](http://127.0.0.1:8000/proyectos/nuevo/)
    - Admin Django: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Ejecución de consultas SQL

1. Selecciona la base de datos:
    ```
    USE portafolio_db;
    ```
2. Ejecuta los scripts de creación y carga:
    - `creacion_tablas.sql`
    - `insert_datos.sql`
3. Utiliza las queries incluidas para explorar y analizar la información.

---

## Diagrama Entidad-Relación

+-------------+ +--------------+ +----------------+
| Cliente | 1 N | Proyecto | 1 N | Diagnóstico |
+-------------+---------+--------------+----------+----------------+
| id | | id | | id |
| nombre | | cliente_id FK| | proyecto_id FK |
| contacto | | nombre | | descripcion |
| direccion | | descripcion | | fecha |
+-------------+ | fecha_inicio | +----------------+
+--------------+


---

## Autor

Patricio Becar  Elissegaray
Arquitecto | Innovador AECO | Desarrollador de soluciones digitales

---

