from textwrap import dedent
from typing import List

from crewai import LLM, Agent
from langchain.tools import BaseTool


class RecipeAgents:
    def recipe_finder(self, llm: LLM, search_tools: List[BaseTool]) -> Agent:
        return Agent(
            role="Recipe finder",
            goal="Serach the web to find high-quality cooking recipes and still obey the user demands",
            backstory=dedent(
                """
                An expert culinary researcher with the ability to find the best recipes online.
                """
            ),
            llm=llm,
            max_iter=10,
            allow_delegation=True,
            verbose=True,
            tools=search_tools,
        )
