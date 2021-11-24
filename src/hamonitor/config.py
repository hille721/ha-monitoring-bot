import json
import os
from pathlib import Path
import logging
import tempfile

from git import Repo

if not os.getenv("BOTCONFIG"):
    raise RuntimeError("BOTCONFIG not defined as environment variable")

_CONFIG = json.loads(Path(os.getenv("BOTCONFIG")).read_text())
_DEBUG_MODE = _CONFIG.get("DEBUG_MODE", False)

if _DEBUG_MODE or _CONFIG.get("BOT_TOKEN", "") == "":
    BACKEND = "Text"
    BOT_LOG_LEVEL = logging.DEBUG
else:
    BACKEND = "Telegram"
    BOT_LOG_LEVEL = logging.INFO

if not Path(f"{Path(__file__).parent}/plugins").exists():
    Path(f"{Path(__file__).parent}/plugins").mkdir()

# Get err-hamonitor plugin
if not Path(f"{Path(__file__).parent}/plugins/err-hamonitor").exists():
    # TODO: whats about updates?
    Repo.clone_from(
        "https://github.com/hille721/err-hamonitor.git",
        f"{Path(__file__).parent}/plugins/err-hamonitor",
    )

BOT_LOG_FILE = None

BOT_DATA_DIR = tempfile.mkdtemp()
BOT_EXTRA_PLUGIN_DIR = f"{Path(__file__).parent}/plugins"

STORAGE = "Memory"

BOT_ADMINS = _CONFIG.get(
    "BOT_ADMINS",
    [
        "@CHANGE_ME",
    ],
)

if not _DEBUG_MODE:
    BOT_IDENTITY = {
        "token": _CONFIG.get("BOT_TOKEN"),
    }

BOT_PREFIX = "/"

CORE_PLUGINS = ["Webserver", "Health", "Help"]

HAMONITOR = _CONFIG["HAMONITOR"]

WEBSERVER = _CONFIG.get(
    "WEBSERVER",
    {
        "HOST": "0.0.0.0",
        "PORT": 3141,
        "SSL": {
            "enabled": False,
            "host": "0.0.0.0",
            "port": 3142,
            "certificate": "",
            "key": "",
        },
    },
)
