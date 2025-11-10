-- Crea la base de datos solo si no existe:
CREATE DATABASE IF NOT EXISTS portafolio_db;

-- Usa la base de datos
USE portafolio_db;

-- Crear tabla clientes
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    telefono VARCHAR(20),
    direccion TEXT
);

-- Crear tabla proyectos
CREATE TABLE IF NOT EXISTS proyectos (
    id_proyecto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_inicio DATE,
    fecha_fin DATE,
    id_cliente INT,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente) ON DELETE CASCADE
);

-- Crear tabla diagnosticos
CREATE TABLE IF NOT EXISTS diagnosticos (
    id_diagnostico INT AUTO_INCREMENT PRIMARY KEY,
    id_proyecto INT,
    fecha DATE NOT NULL,
    resultado VARCHAR(50),
    comentarios TEXT,
    FOREIGN KEY (id_proyecto) REFERENCES proyectos(id_proyecto) ON DELETE CASCADE
);

-- Insertar 4 clientes de ejemplo
INSERT INTO clientes (nombre, email, telefono, direccion) VALUES
('Patricio Becar', 'patricio@email.com', '+56912345678', 'Santiago, Chile'),
('Ana Diaz', 'ana.diaz@example.com', '+56987654321', 'Providencia, Santiago'),
('Carlos Martínez', 'carlos.martinez@example.com', '+56923456789', 'Las Condes, Santiago'),
('María González', 'maria.gonzalez@example.com', '+56934567890', 'Ñuñoa, Santiago');

-- Insertar 4 proyectos relacionados (nota: el id_cliente debe existir)
INSERT INTO proyectos (nombre, descripcion, fecha_inicio, fecha_fin, id_cliente) VALUES
('Proyecto Modular Santiago', 'Construcción modular eficiente', '2025-01-15', '2025-06-30', 1),
('Edificio Sustentable Las Condes', 'Proyecto de edificio con certificación LEED', '2024-09-01', '2025-05-15', 3),
('Remodelación de Vivienda', 'Remodelación para mejorar eficiencia energética', '2025-02-20', '2025-04-30', 2),
('Proyecto Casa Pasiva', 'Diseño y construcción de casa pasiva en Ñuñoa', '2025-03-01', '2025-07-15', 4);

-- Insertar diagnósticos
SELECT * FROM clientes;
SELECT * FROM proyectos;
SELECT * FROM diagnosticos;

INSERT INTO diagnosticos (id_proyecto, fecha, resultado, comentarios) VALUES
(1, '2025-02-10', 'Eficiente', 'Cumple normas DFL2 y OGUC'),
(2, '2025-04-01', 'Regular', 'Requiere mejoras en aislamiento térmico'),
(3, '2025-03-15', 'Eficiente', 'Implementación exitosa de sistemas solares'),
(4, '2025-05-10', 'Inadecuado', 'Problemas en ventilación cruzada');


SELECT * FROM diagnosticos;
