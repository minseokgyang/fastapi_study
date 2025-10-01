from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

app = FastAPI(
    default_response_class=ORJSONResponse
)

print("나는 app/__init__이야",__name__)

