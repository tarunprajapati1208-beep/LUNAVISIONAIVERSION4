import rasterio
import numpy as np
import pandas as pd
import cv2
import os

# Core Space Data Ingestion Module
# Lead Architect: Bhaumik Nandha

class LunarDataLoader:
    def __init__(self):
        pass

    def load_tiff_layer(self, file_path, target_shape=(200, 200)):
        """Parses ISRO GeoTIFF (.tif) files (Track 4)."""
        if not os.path.exists(file_path):
            print(f"Critical Error: Telemetry file {file_path} missing.")
            return None
        try:
            with rasterio.open(file_path) as src:
                band1 = src.read(1)
                band1 = np.nan_to_num(band1)
                return cv2.resize(band1, target_shape, interpolation=cv2.INTER_AREA)
        except Exception as e:
            print(f"TIFF Parsing Exception: {e}")
            return None

    def load_binary_dat(self, file_path, target_shape=(200, 200)):
        """Decodes Raw Binary (.dat) matrices (Track 1)."""
        if not os.path.exists(file_path):
            return None
        try:
            raw_data = np.fromfile(file_path, dtype=np.float32)
            num_elements = len(raw_data)
            side = int(np.sqrt(num_elements))
            
            if side * side == num_elements:
                grid_data = raw_data.reshape((side, side))
            else:
                grid_data = raw_data[:target_shape[0]*target_shape[1]].reshape(target_shape)
                
            grid_data = np.nan_to_num(grid_data)
            return cv2.resize(grid_data, target_shape, interpolation=cv2.INTER_AREA)
        except Exception as e:
            print(f"Binary Decode Exception: {e}")
            return None

    def load_geometry_csv(self, file_path):
        """Extracts spatial coordinate grids."""
        try:
            df = pd.read_csv(file_path)
            return df.to_dict(orient='records')
        except Exception as e:
            print(f"Geometry Parsing Error: {e}")
            return []