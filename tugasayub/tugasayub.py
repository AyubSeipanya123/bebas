from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/{nim}/{nama}")
async def identitas(nim: int, nama: str):
    return{"nim": {nim}, "nama": {nama}}