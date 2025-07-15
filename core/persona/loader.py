import json
from pathlib import Path

from .schema import Persona


def load_persona(path):
    path = Path(path)

    with path.open(encoding="utf-8") as f:
        data = json.load(f)

    return Persona(**data)

if __name__ == "__main__":
    import sys, pprint
    p = load_persona(sys.argv[1])
    pprint.pp(p.dict())

