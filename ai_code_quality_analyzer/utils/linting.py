import tempfile, subprocess, os, sys
def analyze_lint(code: str, timeout: int = 20) -> str:
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.py') as tmp:
            tmp.write(code.encode('utf-8'))
            tmp_path = tmp.name
        cmd = [sys.executable, '-m', 'pylint', tmp_path, '-rn']
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        out = proc.stdout or proc.stderr or ''
    except Exception as e:
        out = f'Linting error: {e}'
    finally:
        try:
            if 'tmp_path' in locals() and os.path.exists(tmp_path):
                os.remove(tmp_path)
        except Exception:
            pass
    return out
