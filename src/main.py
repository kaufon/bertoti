from fastapi import FastAPI

from controllers.request_recipes_controller import RequestRecipeController

app = FastAPI()
RequestRecipeController(app)
