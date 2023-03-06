""" This file is used to launch the Backend. """
import uvicorn
from src.run_backend import app

if __name__ == '__main__':
    uvicorn.run(app)
