from checkio_referee import RefereeBase
from checkio_referee.covercode import py_unwrap_args

import settings
import settings_env
from tests import TESTS

py2_cover_str_unwrap = """
def cover(f, data):
    return f(*[str(x) for x in data])
"""

class Referee(RefereeBase):
    TESTS = TESTS
    EXECUTABLE_PATH = settings.EXECUTABLE_PATH
    CURRENT_ENV = settings_env.CURRENT_ENV
    FUNCTION_NAME = "is_safe"
    ENV_COVERCODE = {
        "python_2": py2_cover_str_unwrap,
        "python_3": py_unwrap_args,
        "javascript": None
    }
