def _fallback_summary(code: str) -> str:
    issues = []
    if 'print(' in code and 'logging' not in code:
        issues.append('Uses print() — consider using logging for production code.')
    if '== None' in code or '!= None' in code:
        issues.append('Use "is None" or "is not None" when comparing to None.')
    if 'for i in range' in code and '[' not in code:
        issues.append('Consider using list comprehensions where appropriate.')
    if 'TODO' in code:
        issues.append('Found TODO comments — consider addressing them.')
    if not issues:
        issues.append('No obvious heuristic issues detected.')
    return '\n'.join(issues)

def _fallback_improve(code: str) -> str:
    lines = [ln.rstrip() for ln in code.splitlines()]
    out = '\n'.join(lines)
    if not out.lstrip().startswith(('"""', "'''")):
        out = '"""Auto-improved: review changes before use."""\n' + out
    return out

try:
    from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
    import torch
    MODEL_NAME = "Salesforce/codet5-small"
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = model.to(device)

    def summarize_issues(code: str) -> str:
        prompt = "Summarize issues in the following python code:\n" + code
        inputs = tokenizer(prompt, return_tensors='pt', truncation=True, max_length=1024).to(device)
        out_ids = model.generate(**inputs, max_length=200)
        return tokenizer.decode(out_ids[0], skip_special_tokens=True)

    def improve_code(code: str) -> str:
        prompt = "Improve and optimize the following python code:\n" + code
        inputs = tokenizer(prompt, return_tensors='pt', truncation=True, max_length=1024).to(device)
        out_ids = model.generate(**inputs, max_length=512)
        return tokenizer.decode(out_ids[0], skip_special_tokens=True)

except Exception:
    def summarize_issues(code: str) -> str:
        return _fallback_summary(code) + "\n\n(Note: AI model unavailable; heuristic summary shown.)"

    def improve_code(code: str) -> str:
        return _fallback_improve(code) + "\n\n# Note: Improved by heuristic fallback."
