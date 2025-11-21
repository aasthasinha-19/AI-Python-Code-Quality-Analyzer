from flask import Flask, render_template, request, redirect, session, send_file, url_for
from utils.complexity import get_complexity
from utils.linting import analyze_lint
from utils.ai_suggestions import improve_code, summarize_issues
from database import init_db, register_user, validate_user, save_history, get_user_history, get_history_entry
import tempfile, json, os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

init_db()

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email','').strip().lower()
        pw = request.form.get('password','')
        name = validate_user(email, pw)
        if name:
            session['user'] = name
            session['email'] = email
            return redirect(url_for('index'))
        return render_template('login.html', error="Invalid email or password")
    return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name','').strip()
        email = request.form.get('email','').strip().lower()
        pw = request.form.get('password','')
        if not name or not email or not pw:
            return render_template('register.html', error="Please fill all fields")
        if register_user(name, email, pw):
            return redirect(url_for('login'))
        return render_template('register.html', error="Email already exists")
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/')
def index():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'user' not in session:
        return redirect(url_for('login'))
    code = request.form.get('code','')
    complexity = get_complexity(code)
    lint = analyze_lint(code)
    summary = summarize_issues(code)
    improved = improve_code(code)
    save_history(session['email'], code, complexity, lint, summary, improved)
    results = {"complexity": complexity, "lint": lint, "summary": summary, "improved": improved}
    return render_template('index.html', results=results, original_code=code)

@app.route('/history')
def history():
    if 'user' not in session:
        return redirect(url_for('login'))
    records = get_user_history(session['email'])
    return render_template('history.html', records=records)

@app.route('/history/view/<int:entry_id>')
def history_view(entry_id):
    if 'user' not in session:
        return redirect(url_for('login'))
    r = get_history_entry(entry_id)
    if not r or r[1] != session['email']:
        return "Not found or access denied", 404
    return render_template('history_view.html', r=r)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
