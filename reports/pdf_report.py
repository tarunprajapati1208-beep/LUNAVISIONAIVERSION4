from fpdf import FPDF
import datetime
import os

class MissionPDFReport:
    def __init__(self):
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_auto_page_break(auto=True, margin=15)

    def generate_report(self, confidence, hazards_count, landing_zone, path_length, briefing_text, slope_avg, ice_area):
        # --- HEADER ---
        self.pdf.set_font("Arial", 'B', 18)
        self.pdf.cell(200, 10, txt="LunaVisionAI - Space-Grade Tactical Mission Briefing", ln=True, align='C')
        
        self.pdf.set_font("Arial", size=10)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.pdf.cell(200, 10, txt=f"Generated: {timestamp} | Core Security Protocol: SHASHANK-AI", ln=True, align='C')
        self.pdf.cell(200, 10, txt="System Architect: Tarun Prajapati", ln=True, align='C')
        self.pdf.ln(8)
        
        # --- SECTION 1 ---
        self.pdf.set_font("Arial", 'B', 13)
        self.pdf.cell(200, 10, txt="1. Subsurface Ice Detection & Analytics", ln=True)
        self.pdf.set_font("Arial", size=11)
        self.pdf.cell(200, 8, txt=f"- Core Segmentation Network Confidence: {confidence:.2f}%", ln=True)
        self.pdf.cell(200, 8, txt=f"- High-Confidence Volatile Core Area: {ice_area} Pixel Footprint", ln=True)
        self.pdf.ln(5)
        
        # INJECTING GRAPHS (ROW 1)
        if os.path.exists("outputs/temp_ice.png") and os.path.exists("outputs/temp_cpr.png"):
            self.pdf.image("outputs/temp_ice.png", x=10, y=self.pdf.get_y(), w=90, h=65)
            self.pdf.image("outputs/temp_cpr.png", x=110, y=self.pdf.get_y(), w=90, h=65)
            self.pdf.ln(70)
        
        # --- SECTION 2 ---
        self.pdf.set_font("Arial", 'B', 13)
        self.pdf.cell(200, 10, txt="2. Landing Site & Terrain Geomorphology", ln=True)
        self.pdf.set_font("Arial", size=11)
        self.pdf.cell(200, 8, txt=f"- Selected Safety Landing Coordinate: X: {landing_zone[0]}, Y: {landing_zone[1]}", ln=True)
        self.pdf.cell(200, 8, txt=f"- Average Surface Slope: {slope_avg:.2f} Degrees", ln=True)
        self.pdf.ln(5)
        
        # INJECTING GRAPHS (ROW 2)
        if os.path.exists("outputs/temp_slope.png") and os.path.exists("outputs/temp_roughness.png"):
            self.pdf.image("outputs/temp_slope.png", x=10, y=self.pdf.get_y(), w=90, h=65)
            self.pdf.image("outputs/temp_roughness.png", x=110, y=self.pdf.get_y(), w=90, h=65)
            self.pdf.ln(70)
            
        self.pdf.add_page() # New page for remaining data
        
        # --- SECTION 3 ---
        self.pdf.set_font("Arial", 'B', 13)
        self.pdf.cell(200, 10, txt="3. Autonomous Path Planning & Hazards", ln=True)
        self.pdf.set_font("Arial", size=11)
        self.pdf.cell(200, 8, txt=f"- Total Computed Trajectory Path Length: {path_length} Waypoints", ln=True)
        self.pdf.ln(5)
        
        # INJECTING GRAPHS (ROW 3)
        if os.path.exists("outputs/temp_path.png") and os.path.exists("outputs/temp_xai.png"):
            self.pdf.image("outputs/temp_path.png", x=10, y=self.pdf.get_y(), w=90, h=65)
            self.pdf.image("outputs/temp_xai.png", x=110, y=self.pdf.get_y(), w=90, h=65)
            self.pdf.ln(70)
        
        # --- SECTION 4 ---
        self.pdf.set_font("Arial", 'B', 13)
        self.pdf.cell(200, 10, txt="4. Executive Commander Summary Vector", ln=True)
        self.pdf.set_font("Arial", size=10)
        self.pdf.multi_cell(0, 7, txt=briefing_text)
        self.pdf.ln(10)
        
        self.pdf.set_font("Arial", 'I', 9)
        self.pdf.cell(200, 10, txt="CONFIDENTIAL REPORT - OPERATED AUTOMATICALLY BY LUNAVISIONAI CORE ENGINE", ln=True, align='C')
        
        target_path = "outputs/reports/LunaVision_Final_Mission_Report.pdf"
        self.pdf.output(target_path)
        return target_path