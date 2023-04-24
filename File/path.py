from pathlib import Path

""""Create a path"""
p = Path("newPath")
print(p)
print(f"Does {p} exists: {p.exists()}")
print(f"Is {p} a directory: {p.is_dir()}")
print(f"Does {p} exists: {p.exists}")