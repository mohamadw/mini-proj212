import os
from pathlib import Path

def _make_dir(path):
    Path(path).mkdir(parents=True, exist_ok=True)
