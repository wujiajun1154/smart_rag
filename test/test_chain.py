
import warnings
warnings.filterwarnings("ignore", message=".*LangChainDeprecationWarning.*")

from my_rag.core_chain import build_qa_chain
from my_rag.embedding import build_vector_store, get_retriever
from langchain_core.documents import Document

def test_chain():
    docs = [
        Document(page_content="强化学习（Reinforcement Learning, RL）是让智能体在环境中通过试错获得最大累积奖励的机器学习方法。", metadata={"source": "dummy1"}),
        Document(page_content="与监督学习不同，强化学习不需要人工标注数据，而是依靠奖励信号进行策略优化。", metadata={"source": "dummy2"})
    ]

    vector_store = build_vector_store(docs, collection_name="test_core")
    retriever = get_retriever(vector_store, top_k=2)

    chain = build_qa_chain(retriever)

    q1 = "什么是强化学习？"
    ans1 = chain.invoke({"question": q1})["answer"]
    print("【第一轮】")
    print("Q:", q1)
    print("A:", ans1, "\n")

    q2 = "它与监督学习有何不同？"
    ans2 = chain.invoke({"question": q2})["answer"]
    print("【第二轮】")
    print("Q:", q2)
    print("A:", ans2)

if __name__ == "__main__":
    test_chain()