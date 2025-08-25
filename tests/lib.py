# pylint: disable=missing-docstring,redefined-outer-name
import subprocess
from unittest import mock

from unittest_fixtures import FixtureContext, Fixtures, fixture


@fixture()
def popen(_fixtures: Fixtures) -> FixtureContext[mock.Mock]:
    with mock.patch.object(subprocess, "Popen") as mock_popen:
        yield mock_popen
