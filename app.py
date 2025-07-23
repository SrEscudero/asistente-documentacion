import streamlit as st
import os
import nest_asyncio EA
nest_asyncio.apply() 
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS 
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
    {question}

    Resposta do Especialista:
    """
    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": PROMPT}
    )
    return qa_chain

# --- INTERFAZ DE STREAMLIT ---
st.title("🤖 Assistente de Documentação Interna")
st.caption("Faça perguntas em português sobre a documentação do projeto.")

try:
    chain = carregar_recursos()
except Exception as e:
    st.error(f"Ocorreu um erro ao carregar os recursos: {e}")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Qual é a sua pergunta?"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("Analisando documentos..."):
        response = chain.invoke(prompt)
        ai_response = response['result']

    st.session_state.messages.append({"role": "assistant", "content": ai_response})

    st.rerun()
