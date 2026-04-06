import os
from dotenv import load_dotenv
from core.extractor import LocalExtractor
from core.summarizer import LocalSummarizer
from core.injector import LocalInjector

# Load the secure environment variables from the .env file
load_dotenv()

def run_bridge():
    # 1. SETUP - Pulling the key securely from the environment
    API_KEY = os.getenv("GEMINI_API_KEY")
    TARGET_DIR = "./"  
    
    if not API_KEY:
        print("CRITICAL ERROR: GEMINI_API_KEY not found in .env file.")
        return

    extractor = LocalExtractor(target_path=TARGET_DIR)
    summarizer = LocalSummarizer(api_key=API_KEY)
    injector = LocalInjector()

    print("--- [Unified Context Bridge] Initializing Secure Handoff ---")

    # 2. EXTRACT 
    print("[1/3] Extracting local context...")
    raw_data = extractor.extract_context()

    # 3. SUMMARIZE 
    print("[2/3] Generating HANDOVER.md via Gemini 3 Flash Preview...")
    handover_content = summarizer.generate_handover(raw_data)

    # 4. INJECT 
    print("[3/3] Injecting state to clipboard and local file...")
    injector.write_to_file(handover_content)
    if injector.inject_to_clipboard(handover_content):
        print("\nSUCCESS: Secure Bridge Complete!")
        print("Your HANDOVER.md is in your clipboard.")
        print("-" * 40)
        print(handover_content[:200] + "...")

if __name__ == "__main__":
    run_bridge()
