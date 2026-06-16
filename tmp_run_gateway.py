import site
import sys
from pathlib import Path

site.addsitedir(str(Path(__file__).resolve().parent / "venv" / "Lib" / "site-packages"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import uvicorn

import gateway


uvicorn.run(gateway.app, host="127.0.0.1", port=8000)
