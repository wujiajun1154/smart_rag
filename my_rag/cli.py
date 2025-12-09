# import os
# import sys
# from typing import List
# from langchain_core.documents import Document
# from my_rag.web_catch import TavilyWebSearch
# from my_rag.embedding import build_vector_store, get_retriever
# from my_rag.core_chain import build_qa_chain
# import warnings
# warnings.filterwarnings("ignore", message=".*LangChainDeprecationWarning.*")
# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#
# chain = None
#
# def init_chain(topic: str):
#     global chain
#     if chain is None:
#         print(f"🔄 首次搜索：{topic}")
#         docs: List[Document] = TavilyWebSearch().load_docs(topic)
#         if not docs:
#             print("未抓到任何文档，程序终止。")
#             sys.exit(1)
#         vector_store = build_vector_store(docs, collection_name="cli_rag")
#         chain = build_qa_chain(get_retriever(vector_store, top_k=4))
#     return chain
#
# def main():
#     print("🤖 已就绪，输入 quit 退出。\n")
#     while True:
#         q = input("User: ").strip()
#         if q.lower() in {"quit"}:
#             print("👋  再见！")
#             break
#         current_chain = init_chain(q)
#         ans = current_chain.invoke({"question": q})["answer"]
#         print(f"Bot: {ans}\n")
#
# if __name__ == "__main__":
#     main()