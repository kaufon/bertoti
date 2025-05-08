from fastapi import FastAPI


class RequestRecipeController:
    def __init__(self, app: FastAPI):
        @app.get("/recipes")
        async def _(request: str):
            return self.handle(request)

    def handle(self, request: str):
        return request
