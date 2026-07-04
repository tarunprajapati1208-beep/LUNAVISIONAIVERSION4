import os
import numpy as np
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

class MissionCommanderAgent:
    def __init__(self, api_key=None):
        GOOGLE_API_KEY = ""
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro", 
            google_api_key=self.api_key,
            temperature=0.15
        )

    def generate_briefing(self, slope, hazards, ice_map):
        """Generates a professional mission report using Gemini."""
        avg_slope = np.mean(slope)
        max_slope = np.max(slope)
        hazard_ratio = (np.sum(hazards) / hazards.size) * 100
        peak_ice_conf = np.max(ice_map)

        # FIXED: Prompt Template variables matched exactly with invocation keys
        template = """
        SYSTEM ROLE: Lead Lunar Mission Commander (AI Analysis Engine).
        PROJECT LEAD: Tarun Prajapati.
        
        Analyze the following telemetry data from the Lunar South Pole:
        - Average Terrain Slope: {avg_slope:.2f}° (Max: {max_slope:.2f}°)
        - Hazardous Region Density: {hazard_ratio:.2f}% of operational area.
        - Peak Subsurface Ice Confidence: {peak_ice_conf:.2f}%
        
        TASK:
        Provide a concise, 3-bullet-point executive briefing for ISRO control.
        Detail the landing viability, rover traversal risks, and ice harvesting potential. 
        Keep the tone professional, urgent, and scientific.
        """
        
        prompt = PromptTemplate.from_template(template)
        chain = prompt | self.llm
        
        try:
            response = chain.invoke({
                "avg_slope": avg_slope, 
                "max_slope": max_slope,
                "hazard_ratio": hazard_ratio, 
                "peak_ice_conf": peak_ice_conf
            })
            return response.content
        except Exception as e:
            return f"Commander Briefing Failed: {str(e)}"