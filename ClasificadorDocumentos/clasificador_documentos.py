#  Clasificador y Gestor de Documentos de Proyectos.
# Aquí es donde organizaremos todos esos planos, informes e imágenes.

import json # Necesitamos esta herramienta para guardar y cargar tus documentos. 

# Esta es la "caja" donde guardamos todos tus documentos en este momento.
documentos = [] 
# Este es el nombre del archivo donde se guardarán tus documentos cuando salgas.
NOMBRE_ARCHIVO_DOCS = 'documentos.json' 

# --- FUNCIONES CLAVE PARA QUE NADA SE PIERDA (¡Persistencia!) ---
def cargar_documentos():
    """Intenta cargar los documentos desde el archivo JSON. Si no lo encuentra o hay un error, empieza con una lista vacía."""
    try:
        # Abrimos el archivo en modo lectura ('r') y con codificación UTF-8 para que todo se lea bien.
        with open(NOMBRE_ARCHIVO_DOCS, 'r', encoding='utf-8') as f:
            return json.load(f) # ¡Cargamos los documentos desde el archivo!
    except FileNotFoundError:
        # Si es la primera vez que lo usas o el archivo no existe, no hay problema, empezamos de cero.
        print("Parece que no hay documentos guardados aún. ¡Vamos a crear algunos!")
        return [] 
    except json.JSONDecodeError:
        # Si el archivo está un poco "roto", te avisamos y empezamos de nuevo para evitar problemas.
        print("¡Ups! Hubo un problema al leer tu archivo de documentos. Quizás esté corrupto.")
        return []

def guardar_documentos():
    """Guarda todos los documentos actuales en nuestro archivo JSON."""
    # Abrimos el archivo en modo escritura ('w') y con codificación UTF-8.
    with open(NOMBRE_ARCHIVO_DOCS, 'w', encoding='utf-8') as f:
        # Usamos json.dump para "volcar" nuestra lista 'documentos' al archivo, ¡bien ordenada!
        json.dump(documentos, f, indent=4) 

# --- MENÚ PARA QUE ELIJAS QUÉ HACER ---
def mostrar_menu():
    """Te muestra las opciones disponibles para gestionar tus documentos."""
    print("\n--- ¡Bienvenido a tu Central de Documentos de Arquitectura! ---")
    print("¿Qué quieres hacer hoy?")
    print("1. Agregar un nuevo Documento")
    print("2. Ver Todos tus Documentos")
    print("3. Buscar un Documento Específico") # Por nombre o cliente
    print("4. Filtrar Documentos") # Por tipo o fase (¡próximamente!)
    print("5. Eliminar un Documento") # (¡próximamente!)
    print("6. Salir (¡No olvides guardar tus cambios!)")

# --- LAS ACCIONES QUE PUEDES REALIZAR CON TUS DOCUMENTOS ---

# 1. Función para agregar un nuevo documento
def agregar_documento():
    """Te guía para añadir los detalles de un nuevo documento a tu colección."""
    print("\n--- ¡Vamos a añadir un Documento fresco! ---")
    nombre = input("¿Cómo se llama este documento? (Ej: Plano Eléctrico Planta 1): ")
    tipo = input("¿Qué tipo de documento es? (Ej: Plano, Informe, Imagen, Contrato): ")
    fase = input("¿En qué fase del proyecto está? (Ej: Conceptual, Construcción, Post-Obra): ")
    cliente = input("¿Para qué cliente o proyecto es este documento? (Ej: Residencia Luz, Edificio Centro): ")

    nuevo_documento = {
        'nombre_documento': nombre,
        'tipo_documento': tipo,
        'fase_proyecto': fase,
        'cliente_asociado': cliente
    }
    documentos.append(nuevo_documento) # Añadimos el nuevo documento a nuestra lista.
    guardar_documentos() # ¡Y lo guardamos de inmediato para que no se pierda!
    print(f"¡Documento '{nombre}' añadido con éxito! Ya está en tu colección.")
    input("Pulsa ENTER para volver al menú principal...")

