import pytest
import sys


@pytest.fixture(autouse=True)
def add_to_path():

    path = 'problems/string_compression_II'

    try:
        sys.path.append(path)
        yield

    except:
        raise

    else:
        sys.path.remove(path)