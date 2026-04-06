import pyperclip
from pathlib import Path

class LocalInjector:
    """
    The Injector module for the Unified Context Bridge.
    Automates state injection to eliminate 'Al brain fry'.
    """

    def inject_to_clipboard(self, content: str) -> bool:
        """
        Pushes the handover artifact directly to the system clipboard.
        Eliminates the manual 'highlight and copy' bottleneck.
        """
        try:
            pyperclip.copy(content)
            return True
        except Exception as e:
            print(f"Clipboard Error: {e}")
            return False

    def write_to_file(self, content: str, filename: str = "HANDOVER.md") -> str:
        """
        Persists the state to a local file to prevent session amnesia.
        """
        file_path = Path(filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return str(file_path.absolute())

if __name__ == "__main__":
    injector = LocalInjector()
    test_text = "# 2026 HANDOVER\nStatus: Clipboard & File Injection Operational."
    
    print("--- [Blue Ocean Orchestrator] Testing Full Injector ---")
    if injector.inject_to_clipboard(test_text):
        print("Success: Test text is now in your clipboard!")
    
    file_loc = injector.write_to_file(test_text)
    print(f"Success: Handover file saved to: {file_loc}")
