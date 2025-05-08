from typing import Any

from crewai.tools import tool
from langchain.tools import DuckDuckGoSearchRun


class RecipeTools:
    @tool("search the web for online recipes")
    def search_web(self, query: str) -> Any:
        search_tool = DuckDuckGoSearchRun()
