""" Global variables. """
import os

# Root Path
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
# Src Path
SRC_PATH = os.path.join(ROOT_PATH, 'src/')
# Classes Path
CLASSES_PATH = os.path.join(SRC_PATH, 'classes/')
# Database Path
DATABASE_PATH = os.path.join(SRC_PATH, 'database/')

# Database File Path
DATABASE_FILE = os.path.join(DATABASE_PATH, 'database.sql')
