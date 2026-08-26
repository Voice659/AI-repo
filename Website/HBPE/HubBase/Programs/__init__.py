from pathlib import Path

programs_dir = Path(__file__).resolve().parent
all_programsl = []

for item in programs_dir.iterdir():
    if item.is_dir() and item.name != "__pycache__" and (item / "main.py").exists():
        all_programsl.append(item.name)

all_programs = sorted(
    all_programsl,
    key=lambda x: (not x.isdigit(), int(x) if x.isdigit() else x)
)
