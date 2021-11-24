import json
from pathlib import Path

CONFIG = json.loads(
    (Path(__file__).parent.parent / "example_botconfig.json").read_text()
)


def test_readconfig():
    assert CONFIG.get("BOT_TOKEN") == ""
