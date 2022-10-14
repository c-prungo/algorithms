import pytest
import sys


@pytest.fixture(autouse=True)
def add_to_path():

    path = 'problems/team_performance'

    try:
        sys.path.append(path)
        yield

    except:
        raise

    else:
        sys.path.remove(path)