def get_complexity(code: str):
    try:
        from radon.complexity import cc_visit
        from radon.metrics import mi_visit
        cc = cc_visit(code)
        mi = mi_visit(code, True)
        funcs = []
        for c in cc:
            funcs.append({
                "name": c.name,
                "complexity": c.complexity,
                "lineno": c.lineno
            })
        return {"functions": funcs, "mi_score": mi}
    except Exception as e:
        return {"error": "radon error: " + str(e)}
