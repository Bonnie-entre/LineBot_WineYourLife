import uvicorn
from fastapi import FastAPI
from routers import webhooks

app = FastAPI()

app.include_router(webhooks.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=80, reload=True)