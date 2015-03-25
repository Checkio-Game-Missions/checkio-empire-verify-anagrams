from checkio_referee import RefereeBase
from checkio_referee import covercodes, representations


import settings_env
from tests import TESTS

py2_cover_str_unwrap = """
def cover(f, data):
    return f(*[str(x) for x in data])
"""


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "is_safe"
    ENV_COVERCODE = {
        "python_2": py2_cover_str_unwrap,
        "python_3": covercodes.py_unwrap_args,
        "javascript": None
    }
    CALLED_REPRESENTATIONS = {
        "python_2": representations.unwrap_arg_representation,
        "python_3": representations.unwrap_arg_representation,
        "javascript": representations.unwrap_arg_representation,
    }
