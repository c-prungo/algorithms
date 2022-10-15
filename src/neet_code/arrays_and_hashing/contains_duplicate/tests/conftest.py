import pytest
import sys
import os
from pathlib import Path


@pytest.fixture(autouse=True)
def neet_code_path():

    path = Path(os.path.realpath(__file__))
    path = str(path.parent.parent)

    try:
        sys.path.append(path)
        yield

    except:
        raise

    else:
        sys.path.remove(path)
