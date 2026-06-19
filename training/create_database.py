import sys
from pathlib import Path

ROOT_DIR = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

sys.path.append(
    str(ROOT_DIR)
)

from app.database.database import (
    engine
)

from app.database.models import (
    Base
)

Base.metadata.create_all(
    bind=engine
)

print(
    "Database Created"
)