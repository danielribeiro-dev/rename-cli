from pathlib import Path

mypath =  Path.home() / "current" / "metrics.csv"

print(mypath.parent)
print(mypath.suffix)
print(mypath.name)
print(mypath.stem)