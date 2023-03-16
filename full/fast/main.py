from fastapi import FastAPI
from .models import Base
from ..core.models import HealthCheck
from ..core.db import async_engine
from .routers import staff, todos
import uvicorn
#from ..core.config import settings


app = FastAPI()

Base.metadata.create_all(bind=async_engine)

app.include_router(staff.router, tags=["staff"])
# app.include_router(todos.router, tags=["todos"])

# @app.get("/", response_model=HealthCheck, tags=["status"])
# async def health_check():
#     return {
#         "name": core.config.settings.project_name,
#         "version": core.config.settings.version,
#         "description": core.config.settings.description
#     }

# if __name__ == "__main__":
#     uvicorn.run(app, host=settings.host, port=settings.port)
