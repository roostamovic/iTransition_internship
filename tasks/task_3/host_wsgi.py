import sys
import os
from fastapi import FastAPI
from starlette.middleware.wsgi import WSGIMiddleware

# Add your project directory to the path
project_dir = os.path.expanduser('~/')
sys.path.insert(0, project_dir)

# Import FastAPI app
from main import app as fastapi_app

# Wrap FastAPI inside WSGI adapter
application = WSGIMiddleware(fastapi_app)
