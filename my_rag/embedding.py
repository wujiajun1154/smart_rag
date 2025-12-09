import os
from typing import List

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from my_rag.web_catch import TavilyWebSearch

os.environ["USER_AGENT"] = "rag-chatbot/0.1"
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

def build_vector_store(docs:List[Document],collection_name: str = "default",) -> Chroma :
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=40
    )
    chunks = splitter.split_documents(docs)
    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-zh-v1.5", cache_folder="./model_cache"
    )
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=collection_name,
    )
    return vector_store

def get_retriever(vector_store:Chroma,top_k:int = 4):
    return vector_store.as_retriever(search_kwargs={"k": top_k})


if __name__ == "__main__":
    loader = TavilyWebSearch()
    docss = loader.load_docs('什么是强化学习')
    vector_store = build_vector_store(docss)
    retriever = get_retriever(vector_store, top_k=4)
    query = "强化学习中的 reward 是什么？"
    hits = retriever.invoke(query)
    print(f"\nRetriever 返回 {len(hits)} 段相关文字：")
    for i, h in enumerate(hits, 1):
        print(f"\n--- 第 {i} 段 ---")
        print(h.page_content[:300], "..." if len(h.page_content) > 300 else "")