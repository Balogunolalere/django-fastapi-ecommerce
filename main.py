from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
import os
import django
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
from fastapi.staticfiles import StaticFiles
from store.api import router as store_router


django_app = get_wsgi_application()

app = FastAPI()

app.mount('/static', StaticFiles(directory='staticfiles'), name='static')
app.mount('/media', StaticFiles(directory='media'), name='media')

@app.get("/")
async def root():
    return {"message": "Hello World"}


app.mount("/django", WSGIMiddleware(django_app))
app.include_router(store_router, prefix="/api")