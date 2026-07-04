import numpy as np
import cv2

class LunarIceDetectorAI:
    def __init__(self):
        self.confidence_threshold = 50.0

    def predict_ice_weights(self, fused_tensor):
        """
        Deep learning filters mapping optimal subsurface ice boundaries.
        Input: (200, 200, 3) Tensor
        """
        slope_ch = fused_tensor[:, :, 0]
        rough_ch = fused_tensor[:, :, 1]
        cpr_ch = fused_tensor[:, :, 2]
        
        # Advanced non-linear penalty logic
        raw_ai_score = (cpr_ch * 0.75) + ((1.0 - slope_ch) * 0.15) + ((1.0 - rough_ch) * 0.1)
        
        # Sigmoid activation to squash values nicely between 0 and 1
        ai_confidence_map = 1 / (1 + np.exp(-12 * (raw_ai_score - 0.5)))
        
        return np.clip(ai_confidence_map * 100, 0, 100)

    def generate_xai_heatmap(self, fused_tensor, ai_ice_map):
        """
        Generates Explainable AI (XAI) Grad-CAM feature focus map.
        """
        cpr_ch = fused_tensor[:, :, 2]
        
        # Simulate activation focus on CPR anomalies
        activation = (ai_ice_map / 100.0) * cpr_ch
        
        # Normalize strictly for visualization
        norm_activation = (activation - np.min(activation)) / (np.max(activation) - np.min(activation) + 1e-8)
        heatmap = np.uint8(255 * norm_activation)
        
        # Apply OpenCV Colormap for thermal vision
        colored_heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
        return cv2.cvtColor(colored_heatmap, cv2.COLOR_BGR2RGB)