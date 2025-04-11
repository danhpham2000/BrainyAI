import chromadb
from langchain_chroma import Chroma
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

def load_pdf() -> Chroma:
    pdf_folder_path = "../documents"
    documents = []
    for file in os.listdir(pdf_folder_path):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder_path, file)
            loader = PyPDFLoader(pdf_path)
            documents.extend(loader.load())

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
    chunked_documents = text_splitter.split_documents(documents)
    chroma_client = chromadb.Client()

    if chroma_client.list_collections():
        study_collection = chroma_client.create_collection("study-collection")
    else:
        print("Collection exists already")
    
    vectordb = Chroma.from_documents(documents=chunked_documents, embedding=OpenAIEmbeddings(api_key=openai_api_key),
                                     persist_directory="../chromastore")
        
    return vectordb


load_pdf()