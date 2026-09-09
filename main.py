from fastapi import FastAPI

from src.services.visits_service import register_visit, get_visits

app = FastAPI()


@app.get("/")
async def root():
    await register_visit("root")

    visits_count = await get_visits("root")

    return {"message": "Hello World", "visits count": visits_count}


@app.get("/hello/{name}")
async def say_hello(name: str):
    await register_visit("hello")

    visits_count = await get_visits("hello")

    return {"message": f"Hello {name}", "visits count": visits_count}


