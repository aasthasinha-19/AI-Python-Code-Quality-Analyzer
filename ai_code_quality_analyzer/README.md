# AI Code Quality Analyzer (Complete)

This project analyzes Python code for complexity, linting, and provides heuristic AI suggestions.
It includes:
- Flask web app with login/register/history
- SQLite storage (users.db created on first run)
- Unicode-safe PDF reports (fpdf2)
- Radon (complexity) and pylint (linting)
- Heuristic AI fallback (works without transformers/torch)

Quick start (Windows):
1. Open PowerShell in the project directory.
2. Run `.un.bat` (this creates a .venv, installs deps, and runs the app).
3. Open http://127.0.0.1:5000 in your browser.

Included screenshot (if present):
static/images/screenshot.png (copied from /mnt/data/Screenshot 2025-11-21 234502.png)

Note: Transformers and torch are not included by default. Install separately if desired.
