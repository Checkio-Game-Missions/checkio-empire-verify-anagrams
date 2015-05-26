from checkio_referee import RefereeBase
from checkio_referee import covercodes, representations


import settings_env
from tests import TESTS

py2_cover_str_unwrap = """
def cover(f, data):
    return f(*[str(x) for x in data])
"""


def py_repr(test, function_name):
    return "{}({})".format(function_name, ", ".join('"{}"'.format(d) for d in test["input"]))


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "verify_anagrams"
    ENV_COVERCODE = {
        "python_3": covercodes.py_unwrap_args,
        "javascript": None
    }
    CALLED_REPRESENTATIONS = {
        "python_3": py_repr,
    }
