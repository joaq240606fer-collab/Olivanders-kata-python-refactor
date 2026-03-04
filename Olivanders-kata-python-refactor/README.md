Gilded Rose Refactor (DDD & OOP)
Este proyecto es una refactorización del clásico Gilded Rose Kata, implementado siguiendo principios de Diseño Orientado a Objetos (OOP) y Diseño Guiado por Dominio (DDD) básico. El objetivo es demostrar cómo transformar un código procedural ("Spaghetti Code") en una arquitectura limpia, mantenible y testeable.

 Características
Arquitectura Limpia: Separación de responsabilidades entre Entidades (Item) y Servicios (GildedRose).
Polimorfismo: Cada tipo de ítem gestiona su propia lógica de calidad.
Pruebas Unitarias: Suite completa de tests con pytest.
Gestión de Dependencias: Uso de uv para una instalación rápida y eficiente.

Requisitos
Python 3.10+
uv (Instalador de paquetes y ejecutor rápido)
 Instalación
Este proyecto utiliza uv para gestionar el entorno virtual y las dependencias. Sigue estos pasos:

Instalar uv (si no lo tienes):

bash

Copy code
curl -LsSf https://astral.sh/uv/install.sh | sh
Inicializar el proyecto (crea pyproject.toml y entorno virtual):

bash

Copy code
uv init
Agregar dependencias (pytest para las pruebas):

bash

Copy code
uv add pytest
Instalar el entorno:

bash

Copy code
uv sync
 Uso de la Aplicación
Ejecutar la Lógica Principal
Para ejecutar el script principal que simula la actualización de calidad de los ítems:

bash

Copy code
uv run python main.py
Nota: Asegúrate de tener un archivo main.py que instancie GildedRose y llame a update_quality().

Ejecutar las Pruebas
Para validar que la refactorización no rompió la lógica original:

bash

Copy code
uv run pytest

 Arquitectura y Funcionamiento
1. Entidades del Dominio (Item)
En lugar de tener toda la lógica en una clase central, cada ítem es una Entidad que conoce sus propias reglas.

Item (Base): Define la estructura común (name, sell_in, quality).
NormalItem, AgedBrieItem, etc.: Heredan de Item y sobrescriben el método update_quality(). Esto aplica el Principio Abierto/Cerrado: puedes agregar nuevos ítems sin tocar el código existente.
2. Fábrica de Objetos (ItemFactory)
Dado que los ítems se crean dinámicamente según su nombre, usamos un patrón de Fábrica. Esto centraliza la creación de objetos y evita if/else dispersos en el código.

3. Servicio de Aplicación (GildedRose)
Esta clase actúa como un Servidor de Aplicación. Su única responsabilidad es orquestar el proceso:

Recibe la lista de ítems.
Itera sobre ellos.
Llama a item.update_quality().
No sabe cómo se actualiza la calidad, solo que debe actualizarse.
Diagrama de Flujo Simplificado
mermaid

Copy code
graph TD
    A[main.py] -->|Crea Ítems| B(ItemFactory)
    B -->|Retorna Subclases| C[NormalItem / AgedBrie / etc.]
    A -->|Pasa Lista| D[GildedRose]
    D -->|Itera| C
    C -->|Ejecuta| E[update_quality()]
    E -->|Modifica Estado| C
 Estructura del Proyecto
text

Copy code
gilded-rose/
├── .venv/                # Entorno virtual (gestionado por uv)
├── src/                  # Código fuente
│   ├── __init__.py
│   ├── gilded_rose.py    # Clases Item, GildedRose, Factory
│   └── main.py           # Punto de entrada
├── tests/                # Pruebas
│   ├── __init__.py
│   └── test_gilded_rose.py
├── pyproject.toml        # Configuración de uv y dependencias
├── README.md
└── uv.lock               # Bloqueo de versiones

