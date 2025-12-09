from typing import List
import bs4
from langchain_community.document_loaders import WebBaseLoader
from tavily import TavilyClient
from utils.env_utils import TAVILY_KEY


class TavilyWebSearch:
    """
    Tavily搜索top-3URL
    WebBaseLoader解析文章
    """
    def __init__(self):
        tavily_key = TAVILY_KEY
        self.tavily = TavilyClient(api_key=tavily_key)

    def _search_top3_urls(self, query:str)->List[str]:
        resp = self.tavily.search(query=query,
                                  max_results=5,
                                  include_domains=[]
                                  )
        return [item['url'] for item in resp.get('results', [])]

    def _web_catch(self, urls:List[str]):
        """
        爬取前三urls
        生成List[Document]
        """
        loader = WebBaseLoader(
            web_paths=urls[:3],
            bs_kwargs=dict(
                parse_only=bs4.SoupStrainer(
                    ["main", "article", "div"],
                    class_=lambda x: x
                                     and any(
                        k in x
                        for k in (
                            "content",
                            "body",
                            "post",
                            "main",
                            "mw-parser-output",
                            "layout-content",
                        )
                    ),
                )
            ),
        )
        docs = loader.load()
        return docs

    def load_docs(self,query:str) -> List:
        urls = self._search_top3_urls(query)
        return self._web_catch(urls)

if __name__ == '__main__':
    loader = TavilyWebSearch()
    docss = loader.load_docs('什么是强化学习')
    for doc in docss:
        print(doc)

