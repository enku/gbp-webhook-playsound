"""Handler(s) for gbp-webhook-playsound"""

import subprocess as sp
from typing import Any

from gbp_webhook_playsound import get_sound_file, get_sound_player


def postpull(_event: Any) -> None:
    """postpull event handler"""
    with sp.Popen([*get_sound_player(), get_sound_file("postpull")]):
        pass