# 2. Función para ver todos los documentos
def ver_todos_los_documentos():
    """Te muestra todos los documentos que tienes registrados."""
    print("\n--- ¡Aquí tienes todos tus Documentos! ---")
    if not documentos: # Si la lista está vacía...
        print("Mmm... Parece que no hay documentos registrados aún. ¡Añade uno con la opción 1!")
        input("Pulsa ENTER para volver al menú principal...")
        return

    # Si hay documentos, los listamos uno por uno, con todos sus detalles.
    for i, doc in enumerate(documentos):
        print(f"\n--- Documento #{i + 1} ---") # Empezamos a contar desde 1, ¡más amigable!
        print(f"  Nombre: {doc['nombre_documento']}")
        print(f"  Tipo: {doc['tipo_documento']}")
        print(f"  Fase: {doc['fase_proyecto']}")
        print(f"  Cliente: {doc['cliente_asociado']}")
    
    input("\nPulsa ENTER para volver al menú principal...") 

# 3. Función para buscar un documento
def buscar_documento():
    """Te ayuda a encontrar documentos específicos por nombre o por cliente."""
    print("\n--- ¡A buscar ese Documento! ---")
    if not documentos:
        print("No hay documentos para buscar, ¡agrega algunos primero!")
        input("Pulsa ENTER para volver al menú principal...")
        return

    termino_busqueda = input("Escribe lo que quieres buscar (ej. 'Plano' o 'Robles'): ").lower()
    
    print("\n¿Dónde quieres buscar?")
    print("1. En el Nombre del Documento")
    print("2. En el Cliente Asociado")
    opcion_busqueda = input("Elige 1 o 2 para tu búsqueda: ")

    documentos_encontrados = []

    if opcion_busqueda == '1':
        for doc in documentos:
            if termino_busqueda in doc['nombre_documento'].lower():
                documentos_encontrados.append(doc)
    elif opcion_busqueda == '2':
        for doc in documentos:
            if termino_busqueda in doc['cliente_asociado'].lower():
                documentos_encontrados.append(doc)
    else:
        print("Opción de búsqueda no válida. ¡Inténtalo de nuevo!")
        input("Pulsa ENTER para continuar...")
        return

    if not documentos_encontrados:
        print(f"¡Vaya! No encontré ningún documento con '{termino_busqueda}'.")
    else:
        print(f"\n--- ¡Encontré estos documentos con '{termino_busqueda}'! ---")
        for i, doc in enumerate(documentos_encontrados):
            print(f"\n--- Resultado #{i + 1} ---")
            print(f"  Nombre: {doc['nombre_documento']}")
            print(f"  Tipo: {doc['tipo_documento']}")
            print(f"  Fase: {doc['fase_proyecto']}")
            print(f"  Cliente: {doc['cliente_asociado']}")
    
    input("\nPulsa ENTER para volver al menú principal...")


# --- ¡AQUÍ ES DONDE TU PROGRAMA COBRA VIDA! ---
# Primero, intentamos cargar los documentos que tenías guardados.
documentos = cargar_documentos()

# Este es el corazón de tu programa, ¡se repite hasta que decidas salir!
while True:
    mostrar_menu() # Te mostramos las opciones.
    opcion = input("¡Tu turno! Selecciona el número de la opción que quieres: ")

    if opcion == '1':
        agregar_documento()
    elif opcion == '2':
        ver_todos_los_documentos()
    elif opcion == '3':
        buscar_documento()
    elif opcion == '6':
        print("\n¡Gracias por usar tu Clasificador de Documentos! ¡Que tengas un gran día!")
        break # ¡Salimos del programa!
    else:
        print(f"¡Uhm! La opción '{opcion}' no es válida o aún no está implementada. ¡Intenta de nuevo!")
        input("Pulsa ENTER para continuar...")
    print("-" * 60) # Una línea para separar y hacer todo más claro.