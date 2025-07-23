import streamlit as st
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS # <-- MUDANÇA 1: Nova importação
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import DirectoryLoader, TextLoader

load_dotenv()

@st.cache_resource
def carregar_recursos():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        st.error("API Key de Google não encontrada. Por favor, configure seus 'secrets'.")
        st.stop()

    print("Carregando documentos...")
    loader = DirectoryLoader('./documentacion/', glob="**/*.md", loader_cls=TextLoader, loader_kwargs={"encoding": "utf-8"})
    documentos = loader.load()
    if not documentos:
        st.error("Não foram encontrados documentos na pasta 'documentacion'.")
        st.stop()

    print("Criando embeddings e base de dados FAISS...")
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004", google_api_key=api_key)

    # --- MUDANÇA 2: Usando FAISS em vez de Chroma ---
    # A FAISS cria o índice em memória, o que é perfeito e rápido para o Streamlit.
    vector_db = FAISS.from_documents(
        documents=documentos,
        embedding=embeddings
    )
    print("Base de dados FAISS pronta!")

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", google_api_key=api_key, temperature=0.2)

    retriever = vector_db.as_retriever(search_kwargs={"k": 3})

    prompt_template = """
    Aja como um especialista de suporte técnico amigável e prestativo. Sua tarefa é responder à pergunta do usuário baseando-se unicamente nos trechos de documentação fornecidos no contexto.
    Instruções:
    1.  Sintetize a informação de todos os trechos de contexto relevantes para formular uma resposta coesa e completa.
    2.  **Não copie e cole o texto do contexto diretamente.** Explique o processo ou a informação com suas próprias palavras, de forma clara e natural.
    3.  Se a resposta envolver um passo a passo, organize-a em uma lista numerada ou com marcadores.
    4.  Se a informação não estiver no contexto, responda educadamente: "Desculpe, não encontrei informações sobre isso em minha base de conhecimento."

    Contexto:
    {context}

    Pergunta do Usuário:
    {question
