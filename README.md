# 🌟 AI Code Quality Analyzer
A Full-Stack Python Application for Static Analysis, Code Refactoring & Intelligent Code Quality Insights

## 📌 Project Overview
The **AI Code Quality Analyzer** evaluates, scores, and improves Python code using:
- Static analysis  
- AST-based linting (Pylint-like logic)  
- Cyclomatic complexity (Radon)  
- A custom heuristic AI refactoring engine  

This tool provides actionable insights and auto-refactored Python code—without heavy ML models.  

---

## 🚀 Key Features
### ✅ Static Code Analysis (Radon)
- Cyclomatic Complexity (McCabe Algorithm)  
- Maintainability Index  
- Grade-based evaluation (A–F)  

### ✅ AST-Based Linting Engine
Detects:
- Naming violations  
- Deep nesting  
- Duplicate logic  
- Unused imports/variables  
- Inefficient loops  
- Magic numbers  
- Unreachable code  

### ✅ Heuristic AI Refactoring Engine
- Renames ambiguous variables  
- Converts loops → list comprehensions  
- Removes redundancy  
- Suggests modularization  
- Adds best-practice explanations  

### ✅ Authentication System
- Login / Register  
- Session-based authentication  

### ✅ Lightweight, Responsive UI
- HTML + CSS  
- No JavaScript  
- Jinja2 templates  

### ✅ SQLite Storage
Stores:
- User data  
- Code submissions  
- Complexity results  
- Lint reports  
- Refactored code  

### ✅ Deployment Ready
- Hosted on **Render**  
- **Gunicorn** WSGI server  

---

## 🧠 System Architecture
Layers:
1. Frontend – HTML/CSS  
2. Backend – Flask  
3. Static Analysis – Radon + AST  
4. AI Engine – Heuristic rules  
5. Database – SQLite  
6. Deployment – Render + Gunicorn  

---

## 🏗 Architecture Diagram
```
User Browser (HTML + CSS)
        |
        v
+------------------------+
|        Flask App       |
| Routes | Auth | Views  |
+------------------------+
        |          
        v
+------------------------+      +------------------------+
|       Radon Engine     |      |    AST Linting Engine  |
+------------------------+      +------------------------+
        |                            |
        +-------------+--------------+
                      |
                      v
           +------------------------+
           | Heuristic AI Engine   |
           +------------------------+
                      |
                      v
           +------------------------+
           |      SQLite DB        |
           +------------------------+
```

---

## 📂 Project Structure
```
📁 project/
│── app.py
│── analysis/
│   ├── radon_engine.py
│   ├── ast_linter.py
│   ├── heuristic_ai.py
│── templates/
│   ├── index.html
│   ├── analyze.html
│   ├── history.html
│── static/
│   ├── style.css
│── database.db
│── requirements.txt
│── README.md
│── gunicorn_config.py
```

---

## ⚙ How It Works
1. User submits Python code  
2. Preprocessing  
3. Radon Complexity Analysis  
4. AST Linting  
5. AI Refactoring Engine  
6. Save results to SQLite  
7. Render results  

---

## 🗄 Database Schema
### Users Table
- id  
- name  
- email  
- password_hash  
- created_at  

### History Table
- id  
- user_id  
- original_code  
- complexity_score  
- lint_report  
- ai_improved_code  
- timestamp  

---

## 📦 Installation
```
git clone https://github.com/yourusername/ai-code-quality-analyzer.git
cd ai-code-quality-analyzer
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

---

## 🌐 Deployment (Render)
**Build Command:**
```
pip install -r requirements.txt
```
**Start Command:**
```
gunicorn app:app
```

---

## 🧪 Technologies Used
| Component | Technology |
|----------|------------|
| Backend | Flask |
| Complexity | Radon |
| Linting | Python AST |
| Refactoring | Heuristic Rule Engine |
| Database | SQLite |
| Templates | Jinja2 |
| Deployment | Render |
| Server | Gunicorn |

---

## 🧩 Future Improvements
- ML-powered code suggestions  
- Multi-language support  
- More refactoring rules  
- CI/CD integration  

---

## ⭐ Why This Project Stands Out
This is a production-level system demonstrating:
- Backend engineering  
- Static analysis  
- AST processing  
- Rule-based AI  
- Database design  
- Deployment skills  
- Full-stack development  

