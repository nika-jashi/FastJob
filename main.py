from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware

from apis.base import api_router
from core.config import settings
from db.sessions import engine
from db.base import Base


def include_router(app):
    app.include_router(api_router)


def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def create_tables():
    print("create_tables")
    Base.metadata.create_all(bind=engine)


middleware = [
    Middleware(AuthenticationMiddleware, backend=None)
]


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION, middleware=middleware)
    include_router(app)
    configure_static(app)
    create_tables()
    return app


app = start_application()
