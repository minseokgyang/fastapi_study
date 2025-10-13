import app
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from app.configs.tortoise_config import initialize_tortoise




app = FastAPI(
    default_response_class=ORJSONResponse
)

initialize_tortoise(app)
print("나는 app/__init__이야",__name__)

