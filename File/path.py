from pathlib import Path

""""Create a path"""
p = Path("\\")
print(p)
print(f"Does {p} exists: {p.exists()}")
print(f"Is {p} a directory: {p.is_dir()}")
print(f"Is {p} a file: {p.is_file()}")
print(f"Is {p} absolute: {p.is_absolute()}")
print(p.absolute())

p = Path(".")
print(f"\n{p}")
print(f"Does {p} exists: {p.exists()}")
print(f"Is {p} a directory: {p.is_dir()}")
print(f"Is {p} a file: {p.is_file()}")
print(f"Is {p} absolute: {p.is_absolute()}")
print(p.absolute())

p = Path("newPath")
print(f"\n{p}")
print(f"Does {p} exists: {p.exists()}")
print(f"Is {p} a directory: {p.is_dir()}")
print(f"Is {p} a file: {p.is_file()}")
print(f"Is {p} absolute: {p.is_absolute()}")
print(p.absolute())

