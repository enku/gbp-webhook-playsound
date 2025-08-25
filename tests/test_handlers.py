# pylint: disable=missing-docstring
import os
from unittest import TestCase

import gbp_testkit.fixtures as testkit
from unittest_fixtures import Fixtures, given, where

from gbp_webhook_playsound import DEFAULT_SOUND
from gbp_webhook_playsound.handlers import build_pulled


@given(testkit.environ, popen=testkit.patch)
@where(environ__clear=True)
@where(popen__target="gbp_webhook_playsound.handlers.sp.Popen")
class BuildPulledTests(TestCase):
    def test(self, fixtures: Fixtures) -> None:
        build_pulled(None)

        popen = fixtures.popen
        popen.assert_called_once_with(["pw-play", DEFAULT_SOUND])

    def test_custom_player(self, fixtures: Fixtures) -> None:
        os.environ["GBP_WEBHOOK_PLAYSOUND_PLAYER"] = "mpg123 -q"

        build_pulled(None)

        popen = fixtures.popen
        popen.assert_called_once_with(["mpg123", "-q", DEFAULT_SOUND])
