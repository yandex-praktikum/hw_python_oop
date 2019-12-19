import sys
from os.path import dirname
from os.path import abspath


root_dir = dirname(dirname(abspath(__file__)))
sys.path.append(root_dir)

pytest_plugins = [
    'fixtures.fixture_data',
    'fixtures.fixture_msg',
]
