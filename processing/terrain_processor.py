import numpy as np
import cv2

# Planetary Geomorphology Engine
# Lead Architect: Bhaumik Nandha

class TerrainProcessor:
    def __init__(self, pixel_resolution=5.0):
        self.res = pixel_resolution

    def calculate_slope(self, dem):
        """Calculates exact surface slope in degrees using Sobel spatial gradients."""
        dz_dx = cv2.Sobel(dem, cv2.CV_64F, 1, 0, ksize=3) / (8 * self.res)
        dz_dy = cv2.Sobel(dem, cv2.CV_64F, 0, 1, ksize=3) / (8 * self.res)
        
        gradient_magnitude = np.sqrt(dz_dx**2 + dz_dy**2)
        slope_rad = np.arctan(gradient_magnitude)
        return np.degrees(slope_rad)

    def calculate_roughness(self, dem, window_size=5):
        """Computes standard deviation of elevation (boulder/crater mapping)."""
        mean = cv2.blur(dem, (window_size, window_size))
        mean_sq = cv2.blur(dem**2, (window_size, window_size))
        variance = mean_sq - mean**2
        variance[variance < 0] = 0  
        return np.sqrt(variance)

    def generate_hazard_map(self, slope, roughness, slope_threshold=15.0, roughness_threshold=1.5):
        """Generates binary danger zones (1 = Hazardous, 0 = Safe)."""
        hazard_map = np.zeros_like(slope, dtype=np.uint8)
        hazard_map[(slope > slope_threshold) | (roughness > roughness_threshold)] = 1
        return hazard_map

    def process_all(self, dem_data):
        """Executes full terrain analysis pipeline."""
        slope = self.calculate_slope(dem_data)
        roughness = self.calculate_roughness(dem_data)
        hazards = self.generate_hazard_map(slope, roughness)
        
        return {
            "slope": slope,
            "roughness": roughness,
            "hazards": hazards
        }