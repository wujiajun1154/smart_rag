
from typing import List

from langchain_classic.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_classic.chains.retrieval_qa.base import RetrievalQA
from langchain_classic.memory import ConversationBufferMemory
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_openai import ChatOpenAI

from utils.env_utils import BAILIAN_API_KEY, BAILIAN_BASE_URL

_prompt = """You are a helpful assistant, always answer in Chinese.
Context:
{context}

Human: {question}
Assistant: """

prompt = PromptTemplate(
    input_variables=['context', 'question'],
    template = _prompt,
)

llm = ChatOpenAI(
    model="deepseek-r1",
    api_key=BAILIAN_API_KEY,
    base_url=BAILIAN_BASE_URL,
    temperature=0.2,
    request_timeout=30,
    max_retries=1,
)

def _format_chat_history(chat_history: List[BaseMessage]) -> str:
    buffer = ""
    for message in chat_history:
        if isinstance(message, HumanMessage):
            buffer += f"Human: {message.content}\n"
        elif isinstance(message, AIMessage):
            buffer += f"AI: {message.content}\n"
    return buffer.strip()

def build_qa_chain(retriever: VectorStoreRetriever):
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
    )
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        combine_docs_chain_kwargs={"prompt": prompt},
    )
    return chain
