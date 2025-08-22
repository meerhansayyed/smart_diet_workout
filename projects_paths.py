import os

# Project root (folder where this file is located)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Subfolders
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
BACKEND_DIR = os.path.join(PROJECT_ROOT, "backend")
FRONTEND_DIR = os.path.join(PROJECT_ROOT, "frontend")

# Specific files
FOOD_DATASET = os.path.join(DATA_DIR, "food_dataset.csv")
