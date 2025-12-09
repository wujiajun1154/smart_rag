# app.py
import gradio as gr
from my_rag.web_catch import TavilyWebSearch
from my_rag.embedding import build_vector_store, get_retriever
from my_rag.core_chain import build_qa_chain

chain = None

def init_chain(topic: str):
    global chain
    if chain is None:
        print(f"🔄 首次搜索：{topic}")
        docs = TavilyWebSearch().load_docs(topic)
        vector_store = build_vector_store(docs, collection_name="gradio")
        chain = build_qa_chain(get_retriever(vector_store, top_k=4))
    return chain

def chat(message, history):
    """
    先确保链已初始化，再回答
    """
    current_chain = init_chain(message)
    return current_chain.invoke({"question": message})["answer"]

demo = gr.ChatInterface(
    fn=chat,
    title="SmartRAG · 万能问答",
    description="输入任何主题，我会实时搜索并回答！"
)

if __name__ == "__main__":
    demo.launch()