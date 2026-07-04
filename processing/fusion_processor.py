import numpy as np

# Multi-Modal Tensor Fusion Engine
# Lead Architect: Bhaumik Nandha

class FeatureFusionProcessor:
    def __init__(self):
        pass

    def normalize_array(self, array):
        """Scales dimensional metrics between 0.0 and 1.0 for Neural Network stability."""
        min_val = np.min(array)
        max_val = np.max(array)
        if max_val - min_val == 0:
            return np.zeros_like(array)
        return (array - min_val) / (max_val - min_val)

    def fuse_features(self, slope, roughness, cpr):
        """
        Fuses topographical and polarimetric layers into a unified 3D Tensor.
        Output Shape Requirement: (Height, Width, 3) 
        """
        norm_slope = self.normalize_array(slope)
        norm_rough = self.normalize_array(roughness)
        norm_cpr = self.normalize_array(cpr)
        
        # Deep algorithmic stacking for U-Net AI ingestion
        fused_tensor = np.dstack((norm_slope, norm_rough, norm_cpr))
        return fused_tensor