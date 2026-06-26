from pathlib import Path

p = Path("./Downloads") / "projetos" / "testes.py"
a = Path.cwd() / "project" / "test2.js"
print(p.name)
print(p.parent)
print(p.suffix)
print(  )
print(a.parent)
print(a.name)
print(a.suffix)