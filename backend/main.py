""" This file is used to launch the Backend. """
import uvicorn
from src.run_api import app

if __name__ == '__main__':
    uvicorn.run(app)
