
  🚀 AI Python Code Quality Analyzer

A fully featured web-based tool built with Flask, NLP heuristics, Radon, Pylint, and SQLite to analyze Python code for quality, complexity, lint issues, and generate improved refactored versions.

This is a powerful portfolio project designed for Data Science, Python Developer, and AI/ML Engineer roles.

🌟 Features

✔ User Authentication (Register/Login/Logout)
✔ Dashboard with "Welcome, <username> 👋" UI
✔ Paste Python code → get full analysis
✔ Complexity metrics via Radon
✔ Linting report via Pylint
✔ AI-powered improvements (heuristic refactor engine)
✔ AI Summary: Issues, smells, recommendations
✔ User History stored in SQLite
✔ Responsive UI (Mobile friendly)
✔ Modern clean UI with custom styling
✔ Zero JS (pure HTML/CSS + Flask)

🧠 Tech Stack

Backend: Python, Flask

Database: SQLite

Static Analysis: Radon (Cyclomatic Complexity), Pylint

AI Logic: Heuristic refactoring engine

Deployment: Gunicorn (for production), Render YAML

UI: Pure HTML + CSS (no JavaScript!)

📂 Project Structure
ai_code_quality_analyzer/
│
├── app.py
├── database.py
├── requirements.txt
├── Procfile
├── render.yaml
├── README.md
│
├── utils/
│   ├── complexity.py
│   ├── linting.py
│   └── ai_suggestions.py
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── index.html
│   ├── history.html
│   └── history_view.html
│
└── static/
    ├── style.css
    └── images/
        └── screenshot.png

🚀 Getting Started (Local Setup)
1️⃣ Clone the Repository
git clone https://github.com/aasthasinha-19/ai_code_quality_analyzer.git
cd ai_code_quality_analyzer

2️⃣ Create Virtual Environment
python -m venv .venv

3️⃣ Activate venv

Windows

.\.venv\Scripts\activate


Mac/Linux

source .venv/bin/activate

4️⃣ Install Requirements
pip install --upgrade pip
pip install -r requirements.txt

5️⃣ Run the App
python app.py


Open in browser:
👉 http://127.0.0.1:5000

📝 How It Works
🔍 1. Static Code Analysis

Your code is passed through:

Module	Purpose
Radon	Cyclomatic complexity, Maintainability index
Pylint	Coding standards, errors, formatting issues
Heuristic AI Engine	Suggests improvements, refactoring
🤖 2. AI Refactor Suggestions

The AI engine improves the code by:

Fixing poor naming

Refactoring repeated logic

Improving readability

Adding docstrings

Replacing anti-patterns

Improving loops & conditions

Adding Pythonic syntax

🗂 3. History Saved in SQLite

Every analysis is stored, and users can view:

Original code

Complexity score

Lint report

AI summary

Improved code


