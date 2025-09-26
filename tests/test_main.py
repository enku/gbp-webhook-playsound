# pylint: disable=missing-docstring,unused-argument
import os
from unittest import TestCase

import gbp_testkit.fixtures as testkit
from unittest_fixtures import Fixtures, given, where

from gbp_webhook_playsound import DEFAULT_SOUND, get_sound_file


@given(testkit.environ)
@where(environ__clear=True)
class GetSoundFileTests(TestCase):
    def test_default(self, fixtures: Fixtures) -> None:
        self.assertEqual(DEFAULT_SOUND, get_sound_file("postpull"))

    def test_environment_variable(self, fixtures: Fixtures) -> None:
        os.environ["GBP_WEBHOOK_PLAYSOUND_POSTPULL"] = "/foo/bar.mp3"

        self.assertEqual("/foo/bar.mp3", get_sound_file("postpull"))
