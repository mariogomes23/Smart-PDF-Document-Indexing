import pandas as pd
import streamlit as st
from io import StringIO
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from groq import Groq

# Carregar variáveis de ambiente
load_dotenv()
api_key = os.environ.get("GROQ_API_KEY")

def get_groq_client(api_key):
    """Cria e retorna um cliente Groq autenticado com a chave da API fornecida."""
    return Groq(api_key=api_key)

def extract_pdf_text(pdf_file):
    """Extrai texto de um arquivo PDF."""
    try:
        pdf_reader = PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        st.error(f"Erro ao extrair texto do PDF: {e}")
        return None

def identify_document_type(text, client):
    """Identifica o tipo de documento com base no texto extraído."""
    try:
        prompt = f"""
        O seguinte texto foi extraído de um documento PDF:
        {text[:2000]}  # Limite de caracteres para evitar excesso de dados.

        Baseado no conteúdo, identifique o tipo de documento (ex.: Contrato, Fatura, Relatório, etc.) e explique o motivo da identificação.
        """
        with st.spinner("Analisando o tipo de documento..."):
            response = analyze_with_groq(client, prompt)
        return response
    except Exception as e:
        st.error(f"Erro ao identificar o tipo de documento: {e}")
        return None

def analyze_with_groq(client, content_to_analyze):
    """Chama a API Groq para obter uma resposta com base no conteúdo analisado."""
    chat_completion = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": content_to_analyze
        }],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

def main():
    if not api_key:
        st.error("A chave de API da Groq não foi encontrada. Verifique o arquivo .env.")
        return

    client = get_groq_client(api_key)

    st.set_page_config(page_title="Indexação Inteligente de Documentos PDF")
    st.header("Indexação Inteligente de Documentos PDF")
    
    pdf_file = st.file_uploader("Carregar arquivo PDF", type="pdf")
    if pdf_file:
        pdf_text = extract_pdf_text(pdf_file)
        if pdf_text:
            st.write("Texto extraído do PDF:")
            st.text_area("Conteúdo do Documento", pdf_text[:5000], height=300)  # Exibe os primeiros 5000 caracteres

            doc_type = identify_document_type(pdf_text, client)
            if doc_type:
                st.success("Tipo de Documento Identificado:")
                st.write(doc_type)

if __name__ == "__main__":
    main()
