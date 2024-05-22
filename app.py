from fastapi import FastAPI
from center.router import center_app
import uvicorn 

app = FastAPI()

app.include_router(center_app, prefix ="/centers")


if __name__=="__main__":
    uvicorn.run(
        "app:app",
        host="localhost",
        port=8000,
        reload=True,
    )
