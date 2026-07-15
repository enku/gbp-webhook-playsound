"""gbp-webhook-playsound"""

import importlib.resources
from os import environ

DEFAULT_SOUND: str

with importlib.resources.path("gbp_webhook_playsound", "level-up-191997.mp3") as _p:
    DEFAULT_SOUND = str(_p)

del _p


def get_sound_file(event_name: str) -> str:
    """Return the path of the given event's sound file

    event_name such as "postpull"

    First looks for the environment variable GBP_WEBHOOK_PLAYSOUND_<event_name>, where
    event_name is capitalized. If the environment variable exists and value is not empty
    the value is returned.  Otherwise the "default" sound's path is returned.
    """
    return environ.get(f"GBP_WEBHOOK_PLAYSOUND_{event_name.upper()}") or DEFAULT_SOUND


def get_sound_player() -> list[str]:
    """Return the sound player executable"""
    return environ.get("GBP_WEBHOOK_PLAYSOUND_PLAYER", "pw-play").split()
