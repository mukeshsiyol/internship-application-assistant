def read_jd(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().lower()
