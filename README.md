# Unified Context Bridge 🌉

A localized, zero-server-OpEx utility designed to cure AI "Context Rot" and eliminate the manual "Copy-Paste Chasm" for solo developers in the 2026 AI landscape.

## The Problem
Developers suffer from "AI brain fry" caused by manually copying code into browser-based LLMs, losing project context, and fighting broken session states when AI memory compacts at 80% capacity. 

## The Solution
This tool acts as a deterministic "Checkpoint-and-Rotate" daemon:
1. **Extracts** your local project state.
2. **Summarizes** the logic via Gemini 3 Flash into a dense `HANDOVER.md` artifact.
3. **Injects** the state directly into your clipboard for a lossless session transfer.

## Installation
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file in the root directory and add your key: `GEMINI_API_KEY="your_api_key_here"`

## Usage
Run the bridge from your terminal:
```bash
python main.py
```
Your project state will be summarized and placed into your clipboard, ready to paste into your next AI session.
