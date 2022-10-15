import pytest
import sys


@pytest.fixture(autouse=True)
def leet_code_path():

    path = "src/leet_code"

    try:
        sys.path.append(path)
        yield

    except:
        raise

    else:
        sys.path.remove(path)
