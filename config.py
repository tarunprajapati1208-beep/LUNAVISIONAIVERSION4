import os

# --- LUNAVISION AI CONFIGURATION ---
# Professional Deployment: Bhaumik Nandha

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Data Directories
DATA_DIR = os.path.join(BASE_DIR, "lunar_data")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")

# Output Directories
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
REPORTS_DIR = os.path.join(OUTPUT_DIR, "reports")
IMAGES_DIR = os.path.join(OUTPUT_DIR, "images")

# Ensure directories exist
for directory in [RAW_DATA_DIR, PROCESSED_DATA_DIR, REPORTS_DIR, IMAGES_DIR]:
    os.makedirs(directory, exist_ok=True)

# AI Models & Processing Config
TARGET_SHAPE = (200, 200)
PIXEL_RESOLUTION_M = 5.0