# 🍋 LIMON IA

**Asistente Inteligente de Ciberseguridad con RAG y User Awareness**

LIMON IA es un asistente inteligente especializado en ciberseguridad que combina procesamiento de lenguaje natural, recuperación aumentada por generación (RAG) y orquestación inteligente para proporcionar respuestas precisas y contextualizadas.

## 🎯 Características Principales

- **Consultas Multimodales**: Interacción por texto y voz
- **RAG Personalizado**: Base de conocimiento propia alimentada por documentos del usuario
- **Orquestación Inteligente**: Sistema que decide dinámicamente el flujo de respuesta
- **Respuestas Especializadas**: Enfoque específico en ciberseguridad y user awareness
- **Procesamiento de Documentos**: Soporte para Excel (.xlsx) y Word (.docx)

## 🏗️ Arquitectura

```
Usuario → Interface (Lovable)
    ↓
Webhooks (n8n/ElevenLabs)
    ↓
LimonOrquestador (AI Agent)
    ↓
    ├── Respuesta General (consultas no técnicas)
    └── LimonChatCohere (RAG para ciberseguridad)
            ↓
        ChromaDB (Base de Conocimiento)
```

## 🛠️ Stack Tecnológico

- **Backend**: Python + LangChain
- **Orquestación**: n8n
- **LLM**: Cohere (Command R+, embed-multilingual-v3.0)
- **Base de Datos Vectorial**: ChromaDB
- **Procesamiento de Voz**: ElevenLabs (STT/TTS)
- **Frontend**: Lovable

## 📦 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/limon-ia.git
cd limon-ia

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

## ⚙️ Configuración

1. Crear archivo `.env` con las siguientes variables:

```env
COHERE_API_KEY=tu_api_key
ELEVENLABS_API_KEY=tu_api_key
N8N_WEBHOOK_URL=tu_webhook_url
CHROMA_PERSIST_DIRECTORY=./chroma_db
```

2. Configurar ChromaDB:

```python
# El sistema creará automáticamente la base de datos vectorial
# en la primera ejecución
```

## 🚀 Uso

### Carga de Documentos

```python
from limon_ia import DocumentLoader

loader = DocumentLoader()
loader.add_document("path/to/document.docx")
loader.add_document("path/to/spreadsheet.xlsx")
```

### Consulta RAG

```python
from limon_ia import rag_query

response = rag_query("¿Cuáles son las mejores prácticas de autenticación?")
print(response)
```

## 📂 Estructura del Proyecto

```
limon-ia/
├── rag_query.py              # Lógica de consulta RAG
├── document_processor.py     # Procesamiento y chunking de documentos
├── embeddings_manager.py     # Gestión de embeddings con Cohere
├── chroma_db/               # Base de datos vectorial persistente
├── requirements.txt         # Dependencias Python
└── README.md
```

## 🔄 Flujo de Procesamiento

1. **Carga de Documentos**
   - Lectura de archivos (.xlsx, .docx)
   - División en chunks mediante `RecursiveCharacterTextSplitter`
   - Generación de embeddings con Cohere
   - Almacenamiento en ChromaDB

2. **Procesamiento de Consultas**
   - Análisis de intención por LimonOrquestador
   - Búsqueda por similitud en base vectorial
   - Construcción de prompt contextualizado
   - Generación de respuesta sin alucinaciones

## 🎯 Principios de Diseño

- **No inventar información**: Respuestas basadas exclusivamente en la base de conocimiento
- **Modularidad**: Arquitectura extensible para nuevos casos de uso
- **Optimización de costos**: RAG activado solo para consultas especializadas
- **Control de alucinaciones**: Reglas estrictas de generación

## 🔮 Roadmap

- [ ] Workflow legal
- [ ] Workflow RRHH
- [ ] Workflow técnico IT
- [ ] Soporte para más formatos (PDF, TXT, CSV)
- [ ] Dashboard de analytics
- [ ] Integración con APIs de seguridad

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork del proyecto
2. Crea tu rama de features (`git checkout -b feature/AmazingFeature`)
3. Commit de cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request


## 📧 Contacto

Facundo Carbajal - [@Facundo_Carbajal](www.linkedin.com/in/facundo-carbajal)

Link del Proyecto: [https://github.com/facundocarbajal2-dev/LimonIA]([https://github.com/tu-usuario/limon-ia](https://github.com/facundocarbajal2-dev/LimonIA/tree/main))

---

**Hecho con 🍋 y mucho ☕**
