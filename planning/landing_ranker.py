import numpy as np

# Autonomous Landing Site Evaluator
# Lead Architect: tarun prajapati

class LandingSiteRanker:
    def __init__(self):
        pass

    def find_best_landing_sites(self, hazard_map, ice_map, top_n=3):
        """
        Evaluates safe coordinates (where hazard == 0) closest to the highest ice concentration.
        Returns the ranked landing zones and the exact target ice coordinates.
        """
        # Identify strictly safe zones (0 = Safe, 1 = Hazard)
        safe_zones = (hazard_map == 0).astype(int)
        
        # Locate the absolute highest probability of subsurface ice
        ice_y, ice_x = np.unravel_index(np.argmax(ice_map, axis=None), ice_map.shape)
        
        # Map all valid safe coordinates
        y_indices, x_indices = np.where(safe_zones == 1)
        
        # Fallback if the entire map is hazardous
        if len(x_indices) == 0:
            return [], (ice_x, ice_y)
            
        # Compute Euclidean distance from every safe point to the target ice
        distances = np.sqrt((x_indices - ice_x)**2 + (y_indices - ice_y)**2)
        sorted_indices = np.argsort(distances)
        
        sites = []
        # Filter for top N coordinates, spreading them out to find distinct zones
        for i in range(min(top_n, len(sorted_indices))):
            idx = sorted_indices[i * 50]  # Spatial jump to avoid picking adjacent pixels
            sites.append({
                "rank": i + 1,
                "x": int(x_indices[idx]),
                "y": int(y_indices[idx]),
                "distance_to_ice": float(distances[idx])
            })
            
        return sites, (ice_x, ice_y)