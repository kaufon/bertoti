from os import getenv

from crewai import LLM

from ai.agents import RecipeAgents
from ai.tools import RecipeTools


class RecipeCrew:
    def __init__(self) -> None:
        qwen_llm = self.__get_qwen_llm()
        recipe_tools_instace = RecipeTools()
        recipe_tools = [recipe_tools_instace.search_web]
        agents = RecipeAgents()
        recipe_finder = agents.recipe_finder(qwen_llm,recipe_tools)

    def __get_qwen_llm(self) -> LLM:
        api_key = getenv("OPEN_ROUTER_API_KEY")
        llm = LLM(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
            model="openrouter/qwen/qwq-32b:free",
            temperature=0,
        )
        return llm
