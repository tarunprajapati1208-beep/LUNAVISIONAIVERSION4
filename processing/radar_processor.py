import numpy as np

# DFSAR Polarimetric Analysis Engine
# Lead Architect: Bhaumik Nandha

class RadarProcessor:
    def __init__(self):
        pass

    def calculate_cpr(self, same_polarization, cross_polarization):
        """Calculates Circular Polarization Ratio (CPR) for volatile detection."""
        epsilon = 1e-6
        cpr = same_polarization / (cross_polarization + epsilon)
        return np.clip(cpr, 0.0, 3.0) # Clip extreme noise outliers

    def calculate_backscatter_coefficient(self, radar_intensity):
        """Converts raw radar return signal to Decibels (dB)."""
        epsilon = 1e-6
        return 10 * np.log10(radar_intensity + epsilon)

    def extract_ice_indicators(self, cpr, db, hazard_map):
        """Isolates true subsurface ice by crossing radar signatures with terrain safety."""
        ice_probability = np.zeros_like(cpr, dtype=np.float32)
        
        # Core Logic: High CPR + safe flat terrain = Subsurface Volatiles
        ice_condition = (cpr > 0.8) & (db > -15) & (hazard_map == 0)
        
        ice_probability[ice_condition] = (cpr[ice_condition] / 3.0) * 100
        return np.clip(ice_probability, 0, 100)

    def process_all(self, sp_data, op_data, hazard_map):
        """Executes full radar analysis pipeline."""
        cpr = self.calculate_cpr(sp_data, op_data)
        db = self.calculate_backscatter_coefficient(sp_data)
        ice_prob = self.extract_ice_indicators(cpr, db, hazard_map)
        
        return {
            "cpr": cpr,
            "backscatter_db": db,
            "ice_probability": ice_prob
        }