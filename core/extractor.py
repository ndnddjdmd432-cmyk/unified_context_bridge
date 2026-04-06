import os
from pathlib import Path
from typing import List, Dict, Optional

class LocalExtractor:
    """
    The Extractor module for the Unified Context Bridge.
    Pulls local project state and conversation history.
    """

    def __init__(self, target_path: str, supported_extensions: Optional[List[str]] = None):
        self.target_path = Path(target_path)
        # Targeting common dev extensions to minimize 'context rot'[cite: 95].
        self.supported_extensions = supported_extensions or ['.py', '.md', '.txt', '.json']

    def _is_valid_file(self, file_path: Path) -> bool:
        """Filters out hidden files and noise (venv, git, pycache)[cite: 15]."""
        if file_path.name.startswith('.') or 'venv' in file_path.parts or '__pycache__' in file_path.parts:
            return False
        return file_path.suffix in self.supported_extensions

    def extract_context(self) -> str:
        """Concatenates file contents into a single formatted string[cite: 223]."""
        if not self.target_path.exists():
            raise FileNotFoundError(f"Path {self.target_path} not found.")

        extracted_data = []
        for root, _, files in os.walk(self.target_path):
            for file in files:
                file_path = Path(root) / file
                if self._is_valid_file(file_path):
                    content = self._read_file(file_path)
                    extracted_data.append(content)
        return "\n\n".join(extracted_data)

    def _read_file(self, file_path: Path) -> str:
        """Reads file and wraps it in Markdown for the LLM[cite: 229]."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f"### File: {file_path.name} ###\n```\n{f.read()}\n```"
        except Exception as e:
            return f"### File: {file_path.name} ###\n[Error reading file: {e}]"

if __name__ == "__main__":
    # Test the module by extracting context from the current directory.
    extractor = LocalExtractor(target_path="./")
    try:
        data = extractor.extract_context()
        print(f"--- SUCCESS ---\nExtracted {len(data)} characters of project context.")
    except Exception as err:
        print(f"--- FAILED ---\nError: {err}")
