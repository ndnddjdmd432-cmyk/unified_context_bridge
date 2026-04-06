import os
import google.generativeai as genai
from typing import Optional

class LocalSummarizer:
    """
    The Summarizer module for the Unified Context Bridge.
    Engineered to solve 'Context Rot' using the Gemini 3 Flash Preview frontier model.
    """

    def __init__(self, api_key: str):
        # Initializing the BYOK (Bring Your Own Key) architecture for zero server OpEx
        genai.configure(api_key=api_key)
        # Targeting the exact 2026 preview model string provided
        self.model = genai.GenerativeModel('models/gemini-3-flash-preview')

    def generate_handover(self, raw_context: str) -> str:
        """
        Requests a strict HANDOVER.md artifact to automate the manual data handoff.
        """
        # Specialized system prompt to eliminate conversational filler and 'Al brain fry'
        system_prompt = """
        ACT AS: A deterministic 'Checkpoint-and-Rotate' daemon. 
        GOAL: Prevent session amnesia by summarizing the current project state.
        
        OUTPUT FORMAT: Generate a strict HANDOVER.md artifact with these specific headers:
        1. [Dispatch-ID]: A unique hex identifier for this state.
        2. [Completed Work]: High-density summary of implemented features/fixes.
        3. [Remaining Tasks]: Clear, technical bullet points for the next iteration.
        4. [Critical Context]: Active bug states, PIDs, and architectural constraints.
        
        STRICT RULES: No conversational filler. Technical accuracy only.
        """
        
        full_prompt = f"{system_prompt}\n\n### RAW PROJECT CONTEXT ###\n{raw_context}"
        
        try:
            # Leveraging the frontier model to handle the complex reasoning chain
            response = self.model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            return f"Summarization Error: {str(e)}"

if __name__ == "__main__":
    # Live API Key Integration
    REAL_KEY = "AIzaSyD8ZZn-rq-lTZE33XQ5wH2PNDm9g8K_Yjs"
    
    summarizer = LocalSummarizer(api_key=REAL_KEY)
    
    print("--- [Blue Ocean Orchestrator] Testing Summarizer (2026 Preview Edition) ---")
    # Simulating project state to test the 'Context Rotator' blueprint logic
    sample_context = "User is building the Unified Context Bridge. Extractor is verified. Moving to Injector."
    
    handover_artifact = summarizer.generate_handover(sample_context)
    print(f"\nGenerated HANDOVER.md Artifact:\n{'-'*30}\n{handover_artifact}\n{'-'*30}")
