from checkio_referee import RefereeBase
from checkio_referee import covercodes, representations, ENV_NAME


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
    FUNCTION_NAMES = {
        ENV_NAME.JS_NODE: "verifyAnagrams"
    }

    ENV_COVERCODE = {
        ENV_NAME.PYTHON: covercodes.py_unwrap_args,
        ENV_NAME.JS_NODE: covercodes.js_unwrap_args
    }
    CALLED_REPRESENTATIONS = {
        ENV_NAME.PYTHON: representations.unwrap_arg_representation,
        ENV_NAME.JS_NODE: representations.unwrap_arg_representation
    }
