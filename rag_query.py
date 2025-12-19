import os
import sys
import json

from langchain_cohere import CohereEmbeddings, ChatCohere
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()


# =====================
# CONFIG
# =====================
CHROMA_PATH = r"E:\Cursos\Gettalent_pi\LimonIA\chroma_db"

EMBED_MODEL = "embed-multilingual-v3.0"
LLM_MODEL = "command-a-translate-08-2025"  # o "command-r"

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
if not COHERE_API_KEY:
    print(json.dumps({"error": "COHERE_API_KEY no definida"}))
    sys.exit(1)


# =====================
# PREGUNTA (desde n8n)
# =====================
if len(sys.argv) < 2:
    print(json.dumps({"error": "No se recibió pregunta"}))
    sys.exit(1)

pregunta = sys.argv[1]

# =====================
# VECTOR DB
# =====================
embeddings = CohereEmbeddings(
    model=EMBED_MODEL,
    cohere_api_key=COHERE_API_KEY
)

db = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=embeddings
)

# =====================
# SEARCH
# =====================
docs = db.similarity_search(pregunta, k=260)
contexto = "\n".join([d.page_content for d in docs])

# =====================
# LLM (COHERE)
# =====================
llm = ChatCohere(
    model=LLM_MODEL,
    temperature=0,
    cohere_api_key=COHERE_API_KEY
)

prompt = f"""
Usa únicamente la información del contexto.
Siempre responde en español.
No inventes datos, no inventes informacion.
Eres un asistente de ciberseguridad donde ayudas desempeñando un rol de UserAwarness.
Siempre responde de forma empatica y con buenos ejemplos.
Recuerda que le explicas a personas de todo tipo de edad y ellos tienen que comprenderte.

Contexto:
{contexto}

Pregunta:
{pregunta}

Respuesta clara:
"""

respuesta = llm.invoke(prompt)

# =====================
# OUTPUT PARA N8N
# =====================
print(json.dumps({
    "pregunta": pregunta,
    "respuesta": respuesta.content
}, ensure_ascii=False))
