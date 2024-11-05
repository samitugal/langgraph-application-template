from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from pydantic_settings import BaseSettings

from .LLM.config_defs import LLMMainConfig
from .LLM.Pipeline import Pipeline


app = FastAPI()
load_dotenv()

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}
